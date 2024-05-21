import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r'C:/Users/miro-/OneDrive/Documentos/University - Coventry-FEI/Subjects/Thesis/Findings/graphics/coded_data_purpose_1.csv'
df = pd.read_csv(file_path)

# Normalize the purpose of use names
df['Purpose of use'] = df['Purpose of use'].str.replace('Complete assig', 'Complete assig.')
df['Purpose of use'] = df['Purpose of use'].str.replace('Taking notes.', 'Taking notes')
df['Purpose of use'] = df['Purpose of use'].str.replace('Taking notes', 'Taking notes')

# Count each unique combination of purposes
purpose_combinations = df['Purpose of use'].value_counts()

# Create the pie chart
labels = purpose_combinations.index
sizes = purpose_combinations.values
colors = plt.cm.Paired(range(len(labels)))  # Generate a color palette

plt.figure(figsize=(14, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 10})
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Purpose of Use of Chatbots', fontsize=14)
plt.tight_layout()
plt.show()
