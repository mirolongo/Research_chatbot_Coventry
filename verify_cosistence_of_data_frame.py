import pandas as pd

# File path for the new data
file_path = r'C:\Thesis_files\Data_frame.csv'  # Atualize com o caminho correto do seu arquivo

# Load the CSV file
data = pd.read_csv(file_path)
print("File loaded successfully.")

# Clean column names to remove unwanted characters
data.columns = data.columns.str.replace('\n', '').str.strip()

# Print cleaned column names to verify
print("Cleaned column names:")
print(data.columns)

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values per column:")
print(missing_values)

# Check for missing values by major
major_column_name = 'Major'  # If different, update this accordingly
majors = data[major_column_name].unique()

for major in majors:
    print(f"\nMissing values for Major: {major}")
    major_data = data[data[major_column_name] == major]
    missing_values_major = major_data.isnull().sum()
    print(missing_values_major)
