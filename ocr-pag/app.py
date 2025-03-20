import cv2
import pytesseract
import re

original_image = cv2.imread("./src/caca_palavras3.png")

gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", original_image)

val, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("thresh", thresh)

print(val)

lines = 11
columns = 11

x_axis = original_image.shape[0]
y_axis = original_image.shape[1]

height = (y_axis/lines).__round__()
width = (x_axis/columns).__round__()

top = 0
bottom = height.__round__()

data = [[], []]

cv2.imshow("caca_palavras", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()


for x in range(lines):

    left = 0
    right = width.__round__()

    letters = []

    """ cropped_image = image[top:bottom, left:x_axis] """
    cropped_image = thresh[top:bottom, left:x_axis]

    """ contrast = 0
    brightness = 5
    
    cropped_image = cv2.convertScaleAbs(cropped_image, contrast, brightness)
    cropped_image = cv2.bilateralFilter(cropped_image,9,75,75) """

    customConfig = '--oem 3 --psm 6'
    data_line = pytesseract.image_to_string(cropped_image, config=customConfig)
    data_line = re.sub(r'[^A-Z]', '', data_line)
    data_line = data_line.replace("\n", "")

    if (data_line.__len__() > columns):
        val, thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
        cropped_image = thresh[top:bottom, left:x_axis]
        customConfig = '--oem 3 --psm 6'
        data_line = pytesseract.image_to_string(
            cropped_image, config=customConfig)
        data_line = re.sub(r'[^A-Z]', '', data_line)
        data_line = data_line.replace("\n", "")

    data[0].append(data_line)
    data_line = ""

    cv2.imshow("line" + str(x), cropped_image)
    cv2.waitKey(0)

    bottom = bottom + height
    top = top + height
    # data[0].append("".join(letters))

print(data)
