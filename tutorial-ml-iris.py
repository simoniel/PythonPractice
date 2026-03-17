from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib
matplotlib.use("QtAgg")  # or "Qt5Agg" if using PyQt5
import matplotlib.pyplot as plt


iris = load_iris()

print(type(iris))

print(iris.keys())
#print(iris.data[:10])
print("target = ",iris.target)
print("target names = ", iris.target_names)

print("data shape = ", iris.data.shape)
print("target shape = ", iris.target.shape)


X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)
#print(X_train[:10])

print("X_train shape = ", X_train.shape)

iris_dataframe = pd.DataFrame(X_train, columns=iris.feature_names)

print(iris_dataframe[:10])
print(iris_dataframe.dtypes)
print(iris_dataframe.head())
print(iris_dataframe.tail())
print(iris_dataframe.index)
print(iris_dataframe.columns)
print(iris_dataframe.describe())

#pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15,15), 
#                           marker='o', hist_kwds={'bins': 20}, 
#                           s=60, alpha=0.8)
#
#plt.show()