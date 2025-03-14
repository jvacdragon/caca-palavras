from flask import Flask, request, jsonify
from PIL import Image, ImageEnhance
import base64
from flask_cors import CORS
import pytesseract
from io import BytesIO
import cv2
import numpy as np
import re

# matriz (19,12)
image = Image.open("./src/caca_palavras.jpg")

print(image.getbbox())
image_dimensions = [image.getbbox()[2], image.getbbox()[3]]
print(image_dimensions)

image.show()

size_h = image_dimensions[1]/12
size_w = image_dimensions[0]

top = 0
bottom = size_h

for x in range(12):

    cropped_image = image.crop((0, top, size_w, bottom))
    # image = image.crop((0, 0, image_dimensions[0], image_dimensions[1]/12))

    cropped_image.show()

    top = top + size_h
    bottom = bottom + size_h
