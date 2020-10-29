import cv2
#chapter 3 sizing

img = cv2.imread("resources/lambo.PNG")
print(img.shape)

imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)

imgCropped = img[46:119,352:495]

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)
