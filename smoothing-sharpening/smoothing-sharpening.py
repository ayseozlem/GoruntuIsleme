import cv2
import numpy as np


img = cv2.imread('manzara.jpg')


smoothed_img = cv2.GaussianBlur(img, (5, 5), 0)


kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
sharpened_img = cv2.filter2D(img, -1, kernel)


cv2.imshow('Orijinal Resim', img)
cv2.imshow('Smoothing (Gaussian Blur)', smoothed_img)
cv2.imshow('Sharpening (Laplacian)', sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
