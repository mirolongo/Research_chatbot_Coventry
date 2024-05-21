import pandas as pd
import matplotlib.pyplot as plt

# Dados fornecidos
data = {
    "Frequency of use": [4, 4, 5, 2, 3, 5, 2, 4, 3, 5, 3, 2, 5, 3, 4, 3, 4, 4, 3, 2, 2, 5, 4, 2, 3, 4, 3, 4, 3, 2, 4, 2, 3, 2, 3, 4, 4, 5, 3, 4],
    "Perception of Improvement": [3, 3, 2, 2, 3, 2, 3, 1, 2, 2, 3, 3, 2, 1, 1, 3, 3, 3, 1, 3, 3, 3, 3, 1, 3, 2, 3, 2, 1, 3, 2, 3, 3, 3, 2, 2, 3, 2, 3, 2]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Agrupar dados para calcular a média dos benefícios relatados por frequência de uso
grouped_data = df.groupby('Frequency of use')['Perception of Improvement'].mean().reset_index()

# Verificar a inversão dos dados (se necessário, inverta aqui)
grouped_data['Perception of Improvement'] = grouped_data['Perception of Improvement'].values[::-1]

# Imprimir os dados agrupados para verificação
print(grouped_data)

# Definir os rótulos dos ticks do eixo x
# tick_labels = ['Always', 'Frequently', 'Occasionally', 'Rarely', 'Never']
tick_labels = ['Never', 'Rarely', 'Occasionally', 'Frequently', 'Always']
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
