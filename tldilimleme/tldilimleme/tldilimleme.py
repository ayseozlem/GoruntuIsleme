import cv2
import matplotlib.pyplot as plt
import requests
import numpy as np
from PIL import Image
from io import BytesIO


url = 'https://en.numista.com/catalogue/photos/turquie/6299fbf2156168.63152135-original.jpg'
response = requests.get(url)
image = Image.open(BytesIO(response.content))


image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)


gray_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)


_, thresholded_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)


plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(np.array(image))
plt.title('Orijinal Resim')

plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Gri Tonlama')

plt.subplot(1, 3, 3)
plt.imshow(thresholded_image, cmap='gray')
plt.title('Eşiklenmiş Resim')

plt.tight_layout()
plt.show()