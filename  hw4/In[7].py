import inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',header=None)
data.columns = ['Sample code','Clump Thckness','Uniformity of Cell Size','Uniformity of Cell Shape','Marginal Adhesion',
                'Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class']

data= data.drop(['Sample code'],axis=1)
data = data.replace('?',np.NaN)

data2 = data.drop(['Class'],axis=1)
data2['Bare Nuclei'] = pd.to_numeric(data2['Bare Nuclei'])

Z = (data2-data2.mean())/data2.std()

print('Number of rows before discarding outliers = %d' % (Z.shape[0]))

Z2 = Z.loc[((Z>-3).sum(axis=1)==9)&((Z<=3).sum(axis=1)==9),:]
print('Number of rows after discarding missing values = %d' % (Z2.shape[0]))