from PIL import Image

img = Image.open('goruntu.jpg')

width = 800
height = 600

resized_img = img.resize((width, height), Image.BILINEAR)
resized_img.show()
