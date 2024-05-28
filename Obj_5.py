import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data_frame_df = pd.read_csv('C:\\Thesis_files\\Data_frame.csv')

# Assumindo que a coluna relevante seja 'Recommendation to Classmates' para representar a intenção de continuar usando chatbots.
intention_col = 'Recommendation to Classmates'

# Mapping the numerical values to textual labels
intention_mapping = {
    1: 'No',
    2: 'Not sure',
    3: 'Yes'
}

# Calculate frequency distribution of intentions
intention_data = data_frame_df[intention_col]
intention_counts = intention_data.value_counts().sort_index()
intention_percentages = (intention_counts / intention_counts.sum()) * 100

# Display the descriptive statistics
print("Descriptive Statistics:")
print(intention_percentages)

# Convert numerical indices to textual labels
labels = intention_counts.index.map(lambda x: intention_mapping[x])

colors = ['#ff9999', '#66b3ff', '#99ff99']  # Adjust or add colors if necessary
explode = (0, 0, 0.1)  # explode the 'Yes' slice if necessary

plt.figure(figsize=(10, 6))
plt.pie(intention_percentages, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors[:len(labels)], explode=explode[:len(labels)])
plt.title('Intent to Continue Using Chatbots')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
