import pandas as pd
import statsmodels.api as sm

# File path
file_path = r'C:\Thesis_files\Objective_1.csv'

# Load the CSV file
data = pd.read_csv(file_path)

# Perform correlation analysis
correlation_matrix = data.corr()
print(correlation_matrix)

# Define dependent and independent variables
X = data[[
    "Frequency of use",
    "Rate of use Chatbot",  # Use the exact column name as printed above
    "Deeper Understanding of Concepts",
    "Personalized Learning Experience",
    "Perception of Improvement",
    "Influence to complete Academic task"
]]
Y = data["Advancement in Studies Perception"]

# Add a constant to the independent variables
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(Y, X).fit()

# Print the model summary
print(model.summary())
