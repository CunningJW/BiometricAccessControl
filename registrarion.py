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
    cap = cv2.VideoCapture(0)

    print("Making directory")

    try:
        os.mkdir(path)
        print("Made directory in " + path)
    except FileExistsError:
        print("Directory already exists")
        pass


    for i in range(NUM_OF_PHOTOS):
        ret, frame = cap.read()
        print("Read " + str(i) + " frame")
        representationsPath = os.path.join(path,'representations_vgg_face.pkl')

        print("opening representations file")

        try:
            with open(representationsPath, 'rb') as f:
                data = pickle.load(f)
        except EOFError:
            data = []
        except FileNotFoundError:
            f = open(representationsPath, "xb")
            f.close()
            data = []

        print("opened representations file")


        with open(representationsPath, 'wb') as f:
            print("got info")
            filename = '{0}/{1}_{2}.jpg'.format(path,username,i)
            representation = DeepFace.represent(img_path = frame, model = model)
            for row in data:
                if row[0] == filename:
                    row[1] = representation
                    
                    print("person already in list")
                    break
            else:
                
                data.append([filename,representation])
                print("new person")
        
            pickle.dump(data,f)
            print("dumped info")
        cv2.waitKey(PHOTO_DELAY)
    cap.release()
    cv2.destroyAllWindows()
