import pandas as pd

# Caminho do arquivo Excel
excel_file_path = r'C:\Thesis_files\Data_frame.xlsx'  # Atualize com o caminho correto do seu arquivo Excel

# Carregar o arquivo Excel
data = pd.read_excel(excel_file_path)

# Verificar as primeiras linhas do DataFrame para garantir que os dados foram carregados corretamente
print("Primeiras linhas do DataFrame carregado:")
print(data.head())

# Caminho para salvar o arquivo CSV
csv_file_path = r'C:\Thesis_files\Data_frame.csv'  # Atualize com o caminho onde deseja salvar o CSV

# Salvar o DataFrame como um arquivo CSV
data.to_csv(csv_file_path, index=False)

print(f"Arquivo CSV salvo com sucesso em: {csv_file_path}")
