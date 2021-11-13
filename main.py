import cv2
import numpy

img: numpy.ndarray = cv2.imread('robot.jpeg', cv2.IMREAD_COLOR)

cv2.imshow('color', img)
print(img.shape)
print(img.size)

b, g, r = cv2.split(img)
# cv2.imshow('blue', b)
# cv2.imshow('green', g)
# cv2.imshow('red', r)
# print(r)

# merge_img = cv2.merge([b, g, r])
# cv2.imshow('merge_img', merge_img)

# img_gray = cv2.imread('robot.jpeg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('img_gray', img_gray)
img_filled: numpy.ndarray = img.copy()

for row in range(0,int(img.shape[0]/2)):
    for colum in range(int(img.shape[1] / 2), int(img.shape[1])):
        img[row,colum] = (208,64,185)
cv2.imshow('img_filled', img_filled)
cv2.imshow('color', img)

# croped_img = img[int(img.shape[0] / 2):, 0:int(img.shape[1]/2)]
croped_img = img[500:400, 1000:600]
cv2.imshow('croped_img', croped_img)

cv2.waitKey(0)
