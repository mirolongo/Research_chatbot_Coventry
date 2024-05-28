import pandas as pd
import statsmodels.api as sm

# File path for the new data
file_path = r'C:\Thesis_files\Data_frame.csv'

# Load the CSV file
data = pd.read_csv(file_path)
print("File loaded successfully.")

# Print column names to verify correct data loading
print(data.columns)

# Clean column names to remove unwanted characters
data.columns = data.columns.str.replace('\n', '').str.strip()

# Print cleaned column names to verify
print("Cleaned column names:")
print(data.columns)

# Assuming the column for major is labeled 'Major'
major_column_name = 'Major'  # If different, update this accordingly

# List of majors to segment by
majors = data[major_column_name].unique()
print(f"Majors found: {majors}")

# Loop through each major and perform the analysis
for major in majors:
    print(f"\nAnalyzing data for Major: {major}")

    # Filter the data for the current major
    major_data = data[data[major_column_name] == major]

    # Define dependent and independent variables
    X = major_data[[
        "Frequency of use",
        "Rate of  useChatbot",
        "Deeper Understanding of Concepts",
        "Personalized Learning Experience",
        "Perception of Improvement",
        "Influence to completeAcademic task"
    ]]
    Y = major_data["Advancement in Studies Perception"]

    # Add a constant to the independent variables
    X = sm.add_constant(X)

    # Fit the regression model
    model = sm.OLS(Y, X).fit()

    # Print the model summary
    print(model.summary())

    # Perform correlation analysis
    correlation_matrix = major_data.corr()
    print("Correlation matrix:")
    print(correlation_matrix)
