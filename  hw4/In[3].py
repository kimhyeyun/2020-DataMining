import pandas as pd
import numpy as np

data = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',header=None)
data.columns = ['Sample code','Clump Thckness','Uniformity of Cell Size','Uniformity of Cell Shape','Marginal Adhesion',
                'Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class']

data=data.replace('?',np.NaN)

data2 = data['Bare Nuclei']

print('Before replacing missing values:')
print(data2[20:25])

data2 = data2.fillna(data2.median())

print('\nAfter replacing missing values:')
print(data2[20:25])
