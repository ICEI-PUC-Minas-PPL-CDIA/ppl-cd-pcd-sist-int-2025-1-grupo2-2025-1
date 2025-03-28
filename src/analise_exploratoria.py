import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo dos gráficos
plt.style.use('ggplot')
sns.set_palette('pastel')

# Carregar dataframe
state_of_data = pd.read_csv("/content/State_of_data_BR_2023_Kaggle - df_survey_2023.csv")
# Lista de colunas a serem analisadas
colunas_selecionadas = [
    ('P1_a ', 'Idade'),
    ('P1_a_1 ', 'Faixa idade'),
    ('P1_b ', 'Genero'),
    ('P1_c ', 'Cor/raca/etnia'),
    ('P1_d ', 'PCD'),
    ('P1_i_1 ', 'uf onde mora'),
    ('P1_e ', 'experiencia_profissional_prejudicada'),
    ('P1_e_1 ', 'Não acredito que minha experiência profissional seja afetada'),
    ('P1_e_2 ', 'Experiencia prejudicada devido a minha Cor Raça Etnia'),
    ('P1_e_3 ', 'Experiencia prejudicada devido a minha identidade de gênero'),
    ('P1_e_4 ', 'Experiencia prejudicada devido ao fato de ser PCD'),
    ('P2_i ', 'Quanto tempo de experiência na área de dados você tem?'),
    ('P2_f ', 'Cargo Atual'),
    ('P1_f_2', 'Senioridade das vagas recebidas em relação à sua experiência'),
    ('P2_g ', 'Nivel'),
    ('P2_h ', 'Faixa salarial')
]

# Criar novo dataframe com as colunas selecionadas
df = state_of_data[colunas_selecionadas].copy()

# Renomear colunas para facilitar o acesso
df.columns = [
    'Idade', 'Faixa_etaria', 'Genero', 'Cor_raca_etnia', 'PCD', 'UF', 
    'Exp_prof_prejudicada', 'Exp_nao_afetada', 'Exp_prej_cor_raca', 
    'Exp_prej_genero', 'Exp_prej_PCD', 'Exp_area_dados', 'Cargo_atual', 
    'Senioridade_vagas', 'Nivel', 'Faixa_salarial'
]
print("\nEstatísticas Descritivas da Idade:")
print(df['Idade'].describe())
count    5293.000000
mean       33.456452
std         6.647268
min        18.000000
25%        29.000000
50%        32.000000
75%        37.000000
max        70.000000
print("\nDistribuição de Gênero:")
print(df['Genero'].value_counts(normalize=True))
Masculino    0.786
Feminino     0.202
Outro        0.012
plt.figure(figsize=(10, 6))
sns.histplot(df['Idade'], bins=20, kde=True)
plt.title('Distribuição de Idade dos Profissionais de Dados')
plt.xlabel('Idade')
plt.ylabel('Contagem')
plt.show()
plt.figure(figsize=(8, 6))
df['Genero'].value_counts().plot(kind='bar')
plt.title('Distribuição de Gênero')
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Exp_area_dados', hue='Faixa_salarial')
plt.title('Faixa Salarial por Tempo de Experiência na Área de Dados')
plt.xticks(rotation=45)
plt.legend(title='Faixa Salarial', bbox_to_anchor=(1.05, 1))
plt.show()
print("\nDados Ausentes por Coluna:")
print(df.isnull().sum())
Exp_prof_prejudicada     4200
Exp_nao_afetada          4200
Exp_prej_cor_raca        4200
Exp_prej_genero          4200
Exp_prej_PCD             4200
