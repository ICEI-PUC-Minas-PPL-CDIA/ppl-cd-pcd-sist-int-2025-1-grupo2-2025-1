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
