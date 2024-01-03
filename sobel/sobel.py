import cv2
import numpy as np


img = cv2.imread('manzara.jpg', cv2.IMREAD_GRAYSCALE)

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)


sobel_combined = cv2.addWeighted(cv2.convertScaleAbs(sobel_x), 0.5, cv2.convertScaleAbs(sobel_y), 0.5, 0)


cv2.imshow('Orijinal Resim', img)
cv2.imshow('Sobel X', cv2.convertScaleAbs(sobel_x))
cv2.imshow('Sobel Y', cv2.convertScaleAbs(sobel_y))
cv2.imshow('Birleştirilmiş Sobel', sobel_combined)

cv2.waitKey(0)
cv2.destroyAllWindows()
