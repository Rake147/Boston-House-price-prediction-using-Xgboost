# -*- coding: utf-8 -*-
"""Boston House price prediction (XGBoost)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_c4wOO8Al0tKbqRToplHD4OAed8K_xh2
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

house_price_dataset = sklearn.datasets.load_boston()

print(house_price_dataset)

house_price_dataframe = pd.DataFrame(house_price_dataset.data, columns = house_price_dataset.feature_names)

house_price_dataframe.head()

house_price_dataframe['price'] = house_price_dataset.target

house_price_dataframe.head()

house_price_dataframe.shape

house_price_dataframe.isnull().sum()

house_price_dataframe.describe()

"""Identifying the correlation """

correlation = house_price_dataframe.corr()

plt.figure(figsize = (10,10))
sns.heatmap(correlation, cbar = True, square = True, fmt = '.1f', annot = True, annot_kws={'size':8}, cmap='Blues')

"""Splitting the data and Target"""

X = house_price_dataframe.drop(['price'], axis=1)
Y = house_price_dataframe['price']

print(X)

print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 2)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training"""

model = XGBRegressor()

model.fit(X_train,Y_train)

"""Evaluation

Prediction on Training Data
"""

training_data_prediction = model.predict(X_train)

print(training_data_prediction)

# R-Squared error
score_1 = metrics.r2_score(Y_train, training_data_prediction)

# Mean Absolute Error
score_2 = metrics.mean_absolute_error(Y_train, training_data_prediction)

print('R-Squared error:',score_1)
print('Mean Absolute Error:',score_2)

"""Visualizing the Actual prices and Predicted Prices"""

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Price vs Predicted prices")
plt.show()

"""Prediction on Test Data"""

test_data_prediction = model.predict(X_test)

# R-Squared error
score_1 = metrics.r2_score(Y_test, test_data_prediction)

# Mean Absolute Error
score_2 = metrics.mean_absolute_error(Y_test, test_data_prediction)

print('R-Squared error:',score_1)
print('Mean Absolute Error:',score_2)

