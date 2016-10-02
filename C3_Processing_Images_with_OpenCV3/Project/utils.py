# coding:utf-8

import cv2
import numpy as np

'''
边缘检测
OpenCV内置的边缘检测：Laplacian(), Sobel(), and Scharr()
当然，边缘检测很容易把噪声当做边缘。所以我们在进行边缘检测之前先进行降噪模糊。
OpenCV内置的模糊函数blur() (simple average), medianBlur(), and GaussianBlur()

下面我们使用medianBlur()，这对于彩色图像的降噪帮助很大。对于边缘检测，我们使用拉普拉斯算子Laplacian()
在降噪之后，我们把色彩空间从BGR转换成灰阶

'''


def strokeEdges(src, dst, blurKsize=7, edgeKsize=5):
    if blurKsize >= 3:
        # 7*7的模板
        blurredSrc = cv2.medianBlur(src, blurKsize)
        # BGR to GRAY
        graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)
    else:
        graySrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # 边缘检测
    cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize=edgeKsize)

    # 归一化
    normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)
    # 分割合并
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel * normalizedInverseAlpha
    cv2.merge(channels, dst)

import copy
img = cv2.imread("lena.bmp")
dst=copy.deepcopy(img)
strokeEdges(img,dst)
cv2.imshow("src",img)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()