import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Frequency of use": [4, 4, 5, 2, 3, 5, 2, 4, 3, 5, 3, 2, 5, 3, 4, 3, 4, 4, 3, 2, 2, 5, 4, 2, 3, 4, 3, 4, 3, 2, 4, 2, 3, 2, 3, 4, 4, 5, 3, 4],
    "Perception of Improvement": [3, 3, 2, 2, 3, 2, 3, 1, 2, 2, 3, 3, 2, 1, 1, 3, 3, 3, 1, 3, 3, 3, 3, 1, 3, 2, 3, 2, 1, 3, 2, 3, 3, 3, 2, 2, 3, 2, 3, 2]
}


df = pd.DataFrame(data)

grouped_data = df.groupby('Frequency of use')['Perception of Improvement'].mean().reset_index()

grouped_data['Perception of Improvement'] = grouped_data['Perception of Improvement'].values[::-1]

print(grouped_data)

tick_labels = ['Rarely', 'Occasionally', 'Frequently', 'Always']
# Gráfico de Barras: Frequency of Use and Perception of Improvement
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['Frequency of use'], grouped_data['Perception of Improvement'], color='skyblue', edgecolor='black')
plt.xlabel('Frequency of Use')
plt.ylabel('Perception of Improvement')
plt.title('Frequency of Use and Perception of Improvement')
plt.xticks(ticks=grouped_data['Frequency of use'], labels=tick_labels[:len(grouped_data)])
plt.ylim(0, grouped_data['Perception of Improvement'].max() + 1)  # Ajustar limite do eixo y para melhor visualização

# Salvar o gráfico
plt.savefig(r'C:/Users/miro-/OneDrive/Documentos/University - Coventry-FEI/Subjects/Thesis/Findings/graphics/Frequency_Use_Improvement_Bar_Corrected.png')
plt.show()
plt.close()
