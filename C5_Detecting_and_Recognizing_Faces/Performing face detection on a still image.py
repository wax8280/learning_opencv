# coding:utf-8
import cv2

filename = './img/face.jpg'


def detect(filename):
    # 级联分类器
    face_cascade = cv2.CascadeClassifier(
            './cascades/haarcascade_frontalface_default.xml')
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detectMultiScale(img,scaleFactor,minNeighbors)
    # scaleFactor:每次图像尺寸减小的比例;minNeighbors每一个目标至少要被检测到n次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # 绘制矩形
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.namedWindow('Vikings Detected!!')
    cv2.imshow('Vikings Detected!!', img)
    cv2.imwrite('./img/detect_face.jpg', img)
    cv2.waitKey(0)

detect(filename)