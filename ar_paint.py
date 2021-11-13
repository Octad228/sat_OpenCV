import cv2
import numpy

'''
83,120,0,107,255,255 - зелёный
0,201,126,179,255,255 - красный
19,54,18,41,255,255 - желтый
'''

frameWidth = 640
frameHigth = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHigth)
cap.set(10, 0)

myColors = [[83,120,0,107,255,255],
           [0,201,126,179,255,255],
           [18,43,216,47,255,255]]
color_val = [[0,255,255],
            [255,0,0],
            [0,0,255]]
my_points = []
def findColor(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    counter = 0
    new_points = []
    for color in myColors:
        lower = numpy.array(color[0:3])
        upper = numpy.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        # cv2.imshow(f'{color[0]}', mask)
        x, y = getContors(mask)
        if x !=0 and y !=0:
            new_points.append(x, y, counter)
        cv2.circle(imgResult, (x,y), 10, (0,255,255), cv2.FILLED)
        counter += 1
    return new_points
def getContors(img):
    contors, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x, y, w, h = 0,0,0,0
    for cnt in contors:
        area = cv2.contourArea(cnt)
        if area > 1000:
            cv2.drawContours(imgResult, contors, -1, (255,0,0), 3, cv2.LINE_8, hierarchy)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w//2, y

def drawOnCanvas(my_points):
    for point in my_points:
        cv2.circle(imgResult, (point[0], point[1]), 10, color_val[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    cv2.imshow('imgResult',imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgResult = img.copy()
    newPoints = findColor(img)
    if len(newPoints):
        for point in newPoints:
            my_points.append(point)
    if len(my_points):
        drawOnCanvas(my_points)
    cv2.imshow('imgResult',imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break