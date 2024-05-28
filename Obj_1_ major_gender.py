import pandas as pd
import statsmodels.api as sm

# File path for the new data
file_path = r'C:\Thesis_files\Data_frame.csv'

# Load the CSV file
data = pd.read_csv(file_path)
print("File loaded successfully.")

# Clean column names to remove unwanted characters
data.columns = data.columns.str.replace('\n', '').str.strip()

# Print cleaned column names to verify
print("Cleaned column names:")
print(data.columns)

# Assuming the columns for major and gender are labeled 'Major' and 'Gender'
major_column_name = 'Major'
gender_column_name = 'Gender'

# List of majors and genders to segment by
majors = data[major_column_name].unique()
genders = data[gender_column_name].unique()
print(f"Majors found: {majors}")
print(f"Genders found: {genders}")

# Loop through each combination of major and gender and perform the analysis
for major in majors:
    for gender in genders:
        print(f"\nAnalyzing data for Major: {major}, Gender: {gender}")

        # Filter the data for the current combination of major and gender
        subset_data = data[(data[major_column_name] == major) & (data[gender_column_name] == gender)]

        # Check if the subset data is not empty and has enough data points
        if subset_data.empty or len(subset_data) < 3:
            print(f"Insufficient data for Major: {major}, Gender: {gender}")
            continue

        try:
            # Define dependent and independent variables
            X = subset_data[[
                "Frequency of use",
                "Rate of  useChatbot",
                "Deeper Understanding of Concepts",
                "Personalized Learning Experience",
                "Perception of Improvement",
                "Influence to completeAcademic task"
            ]]
            Y = subset_data["Advancement in Studies Perception"]

            # Add a constant to the independent variables
            X = sm.add_constant(X)

            # Fit the regression model
            model = sm.OLS(Y, X).fit()

            # Print the model summary
            print(model.summary())

            # Perform correlation analysis
            correlation_matrix = subset_data.corr()
            print("Correlation matrix:")
            print(correlation_matrix)

        except Exception as e:
            print(f"Error analyzing data for Major: {major}, Gender: {gender}: {e}")
