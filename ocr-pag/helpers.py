import cv2


def cut(image, lines, columns):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    x_axis = image.shape[0]
    y_axis = image.shape[1]
    height = (y_axis/lines).__round__()
    width = (x_axis/columns).__round__()

    top = 0
    bottom = height.__round__()
    
    return(gray, top, bottom, x_axis, width, height)

