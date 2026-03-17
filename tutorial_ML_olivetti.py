from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib
matplotlib.use("QtAgg")  # or "Qt5Agg" if using PyQt5
import matplotlib.pyplot as plt


olivetti = fetch_olivetti_faces()

print(olivetti.keys())
#print(olivetti.DESCR)
print(olivetti.target)
print(olivetti.data[0])
print(olivetti.images[0])


#plt.imshow(olivetti.images[0])
#plt.show()

print("data.shape = ", olivetti.data.shape)
print("data[0].shape = ", olivetti.data[0].shape)
print("images[0].shape = ", olivetti.images[0].shape)
print("target.shape = ", olivetti.target.shape)

X_train, X_test, y_train, y_test = train_test_split(olivetti.data, olivetti.target, random_state=0)
print(type(X_train))

print("X_train.shape = ", X_train.shape)

