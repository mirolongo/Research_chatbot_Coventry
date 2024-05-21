import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import statsmodels.api as sm

# Carregar os dados
df = pd.read_csv(r'C:/Users/miro-/OneDrive/Documentos/University - Coventry-FEI/Subjects/Thesis/Findings/graphics/coded_data.csv')

# Função para cálculo de correlação e regressão
def calculate_correlation_and_regression(x, y):
    correlation, _ = pearsonr(x, y)
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    regression_slope = model.params.iloc[1]
    regression_intercept = model.params.iloc[0]
    regression_p_value = model.pvalues.iloc[1]
    return correlation, regression_slope, regression_intercept, regression_p_value

# Cálculo para Frequency of Use vs. Advancement in Studies Perception
x1 = df['Frequency of use']
y1 = df['Advancement in Studies Perception']
correlation1, slope1, intercept1, p_value1 = calculate_correlation_and_regression(x1, y1)
print(f'Correlation between Frequency of Use and Advancement in Studies Perception: r = {correlation1}')
print(f'Regression slope: {slope1}, intercept: {intercept1}, p-value: {p_value1}')

# Cálculo para Perception of Improvement vs. Influence to Complete Academic Tasks
x2 = df['Perception of Improvement']
y2 = df['Influence to complete Academic task']
correlation2, slope2, intercept2, p_value2 = calculate_correlation_and_regression(x2, y2)
print(f'Correlation between Perception of Improvement and Influence to Complete Academic Tasks: r = {correlation2}')
print(f'Regression slope: {slope2}, intercept: {intercept2}, p-value: {p_value2}')

# Verificar se a coluna 'Reported Benefits' existe no DataFrame
if 'Reported Benefits' in df.columns:
    x3 = df['Frequency of use']
    y3 = df['Reported Benefits']
    correlation3, slope3, intercept3, p_value3 = calculate_correlation_and_regression(x3, y3)
    print(f'Correlation between Frequency of Use and Reported Benefits: r = {correlation3}')
    print(f'Regression slope: {slope3}, intercept: {intercept3}, p-value: {p_value3}')
else:
    print("A coluna 'Reported Benefits' não existe no DataFrame.")
