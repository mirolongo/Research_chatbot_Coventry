import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

# Load the CSV file
data_frame_df = pd.read_csv('C:\\Thesis_files\\Data_frame.csv')

# Extract the necessary columns for analysis
X = data_frame_df[['Perception of \nImprovement']]
y = data_frame_df['Influence to \ncomplete\nAcademic task']

# Calculate Pearson correlation coefficient
pearson_corr, _ = pearsonr(X.squeeze(), y)
print(f'Pearson Correlation Coefficient: {pearson_corr}')

# Perform Linear Regression
reg = LinearRegression().fit(X, y)

# Get the R-squared value
r_squared = reg.score(X, y)

# Get the coefficients and intercept
coefficients = reg.coef_
intercept = reg.intercept_

# Displaying the results
results = {
    "R_squared": r_squared,
    "Intercept": intercept,
    "Coefficients": coefficients,
    "Pearson Correlation": pearson_corr
}

print("R-squared:", results["R_squared"])
print("Intercept:", results["Intercept"])
print("Coefficients:", results["Coefficients"])
print("Pearson Correlation:", results["Pearson Correlation"])

# Predict the values using the regression model
y_pred = reg.predict(X)

# Plotting the scatter plot and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Regression Line')

plt.title('Scatter Plot with Regression Line')
plt.xlabel('Perception of Improvement')
plt.ylabel('Influence on Complete Academic Tasks')
plt.legend()
plt.grid(True)
plt.show()
