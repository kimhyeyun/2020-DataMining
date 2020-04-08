import inline
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

data = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

plt.show(parallel_coordinates(data,'class'))

