# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 10:21:10 2023

@author: isor
"""
import math
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow import keras
from keras import layers

dataset_name="oxford_flowers102" # 옥스퍼드 꽃 데이터셋
dataset_repetitions=5
img_siz=64
batch_siz=64

kid_img_siz=75 # KID
kid_diffusion_steps=5
plot_diffusion_steps=20

min_signal_rate=0.02 # 샘플링
max_signal_rate=0.95

zdim=32 # 신경망 구조
embed_max_freq=1000.0
widths=[32,64,96,128]
block_depth=2

def preprocess_image(data):
    height=tf.shape(data["image"])[0] # 중앙 잘라내기(center cropping)
    width=tf.shape(data["image"])[1]
    crop_siz=tf.minimum(height, width)
    image=tf.image.crop_to_bounding_box(data["image"],(height-crop_siz)//2,(width-crop_siz)//2,crop_siz,crop_siz)
    image=tf.image.resize(image,size=[img_siz,img_siz],antialias=True) # antialias=True 설정 중요
    return tf.clip_by_value(image/255.0,0.0,1.0)

def prepare_dataset(split):
    return (tfds.load(dataset_name,split=split,shuffle_files=True)
        .map(preprocess_image, num_parallel_calls=tf.data.AUTOTUNE).cache()
        .repeat(dataset_repetitions).shuffle(10*batch_siz) # 셔플링은 KID에 중요
        .batch(batch_siz,drop_remainder=True).prefetch(buffer_size=tf.data.AUTOTUNE))

train_dataset=prepare_dataset("train[:80%]+validation[:80%]+test[:80%]") # 데이터셋
val_dataset=prepare_dataset("train[80%:]+validation[80%:]+test[80%:]")

class KID(keras.metrics.Metric): # KID 측정을 위한 클래스
    def __init__(self,name,**kwargs):
        super().__init__(name=name,**kwargs)
        self.kid_tracker=keras.metrics.Mean(name="kid_tracker")    
        self.encoder=keras.Sequential( # InceptionV3 사용
            [keras.Input(shape=(img_siz,img_siz,3)),layers.Rescaling(255.0),
             layers.Resizing(height=kid_img_siz,width=kid_img_siz),
             layers.Lambda(keras.applications.inception_v3.preprocess_input),
             keras.applications.InceptionV3(include_top=False,input_shape=(kid_img_siz,kid_img_siz,3),weights="imagenet"),
             layers.GlobalAveragePooling2D()],name="inception_encoder")

    def polynomial_kernel(self,features_1,features_2):
        feature_dimensions=tf.cast(tf.shape(features_1)[1],dtype=tf.float32)
        return (features_1 @ tf.transpose(features_2)/feature_dimensions+1.0)**3.0

    def update_state(self,real_images,generated_images,sample_weight=None):
        real_features=self.encoder(real_images,training=False)
        generated_features=self.encoder(generated_images,training=False)

        kernel_real=self.polynomial_kernel(real_features,real_features) # 두 특징으로 다항식 커널 계산
        kernel_generated=self.polynomial_kernel(generated_features,generated_features)
        kernel_cross = self.polynomial_kernel(real_features, generated_features)

        batch_siz=tf.shape(real_features)[0] # 평균 커널값으로 squared maximum mean discrepancy 측정
        batch_sizf=tf.cast(batch_siz,dtype=tf.float32)
        mean_kernel_real=tf.reduce_sum(kernel_real*(1.0-tf.eye(batch_siz)))/(batch_sizf*(batch_sizf-1.0))
        mean_kernel_generated=tf.reduce_sum(kernel_generated*(1.0-tf.eye(batch_siz)))/(batch_sizf*(batch_sizf-1.0))
        mean_kernel_cross=tf.reduce_mean(kernel_cross)
        kid=mean_kernel_real+mean_kernel_generated-2.0*mean_kernel_cross
        self.kid_tracker.update_state(kid) # 평균 KID 측정을 갱신

    def result(self):
        return self.kid_tracker.result()

    def reset_state(self):
        self.kid_tracker.reset_state()

def sinusoidal_embedding(x):
    embed_min_freq=1.0
    freq=tf.exp(tf.linspace(tf.math.log(embed_min_freq),tf.math.log(embed_max_freq),zdim//2))
    angular_speeds=2.0*math.pi*freq
    embeddings=tf.concat([tf.sin(angular_speeds*x),tf.cos(angular_speeds*x)],axis=3)
    return embeddings

def ResidualBlock(width):
    def apply(x):
        input_width=x.shape[3]
        if input_width==width: residual=x
        else: residual=layers.Conv2D(width,kernel_size=1)(x)
        
        x=layers.BatchNormalization(center=False,scale=False)(x)
        x=layers.Conv2D(width,kernel_size=3,padding="same",activation=keras.activations.swish)(x)
        x=layers.Conv2D(width,kernel_size=3,padding="same")(x)
        x=layers.Add()([x,residual])
        return x

    return apply

def DownBlock(width,block_depth):
    def apply(x):
        x,skips=x
        for _ in range(block_depth):
            x=ResidualBlock(width)(x)
            skips.append(x)
        x=layers.AveragePooling2D(pool_size=2)(x)
        return x

    return apply

def UpBlock(width,block_depth):
    def apply(x):
        x,skips=x
        x=layers.UpSampling2D(size=2,interpolation="bilinear")(x)
        for _ in range(block_depth):
            x=layers.Concatenate()([x,skips.pop()])
            x=ResidualBlock(width)(x)
        return x

    return apply

def get_network(image_size,widths,block_depth):
    noisy_images=keras.Input(shape=(image_size,image_size,3))
    noise_variances=keras.Input(shape=(1,1,1))

    e=layers.Lambda(sinusoidal_embedding)(noise_variances)
    e=layers.UpSampling2D(size=image_size,interpolation="nearest")(e)

    x=layers.Conv2D(widths[0],kernel_size=1)(noisy_images)
    x=layers.Concatenate()([x,e])

    skips=[]
    for width in widths[:-1]:
        x=DownBlock(width,block_depth)([x,skips])
    for _ in range(block_depth):
        x=ResidualBlock(widths[-1])(x)
    for width in reversed(widths[:-1]):
        x=UpBlock(width,block_depth)([x,skips])
    x=layers.Conv2D(3,kernel_size=1,kernel_initializer="zeros")(x)

    return keras.Model([noisy_images,noise_variances],x,name="residual_unet")

class DiffusionModel(keras.Model): # 확산 모델을 위한 클래스
    def __init__(self,image_size,widths,block_depth):
        super().__init__()
        self.normalizer=layers.Normalization()
        self.network=get_network(image_size,widths,block_depth) # denoise용 U-net
        self.ema_network=keras.models.clone_model(self.network) # KID용 U-net

    def compile(self, **kwargs):
        super().compile(**kwargs)
        self.noise_loss_tracker = keras.metrics.Mean(name="n_loss")
        self.image_loss_tracker = keras.metrics.Mean(name="i_loss")
        self.kid = KID(name="kid")

    @property
    def metrics(self):
        return [self.noise_loss_tracker, self.image_loss_tracker, self.kid]

    def denormalize(self, images): # 화소 값을 [0,1] 사이로 역변환
        images=self.normalizer.mean+images*self.normalizer.variance**0.5
        return tf.clip_by_value(images,0.0,1.0)

    def diffusion_schedule(self, diffusion_times):
        start_angle=tf.acos(max_signal_rate) # 확산 시간을 각도로 변환
        end_angle=tf.acos(min_signal_rate)
        diffusion_angles=start_angle+diffusion_times*(end_angle-start_angle)

        signal_rates=tf.cos(diffusion_angles) # signal_rates와 
        noise_rates=tf.sin(diffusion_angles)  # noise_rates의 제곱 합은 1
        return noise_rates,signal_rates
    
    def denoise(self, noisy_images, noise_rates, signal_rates, training):
        if training: network=self.network # 학습할 때 쓰는 신경망
        else: network=self.ema_network # KID 평가할 때 쓰는 신경망

        pred_noises=network([noisy_images,noise_rates**2],training=training)
        pred_images=(noisy_images-noise_rates*pred_noises)/signal_rates
        return pred_noises,pred_images

    def reverse_diffusion(self,initial_noise,diffusion_steps):
        num_images=initial_noise.shape[0]
        step_size=1.0/diffusion_steps

        next_noisy_images=initial_noise
        for step in range(diffusion_steps):
            noisy_images = next_noisy_images

            diffusion_times=tf.ones((num_images,1,1,1))-step*step_size
            noise_rates,signal_rates=self.diffusion_schedule(diffusion_times)
            pred_noises,pred_images=self.denoise(noisy_images,noise_rates,signal_rates,training=False)
            
            next_diffusion_times=diffusion_times-step_size
            next_noise_rates,next_signal_rates=self.diffusion_schedule(next_diffusion_times)
            next_noisy_images=(next_signal_rates*pred_images+next_noise_rates*pred_noises)

        return pred_images

    def generate(self,num_images,diffusion_steps):
        initial_noise=tf.random.normal(shape=(num_images,img_siz,img_siz,3))
        generated_images=self.reverse_diffusion(initial_noise,diffusion_steps) # 역확산
        generated_images=self.denormalize(generated_images) # 역정규화
        return generated_images

    def train_step(self, images):
        images=self.normalizer(images,training=True) # 정규화
        noises=tf.random.normal(shape=(batch_siz,img_siz,img_siz,3)) # 잡음
        
        diffusion_times=tf.random.uniform(shape=(batch_siz,1,1,1),minval=0.0,maxval=1.0)
        noise_rates,signal_rates=self.diffusion_schedule(diffusion_times)
        noisy_images=signal_rates*images+noise_rates*noises # 확산 스케쥴에 따라 잡음과 영상 혼합

        with tf.GradientTape() as tape: # denoise로 잡음과 영상 분리하고 손실 게산
            pred_noises,pred_images=self.denoise(noisy_images,noise_rates,signal_rates,training=True)
            noise_loss=self.loss(noises,pred_noises) # 학습에 사용하는 손실
            image_loss=self.loss(images,pred_images) # 평가에 사용하는 손실

        gradients=tape.gradient(noise_loss,self.network.trainable_weights)
        self.optimizer.apply_gradients(zip(gradients,self.network.trainable_weights))
        self.noise_loss_tracker.update_state(noise_loss)
        self.image_loss_tracker.update_state(image_loss)

        for weight,ema_weight in zip(self.network.weights,self.ema_network.weights):
            ema_weight.assign(0.999*ema_weight+(1-0.999)*weight) # 가중치의 EMA 추적

        return {m.name:m.result() for m in self.metrics[:-1]}

    def test_step(self, images):
        images=self.normalizer(images,training=False)
        noises=tf.random.normal(shape=(batch_siz,img_siz,img_siz,3))
        diffusion_times=tf.random.uniform(shape=(batch_siz,1,1,1),minval=0.0,maxval=1.0)
        noise_rates,signal_rates=self.diffusion_schedule(diffusion_times)
        noisy_images=signal_rates*images+noise_rates*noises
        
        pred_noises,pred_images=self.denoise(noisy_images,noise_rates,signal_rates,training=False)
        noise_loss=self.loss(noises,pred_noises)
        image_loss=self.loss(images,pred_images)
        self.image_loss_tracker.update_state(image_loss)
        self.noise_loss_tracker.update_state(noise_loss)

        images=self.denormalize(images)
        generated_images=self.generate(num_images=batch_siz,diffusion_steps=kid_diffusion_steps)
        self.kid.update_state(images, generated_images)
        return {m.name: m.result() for m in self.metrics}

    def plot_images(self,epoch=None,logs=None,num_rows=1,num_cols=8): # 영상 생성하고 그리기
        generated_images=self.generate(num_images=num_rows*num_cols,diffusion_steps=plot_diffusion_steps)

        plt.figure(figsize=(num_cols*2.0,num_rows*2.0))
        for row in range(num_rows):
            for col in range(num_cols):
                index=row*num_cols+col
                plt.subplot(num_rows,num_cols,index+1)
                plt.imshow(generated_images[index])
                plt.axis("off")
        plt.tight_layout()
        plt.show()
        plt.close()

model=DiffusionModel(img_siz, widths, block_depth) # 모델 생성

cp_path="checkpoints/diffusion_model" # 체크포인트: 최고 모델 저장(KID 메트릭 사용)
model.normalizer.adapt(train_dataset) # 데이터 정규화에 쓸 값 추정하고 저장

model.load_weights(cp_path) # 추론:체크포인트로 저장해둔 모델 불러와 영상 생성
model.plot_images(num_rows=10,num_cols=8)