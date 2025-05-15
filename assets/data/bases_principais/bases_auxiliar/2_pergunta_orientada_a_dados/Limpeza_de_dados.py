import pandas as pd

# 1. 
df = pd.read_csv('/content/MICRODADOS_ED_SUP_IES_2023 (1).CSV', sep=';', encoding='latin1')

# 2. Visualizar as primeiras linhas e tipos de dados
print("Primeiras linhas:")
print(df.head())
print("\nTipos de dados:")
print(df.dtypes)

# 3. Remover colunas totalmente vazias ou irrelevantes (exemplo: endereço, complemento, etc)
colunas_irrelevantes = [
    'DS_COMPLEMENTO_ENDERECO_IES', 'DS_NUMERO_ENDERECO_IES', 'DS_ENDERECO_IES', 
    'NO_BAIRRO_IES', 'NU_CEP_IES', 'DS_COMPLEMENTO_ENDERECO_IES'
]
colunas_irrelevantes = [col for col in colunas_irrelevantes if col in df.columns]
df.drop(columns=colunas_irrelevantes, inplace=True)

# 4. Remover colunas com mais de 80% de valores nulos
limite_nulos = 0.8
colunas_muitos_nulos = df.columns[df.isnull().mean() > limite_nulos]
df.drop(columns=colunas_muitos_nulos, inplace=True)

# 5. Remover duplicatas
df.drop_duplicates(inplace=True)

# 6. Tratar valores nulos restantes
# - Para variáveis numéricas: preencher com 0
# - Para variáveis categóricas: preencher com 'Não informado'
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    df[col].fillna(0, inplace=True)
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna('Não informado', inplace=True)

# 7. Padronizar nomes das colunas (opcional)
df.columns = [col.strip().replace(' ', '_').upper() for col in df.columns]

# 8. Exibir resumo final
print("\nResumo pós-limpeza:")
print(df.info())
print("\nExemplo de dados limpos:")
print(df.head())

# 9. Salvar arquivo limpo
df.to_csv('/content/MICRODADOS_ED_SUP_IES_2023_LIMPO.csv', index=False)
print("\nArquivo salvo como MICRODADOS_ED_SUP_IES_2023_LIMPO.csv")
