import cv2
import numpy as np


img = cv2.imread('manzara.jpg')


def gamma_correction(image, gamma=1.0):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)
gamma_value = 1.5

gamma_corrected = gamma_correction(img, gamma=gamma_value)


cv2.imshow('Orijinal Resim', img)
cv2.imshow(f'Gamma (Gamma: {gamma_value})', gamma_corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()
