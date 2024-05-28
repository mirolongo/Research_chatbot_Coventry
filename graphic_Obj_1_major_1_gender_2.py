import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the CSV file
data_frame_df = pd.read_csv('C:\Thesis_files\Data_frame.csv')

# Filter the dataframe for Exact Science (Major = 1) and Female (Gender = 2)
filtered_df = data_frame_df[(data_frame_df['Major'] == 1) & (data_frame_df['Gender'] == 2)]

# Extract the necessary columns for analysis
X = filtered_df[['Frequency of use', 'Rate of  use\nChatbot', 'Deeper Understanding of Concepts',
                 'Personalized\n Learning Experience', 'Perception of \nImprovement',
                 'Influence to \ncomplete\nAcademic task']]
y = filtered_df['Advancement\n in Studies Perception']

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
    "Coefficients": coefficients
}

print("R-squared:", results["R_squared"])
print("Intercept:", results["Intercept"])
print("Coefficients:", results["Coefficients"])
