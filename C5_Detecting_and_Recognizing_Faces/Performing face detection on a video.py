# coding:utf-8
import cv2


def detect():
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')
    camera = cv2.VideoCapture(1)

    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 6, 0, (40, 40))

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 255), 2)

        cv2.imshow("camera", frame)
        if cv2.waitKey(1000 / 12) & 0xff == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect()
