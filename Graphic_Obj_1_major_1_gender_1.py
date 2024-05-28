import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the CSV file
data_frame_df = pd.read_csv('C:\Thesis_files\Data_frame.csv')

# Filter the dataframe for Exact Science (Major = 1) and Male (Gender = 1)
filtered_df = data_frame_df[(data_frame_df['Major'] == 1) & (data_frame_df['Gender'] == 1)]

# Extract the necessary columns for analysis
X = filtered_df[['Frequency of use']]
y = filtered_df['Advancement\n in Studies Perception']

# Perform Linear Regression
reg = LinearRegression().fit(X, y)

# Predict the values using the regression model
y_pred = reg.predict(X)

# Plotting the scatter plot and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Regression Line')

plt.title('Scatter Plot with Regression Line')
plt.xlabel('Frequency of Use')
plt.ylabel('Advancement in Studies Perception')
plt.legend()
plt.grid(True)
plt.show()
