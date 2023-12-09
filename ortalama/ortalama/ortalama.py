import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('goruntu.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


filtered_img = cv2.blur(img, (5, 5))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Orijinal Resim')

plt.subplot(1, 2, 2)
plt.imshow(filtered_img)
plt.title('Ortalama Filtreli Hali')

plt.tight_layout()
plt.show()