import cv2

face_cas=cv2.CascadeClassifier('H:\Codes\\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
img=cv2.imread("H:\\Codes\\images\\test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cas.detectMultiScale(img)

var=True

if len(faces):
    var=True
else:
    var=False

if var==True:
    print("Face detected")
else:
    print("NO face detected")

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0),2)
cv2.imshow("img", img)
cv2.waitKey()

"""
import cv2
import sys
import time

imagePath = sys.argv[1]
cascPath = sys.argv[2]

faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(30, 30))#,flags = cv2.cv.CV_HAAR_IMAGE_SCALE)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

if faces == True:
    cv2.imshow("(1) Pamela(s) Found" ,image)
    cv2.waitKey(0)&0xFF
else:
    cv2.imshow("(0) Pamela(s) Found" ,image)
    cv2.waitKey(0)&0xFF
"""    