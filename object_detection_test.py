# from imageai.Detection import ObjectDetection
import pandas as pd
import os
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# detector = ObjectDetection()
# detector.setModelTypeAsTinyYOLOv3()
# detector.setModelPath("./models/yolo-tiny.h5")
# detector.loadModel()

with open('./models/coco.names','rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = './models/yolov3.cfg'
weightsPath = './models/yolov3.weights'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320,320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)




while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    key = cv2.waitKey(20)

    classIds,confs,_ = net.detect(frame,confThreshold=0.3)

    if len(classIds) != 0:
        for classId,conf in zip(classIds.flatten(),confs.flatten()):
            print('=======================')
            print('*********')
            print(classNames[classId],' - ',conf)
            print('*********')
            print('=======================')


    # _,detections = detector.detectObjectsFromImage(input_image = frame,
    #                                              input_type= "array",
    #                                              output_type="array",
    #                                              minimum_percentage_probability=30)
    #
    # for detection in detections:
    #     print(detection["name"],' - ',detection["percentage_probability"])

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
