import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('goruntu.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


max_filtered = cv2.blur(img, (5, 5))


box_filtered = cv2.boxFilter(img, -1, (5, 5))


plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Orijinal Resim')

plt.subplot(1, 3, 2)
plt.imshow(max_filtered)
plt.title('Max Filtreli')

plt.subplot(1, 3, 3)
plt.imshow(box_filtered)
plt.title('Box Filtreli')

plt.tight_layout()
plt.show()