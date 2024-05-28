import pandas as pd
import matplotlib.pyplot as plt

# Definindo os dados diretamente no script
data = [
    "Clarify doubts\nTranslations",
    "Clarify doubts\nTranslations",
    "Clarify doubts\nTranslations",
    "Clarify doubts\nTranslations",
    "Clarify doubts",
    "Clarify doubts\nTranslations\nTaking notes\nComplete assig.",
    "Clarify doubts",
    "Clarify doubts",
    "Clarify doubts",
    "Clarify doubts\nTaking notes\nComplete assig.",
    "Clarify doubts",
    "Clarify doubts",
    "Clarify doubts\nTranslations\nTaking notes",
    "Clarify doubts\nComplete assig.",
    "Complete assig.",
    "Clarify doubts",
    "Clarify doubts",
    "Clarify doubts",
    "Clarify doubts",
    "Clarify doubts\nTaking notes\nComplete assig.",
    "Clarify doubts",
    "Clarify doubts",
    "Clarify doubts\nTaking notes\nComplete assig.",
    "Clarify doubts\nTaking notes",
    "Clarify doubts",
    "Taking notes",
    "Clarify doubts",
    "Clarify doubts\nTaking notes",
    "Clarify doubts\nTranslation",
    "Clarify doubts",
    "Complete assig.",
    "Clarify doubts\nTranslations\nTaking notes\nComplete assig.",
    "Clarify doubts",
    "Clarify doubts",
    "Clarify doubts\nTranslations",
    "Clarify doubts\nTranslations\nTaking notes\nComplete assig.",
    "Clarify doubts",
    "Clarify doubts\nComplete assig.",
    "Clarify doubts",
    "Complete assig.",
    "Translations\ncheck grammar",
    "Clarify doubts\ncheck grammar",
    "check grammar",
    "check grammar\nSynonyms",
    "Clarify doubts",
    "Clarify doubts\nComplete assig.\nCoding",
    "Clarify doubts",
    "Clarify doubts\nTaking notes",
    "Clarify doubts",
    "Clarify doubts\nTranslations\nIdea generation",
    "get information",
    "Complete assig."
]

# Criando um DataFrame a partir dos dados
df = pd.DataFrame(data, columns=['Purpose of Use'])

# Calculando a frequência de cada combinação de propósito de uso
purpose_combinations = df['Purpose of Use'].value_counts()
purpose_percentages = (purpose_combinations / purpose_combinations.sum()) * 100

# Exibindo as estatísticas descritivas
print("Descriptive Statistics:")
print(purpose_percentages)

# Plotando o gráfico de pizza com legendas separadas
fig, ax = plt.subplots(figsize=(14, 8))
wedges, texts = ax.pie(
    purpose_percentages, startangle=140
)

# Adicionando a legenda fora do gráfico
plt.legend(wedges, [f'{i+1}. {label}: {percent:.1f}%' for i, (label, percent) in enumerate(zip(purpose_percentages.index, purpose_percentages))],
           title="Purpose of Use", loc="center left", bbox_to_anchor=(1, 0.5), fontsize='small')

ax.set_title("Purpose of Use of Chatbots")

plt.show()
