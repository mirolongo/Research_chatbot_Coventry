import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Carregar dados
data = {
    "Aspect to improve chatbot": [
        "Helpful to improve language", "Be able to upload docs", "More external tools to gain more knowledge", "Transparency",
        "The possibility to rephrase text", "Follow up questions", "Automate tasks", "Automate tasks", "Specific guidelines",
        "Specific guidelines", "I have when chatbot take mouse control a page", "If a chatbot has specific knowledge on a subject"
    ],
    "Comments Suggestions": [
        "Informs that the information is outdated and for IT the free chatbot is not usable for researching new technologies",
        "There is a lot of wrong information in the chatbot",
        "He uses it very often and is a fan of the chatbot",
        "think this tool needs to be improved a lot",
        "Working on building a new chatbot model",
        "I believe that neural analysis will still grow a lot",
        "think that in a few years the chatbot will replace teachers in many subjects",
        "He doesn't see much use in using the chatbot and prefers to use the material provided by the university.",
        "I have not use AI before but my classmates thinks it is positive",
        "",
        "",
        "A chatbot can both be negative and positive, depending on usage it for problem solving in school assignment is bad but having it as a tutor is beneficial"
    ]
}
df = pd.DataFrame(data)

# Função para análise de sentimentos
def analyze_sentiment(comment):
    if comment:
        analysis = TextBlob(comment)
        return analysis.sentiment.polarity
    return 0

# Aplicar análise de sentimentos
df['Sentiment'] = df['Comments Suggestions'].apply(analyze_sentiment)

# Exibir resultados
print(df)

# Plotar análise de sentimentos
plt.figure(figsize=(14, 10))
bars = plt.barh(df['Aspect to improve chatbot'], df['Sentiment'], color='skyblue')

# Adicionando rótulos de valor nas barras
for bar in bars:
    plt.gca().text(
        bar.get_width(),
        bar.get_y() + bar.get_height() / 2,
        f'{bar.get_width():.2f}',
        ha='left' if bar.get_width() < 0 else 'right',
        va='center',
        color='black'
    )

plt.xlabel('Sentiment Polarity')
plt.title('Sentiment Analysis of Comments and Suggestions')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()  # Ajustar layout para evitar corte
plt.show()
