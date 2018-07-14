import pandas as pd
from sklearn import preprocessing
import numpy as np

def get_OR_data():
    data = pd.read_csv('data/or.txt', header = None)
    values = data.values
    x = values[:,0:2]
    y = values[:,2][np.newaxis].transpose()
    return x,y

def get_Cubic_data():
    data = pd.read_csv('data/cubic.txt', header=None)
    scalar = preprocessing.StandardScaler().fit(data)
    trans_data = pd.DataFrame(scalar.transform(data))
    print(trans_data.describe())
    values = trans_data.values
    x = values[:, 0:1]
    y = values[:, 1][np.newaxis].transpose()

    return x, y

def get_complex_data():
    data = pd.read_csv('data/complex.txt', header=None)
    scalar = preprocessing.StandardScaler().fit(data)
    trans_data = pd.DataFrame(scalar.transform(data))
    print(trans_data.describe())
    values = trans_data.values
    x = values[:, 0:2]
    y = values[:, 2][np.newaxis].transpose()

    return x, y