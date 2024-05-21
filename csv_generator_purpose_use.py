import pandas as pd

# Load the CSV file
file_path = r'C:/Users/miro-/OneDrive/Documentos/University - Coventry-FEI/Subjects/Thesis/Findings/graphics/coded_data_purpose_1.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
print(df.head())

# Display the unique values to ensure all categories are correct
unique_values = df['Purpose of use'].unique()
print(unique_values)
