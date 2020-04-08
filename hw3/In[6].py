import pandas as pd
from pandas.api.types import is_numeric_dtype

data = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)
data.columns = ['sepal length','sepal width','petal length','petal width','class']

print('Correlation:')
print(data.corr())
