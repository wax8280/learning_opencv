# coding:utf-8
import cv2
import numpy as np

img = cv2.imread('line.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
minLineLength = 3
maxLineGap = 200

# lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 200)
# for line in lines:
#     for x1, y1, x2, y2 in line:
#         cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# 第一个参数是一个二值化图像（所以在进行霍夫变换之前要首先进行二值化，或者进行 Canny 边缘检测。）
# 第二三个参数分别代表 ρ 和 θ 的精确度
# 第四个参数是阈值，只有累加其中的值高于阈值时才被认为是一条直

lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
for line in lines:
    for rho, theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("edges", edges)
cv2.imshow("lines", img)
cv2.waitKey()
cv2.destroyAllWindows()
