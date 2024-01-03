import cv2
import matplotlib.pyplot as plt


img = cv2.imread('manzara.jpg', 0)

equ = cv2.equalizeHist(img)


plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Orijinal Resim')

plt.subplot(1, 2, 2)
plt.imshow(equ, cmap='gray')
plt.title('Histogram Eşitlenmiş Resim')

plt.tight_layout()
plt.show()
