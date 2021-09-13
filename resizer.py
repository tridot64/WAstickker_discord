import PIL
from PIL import Image
import os

directory = os.listdir()

webp = [i for i in directory if i.endswith(('.webp'))]

for image in webp:
	img = Image.open(image)
	img = img.resize((128,128), PIL.Image.ANTIALIAS)
	img.save(image, optimize = True)
