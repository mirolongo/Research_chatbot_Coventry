import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv(r'C:/Users/miro-/OneDrive/Documentos/University - Coventry-FEI/Subjects/Thesis/Findings/graphics/coded_data.csv')

# Agrupar dados para somar as percepções de avanço nos estudos por frequência de uso
grouped_data = df.groupby('Frequency of use')['Advancement in Studies Perception'].mean().reset_index()

# Graph 1: Frequency of Use vs. Advancement in Studies Perception
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['Frequency of use'], grouped_data['Advancement in Studies Perception'], edgecolor='black')
plt.xlabel('Frequency of Use')
plt.ylabel('Advancement in Studies Perception (Average)')
plt.title('Frequency of Use vs. Advancement in Studies Perception')
plt.xticks([1, 2, 3, 4, 5], ['Never', 'Rarely', 'Occasionally', 'Frequently', 'Always'])
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.savefig(r'C:/Users/miro-/OneDrive/Documentos/University - Coventry-FEI/Subjects/Thesis/Findings/graphics/Frequency_Use_vs_Advancement.png')
plt.show()
plt.close()
