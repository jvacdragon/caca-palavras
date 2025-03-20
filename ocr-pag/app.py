import cv2
import pytesseract
import re

from test import cut

original_image = cv2.imread("./src/caca_palavras.jpg")

lines = 7
columns = 7

# original_image = cv2.resize(original_image, None, fx= 0.8, fy=0.8, interpolation=cv2.INTER_AREA)

gray, top, bottom, x_axis, width, height = cut(original_image, lines, columns)
val, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

data = [[], []]

cv2.imshow("caca_palavras", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()


for x in range(lines):

    left = 0
    right = width.__round__()

    letters = []
    cropped_image = thresh[top:bottom, left:x_axis]

    customConfig = '--oem 3 --psm 6'
    data_line = pytesseract.image_to_string(cropped_image, config=customConfig)
    data_line = re.sub(r'[^A-Z]', '', data_line)
    data_line = data_line.replace("\n", "")

    
        
    print(x)
    if(data_line.__len__() >= (columns+2)):
        resized_image = cv2.resize(original_image, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
        
        new_gray, new_top, new_bottom, new_x_axis, new_width, new_height = cut(resized_image, lines, columns)
        
        val, thresh = cv2.threshold(new_gray, 200, 255, cv2.THRESH_BINARY)

        new_left = 0
        new_right = new_width.__round__()
        
        if(x>=1):
            new_bottom = (new_bottom + new_height*x)
            new_top = (new_top + new_height*x)
                
        cropped_image = thresh[new_top:new_bottom, new_left:new_x_axis]
        
        cv2.imshow("amplified" + str(x), cropped_image)
        cv2.waitKey(0)
        #cropped_image = resized_image[top:bottom, left:x_axis]
        customConfig = '--oem 3 --psm 6'
        data_line = pytesseract.image_to_string(
        cropped_image, config=customConfig)
        data_line = re.sub(r'[^A-Z]', '', data_line)
        data_line = data_line.replace("\n", "")

    if (data_line.__len__() == columns+1 or data_line.__len__() < columns):
        val, thresh_replace = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
        cropped_image = thresh_replace[top:bottom, left:x_axis]
        
        cv2.imshow("teste", cropped_image)
        cv2.waitKey(0)
        
        customConfig = '--oem 3 --psm 6'
        data_line = pytesseract.image_to_string(
        cropped_image, config=customConfig)
        data_line = re.sub(r'[^A-Z]', '', data_line)
        data_line = data_line.replace("\n", "")
    
    data[0].append(data_line)
    data_line = ""
    print(data)
    bottom = bottom + height
    top = top + height
    # data[0].append("".join(letters))

print(data)
