# coding: utf-8
import cv2
cameraCapture = cv2.VideoCapture(0)
fps = 30 # an assumption
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter( 'MyOutputVid.avi', cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)
success, frame = cameraCapture.read()
numFramesRemaining = 10 * fps - 1
while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1
cameraCapture.release()

'''
在这里videoCapture的get方法不会返回fps，而是总会返回0。
官方文档解释：“When querying a property that is not supported by the backend used by the VideoCapture class, value 0 is returned.”

'''
# 我们也可以用grab() 和 retrieve()

success0 = cameraCapture0.grab()
success1 = cameraCapture1.grab()
if success0 and success1:
    frame0 = cameraCapture0.retrieve()
    frame1 = cameraCapture1.retrieve()