import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "data_science\data_set\ML_Data_Set.csv"
dataset = pd.read_csv(url)
print(f"testing:{dataset.head()}\n")

X = dataset.iloc[:, :-1].values#rows,columns, (:)-> features(input data frame)
y = dataset.iloc[:, -1].values #all rows, only the last column - output data frame
print(f"X:\n{X}\n")
print(f"y:\n{y}\n")

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3]) #fills in gaps using average of columns

from sklearn.compose import ColumnTransformer #allows changes to be made to a specific column
from sklearn.preprocessing import OneHotEncoder #converts categorical data into a format that helps the ml algorithm to make better predictions

ct = ColumnTransformer(transformers = [("encoder",OneHotEncoder(),[0])],remainder = "passthrough")
X = np.array(ct.fit_transform(X))
print(f"X:\n{X}\n")

#encoding the dependent variable (y)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(f"y: \n{y}\n")

#splitting into training and testing data set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2, random_state = 1)
print(f"X train:\n{X_train}\n")
print(f"X test:\n{X_test}\n")
print(f"y train:\n{y_train}\n")
print(f"y test:\n{y_test}\n")
