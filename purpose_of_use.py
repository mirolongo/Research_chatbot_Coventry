import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

data = [
    "Clarify doubts",
    "Clarify doubts Translations",
    "Clarify doubts Translations",
    "Clarify doubts Translations Taking notes",
    "Clarify doubts Translations Complete assig. Taking notes",
    "Clarify doubts",
    "Clarify doubts Translations Complete assig. Taking notes",
    "Clarify doubts",
    "Clarify doubts",
    "Clarify doubts Complete assig. Taking notes",
    "Clarify doubts",
    "Clarify doubts",
    "Clarify doubts Translations Taking notes",
    "Clarify doubts Complete assig.",
    "Complete assig.",
    "Clarify doubts",
    "Clarify doubts",
    "Clarify doubts",
    "Clarify doubts",
    "Clarify doubts Complete assig. Taking notes",
    "Clarify doubts",
    "Clarify doubts Complete assig. Taking notes",
    "Clarify doubts Taking notes",
    "Clarify doubts",
    "Taking notes",
    "Clarify doubts",
    "Clarify doubts Taking notes",
    "Clarify doubts Translations",
    "Clarify doubts",
    "Complete assig.",
    "Clarify doubts Translations Complete assig. Taking notes",
    "Clarify doubts",
    "Clarify doubts Translations",
    "Clarify doubts",
    "Clarify doubts Translations Complete assig. Taking notes",
    "Clarify doubts",
    "Clarify doubts Complete assig.",
    "Clarify doubts",
    "Complete assig."
]

all_purposes = []
for purposes in data:
    all_purposes.extend(purposes.split())

purpose_counts = Counter(all_purposes)

labels = {
    'Clarify': 'Clarify doubts',
    'doubts': 'Clarify doubts',
    'Translations': 'Translations',
    'Complete': 'Complete assignments',
    'assig.': 'Complete assignments',
    'Taking': 'Taking notes',
    'notes': 'Taking notes'
}

purpose_counts_adjusted = Counter()
for key, count in purpose_counts.items():
    purpose_counts_adjusted[labels.get(key, key)] += count

plt.figure(figsize=(10, 6))
plt.pie(purpose_counts_adjusted.values(), labels=purpose_counts_adjusted.keys(), autopct='%1.1f%%', startangle=140, colors=['red', 'orange', 'yellow', 'green', 'blue'])
plt.title('Purpose of Use')
plt.savefig(r'C:/Users/miro-/OneDrive/Documentos/University - Coventry-FEI/Subjects/Thesis/Findings/graphics/Purpose_of_Use_Pie.png')
plt.show()
plt.close()
