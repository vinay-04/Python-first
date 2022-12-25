import pytesseract , cv2

pytesseract.pytesseract.tesseract_cmd='H:\\codes\\pythoncode\\pytesseract\\tesseract.exe'
img=cv2.imread('H:\\codes\\images\\optes.png')
text = pytesseract.image_to_string(img)
cv2.imshow("op",img)
print(text)
cv2.waitKey(0)

