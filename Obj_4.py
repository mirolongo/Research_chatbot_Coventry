import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

# Load the CSV file
data_frame_df = pd.read_csv('C:\\Thesis_files\\Data_frame.csv')

# Mapping the numerical values to textual labels
label_mapping = {
    1: 'Never',
    2: 'Rarely',
    3: 'Occasionally',
    4: 'Frequently',
    5: 'Always'
}

# Extract the necessary columns for analysis
X = data_frame_df[['Frequency of use']]
y = data_frame_df['Perception of \nImprovement']

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

# Convert numerical indices to textual labels
data_frame_df['Frequency of use (Text)'] = data_frame_df['Frequency of use'].map(label_mapping)

# Aggregate the mean of reported benefits for each frequency of use category
mean_reported_benefits = data_frame_df.groupby('Frequency of use (Text)')['Perception of \nImprovement'].mean().reindex(['Never', 'Rarely', 'Occasionally', 'Frequently', 'Always'])

# Plotting the bar chart with regression line
plt.figure(figsize=(10, 6))
bars = plt.bar(mean_reported_benefits.index, mean_reported_benefits, color='blue', alpha=0.5, label='Reported Benefits')

# Adding the regression line
x_vals = np.array([1, 2, 3, 4, 5])
x_labels = ['Never', 'Rarely', 'Occasionally', 'Frequently', 'Always']
y_vals = reg.predict(x_vals.reshape(-1, 1))

plt.plot(x_labels, y_vals, color='red', label='Regression Line', linewidth=2)

plt.title('Bar Chart with Regression Line')
plt.xlabel('Frequency of Use')
plt.ylabel('Reported Benefits')
plt.legend()
plt.grid(True)
plt.show()
