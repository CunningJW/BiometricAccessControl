from deepface import DeepFace
from deepface.basemodels import VGGFace
import pandas as pd
import os
import cv2

MAX_DISTANCE = 0.3

model = VGGFace.loadModel()
# df = DeepFace.find(img_path = "./images/Max.jpg",model_name='VGG-Face', db_path = "C:/Users/mmusc/Diploma/Saved", model = model)

# DeepFace.represent("./images/Max.jpg")
# print(df)
cap = cv2.VideoCapture(0) #, cv2.CAP_DSHOW
#cap.set(CV_CAP_PROP_FRAME_WIDTH , 640);
#cap.set(CV_CAP_PROP_FRAME_HEIGHT , 480);
while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)

    key = cv2.waitKey(20)

    try:
        DeepFace.detectFace(frame, detector_backend = 'opencv')
        df = DeepFace.find(img_path = frame ,model_name='VGG-Face', db_path = "./Saved", model = model, )
        if not df.empty:
            distance = df.iloc[0]["VGG-Face_cosine"]
            if distance<MAX_DISTANCE:
                filename = os.path.basename(df.iloc[0]["identity"])
                username = filename.split('_')[0]
                print('-----------\n***********\n')
                print(username)
                print('\n-----------\n***********\n')
        else:
            print('person not found')

    except ValueError:
        print('no face here :(')




    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
