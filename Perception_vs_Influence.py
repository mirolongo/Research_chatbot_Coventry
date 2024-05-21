import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv(r'C:/Users/miro-/OneDrive/Documentos/University - Coventry-FEI/Subjects/Thesis/Findings/graphics/coded_data.csv')

# Agrupar dados para somar a influência na conclusão das tarefas acadêmicas por percepção de melhoria
grouped_data = df.groupby('Perception of Improvement')['Influence to complete Academic task'].mean().reset_index()

# Graph 2: Perception of Improvement vs. Influence to Complete Academic Tasks
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['Perception of Improvement'], grouped_data['Influence to complete Academic task'], edgecolor='black')
plt.xlabel('Perception of Improvement')
plt.ylabel('Influence to Complete Academic Task (Average)')
plt.title('Perception of Improvement vs. Influence to Complete Academic Tasks')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.savefig(r'C:/Users/miro-/OneDrive/Documentos/University - Coventry-FEI/Subjects/Thesis/Findings/graphics/Perception_vs_Influence.png')
plt.show()
plt.close()
