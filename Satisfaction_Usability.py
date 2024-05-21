import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv(r'C:/Users/miro-/OneDrive/Documentos/University - Coventry-FEI/Subjects/Thesis/Findings/graphics/coded_data.csv')

value_counts = df['Rate of use - Chatbot'].value_counts().sort_index()

labels = {1: 'Very Difficult', 2: 'Difficult', 3: 'Neutral', 4: 'Easy', 5: 'Very Easy'}
satisfaction_labels = [labels[i] for i in value_counts.index]

plt.figure(figsize=(10, 6))
plt.pie(value_counts, labels=satisfaction_labels, autopct='%1.1f%%', startangle=140, colors=['red', 'orange', 'yellow', 'green', 'blue'])
plt.title('Satisfaction with Usability of Chatbots')
plt.savefig(r'C:/Users/miro-/OneDrive/Documentos/University - Coventry-FEI/Subjects/Thesis/Findings/graphics/Satisfaction_Usability_Pie.png')
plt.show()
plt.close()
