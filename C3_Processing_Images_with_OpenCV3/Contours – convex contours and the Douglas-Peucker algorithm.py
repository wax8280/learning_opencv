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
cnt = contours[0]

img = np.zeros((img.shape[0], img.shape[1],3), dtype=np.uint8)

# 求周长，True表示闭合
epsilon = 0.01 * cv2.arcLength(cnt, True)
# 近似多边形，True表示闭合
approx = cv2.approxPolyDP(cnt, epsilon, True)
# 直接使用轮廓，制作凸型（convex shapes）
hull = cv2.convexHull(cnt)
cv2.drawContours(img, [approx], 0, (0,0, 255), 2)
cv2.drawContours(img, [hull], 0, (0,255, 0), 2)

cv2.drawContours(img, contours, -1, (255, 255, 255), 1)
cv2.imshow("done", img)
cv2.waitKey()
cv2.destroyAllWindows()