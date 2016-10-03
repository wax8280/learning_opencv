import cv2
clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

cameraCapture = cv2.VideoCapture(0)
# 创建名为MyWindow的窗口
cv2.namedWindow('MyWindow')
# 绑定事件
cv2.setMouseCallback('MyWindow', onMouse)

print 'Showing camera feed. Click window or press any key to stop.'
success, frame = cameraCapture.read()

# 任何窗口都可以通过waitKey()捕获按键输入，接受的参数代表按键的毫秒数。返回-1或者ASCII码如Esc是27
# 当然可以用python内置函数。如ord('a')返回97
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('MyWindow', frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow('MyWindow')
cameraCapture.release()

'''
Tip:
    1.OpenCV的窗口和waitKey函数是相互依赖的，窗口只有在waitKey函数被调用之后才会更新，waitKey只会捕获现在正在聚焦的窗口的输入
    2.不是所有系统中waitKey都会返回ASCII码的。一个更有效的保证
    keycode = cv2.waitKey(1)
    if keycode != -1: keycode &= 0xFF
    3.
        setMouseCallback的event参数
        cv2.EVENT_MOUSEMOVE: This event refers to mouse movement
        cv2.EVENT_LBUTTONDOWN: This event refers to the left button down
        cv2.EVENT_RBUTTONDOWN: This refers to the right button down
        cv2.EVENT_MBUTTONDOWN: This refers to the middle button down
        cv2.EVENT_LBUTTONUP: This refers to the left button up
        cv2.EVENT_RBUTTONUP: This event refers to the right button up
        cv2.EVENT_MBUTTONUP: This event refers to the middle button up
        cv2.EVENT_LBUTTONDBLCLK: This event refers to the left button being double-clicked
        cv2.EVENT_RBUTTONDBLCLK: This refers to the right button being double-clicked
        cv2.EVENT_MBUTTONDBLCLK: This refers to the middle button being double-clicked

        flag参数
        cv2.EVENT_FLAG_LBUTTON: This event refers to the left button being pressed
        cv2.EVENT_FLAG_RBUTTON: This event refers to the right button being pressed
        cv2.EVENT_FLAG_MBUTTON: This event refers to the middle button being pressed
        cv2.EVENT_FLAG_CTRLKEY: This event refers to the Ctrl key being pressed
        cv2.EVENT_FLAG_SHIFTKEY: This event refers to the Shift key being pressed
        cv2.EVENT_FLAG_ALTKEY: This event refers to the Alt key being pressed

        
'''