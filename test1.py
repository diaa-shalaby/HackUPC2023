import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import os

# load the json sample data
data = pd.read_json("data/hackupc2023_restbai__dataset_sample.json").T

# get the "square_meters", "bedrooms", "bathrooms", and "num_images" columns
# and convert them to numpy arrays
x = data[["square_meters", "bedrooms", "bathrooms", "num_images"]].to_numpy()

# get the "price" column and convert it to a numpy array
y = data["price"].to_numpy()

# create some sample data
# x = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
# y = np.array([2, 4, 5, 4, 5])

# create a linear regression model and fit it to the data
model = LinearRegression()
model.fit(x, y)

# make a prediction using the model
# x_new = np.array([[6]])
x_new = np.array([[100, 2, 1, 1]])
y_new = model.predict(x_new)
print("Predicted value for x={}: {}".format(x_new[0][0], y_new[0]))
