import inline
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)
data.columns = ['sepal length','sepal width','petal length','petal width','class']

plt.show(data['sepal length'].hist(bins=8))
