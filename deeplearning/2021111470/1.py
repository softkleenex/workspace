#동일 위치의 face.jpg에 적용한다

import cv2
import matplotlib.pyplot as plt


image_path = 'face.jpg'


image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


if image is None:
    raise FileNotFoundError(f"이미지 파일 '{image_path}'을(를) 찾을 수 없습니다.")


edges = cv2.Canny(image, threshold1=100, threshold2=200)


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Canny Edge Detection')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()