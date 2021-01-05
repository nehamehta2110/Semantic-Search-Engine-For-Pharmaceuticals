import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# image path
originalImage = cv2.imread('media/mersynofen.png')

# morphological operations
gray = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('gray_image', cv2.WINDOW_NORMAL)
cv2.imshow('gray_image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel = np.ones((2, 1), np.uint8)
img = cv2.erode(gray, kernel, iterations=1)
cv2.namedWindow('eroded_image', cv2.WINDOW_NORMAL)
cv2.imshow('eroded_image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.dilate(img, kernel, iterations=1)
cv2.namedWindow('dilated_image', cv2.WINDOW_NORMAL)
cv2.imshow('dilated_image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# converting image to text using pytesseract
out_below = pytesseract.image_to_string(img)
print("Text to Image:", out_below)