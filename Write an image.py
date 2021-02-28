import cv2

img =cv2.imread('name of file which is to be written.jpg')

cv2.imshow('Output image',img)

cv2.imwrite('output.jpg',img) #In the folder where you saved this file there will be a new photo with name output.jpg
cv2.imwrite('output.png',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
