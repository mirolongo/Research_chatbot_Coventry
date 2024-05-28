import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data_frame_df = pd.read_csv('C:\\Thesis_files\\Data_frame.csv')

# Use the correct column name found from the previous step
satisfaction_col = 'Rate of  use\nChatbot'  # Coluna correta identificada

# Mapping the numerical values to textual labels
label_mapping = {
    1: 'Very Difficult',
    2: 'Difficult',
    3: 'Neutral',
    4: 'Easy',
    5: 'Very Easy'
}

# Calculate frequency distribution of satisfaction ratings
satisfaction_data = data_frame_df[satisfaction_col]
satisfaction_counts = satisfaction_data.value_counts().sort_index()
satisfaction_percentages = (satisfaction_counts / satisfaction_counts.sum()) * 100

# Display the descriptive statistics
print("Descriptive Statistics:")
print(satisfaction_percentages)

# Convert numerical indices to textual labels
labels = satisfaction_counts.index.map(lambda x: label_mapping[x])

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']  # Adjust or add colors if necessary
explode = (0, 0, 0, 0.1, 0.1)  # explode the 'Easy' and 'Very Easy' slices if they exist in your data

plt.figure(figsize=(10, 6))
plt.pie(satisfaction_percentages, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors[:len(labels)], explode=explode[:len(labels)])
plt.title('Student Satisfaction with Chatbot Usability')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
