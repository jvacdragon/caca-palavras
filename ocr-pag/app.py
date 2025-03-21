import cv2
import pytesseract
import re

from helpers import cut

original_image = cv2.imread("./src/caca_palavras.jpg")
lines = 7
columns = 7

def main(original_image, lines, columns):
    gray, top, bottom, x_axis, width, height = cut(original_image, lines, columns)
    val, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    data = [[], []]

    for x in range(lines):

        left = 0
        right = width.__round__()

        cropped_image = thresh[top:bottom, left:x_axis]

        customConfig = '--oem 3 --psm 6'
        data_line = pytesseract.image_to_string(cropped_image, config=customConfig)
        data_line = re.sub(r'[^A-Z]', '', data_line)
        data_line = data_line.replace("\n", "")
            
        if(len(data_line) >= (columns+2)):
            resized_image = cv2.resize(original_image, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
            
            new_gray, new_top, new_bottom, new_x_axis, new_width, new_height = cut(resized_image, lines, columns)
            
            val, new_thresh = cv2.threshold(new_gray, 200, 255, cv2.THRESH_BINARY)

            new_left = 0
            new_right = new_width.__round__()
            
            if(x>=1):
                new_bottom = (new_bottom + new_height*x)
                new_top = (new_top + new_height*x)
                    
            new_cropped_image = new_thresh[new_top:new_bottom, new_left:new_x_axis]
            
            data_line = pytesseract.image_to_string(
            new_cropped_image, config=customConfig)
            data_line = re.sub(r'[^A-Z]', '', data_line)
            data_line = data_line.replace("\n", "")

        if (len(data_line) == (columns+1) or len(data_line) < columns):
            val, thresh_replace = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
            cropped_image = thresh_replace[top:bottom, left:x_axis]
            
            data_line = pytesseract.image_to_string(
            cropped_image, config=customConfig)
            data_line = re.sub(r'[^A-Z]', '', data_line)
            data_line = data_line.replace("\n", "")
        
        data[0].append(data_line)
        
        for i, letter in enumerate(data[0][x]):
            if(len(data[1]) <= i):
                data[1].append(letter)
            else:
                data[1][i] = data[1][i] + letter
            
        data_line = ""
        bottom = bottom + height
        top = top + height
        
    return data

print(main(original_image, lines, columns))