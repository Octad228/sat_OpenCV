import cv2
import numpy as np

img = np.zeros((500,500,3), np.uint8)
img_height,  img_width, _ = img.shape
# img[200:300, 100:499]=255,0,173

cv2.line(img, (0,0), (img_height//2,img_width//2), (99,26,170),3)
cv2.line(img, (0,img_height), (img_width,0), (255,0,0),50)
cv2.rectangle(img, (250,250), (img_height,img_width), (123,222,222), cv2.FILLED)
cv2.circle(img, (img_height//2,img_width//2), 50, (111,163,87),7)
cv2.putText(img, "bruh", (300,100), cv2.FONT_HERSHEY_SIMPLEX, 3, (56,66,90), 3)

cv2.imshow("image", img)

cv2.waitKey(0)