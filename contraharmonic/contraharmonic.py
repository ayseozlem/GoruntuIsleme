import cv2
import numpy as np

def contraharmonic_mean_filter(img, kernel_size, Q):
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
    result = cv2.filter2D(img, -1, kernel)
    return result

img = cv2.imread('manzara.jpg', cv2.IMREAD_GRAYSCALE)

filtered_img = contraharmonic_mean_filter(img, 3, 1.5)

cv2.imshow('Orijinal Resim', img)
cv2.imshow('Contraharmonic Mean Filtrelenmiş Resim', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
