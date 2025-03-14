from flask import Flask, request, jsonify
from PIL import Image, ImageEnhance
import base64
from flask_cors import CORS
import pytesseract
from io import BytesIO
import cv2
import numpy as np
import re

image = Image.open("./src/caca_palavras2.jpg")

image = ImageEnhance.Contrast(image)
image = image.enhance(2)

image_dimensions = [image.getbbox()[2], image.getbbox()[3]]
dimensao_caca_palavra = [7, 7]

arrData = []

#image.show()

size_h = image_dimensions[1]/dimensao_caca_palavra[1]
size_w = image_dimensions[0]/dimensao_caca_palavra[0]

top = 0
bottom = size_h

for x in range(2):#dimensao_caca_palavra[1]):

    left = 0
    right = size_w
    
    line = []
    for y in range(dimensao_caca_palavra[0]):
        
        cropped_image = image.crop((left, top, right, bottom))
    
        #configuração do pytesseract e transformando em string
        customConfig = '--oem 3 --psm 6'
        letra = pytesseract.image_to_string(cropped_image, config=customConfig)
        
        letra = re.sub(r'[^a-zA-Z\s]', '', letra)
        letra = letra.replace("\n", "")
        
        line.append(letra)
        
        left = left + size_w
        right = right + size_w

    
    line = "".join(line)
    arrData.append(line)
    print(line)
    line = ""
    top = top + size_h
    bottom = bottom + size_h

print(arrData)
image.show()