import random
import cv2
import numpy

def getContors(img):
    contors, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contors:
        area = cv2.contourArea(cnt)
        if area > 1000:
            cv2.drawContours(imgContors, contors, -1, (255,0,0), 3, cv2.LINE_8, hierarchy)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h, = cv2.boundingRect(approx)
            # cv2.rectangle(imgContors, (x,y), (x+w, y+h), (0.255,0),3)
            corner_amount = len(approx)
            if corner_amount == 3:
                objectType = "treugolnik"
            elif corner_amount == 4:

                ratio = w/float(h)
                if 0.98<ratio<1.02:
                    objectType= "qvadrat"
                else:
                    objectType = "rect"
            elif corner_amount == 8:
                objectType = "krug"
            else:
                objectType = "none"
            text_x = x + w // 2 - 20
            text_y = y + w // 2
            cv2.putText(imgContors, objectType, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)
    cv2.imshow('imgContors',imgContors)

def thresh_callback(val):
    imgCanny = cv2.Canny(imgBlur, val, val)
    cv2.imshow('ingCanny', imgCanny)
    contors, hierarchy = cv2.findContours(imgCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    drawing = numpy.zeros((imgCanny.shape[0], imgCanny.shape[1], 3), numpy.uint8)
    for contour_index in range(len(contors)):
        color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        cv2.drawContours(drawing, contors, contour_index, color, 2, cv2.LINE_8, hierarchy)
    cv2.imshow('ingCanny', drawing)

img: numpy.ndarray = cv2.imread('shapes.png', cv2.IMREAD_COLOR)
imgContors = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (3,3), 1)
imgCanny = cv2.Canny(imgBlur, 255, 255)
getContors(imgCanny)

# create window
# wind_name = 'aboba'
# cv2.namedWindow(wind_name)
# cv2.imshow(wind_name, img)
# max_thresh = 255
# init_thresh = 50
# cv2.createTrackbar("Canny thresh:", wind_name, init_thresh, max_thresh, thresh_callback)
# thresh_callback(init_thresh)

# cv2.imshow('amogus', img)
# cv2.imshow('gray', imgGray)
# cv2.imshow('imgBlur', imgBlur)
# cv2.imshow('imgCanny', imgCanny)


cv2.waitKey(0)
