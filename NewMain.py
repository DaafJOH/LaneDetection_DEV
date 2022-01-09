import cv2, pyautogui
import numpy as np
from PIL import Image, ImageEnhance

# define white color range
minimum = np.array([0, 0, 230])
maximum = np.array([360, 10, 255])

rho = 1  # distance resolution in pixels of the Hough grid
theta = np.pi / 180  # angular resolution in radians of the Hough grid
threshold = 5  # minimum number of votes (intersections in Hough grid cell)
min_line_length = 5  # minimum number of pixels making up a line
max_line_gap = 50  # maximum gap in pixels between connectable line segments

kernel_size = 9

low_threshold = 50
high_threshold = 150
while True:
    #im = Image.open("img.jpg")

    im = pyautogui.screenshot()
    #image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    #image brightness enhancer

    Benhancer = ImageEnhance.Brightness(im)
    Cenhancer = ImageEnhance.Contrast(Benhancer.enhance(0.005))
    image = np.array(Cenhancer.enhance(500))
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, minimum, maximum)

    # Bitwise-AND mask and original image
    output = cv2.bitwise_and(image, image, mask=mask)

    blur_gray = cv2.GaussianBlur(output,(kernel_size, kernel_size),0)

    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

    line_image = np.copy(image) * 0  # creating a blank to draw lines on

    # Run Hough on edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)

    # Draw the lines on the  image
    lines_edges = cv2.addWeighted(blur_gray, 0.8, line_image, 1, 0)

    cv2.imshow("Color Detected", lines_edges)
    cv2.waitKey(1)