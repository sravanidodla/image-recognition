import cv2
import numpy as np
 
filename = 'im.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.06)

# result is dilated for marking the corners, not important
dst = cv2.dilate(dst, None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.01 * dst.max()] = [0, 120, 255]
X, Y = np.nonzero(dst > 0.01 * dst.max())
points = np.array([[x, y] for x, y in zip(X, Y)], dtype=np.float32)

# define criteria and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, label, center = cv2.kmeans(points, 3, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Now separate the data, Note the flatten()
A = points[label.ravel() == 0]
B = points[label.ravel() == 1]
C = points[label.ravel() == 2]
for p in A:
    img[int(p[0]), int(p[1])] = [255, 0, 0]
for p in B:
    img[int(p[0]), int(p[1])] = [0, 255, 0]
for p in C:
    img[int(p[0]), int(p[1])] = [0, 0, 255]

cv2.imwrite('result2.jpg', img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()