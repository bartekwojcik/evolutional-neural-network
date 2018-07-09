import pandas as pd

def get_OR_data():
    data = pd.read_csv('data/or.txt', header = None)
    print(data)