import pandas as pd
import matplotlib.pyplot as plt

# Coleta de dados
base_csv = 'Playoffs.csv'
base_excel = 'Playoffs.xlsx'

# Ler o arquivo CSV com o delimitador correto
df = pd.read_csv(base_csv, encoding='ISO-8859-1', delimiter=';')
print(df.head())

# Converter o dataframe para um arquivo Excel
df.to_excel(base_excel, index=False)

# Ler o arquivo Excel gerado
df_excel = pd.read_excel(base_excel)
print(df_excel.head())

# Tratamento de dados
df_excel.info()  # Exibe informações sobre o dataframe
df_sem_celulas_em_branco = df_excel.dropna()  # Remove linhas com células em branco
df_sem_celulas_em_branco.info()  # Exibe informações sobre o dataframe após a remoção

# Análise de dados
resumo_estatistico = df_sem_celulas_em_branco.describe()  # Gera estatísticas descritivas
print(resumo_estatistico)

# Verificação se a coluna 'Pos' existe no dataset antes de tentar plotar
posicao = 'Pos'
if posicao in df_sem_celulas_em_branco.columns:
    plt.hist(df_sem_celulas_em_branco[posicao], bins=5)
    plt.xlabel('Pos')
    plt.ylabel('Frequency')
    plt.title('Distribution of Position')
    plt.show()
else:
    print(f"A coluna '{posicao}' não foi encontrada no dataset.")
