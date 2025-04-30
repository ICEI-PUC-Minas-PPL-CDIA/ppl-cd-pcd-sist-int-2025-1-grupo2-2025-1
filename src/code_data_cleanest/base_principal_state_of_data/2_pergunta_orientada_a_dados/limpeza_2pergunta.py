import pandas as pd
import numpy as np

# Carregar o dataset State of Data Brazil 2023
df = pd.read_csv('state_of_data_br_2023.csv')

# Selecionar apenas as colunas relevantes para a análise
cols_interesse = ['P2i', 'P2g', 'P2h', 'P2b', 'P1i1', 'P1b', 'P1a1']
df_clean = df[cols_interesse].copy()

# Renomear colunas para melhor compreensão
df_clean.rename(columns={
    'P2i': 'tempo_experiencia',
    'P2g': 'nivel_senioridade',
    'P2h': 'faixa_salarial',
    'P2b': 'setor_atuacao',
    'P1i1': 'uf',
    'P1b': 'genero',
    'P1a1': 'faixa_etaria'
}, inplace=True)

# Remover registros com valores ausentes nas colunas principais
df_clean = df_clean.dropna(subset=['tempo_experiencia', 'nivel_senioridade', 'faixa_salarial'])
# Padronizar os níveis de senioridade
df_clean['nivel_senioridade'] = df_clean['nivel_senioridade'].str.lower()
df_clean['nivel_senioridade'] = df_clean['nivel_senioridade'].replace({
    'júnior': 'junior',
    'jr': 'junior',
    'jr.': 'junior',
    'pleno': 'pleno',
    'pl': 'pleno',
    'pl.': 'pleno',
    'sênior': 'senior',
    'sr': 'senior',
    'sr.': 'senior'
})

# Função para converter a faixa salarial em ponto médio numérico
def extrair_ponto_medio_salarial(faixa):
    try:
        # Remover "R$" e substituir vírgulas por pontos
        faixa = faixa.replace('R$', '').replace('.', '').replace(',', '.')
        
        # Extrair os valores numéricos
        valores = [float(val.strip()) for val in faixa.split('a') if val.strip()]
        
        # Calcular o ponto médio
        if len(valores) == 2:
            return (valores[0] + valores[1]) / 2
        elif len(valores) == 1:
            return valores[0]
        else:
            return np.nan
    except:
        return np.nan

# Aplicar a função para criar a coluna de salário médio
df_clean['salario_medio'] = df_clean['faixa_salarial'].apply(extrair_ponto_medio_salarial)
# Converter tempo de experiência para numérico (anos)
def converter_tempo_experiencia(tempo):
    try:
        if isinstance(tempo, str) and 'menos de 1' in tempo.lower():
            return 0.5
        elif isinstance(tempo, str) and 'anos' in tempo.lower():
            return float(tempo.lower().replace('anos', '').strip())
        else:
            return float(tempo)
    except:
        return np.nan

df_clean['tempo_experiencia_anos'] = df_clean['tempo_experiencia'].apply(converter_tempo_experiencia)

# Remover outliers de salário (método IQR)
Q1 = df_clean['salario_medio'].quantile(0.25)
Q3 = df_clean['salario_medio'].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

df_clean = df_clean[(df_clean['salario_medio'] >= limite_inferior) & 
                   (df_clean['salario_medio'] <= limite_superior)]

# Adicionar variáveis dummy para a análise (One-Hot Encoding)
df_clean_encoded = pd.get_dummies(df_clean, columns=['nivel_senioridade', 'setor_atuacao', 'uf'])

# Salvar o DataFrame limpo em um arquivo CSV
df_clean.to_csv('dados_limpos_pergunta2.csv', index=False)
df_clean_encoded.to_csv('dados_limpos_pergunta2_encoded.csv', index=False)

print(f"Dados limpos salvos. Total de registros: {len(df_clean)}")
