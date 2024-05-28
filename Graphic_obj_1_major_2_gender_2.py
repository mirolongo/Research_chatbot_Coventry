import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Load the CSV file
data_frame_df = pd.read_csv('C:\\Thesis_files\\Data_frame.csv')

# Filter the dataframe for Biological Science (Major = 2) and Female (Gender = 2)
filtered_df = data_frame_df[(data_frame_df['Major'] == 2) & (data_frame_df['Gender'] == 2)]

# Extract the necessary columns for analysis
X = filtered_df[['Frequency of use', 'Rate of  use\nChatbot',
                 'Personalized\n Learning Experience']]
y = filtered_df['Advancement\n in Studies Perception']

# Normalize the variables
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform Linear Regression
reg = LinearRegression().fit(X_scaled, y)

# Get the R-squared value
r_squared = reg.score(X_scaled, y)

# Get the coefficients and intercept
coefficients = reg.coef_
intercept = reg.intercept_

# Displaying the results
results = {
    "R_squared": r_squared,
    "Intercept": intercept,
    "Coefficients": coefficients
}

print("R-squared:", results["R_squared"])
print("Intercept:", results["Intercept"])
print("Coefficients:", results["Coefficients"])

# Scatter plot for 'Frequency of Use' against 'Advancement in Studies Perception'
plt.figure(figsize=(10, 6))
plt.scatter(filtered_df['Frequency of use'], y, color='blue', label='Actual Data')

# Create a new dataframe for plotting the regression line
X_frequency = filtered_df[['Frequency of use']]
X_frequency_scaled = scaler.fit_transform(X_frequency)

# Fit the model for 'Frequency of use' only to plot the regression line
reg_frequency = LinearRegression().fit(X_frequency_scaled, y)
y_pred_frequency = reg_frequency.predict(X_frequency_scaled)

plt.plot(filtered_df['Frequency of use'], y_pred_frequency, color='red', label='Regression Line')

plt.title('Scatter Plot with Regression Line')
plt.xlabel('Frequency of Use')
plt.ylabel('Advancement in Studies Perception')
plt.legend()
plt.grid(True)
plt.show()
