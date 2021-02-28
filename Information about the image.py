import cv2

img =cv2.imread('Bride.jpg')

cv2.imshow('Output image',img)

print(img.shape)

print("Height Pixel value: ",img.shape[0])
print("Width Pixel value: ",img.shape[1])
print("Number of layers : ",img.shape[2]) #in my case 3 to show rgb value


cv2.waitKey(0)

cv2.destroyAllWindows()
