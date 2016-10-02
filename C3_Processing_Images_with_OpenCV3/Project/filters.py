# coding:utf-8

import cv2
import numpy

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


class VConvolutionFilter(object):

    def __init__(self, kernel):
        self._kernel = kernel

    def apply(self, src, dst):
        """应用滤波器"""
        # 第二个参数 -1，指的是目标图跟原图具有同样的通道深度（per-channel depth）
        cv2.filter2D(src, -1, self._kernel, dst)


class SharpenFilter(VConvolutionFilter):
    """锐化"""

    def __init__(self):
        # 注意到模板权重总和为1。这种情况下，图像的总体亮度不变。
        kernel = numpy.array(
                [[-1, -1, -1],
                 [-1, 9, -1],
                 [-1, -1, -1]]
        )
        VConvolutionFilter.__init__(self, kernel)


class FindEdgesFilter(VConvolutionFilter):
    """边缘检测"""

    def __init__(self):
        # 权重总和0，边缘白色，不是边缘黑色
        kernel = numpy.array(
                [[-1, -1, -1],
                 [-1, 8, -1],
                 [-1, -1, -1]]
        )
        VConvolutionFilter.__init__(self, kernel)


class BlurFilter(VConvolutionFilter):
    """模糊"""

    def __init__(self):
        # 权重总和为1
        kernel = numpy.array(
                [[0.04, 0.04, 0.04, 0.04, 0.04],
                 [0.04, 0.04, 0.04, 0.04, 0.04],
                 [0.04, 0.04, 0.04, 0.04, 0.04],
                 [0.04, 0.04, 0.04, 0.04, 0.04],
                 [0.04, 0.04, 0.04, 0.04, 0.04]]
        )
        VConvolutionFilter.__init__(self, kernel)


class EmbossFilter(VConvolutionFilter):
    """浮雕"""

    def __init__(self):
        # 绝大多数模板都是对称的，若一边模糊（取正），一边锐化（取负），将会有奇异的效果（浮雕）
        kernel = numpy.array(
                [[-2, -1, 0],
                 [-1, 1, 1],
                 [0, 1, 2]]
        )
        VConvolutionFilter.__init__(self, kernel)


# import copy
# img = cv2.imread("lena.bmp")
# dst=copy.deepcopy(img)
# src=copy.deepcopy(img)
# SharpenFilter_object=EmbossFilter()
# SharpenFilter_object.apply(src,dst)
# cv2.imshow("src",src)
# cv2.imshow("dst", dst)
#
# cv2.waitKey()
# cv2.destroyAllWindows()
