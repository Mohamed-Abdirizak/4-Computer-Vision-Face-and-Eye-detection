import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# isticmaal predefined data oo ah face.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# ayadoo ah indho...
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()
# gray u adal vidoega.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        # indhaha ku sawir rectangle...
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            # 2da indhood ku sawirk rectangle....
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
# soo muuji videoga...
    cv2.imshow('frame', frame)
# hadii lataabto q: xer caamerada...
    if cv2.waitKey(1) == ord('q'):
        break
# vidoega maskaxda ka tirtir....
cap.release()
cv2.destroyAllWindows()