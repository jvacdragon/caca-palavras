import cv2
import pytesseract
import re


image = cv2.imread("./src/caca_palavras2.jpg")

#image = cv2.bitwise_not(image, cv2.COLOR_BGR2GRAY)

contrast = 2
brightness = 3

image = cv2.convertScaleAbs(image, contrast, brightness)

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

    for y in range(columns):
        cropped_image = image[top:bottom, left:right]

        cropperd_image = cv2.bilateralFilter(cropped_image,9,75,75)
        
        
        #configuração do pytesseract e transformando em string
        customConfig = '--oem 3 --psm 6'
        letter = pytesseract.image_to_string(cropped_image, config=customConfig)
        letter = re.sub(r'[^A-Z]', '', letter)
        letter = letter.replace("\n", "")
        
        """ if(x==2 and y==3):
            cv2.imshow("3letra", cropped_image)
            cv2.waitKey(0) """
        
        letters.append(letter)
        
        left = left + width
        right = right + width
        
    bottom = bottom + height
    top = top + height
    data[0].append("".join(letters))
    
print(data)
