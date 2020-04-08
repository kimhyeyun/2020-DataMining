import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)
data.columns = ['sepal length','sepal width','petal length','petal width','class']

fig, axes = plt.subplots(3, 2, figsize=(12, 12))
index = 0

for i in range(3):
    for j in range(i+1,4):
        ax1 = int(index/2)
        ax2 = index % 2
        axes[ax1][ax2].scatter(data[data.columns[i]],data[data.columns[j]],color='red')
        axes[ax1][ax2].set_xlabel(data.columns[i])
        axes[ax1][ax2].set_ylabel(data.columns[j])
        index=index+1

plt.show()