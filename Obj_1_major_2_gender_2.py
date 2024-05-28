import pandas as pd
from sklearn.linear_model import LinearRegression
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

# Load the CSV file
data_frame_df = pd.read_csv('C:\\Thesis_files\\Data_frame.csv')

# Filter the dataframe for Biological Science (Major = 2) and Female (Gender = 2)
filtered_df = data_frame_df[(data_frame_df['Major'] == 2) & (data_frame_df['Gender'] == 2)]

# Extract the necessary columns for analysis (excluding variables with infinite VIF)
X = filtered_df[['Frequency of use', 'Rate of  use\nChatbot', 'Personalized\n Learning Experience']]
y = filtered_df['Advancement\n in Studies Perception']

# Add a constant for VIF calculation
X_const = sm.add_constant(X)

# Calculate VIF for each variable
vif_data = pd.DataFrame()
vif_data["feature"] = X_const.columns
vif_data["VIF"] = [variance_inflation_factor(X_const.values, i) for i in range(X_const.shape[1])]

print("VIF Data:")
print(vif_data)

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
