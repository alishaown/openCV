import cv2
import numpy as np

print("package imported")
#importing image


img = cv2.imread("resources/gajeel.jpg")

cv2.imshow("output",img)
cv2.waitKey(0)



#importing video
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break







