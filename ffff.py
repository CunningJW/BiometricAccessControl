import cv2

cap = cv2.VideoCapture(0)
while True:
    key = cv2.waitKey(20)
    ret_val, img = cap.read()
    cv2.imshow('my webcam', img)
    if key == 27:
        break
cap.release()
