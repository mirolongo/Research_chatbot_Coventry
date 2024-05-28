import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
data = pd.read_csv('C:\Thesis_files\Objective_1.csv')
X = data['Frequency of use'].values.reshape(-1, 1)
y = data['Advancement in Studies Perception'].values
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
plt.scatter(data['Frequency of use'], data['Advancement in Studies Perception'], alpha=0.5, label='Student Data')
plt.plot(data['Frequency of use'], y_pred, color='red', label='Regression Line')
plt.xlabel('Frequency of Use')
plt.ylabel('Perception of academic advancement')
plt.title('Scatter Plot with Regression Line')
plt.legend()
plt.show()
