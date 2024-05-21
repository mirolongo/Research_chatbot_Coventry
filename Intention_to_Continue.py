import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv(r'C:/Users/miro-/OneDrive/Documentos/University - Coventry-FEI/Subjects/Thesis/Findings/graphics/coded_data.csv')

# Count the occurrences of each intention
intention_counts = df['Recommendation to Classmates'].value_counts().sort_index()

# Map the values to the correct labels
labels = {1: 'No', 2: 'Yes', 3: 'Not sure'}
intention_labels = [labels[i] for i in intention_counts.index]

# Graph 5: Intent to Continue Using Chatbots
plt.figure(figsize=(10, 6))
plt.pie(intention_counts, labels=intention_labels, autopct='%1.1f%%', startangle=140, colors=['red', 'green', 'orange'])
plt.title('Intent to Continue Using Chatbots')
plt.savefig(r'C:/Users/miro-/OneDrive/Documentos/University - Coventry-FEI/Subjects/Thesis/Findings/graphics/Intention_to_Continue.png')
plt.show()
plt.close()
