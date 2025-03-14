import cv2
import pytesseract
import re

image = cv2.imread("./src/caca_palavras2.jpg")

image = cv2.bitwise_not(image,cv2.COLOR_BAYER_BG2BGR)
#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#image = cv2.convertScaleAbs(image, contrast, brightness)
#image = cv2.bilateralFilter(image,9,75,75)

lines = 7
columns = 7

x_axis = image.shape[0]
y_axis = image.shape[1]

height = (y_axis/lines).__round__()
width = (x_axis/columns).__round__()

top = 0
bottom = height.__round__()

data = [[],[]]

cv2.imshow("caca_palavras", image)
cv2.waitKey(0)
cv2.destroyAllWindows()



for x in range(lines):

    left = 0
    right = width.__round__()
    
    letters = []
    
    cropped_image = image[top:bottom, left:x_axis]
    
    contrast = 0
    brightness = 5
    
    cropped_image = cv2.convertScaleAbs(cropped_image, contrast, brightness)
    cropped_image = cv2.bilateralFilter(cropped_image,9,75,75)


    customConfig = '--oem 3 --psm 6'
    data_line = pytesseract.image_to_string(cropped_image, config=customConfig)
    data_line = re.sub(r'[^A-Z]', '', data_line)
    data_line = data_line.replace("\n", "")
    
    data[0].append(data_line)
    data_line = ""
    cv2.imshow("line" + str(x), cropped_image)
    cv2.waitKey(0)
        
    bottom = bottom + height
    top = top + height
    #data[0].append("".join(letters))
    
print(data)