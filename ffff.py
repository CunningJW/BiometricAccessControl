import pickle


with open('./Saved/representations_vgg_face.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data[0])
