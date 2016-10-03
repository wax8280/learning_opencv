# coding:utf-8

import copy
import cv2
import numpy

kernel = numpy.array(
        [[-1, -1, -1],
         [-1, 9, -1],
         [-1, -1, -1]]
)
img = cv2.imread('Project/lena.bmp')
src = copy.deepcopy(img)
dst = copy.deepcopy(img)
# 第二个参数，-1表示目标的每个通道channel的深度跟原图一样
# 对于彩色图，filter2D对每个颜色通道都使用模板。如果想对每个颜色通道使用不同的模板，我们需要使用split() 和 merge()
cv2.filter2D(src, -1, kernel, dst)

cv2.imshow("src", img)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()
