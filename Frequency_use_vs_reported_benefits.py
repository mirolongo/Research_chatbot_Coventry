import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:/Users/miro-/OneDrive/Documentos/University - Coventry-FEI/Subjects/Thesis/Findings/graphics/coded_data.csv')

grouped_data = df.groupby('Frequency of use')['Perception of Improvement'].mean().reset_index()

print(grouped_data['Frequency of use'].unique())

plt.figure(figsize=(10, 6))
plt.bar(grouped_data['Frequency of use'], grouped_data['Perception of Improvement'], color='skyblue')
plt.xlabel('Frequency of Use')
plt.ylabel('Perception of Improvement (Average)')
plt.title('Frequency of Use vs. Perception of Improvement')

tick_labels = ['Always', 'Frequently', 'Occasionally', 'Rarely', 'Never']
# tick_labels = ['Never', 'Rarely', 'Occasionally', 'Frequently', 'Always']
plt.xticks(ticks=grouped_data['Frequency of use'], labels=tick_labels[:len(grouped_data)])


plt.savefig(r'C:/Users/miro-/OneDrive/Documentos/University - Coventry-FEI/Subjects/Thesis/Findings/graphics/Frequency_use_vs_reported_benefits.png')
plt.close()
