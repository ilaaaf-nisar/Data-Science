#!pip install opencv-python

import cv2


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


img = cv2.imread("test.jpg")


grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )


faces = faceCascade.detectMultiScale(grayScale, 1.1, 4)


for (x,y,w,z) in faces:
    cv2.rectangle(img,(x,y),(x+w, y+z),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey()

