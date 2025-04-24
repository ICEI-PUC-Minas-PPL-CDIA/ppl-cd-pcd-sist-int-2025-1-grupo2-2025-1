# Análise Exploratória de Dados: Relação entre Experiência, Senioridade e Salário
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configurações de estilo
plt.style.use('seaborn')
sns.set_palette("viridis")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12

# Função para converter faixas salariais
def convert_salary_range(salary_range):
    conversions = {
        'de R$ 4.001/mês a R$ 6.000/mês': 5000.50,
        'de R$ 6.001/mês a R$ 8.000/mês': 7000.50,
        'de R$ 8.001/mês a R$ 12.000/mês': 10000.50,
        'de R$ 12.001/mês a R$ 16.000/mês': 14000.50,
        'de R$ 16.001/mês a R$ 20.000/mês': 18000.50,
        'de R$ 20.001/mês a R$ 25.000/mês': 22500.50,
        'Acima de R$ 25.001/mês': 27500.50
    }
    return conversions.get(salary_range, np.nan)

# Carregar e preparar dados
df = pd.read_csv("survey_cleaned.csv")
df['Salario_Medio'] = df['Faixa_Salarial'].apply(convert_salary_range)

# 1. Distribuição Salarial por Nível de Senioridade
plt.figure(figsize=(14, 7))
order = ['Júnior', 'Pleno', 'Sênior', 'Especialista', 'Gerente']
sns.boxplot(x='Nivel_Senioridade', y='Salario_Medio', data=df, order=order)
plt.title('Distribuição Salarial por Nível de Senioridade')
plt.xlabel('Nível de Senioridade')
plt.ylabel('Salário Médio (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Progressão Salarial por Experiência
plt.figure(figsize=(14, 7))
exp_order = ['Menos de 1 ano', 'de 1 a 2 anos', 'de 3 a 4 anos', 
            'de 5 a 6 anos', 'Mais de 10 anos']
sns.lineplot(x='Tempo_Experiencia', y='Salario_Medio', data=df, 
             estimator='median', err_style=None, marker='o', sort=False, 
             order=exp_order)
plt.title('Progressão Salarial por Tempo de Experiência')
plt.xlabel('Tempo de Experiência')
plt.ylabel('Salário Médio (R$)')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 3. Impacto da Formação Acadêmica
plt.figure(figsize=(14, 7))
edu_order = ['Estudante de Graduação', 'Graduação/Bacharelado', 
            'Pós-graduação', 'Mestrado', 'Doutorado ou Phd']
sns.barplot(x='Nivel_Ensino', y='Salario_Medio', data=df, order=edu_order, ci=None)
plt.title('Salário Médio por Nível de Formação Acadêmica')
plt.xlabel('Nível de Formação')
plt.ylabel('Salário Médio (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Disparidade Regional
plt.figure(figsize=(16, 8))
uf_stats = df.groupby('UF')['Salario_Medio'].agg(['median', 'count']).reset_index()
uf_stats = uf_stats[uf_stats['count'] >= 10].sort_values('median', ascending=False)

sns.barplot(x='UF', y='median', data=uf_stats, palette='rocket')
plt.title('Salário Médio por Estado (UF) - Mínimo 10 respondentes')
plt.xlabel('Estado (UF)')
plt.ylabel('Salário Médio (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Relação entre Habilidades Técnicas e Salário
df['Habilidades'] = df['SQL'] + df['Python']
plt.figure(figsize=(14, 7))
sns.boxplot(x='Habilidades', y='Salario_Medio', data=df)
plt.title('Distribuição Salarial por Número de Habilidades Técnicas')
plt.xlabel('Quantidade de Habilidades (SQL + Python)')
plt.ylabel('Salário Médio (R$)')
plt.xticks([0, 1, 2], ['Nenhuma', '1 Habilidade', '2 Habilidades'])
plt.tight_layout()
plt.show()
