import pickle

def saveDbase(filename, object):
    file = open(filename, 'w')
    pickle.dump(object, file)
    file.close()

def loadDbase(filename):
    file = open(filename, 'r')
    object = pickle.load(file)
    file.close()
    return object

from pickle import *



L = [0]
D = {'x': 0,'y':L}

table = {'A':L,'B':D}

saveDbase('myfile', table)

