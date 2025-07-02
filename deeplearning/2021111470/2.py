import cv2 as cv
import numpy as np


prototxt = 'hed/models/deploy.prototxt'  # deploy 구조 정의
caffemodel = 'hed/models/hed_pretrained_bsds.caffemodel'  # 학습된 가중치
image_path = 'face.jpg'  # 얼굴 이미지


image = cv.imread(image_path)
if image is None:
    raise FileNotFoundError(f"{image_path} not found")


net = cv.dnn.readNetFromCaffe(prototxt, caffemodel)

#  전처리
blob = cv.dnn.blobFromImage(image, scalefactor=1.0, size=(image.shape[1], image.shape[0]),
                            mean=(104.00698793, 116.66876762, 122.67891434),
                            swapRB=False, crop=False)

net.setInput(blob)
hed = net.forward()


hed = hed[0, 0]
hed = cv.resize(hed, (image.shape[1], image.shape[0]))
hed = (255 * hed).astype("uint8")

cv.imshow("Original", image)
cv.imshow("HED Edge", hed)
cv.waitKey(0)
cv.destroyAllWindows()