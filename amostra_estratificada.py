import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv')
print(iris['class'].value_counts())

x, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4],
                              test_size = 0.5, stratify = iris.iloc[:, 4])

infert = pd.read_csv('infert.csv')
infert['education'].value_counts()

x1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1],
                                test_size = 0.6, stratify = infert.iloc[:, 1])

print(y1.value_counts())