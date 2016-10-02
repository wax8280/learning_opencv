# coding:utf-8
import cv2
import numpy as np
# 读取图像，降低分辨率
img = cv2.pyrDown(cv2.imread("hammer.jpg", cv2.IMREAD_UNCHANGED))
# 转换成灰度图，进行简单阀值处理
# 这个本来不是80，而是127的，不过考虑到实际。还是将阀值降低，不然效果不好。
ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY) ,
                            80, 255, cv2.THRESH_BINARY)

# 识别轮廓
image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                         cv2.CHAIN_APPROX_SIMPLE)
for c in contours:

    # 边界框坐标
    # 坐标x,y；宽度高度w,h
    x,y,w,h = cv2.boundingRect(c)
    # 绘制矩形（绿色
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

    # 找出最小区域（OpenCV没有直接求出最小区域坐标的函数，我们需要转换）
    rect = cv2.minAreaRect(c)
    # 计算最小矩形区域的坐标（结果为float）
    box = cv2.boxPoints(rect)
    # 正常化坐标。将其化成整数
    box = np.int0(box)
    # 绘制轮廓（红色；第三个参数，数组索引0开始
    cv2.drawContours(img, [box], 0, (0,0, 255), 3)

    # 计算最小封闭圆的中心与半径（绿
    (x,y),radius = cv2.minEnclosingCircle(c)
    # 转换成int
    center = (int(x),int(y))
    radius = int(radius)
    # 绘制圆形
    img = cv2.circle(img,center,radius,(0,255,0),2)

cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow("contours", img)
cv2.waitKey()
cv2.destroyAllWindows()