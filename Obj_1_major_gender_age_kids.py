import pandas as pd
import statsmodels.api as sm

# Path to the data file
file_path = r'C:\Thesis_files\Data_frame.csv'  # Update with the correct path to your file

# Load the CSV file
data = pd.read_csv(file_path)
print("File loaded successfully.")

# Clean column names to remove unwanted characters
data.columns = data.columns.str.replace('\n', '').str.strip()

# Print cleaned column names for verification
print("Cleaned column names:")
print(data.columns)

# Define the column names for major, gender, age group, and children
major_column_name = 'Major'
gender_column_name = 'Gender'
age_group_column_name = 'Age group'
children_column_name = 'Children'

# List unique values for major, gender, age group, and children
majors = data[major_column_name].unique()
genders = data[gender_column_name].unique()
age_groups = data[age_group_column_name].unique()
children_status = data[children_column_name].unique()

print(f"Majors found: {majors}")
print(f"Genders found: {genders}")
print(f"Age groups found: {age_groups}")
print(f"Children status found: {children_status}")

# Loop through each combination of major, gender, age group, and children
for major in majors:
    for gender in genders:
        for age_group in age_groups:
            for children in children_status:
                print(f"\nAnalyzing data for Major: {major}, Gender: {gender}, Age group: {age_group}, Children: {children}")

                # Filter data for the current combination of major, gender, age group, and children
                subset_data = data[(data[major_column_name] == major) &
                                   (data[gender_column_name] == gender) &
                                   (data[age_group_column_name] == age_group) &
                                   (data[children_column_name] == children)]

                # Check if the subset data is not empty and has enough data points
                if subset_data.empty or len(subset_data) < 3:
                    print(f"Insufficient data for Major: {major}, Gender: {gender}, Age group: {age_group}, Children: {children}")
                    continue

                try:
                    # Define dependent and independent variables
                    X = subset_data[[
                        "Frequency of use",
                        "Rate of useChatbot",
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
                    print(f"Error analyzing data for Major: {major}, Gender: {gender}, Age group: {age_group}, Children: {children}: {e}")

print("Analysis complete.")
