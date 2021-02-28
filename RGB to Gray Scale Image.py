# GRAYSCALE Image - All the Pixels of image is between the scale of Black and White. Basically converting Colored to Black & White Image

import cv2

img = cv2.imread("Bride.jpg")

cv2.imshow("Original",img)

cv2.waitKey(0)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Scale Image",gray_img)

cv2.waitKey(0)

cv2.destroyAllWindows()






