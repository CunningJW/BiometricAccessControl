import pickle

with open('./saved/representations_vgg_face.pkl', 'rb') as f:
    data = pickle.load(f)
    for line in data:
        print(line[0])
