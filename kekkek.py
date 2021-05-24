import cv2
from deepface import DeepFace
from deepface.basemodels import VGGFace


model = VGGFace.loadModel()
cam = cv2.VideoCapture(0)


for i in range(5):
    print('i am working')
    ret_val, img = cam.read()
    cv2.imshow('my webcam', img)

    key = cv2.waitKey(1)

    representation = DeepFace.represent(img_path = img, model = model)



cam.release()
cv2.destroyAllWindows()
