import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

originalImage = cv2.imread('media/paracetamol-tablets-500x500.jpg')
#gray = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
#kernel = np.ones((2, 1), np.uint8)
#img = cv2.erode(gray, kernel, iterations=1)
#img = cv2.dilate(img, kernel, iterations=1)
out_below = pytesseract.image_to_string(originalImage)
print("OUTPUT:", out_below)