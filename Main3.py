from PIL import Image, ImageEnhance
import numpy, cv2

from NewMain import Cenhancer

#read the image
im = Image.open("img.jpg")

#image brightness enhancer

Benhancer = ImageEnhance.Brightness(im)
Benhancer = ImageEnhance.Brightness(Benhancer.enhance(0.05))
Cenhancer = ImageEnhance.Contrast(Benhancer.enhance(0.05))
Benhancer = ImageEnhance.Brightness(Cenhancer.enhance(1000))


cv2.imshow("Color Detected", numpy.array(Benhancer.enhance(0.5)))
cv2.waitKey()