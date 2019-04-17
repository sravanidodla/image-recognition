import cv2
import numpy as np
filename = 'im.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
corners = cv2.goodFeaturesToTrack(gray, 255, 0.04, 12)
corners = np.int0(corners)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 3 ,255, -1)
cv2.imwrite('result1_1.jpg',img)  