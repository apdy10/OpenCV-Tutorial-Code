import cv2

img =cv2.imread('name of the image you want to open.jpg') #Image to be saved in the same folder as of code file else give the location of the image

cv2.imshow('Output image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
