import pandas as pd
import numpy as np

def get_OR_data():
    data = pd.read_csv('data/or.txt', header = None)
    values = data.values
    x = values[:,0:2]
    y = values[:,2][np.newaxis].transpose()
    return x,y