import numpy
from deepface import DeepFace
from deepface.basemodels import VGGFace
import cv2
import os

import pickle


NUM_OF_PHOTOS = 5
DIRECTORY_NAME = 'Saved'
DIRECTORY_PLACE = './'
PHOTO_DELAY = 1000


model = VGGFace.loadModel()
path = os.path.join(DIRECTORY_PLACE,DIRECTORY_NAME)

if __name__ == '__main__':

    username = str(input())
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    try:
        os.mkdir(path)
    except FileExistsError:
        pass


    for i in range(NUM_OF_PHOTOS):
        ret, frame = cap.read()
        representationsPath = os.path.join(path,'representations_vgg_face.pkl')

        try:
            with open(representationsPath, 'rb') as f:
                data = pickle.load(f)
        except EOFError:
            data = []
        except FileNotFoundError:
            f = open(representationsPath, "xb")
            f.close()
            data = []

        with open(representationsPath, 'wb') as f:
            filename = '{0}/{1}_{2}.jpg'.format(path,username,i)
            representation = DeepFace.represent(img_path = frame, model = model)
            for row in data:
                if row[0] == filename:
                    row[1] = representation
                    break
            else:
                data.append([filename,representation])

            pickle.dump(data,f)
        cv2.waitKey(PHOTO_DELAY)
    cap.release()
    cv2.destroyAllWindows()
