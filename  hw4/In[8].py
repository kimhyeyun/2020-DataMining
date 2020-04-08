import inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',header=None)
data.columns = ['Sample code','Clump Thckness','Uniformity of Cell Size','Uniformity of Cell Shape','Marginal Adhesion',
                'Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class']

data= data.drop(['Sample code'],axis=1)
data = data.replace('?',np.NaN)

dups=data.duplicated()
print('Number of duplicate rows = %d' % (dups.sum()))
print(data.loc[[11,28]])
