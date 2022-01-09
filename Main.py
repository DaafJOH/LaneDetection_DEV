import cv2, pyautogui
import numpy as np
from PIL import Image, ImageEnhance

while True:
    # Convert BGR to HSV
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # -----Converting image to LAB Color model-------------------
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
# -----Splitting the LAB image to different channels---------
    l, a, b = cv2.split(lab)
# -----Applying CLAHE to L-channel----------------------------
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
# -----Merge the CLAHE enhanced L-channel with the a and b channel----
    limg = cv2.merge((cl,a,b))
# -----Converting image from LAB Color model to RGB model-----
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    hsv = cv2.cvtColor(final, cv2.COLOR_BGR2HSV)

    # define white color range
    minimum = np.array([0, 0, 0])
    maximum = np.array([360, 100, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, minimum, maximum)

    # Bitwise-AND mask and original image
    output = cv2.bitwise_and(final, final, mask=mask)

    kernel_size = 9
    blur_gray = cv2.GaussianBlur(cv2.cvtColor(output, cv2.COLOR_RGB2GRAY),(kernel_size, kernel_size),0)

    low_threshold = 30
    high_threshold = 300
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

    cv2.imshow("Color Detected", final)
    cv2.waitKey(2)