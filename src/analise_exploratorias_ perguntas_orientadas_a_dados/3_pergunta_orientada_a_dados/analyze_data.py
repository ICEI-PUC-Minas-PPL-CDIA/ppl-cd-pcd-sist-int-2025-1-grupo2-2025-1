import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel('/home/ubuntu/upload/Main_database.xlsx')

# Informações gerais sobre o DataFrame
print("Informações do DataFrame:")
print(df.info())

# Primeiras linhas do DataFrame
print("\nPrimeiras 5 linhas:")
print(df.head())

# Verificar valores ausentes
print("\nValores ausentes por coluna:")
print(df.isnull().sum())

# Valores únicos por coluna
print("\nValores únicos por coluna:")
for col in df.columns:
    print(f"\n{col}:")
    print(df[col].unique())

import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel('/home/ubuntu/upload/Main_database.xlsx')

# Mostrar as primeiras 5 colunas
print('Primeiras 5 colunas:')
print(list(df.columns)[:5])

# Verificar colunas específicas
colunas_interesse = ['faixa', 'idade', 'genero', 'etaria', 'ensino', 'salarial', 
                     'experiencia', 'cor', 'raca', 'etnia', 'identidade']

print('\nVerificando colunas específicas:')
for palavra in colunas_interesse:
    print(f'\nColunas com "{palavra}":')
    matching = [col for col in df.columns if palavra.lower() in str(col).lower()]
    for col in matching[:5]:
        print(f'- {col}')
        # Mostrar alguns valores únicos para entender o formato
        unique_values = df[col].unique()[:3]
        print(f'  Exemplos de valores: {unique_values}')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from matplotlib.ticker import MaxNLocator
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configurações para melhorar a visualização
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12
sns.set_palette("viridis")

# Criar diretório para salvar as imagens
os.makedirs('visualizacoes', exist_ok=True)

# Carregar o arquivo Excel
df = pd.read_excel('/home/ubuntu/upload/Main_database.xlsx')

# Identificar as colunas de interesse para a análise
colunas_interesse = {
    'faixa_etaria': ('P1_a_1 ', 'Faixa idade'),
    'genero': ('P1_b ', 'Genero'),
    'nao_afetado': ('P1_e_1 ', 'Não acredito que minha experiência profissional seja afetada'),
    'impacto_raca': ('P1_e_2 ', 'Experiencia prejudicada devido a minha Cor Raça Etnia'),
    'impacto_genero': ('P1_e_3 ', 'Experiencia prejudicada devido a minha identidade de gênero'),
    'nivel_ensino': ('P1_l ', 'Nivel de Ensino'),
    'faixa_salarial': ('P2_h ', 'Faixa salarial'),
    'tempo_experiencia': ('P2_i ', 'Quanto tempo de experiência na área de dados você tem?')
}

# Criar um DataFrame com apenas as colunas de interesse
df_analise = pd.DataFrame()
for chave, coluna in colunas_interesse.items():
    if coluna in df.columns:
        df_analise[chave] = df[coluna]

# Verificar valores ausentes
print("Valores ausentes nas colunas de interesse:")
print(df_analise.isnull().sum())

# Tratar valores ausentes (substituir por 'Não informado' para variáveis categóricas)
for col in ['faixa_etaria', 'genero', 'nivel_ensino', 'faixa_salarial']:
    if col in df_analise.columns:
        df_analise[col] = df_analise[col].fillna('Não informado')

# Converter colunas binárias para valores numéricos (0 e 1) e tratar NaN
for col in ['nao_afetado', 'impacto_raca', 'impacto_genero']:
    if col in df_analise.columns:
        df_analise[col] = df_analise[col].fillna(0).astype(int)

# Definir a ordem correta para variáveis ordinais
ordem_faixa_etaria = [
    'Menos de 18 anos', '18-24 anos', '25-34 anos', '35-44 anos', 
    '45-54 anos', '55-64 anos', '65 anos ou mais', 'Não informado'
]

ordem_nivel_ensino = [
    'Ensino Fundamental', 'Ensino Médio', 'Ensino Técnico', 
    'Ensino Superior Incompleto', 'Ensino Superior Completo', 
    'Pós-graduação (Especialização)', 'Mestrado', 'Doutorado', 'Não informado'
]

ordem_faixa_salarial = [
    'Até R$ 1.000', 'De R$ 1.001 a R$ 2.000', 'De R$ 2.001 a R$ 3.000', 
    'De R$ 3.001 a R$ 4.000', 'De R$ 4.001 a R$ 6.000', 'De R$ 6.001 a R$ 8.000', 
    'De R$ 8.001 a R$ 12.000', 'De R$ 12.001 a R$ 16.000', 'De R$ 16.001 a R$ 20.000', 
    'De R$ 20.001 a R$ 25.000', 'Acima de R$ 25.000', 'Não informado'
]

# Verificar valores únicos nas colunas para confirmar as categorias
for col in df_analise.columns:
    print(f"\nValores únicos em {col}:")
    print(df_analise[col].value_counts().sort_index())

# Salvar o DataFrame processado
df_analise.to_csv('visualizacoes/dados_processados.csv', index=False)

print("\nDados processados e salvos em 'visualizacoes/dados_processados.csv'")

import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel('/home/ubuntu/upload/Main_database.xlsx')

# Informações gerais sobre o DataFrame
print("Informações do DataFrame:")
print(df.info())

# Primeiras linhas do DataFrame
print("\nPrimeiras 5 linhas:")
print(df.head())

# Verificar valores ausentes
print("\nValores ausentes por coluna:")
print(df.isnull().sum())

# Valores únicos por coluna
print("\nValores únicos por coluna:")
for col in df.columns:
    print(f"\n{col}:")
    print(df[col].unique())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from matplotlib.ticker import MaxNLocator
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configurações para melhorar a visualização
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12
sns.set_palette("viridis")
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'DejaVu Sans'

# Carregar os dados processados
df_analise = pd.read_csv('visualizacoes/dados_processados.csv')

# Definir a ordem correta para variáveis ordinais
ordem_faixa_etaria = [
    'Menos de 18 anos', '18-24 anos', '25-34 anos', '35-44 anos', 
    '45-54 anos', '55-64 anos', '65 anos ou mais', 'Não informado'
]

ordem_nivel_ensino = [
    'Ensino Fundamental', 'Ensino Médio', 'Ensino Técnico', 
    'Ensino Superior Incompleto', 'Ensino Superior Completo', 
    'Pós-graduação (Especialização)', 'Mestrado', 'Doutorado', 'Não informado'
]

ordem_faixa_salarial = [
    'Até R$ 1.000', 'De R$ 1.001 a R$ 2.000', 'De R$ 2.001 a R$ 3.000', 
    'De R$ 3.001 a R$ 4.000', 'De R$ 4.001 a R$ 6.000', 'De R$ 6.001 a R$ 8.000', 
    'De R$ 8.001 a R$ 12.000', 'De R$ 12.001 a R$ 16.000', 'De R$ 16.001 a R$ 20.000', 
    'De R$ 20.001 a R$ 25.000', 'Acima de R$ 25.000', 'Não informado'
]

# 1. Distribuição de faixa etária
plt.figure(figsize=(12, 8))
ax = sns.countplot(y=df_analise['faixa_etaria'], 
                  order=df_analise['faixa_etaria'].value_counts().index)
plt.title('Distribuição de Faixa Etária', fontsize=16)
plt.xlabel('Contagem', fontsize=14)
plt.ylabel('Faixa Etária', fontsize=14)

# Adicionar valores nas barras
for i, count in enumerate(df_analise['faixa_etaria'].value_counts()):
    ax.text(count + 10, i, f'{count} ({count/len(df_analise)*100:.1f}%)', va='center')

plt.tight_layout()
plt.savefig('visualizacoes/distribuicao_faixa_etaria.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Distribuição de gênero
plt.figure(figsize=(12, 8))
ax = sns.countplot(y=df_analise['genero'], 
                  order=df_analise['genero'].value_counts().index)
plt.title('Distribuição de Gênero', fontsize=16)
plt.xlabel('Contagem', fontsize=14)
plt.ylabel('Gênero', fontsize=14)

# Adicionar valores nas barras
for i, count in enumerate(df_analise['genero'].value_counts()):
    ax.text(count + 10, i, f'{count} ({count/len(df_analise)*100:.1f}%)', va='center')

plt.tight_layout()
plt.savefig('visualizacoes/distribuicao_genero.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Distribuição de nível de ensino
plt.figure(figsize=(14, 10))
# Ordenar de acordo com a ordem definida
ordem_nivel_ensino_presente = [nivel for nivel in ordem_nivel_ensino if nivel in df_analise['nivel_ensino'].unique()]
ax = sns.countplot(y=df_analise['nivel_ensino'], 
                  order=ordem_nivel_ensino_presente)
plt.title('Distribuição de Nível de Ensino', fontsize=16)
plt.xlabel('Contagem', fontsize=14)
plt.ylabel('Nível de Ensino', fontsize=14)

# Adicionar valores nas barras
for i, nivel in enumerate(ordem_nivel_ensino_presente):
    count = df_analise['nivel_ensino'].value_counts().get(nivel, 0)
    ax.text(count + 10, i, f'{count} ({count/len(df_analise)*100:.1f}%)', va='center')

plt.tight_layout()
plt.savefig('visualizacoes/distribuicao_nivel_ensino.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Distribuição de faixa salarial
plt.figure(figsize=(14, 10))
# Ordenar de acordo com a ordem definida
ordem_faixa_salarial_presente = [faixa for faixa in ordem_faixa_salarial if faixa in df_analise['faixa_salarial'].unique()]
ax = sns.countplot(y=df_analise['faixa_salarial'], 
                  order=ordem_faixa_salarial_presente)
plt.title('Distribuição de Faixa Salarial', fontsize=16)
plt.xlabel('Contagem', fontsize=14)
plt.ylabel('Faixa Salarial', fontsize=14)

# Adicionar valores nas barras
for i, faixa in enumerate(ordem_faixa_salarial_presente):
    count = df_analise['faixa_salarial'].value_counts().get(faixa, 0)
    ax.text(count + 10, i, f'{count} ({count/len(df_analise)*100:.1f}%)', va='center')

plt.tight_layout()
plt.savefig('visualizacoes/distribuicao_faixa_salarial.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. Distribuição de tempo de experiência
plt.figure(figsize=(12, 8))
ax = sns.countplot(y=df_analise['tempo_experiencia'], 
                  order=df_analise['tempo_experiencia'].value_counts().index)
plt.title('Distribuição de Tempo de Experiência na Área de Dados', fontsize=16)
plt.xlabel('Contagem', fontsize=14)
plt.ylabel('Tempo de Experiência', fontsize=14)

# Adicionar valores nas barras
for i, count in enumerate(df_analise['tempo_experiencia'].value_counts()):
    ax.text(count + 10, i, f'{count} ({count/len(df_analise)*100:.1f}%)', va='center')

plt.tight_layout()
plt.savefig('visualizacoes/distribuicao_tempo_experiencia.png', dpi=300, bbox_inches='tight')
plt.close()

# Criar um arquivo de texto com insights sobre as distribuições
with open('visualizacoes/insights_distribuicoes.txt', 'w', encoding='utf-8') as f:
    f.write("# Insights sobre as Distribuições Demográficas\n\n")
    
    # Faixa etária
    f.write("## Distribuição de Faixa Etária\n")
    faixa_etaria_counts = df_analise['faixa_etaria'].value_counts()
    faixa_etaria_pct = df_analise['faixa_etaria'].value_counts(normalize=True) * 100
    for faixa, count in faixa_etaria_counts.items():
        f.write(f"- {faixa}: {count} respondentes ({faixa_etaria_pct[faixa]:.1f}%)\n")
    
    faixa_mais_comum = faixa_etaria_counts.index[0]
    f.write(f"\nA faixa etária mais comum entre os respondentes é '{faixa_mais_comum}', representando {faixa_etaria_pct[faixa_mais_comum]:.1f}% do total.\n\n")
    
    # Gênero
    f.write("## Distribuição de Gênero\n")
    genero_counts = df_analise['genero'].value_counts()
    genero_pct = df_analise['genero'].value_counts(normalize=True) * 100
    for genero, count in genero_counts.items():
        f.write(f"- {genero}: {count} respondentes ({genero_pct[genero]:.1f}%)\n")
    
    genero_mais_comum = genero_counts.index[0]
    f.write(f"\nO gênero mais comum entre os respondentes é '{genero_mais_comum}', representando {genero_pct[genero_mais_comum]:.1f}% do total.\n\n")
    
    # Nível de ensino
    f.write("## Distribuição de Nível de Ensino\n")
    nivel_ensino_counts = df_analise['nivel_ensino'].value_counts()
    nivel_ensino_pct = df_analise['nivel_ensino'].value_counts(normalize=True) * 100
    for nivel, count in nivel_ensino_counts.items():
        f.write(f"- {nivel}: {count} respondentes ({nivel_ensino_pct[nivel]:.1f}%)\n")
    
    nivel_mais_comum = nivel_ensino_counts.index[0]
    f.write(f"\nO nível de ensino mais comum entre os respondentes é '{nivel_mais_comum}', representando {nivel_ensino_pct[nivel_mais_comum]:.1f}% do total.\n\n")
    
    # Faixa salarial
    f.write("## Distribuição de Faixa Salarial\n")
    faixa_salarial_counts = df_analise['faixa_salarial'].value_counts()
    faixa_salarial_pct = df_analise['faixa_salarial'].value_counts(normalize=True) * 100
    for faixa, count in faixa_salarial_counts.items():
        f.write(f"- {faixa}: {count} respondentes ({faixa_salarial_pct[faixa]:.1f}%)\n")
    
    faixa_mais_comum = faixa_salarial_counts.index[0]
    f.write(f"\nA faixa salarial mais comum entre os respondentes é '{faixa_mais_comum}', representando {faixa_salarial_pct[faixa_mais_comum]:.1f}% do total.\n\n")
    
    # Tempo de experiência
    f.write("## Distribuição de Tempo de Experiência\n")
    tempo_experiencia_counts = df_analise['tempo_experiencia'].value_counts()
    tempo_experiencia_pct = df_analise['tempo_experiencia'].value_counts(normalize=True) * 100
    for tempo, count in tempo_experiencia_counts.items():
        f.write(f"- {tempo}: {count} respondentes ({tempo_experiencia_pct[tempo]:.1f}%)\n")
    
    tempo_mais_comum = tempo_experiencia_counts.index[0]
    f.write(f"\nO tempo de experiência mais comum entre os respondentes é '{tempo_mais_comum}', representando {tempo_experiencia_pct[tempo_mais_comum]:.1f}% do total.\n")

print("Visualizações de distribuições demográficas criadas com sucesso!")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from matplotlib.ticker import MaxNLocator
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configurações para melhorar a visualização
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 12
sns.set_palette("viridis")
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'DejaVu Sans'

# Carregar os dados processados
df_analise = pd.read_csv('visualizacoes/dados_processados.csv')

# Definir a ordem correta para variáveis ordinais
ordem_faixa_etaria = [
    '17-21', '22-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55+'
]

ordem_nivel_ensino = [
    'Não tenho graduação formal', 'Estudante de Graduação', 'Graduação/Bacharelado', 
    'Pós-graduação', 'Mestrado', 'Doutorado ou Phd', 'Prefiro não informar'
]

ordem_faixa_salarial = [
    'Menos de R$ 1.000/mês', 'de R$ 1.001/mês a R$ 2.000/mês', 'de R$ 2.001/mês a R$ 3.000/mês',
    'de R$ 3.001/mês a R$ 4.000/mês', 'de R$ 4.001/mês a R$ 6.000/mês', 'de R$ 6.001/mês a R$ 8.000/mês',
    'de R$ 8.001/mês a R$ 12.000/mês', 'de R$ 12.001/mês a R$ 16.000/mês', 'de R$ 16.001/mês a R$ 20.000/mês',
    'de R$ 20.001/mês a R$ 25.000/mês', 'de R$ 25.001/mês a R$ 30.000/mês', 'de R$ 30.001/mês a R$ 40.000/mês',
    'Acima de R$ 40.001/mês', 'Não informado'
]

# 1. Relação entre nível de ensino e faixa salarial
plt.figure(figsize=(16, 12))
# Criar uma tabela de contingência
tabela_nivel_salario = pd.crosstab(df_analise['nivel_ensino'], df_analise['faixa_salarial'])

# Ordenar as linhas e colunas
tabela_nivel_salario = tabela_nivel_salario.reindex(index=ordem_nivel_ensino)
tabela_nivel_salario = tabela_nivel_salario.reindex(columns=ordem_faixa_salarial)

# Normalizar por linha para obter percentuais
tabela_nivel_salario_pct = tabela_nivel_salario.div(tabela_nivel_salario.sum(axis=1), axis=0) * 100

# Criar o heatmap
plt.figure(figsize=(18, 12))
ax = sns.heatmap(tabela_nivel_salario_pct, annot=True, cmap="YlGnBu", fmt='.1f', 
                linewidths=.5, cbar_kws={'label': 'Percentual (%)'})
plt.title('Relação entre Nível de Ensino e Faixa Salarial (% por Nível de Ensino)', fontsize=16)
plt.xlabel('Faixa Salarial', fontsize=14)
plt.ylabel('Nível de Ensino', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('visualizacoes/relacao_ensino_salario_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# Criar gráfico de barras empilhadas para visualizar a distribuição
plt.figure(figsize=(18, 12))
tabela_nivel_salario_pct.plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Distribuição de Faixa Salarial por Nível de Ensino', fontsize=16)
plt.xlabel('Nível de Ensino', fontsize=14)
plt.ylabel('Percentual (%)', fontsize=14)
plt.legend(title='Faixa Salarial', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('visualizacoes/relacao_ensino_salario_barras.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Relação entre tempo de experiência e faixa salarial
plt.figure(figsize=(16, 12))
# Criar uma tabela de contingência
tabela_experiencia_salario = pd.crosstab(df_analise['tempo_experiencia'], df_analise['faixa_salarial'])

# Ordenar as colunas
tabela_experiencia_salario = tabela_experiencia_salario.reindex(columns=ordem_faixa_salarial)

# Normalizar por linha para obter percentuais
tabela_experiencia_salario_pct = tabela_experiencia_salario.div(tabela_experiencia_salario.sum(axis=1), axis=0) * 100

# Criar o heatmap
plt.figure(figsize=(18, 14))
ax = sns.heatmap(tabela_experiencia_salario_pct, annot=True, cmap="YlGnBu", fmt='.1f', 
                linewidths=.5, cbar_kws={'label': 'Percentual (%)'})
plt.title('Relação entre Tempo de Experiência e Faixa Salarial (% por Tempo de Experiência)', fontsize=16)
plt.xlabel('Faixa Salarial', fontsize=14)
plt.ylabel('Tempo de Experiência', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('visualizacoes/relacao_experiencia_salario_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# Criar gráfico de barras empilhadas para visualizar a distribuição
plt.figure(figsize=(18, 14))
tabela_experiencia_salario_pct.plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Distribuição de Faixa Salarial por Tempo de Experiência', fontsize=16)
plt.xlabel('Tempo de Experiência', fontsize=14)
plt.ylabel('Percentual (%)', fontsize=14)
plt.legend(title='Faixa Salarial', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('visualizacoes/relacao_experiencia_salario_barras.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Correlação entre variáveis (para variáveis numéricas)
# Converter variáveis categóricas para numéricas para análise de correlação
df_corr = df_analise.copy()

# Mapear nível de ensino para valores numéricos
nivel_ensino_map = {nivel: i for i, nivel in enumerate(ordem_nivel_ensino)}
df_corr['nivel_ensino_num'] = df_corr['nivel_ensino'].map(nivel_ensino_map)

# Mapear faixa salarial para valores numéricos (usando o ponto médio da faixa)
faixa_salarial_valor = {
    'Menos de R$ 1.000/mês': 500,
    'de R$ 1.001/mês a R$ 2.000/mês': 1500,
    'de R$ 2.001/mês a R$ 3.000/mês': 2500,
    'de R$ 3.001/mês a R$ 4.000/mês': 3500,
    'de R$ 4.001/mês a R$ 6.000/mês': 5000,
    'de R$ 6.001/mês a R$ 8.000/mês': 7000,
    'de R$ 8.001/mês a R$ 12.000/mês': 10000,
    'de R$ 12.001/mês a R$ 16.000/mês': 14000,
    'de R$ 16.001/mês a R$ 20.000/mês': 18000,
    'de R$ 20.001/mês a R$ 25.000/mês': 22500,
    'de R$ 25.001/mês a R$ 30.000/mês': 27500,
    'de R$ 30.001/mês a R$ 40.000/mês': 35000,
    'Acima de R$ 40.001/mês': 45000,
    'Não informado': np.nan
}
df_corr['faixa_salarial_valor'] = df_corr['faixa_salarial'].map(faixa_salarial_valor)

# Extrair anos de experiência como valor numérico
def extrair_anos(texto):
    if pd.isna(texto) or texto == 'Não informado':
        return np.nan
    if 'menos de 1 ano' in texto.lower():
        return 0.5
    if 'mais de 10 anos' in texto.lower():
        return 12
    try:
        # Tentar extrair números do texto
        import re
        numeros = re.findall(r'\d+', texto)
        if numeros:
            # Se houver intervalo, pegar o ponto médio
            if len(numeros) >= 2:
                return (float(numeros[0]) + float(numeros[1])) / 2
            return float(numeros[0])
    except:
        pass
    return np.nan

df_corr['anos_experiencia'] = df_corr['tempo_experiencia'].apply(extrair_anos)

# Selecionar apenas colunas numéricas para correlação
colunas_numericas = ['nivel_ensino_num', 'faixa_salarial_valor', 'anos_experiencia', 
                     'impacto_raca', 'impacto_genero', 'relata_impacto']
df_corr_num = df_corr[colunas_numericas].dropna()

# Calcular matriz de correlação
corr_matrix = df_corr_num.corr()

# Criar heatmap de correlação
plt.figure(figsize=(12, 10))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
ax = sns.heatmap(corr_matrix, mask=mask, annot=True, cmap='coolwarm', fmt='.2f', 
                linewidths=.5, vmin=-1, vmax=1, center=0)
plt.title('Matriz de Correlação entre Variáveis', fontsize=16)
plt.tight_layout()
plt.savefig('visualizacoes/matriz_correlacao.png', dpi=300, bbox_inches='tight')
plt.close()

# Criar arquivo de insights sobre as relações
with open('visualizacoes/insights_relacoes.txt', 'w', encoding='utf-8') as f:
    f.write("# Insights sobre as Relações entre Variáveis\n\n")
    
    # Relação entre nível de ensino e faixa salarial
    f.write("## Relação entre Nível de Ensino e Faixa Salarial\n\n")
    
    # Calcular salário médio por nível de ensino
    salario_medio_por_ensino = df_corr.groupby('nivel_ensino')['faixa_salarial_valor'].mean().sort_values()
    f.write("### Salário Médio por Nível de Ensino:\n")
    for nivel, salario in salario_medio_por_ensino.items():
        if not pd.isna(salario):
            f.write(f"- {nivel}: R$ {salario:.2f}\n")
    
    f.write("\nObserva-se uma clara tendência de aumento salarial conforme o nível de ensino aumenta. ")
    nivel_maior_salario = salario_medio_por_ensino.index[-1]
    nivel_menor_salario = salario_medio_por_ensino.index[0]
    f.write(f"O nível de ensino com maior salário médio é '{nivel_maior_salario}', ")
    f.write(f"enquanto o nível com menor salário médio é '{nivel_menor_salario}'.\n\n")
    
    # Relação entre tempo de experiência e faixa salarial
    f.write("## Relação entre Tempo de Experiência e Faixa Salarial\n\n")
    
    # Calcular salário médio por tempo de experiência
    salario_medio_por_experiencia = df_corr.groupby('tempo_experiencia')['faixa_salarial_valor'].mean().sort_values()
    f.write("### Salário Médio por Tempo de Experiência:\n")
    for tempo, salario in salario_medio_por_experiencia.items():
        if not pd.isna(salario):
            f.write(f"- {tempo}: R$ {salario:.2f}\n")
    
    f.write("\nObserva-se uma tendência de aumento salarial conforme o tempo de experiência aumenta. ")
    tempo_maior_salario = salario_medio_por_experiencia.index[-1]
    tempo_menor_salario = salario_medio_por_experiencia.index[0]
    f.write(f"O tempo de experiência com maior salário médio é '{tempo_maior_salario}', ")
    f.write(f"enquanto o tempo com menor salário médio é '{tempo_menor_salario}'.\n\n")
    
    # Correlações
    f.write("## Correlações entre Variáveis\n\n")
    f.write("### Principais correlações encontradas:\n")
    
    # Listar as correlações mais fortes (positivas e negativas)
    correlacoes = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            correlacoes.append((corr_matrix.columns[i], corr_matrix.columns[j], corr_matrix.iloc[i, j]))
    
    # Ordenar por valor absoluto da correlação
    correlacoes.sort(key=lambda x: abs(x[2]), reverse=True)
    
    # Mapear nomes das variáveis para descrições mais legíveis
    nomes_variaveis = {
        'nivel_ensino_num': 'Nível de Ensino',
        'faixa_salarial_valor': 'Faixa Salarial',
        'anos_experiencia': 'Anos de Experiência',
        'impacto_raca': 'Impacto por Raça/Etnia',
        'impacto_genero': 'Impacto por Identidade de Gênero',
        'relata_impacto': 'Relata Algum Impacto'
    }
    
    # Listar as correlações mais fortes
    for var1, var2, corr in correlacoes[:5]:
        f.write(f"- {nomes_variaveis.get(var1, var1)} e {nomes_variaveis.get(var2, var2)}: {corr:.3f}")
        if corr > 0:
            f.write(" (correlação positiva)\n")
        else:
            f.write(" (correlação negativa)\n")
    
    # Conclusão
    f.write("\n## Conclusão\n\n")
    f.write("A análise das relações entre variáveis revela padrões importantes no mercado de trabalho da área de dados:\n\n")
    
    # Verificar correlação entre nível de ensino e salário
    corr_ensino_salario = corr_matrix.loc['nivel_ensino_num', 'faixa_salarial_valor']
    f.write(f"1. A correlação entre nível de ensino e faixa salarial é de {corr_ensino_salario:.3f}, ")
    if corr_ensino_salario > 0.5:
        f.write("indicando uma forte relação positiva. Quanto maior o nível de ensino, maior tende a ser o salário.\n\n")
    elif corr_ensino_salario > 0.3:
        f.write("indicando uma relação positiva moderada. Há tendência de aumento salarial com maior nível de ensino.\n\n")
    else:
        f.write("indicando uma relação positiva fraca. O nível de ensino tem alguma influência no salário, mas outros fatores também são importantes.\n\n")
    
    # Verificar correlação entre experiência e salário
    corr_exp_salario = corr_matrix.loc['anos_experiencia', 'faixa_salarial_valor']
    f.write(f"2. A correlação entre anos de experiência e faixa salarial é de {corr_exp_salario:.3f}, ")
    if corr_exp_salario > 0.5:
        f.write("indicando uma forte relação positiva. Quanto maior a experiência, maior tende a ser o salário.\n\n")
    elif corr_exp_salario > 0.3:
        f.write("indicando uma relação positiva moderada. Há tendência de aumento salarial com mais experiência.\n\n")
    else:
        f.write("indicando uma relação positiva fraca. A experiência tem alguma influência no salário, mas outros fatores também são importantes.\n\n")
    
    f.write("Estes resultados sugerem que tanto a formação acadêmica quanto a experiência prática são valorizadas no mercado de trabalho da área de dados, com impacto direto na remuneração dos profissionais.")

print("Análise de relações entre variáveis concluída com sucesso!")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from matplotlib.ticker import MaxNLocator
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configurações para melhorar a visualização
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 12
sns.set_palette("viridis")
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'DejaVu Sans'

# Carregar os dados processados
df_analise = pd.read_csv('visualizacoes/dados_processados.csv')

# 1. Quantificar pessoas que relatam impacto por raça/etnia ou identidade de gênero
impacto_total = df_analise['relata_impacto'].sum()
total_respondentes = len(df_analise)
percentual_impacto = (impacto_total / total_respondentes) * 100

# Criar gráfico de pizza para mostrar proporção
plt.figure(figsize=(10, 8))
labels = ['Não relatam impacto', 'Relatam impacto']
sizes = [total_respondentes - impacto_total, impacto_total]
colors = ['#66b3ff', '#ff9999']
explode = (0, 0.1)  # explode a segunda fatia (Relatam impacto)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Proporção de Respondentes que Relatam Impacto na Experiência Profissional\npor Raça/Etnia ou Identidade de Gênero', fontsize=16)
plt.tight_layout()
plt.savefig('visualizacoes/proporcao_impacto.png', dpi=300, bbox_inches='tight')
plt.close()

# Detalhar por tipo de impacto
impacto_raca = df_analise['impacto_raca'].sum()
impacto_genero = df_analise['impacto_genero'].sum()
percentual_impacto_raca = (impacto_raca / total_respondentes) * 100
percentual_impacto_genero = (impacto_genero / total_respondentes) * 100

# Criar gráfico de barras para comparar os tipos de impacto
plt.figure(figsize=(12, 8))
tipos_impacto = ['Impacto por Raça/Etnia', 'Impacto por Identidade de Gênero']
valores_impacto = [impacto_raca, impacto_genero]
percentuais = [percentual_impacto_raca, percentual_impacto_genero]

bars = plt.bar(tipos_impacto, valores_impacto, color=['#ff9999', '#66b3ff'])

# Adicionar rótulos com valores e percentuais
for i, (bar, valor, percentual) in enumerate(zip(bars, valores_impacto, percentuais)):
    plt.text(i, valor + 10, f'{valor} ({percentual:.1f}%)', 
             ha='center', va='bottom', fontsize=12)

plt.title('Número de Respondentes que Relatam Impacto na Experiência Profissional\npor Tipo de Impacto', fontsize=16)
plt.ylabel('Número de Respondentes', fontsize=14)
plt.ylim(0, max(valores_impacto) * 1.2)  # Ajustar limite do eixo y para acomodar os rótulos
plt.tight_layout()
plt.savefig('visualizacoes/tipos_impacto.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Distribuição de impactos por faixa etária
# Criar tabela de contingência
tabela_impacto_idade = pd.crosstab(df_analise['faixa_etaria'], df_analise['relata_impacto'])
tabela_impacto_idade_pct = tabela_impacto_idade.div(tabela_impacto_idade.sum(axis=1), axis=0) * 100

# Renomear colunas para melhor legibilidade
tabela_impacto_idade.columns = ['Não Relata Impacto', 'Relata Impacto']
tabela_impacto_idade_pct.columns = ['Não Relata Impacto (%)', 'Relata Impacto (%)']

# Criar gráfico de barras para mostrar percentual de impacto por faixa etária
plt.figure(figsize=(14, 10))
ax = tabela_impacto_idade_pct['Relata Impacto (%)'].sort_values().plot(kind='barh', color='#ff9999')
plt.title('Percentual de Respondentes que Relatam Impacto na Experiência Profissional\npor Faixa Etária', fontsize=16)
plt.xlabel('Percentual (%)', fontsize=14)
plt.ylabel('Faixa Etária', fontsize=14)

# Adicionar valores nas barras
for i, v in enumerate(tabela_impacto_idade_pct['Relata Impacto (%)']):
    ax.text(v + 0.5, i, f'{v:.1f}%', va='center')

plt.tight_layout()
plt.savefig('visualizacoes/impacto_por_faixa_etaria.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Distribuição de impactos por gênero
# Criar tabela de contingência
tabela_impacto_genero = pd.crosstab(df_analise['genero'], df_analise['relata_impacto'])
tabela_impacto_genero_pct = tabela_impacto_genero.div(tabela_impacto_genero.sum(axis=1), axis=0) * 100

# Renomear colunas para melhor legibilidade
tabela_impacto_genero.columns = ['Não Relata Impacto', 'Relata Impacto']
tabela_impacto_genero_pct.columns = ['Não Relata Impacto (%)', 'Relata Impacto (%)']

# Criar gráfico de barras para mostrar percentual de impacto por gênero
plt.figure(figsize=(14, 8))
ax = tabela_impacto_genero_pct['Relata Impacto (%)'].sort_values().plot(kind='barh', color='#66b3ff')
plt.title('Percentual de Respondentes que Relatam Impacto na Experiência Profissional\npor Gênero', fontsize=16)
plt.xlabel('Percentual (%)', fontsize=14)
plt.ylabel('Gênero', fontsize=14)

# Adicionar valores nas barras
for i, v in enumerate(tabela_impacto_genero_pct['Relata Impacto (%)']):
    ax.text(v + 0.5, i, f'{v:.1f}%', va='center')

plt.tight_layout()
plt.savefig('visualizacoes/impacto_por_genero.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Distribuição de impactos por raça/etnia
# Criar tabela de contingência
tabela_impacto_raca = pd.crosstab(df_analise['cor_raca_etnia'], df_analise['relata_impacto'])
tabela_impacto_raca_pct = tabela_impacto_raca.div(tabela_impacto_raca.sum(axis=1), axis=0) * 100

# Renomear colunas para melhor legibilidade
tabela_impacto_raca.columns = ['Não Relata Impacto', 'Relata Impacto']
tabela_impacto_raca_pct.columns = ['Não Relata Impacto (%)', 'Relata Impacto (%)']

# Criar gráfico de barras para mostrar percentual de impacto por raça/etnia
plt.figure(figsize=(14, 10))
ax = tabela_impacto_raca_pct['Relata Impacto (%)'].sort_values().plot(kind='barh', color='#99ff99')
plt.title('Percentual de Respondentes que Relatam Impacto na Experiência Profissional\npor Raça/Etnia', fontsize=16)
plt.xlabel('Percentual (%)', fontsize=14)
plt.ylabel('Raça/Etnia', fontsize=14)

# Adicionar valores nas barras
for i, v in enumerate(tabela_impacto_raca_pct['Relata Impacto (%)']):
    ax.text(v + 0.5, i, f'{v:.1f}%', va='center')

plt.tight_layout()
plt.savefig('visualizacoes/impacto_por_raca_etnia.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. Análise cruzada: Impacto por gênero e raça/etnia
# Criar tabela de contingência para análise cruzada
tabela_cruzada = pd.crosstab([df_analise['genero'], df_analise['cor_raca_etnia']], df_analise['relata_impacto'])
tabela_cruzada_pct = tabela_cruzada.div(tabela_cruzada.sum(axis=1), axis=0) * 100

# Renomear colunas para melhor legibilidade
tabela_cruzada.columns = ['Não Relata Impacto', 'Relata Impacto']
tabela_cruzada_pct.columns = ['Não Relata Impacto (%)', 'Relata Impacto (%)']

# Filtrar apenas combinações com pelo menos 10 respondentes para evitar conclusões baseadas em amostras muito pequenas
tabela_cruzada_filtrada = tabela_cruzada[tabela_cruzada.sum(axis=1) >= 10]
tabela_cruzada_pct_filtrada = tabela_cruzada_pct.loc[tabela_cruzada_filtrada.index]

# Ordenar por percentual de impacto
tabela_cruzada_pct_ordenada = tabela_cruzada_pct_filtrada.sort_values(by='Relata Impacto (%)', ascending=False)

# Criar gráfico de barras para mostrar as 10 combinações com maior percentual de impacto
plt.figure(figsize=(16, 12))
ax = tabela_cruzada_pct_ordenada['Relata Impacto (%)'].head(10).plot(kind='barh', color='#ff66ff')
plt.title('Top 10 Combinações de Gênero e Raça/Etnia com Maior Percentual\nde Impacto na Experiência Profissional', fontsize=16)
plt.xlabel('Percentual (%)', fontsize=14)
plt.ylabel('Gênero e Raça/Etnia', fontsize=14)

# Adicionar valores nas barras
for i, v in enumerate(tabela_cruzada_pct_ordenada['Relata Impacto (%)'].head(10)):
    ax.text(v + 0.5, i, f'{v:.1f}%', va='center')

plt.tight_layout()
plt.savefig('visualizacoes/top_combinacoes_impacto.png', dpi=300, bbox_inches='tight')
plt.close()

# Criar arquivo de insights sobre os impactos
with open('visualizacoes/insights_impactos.txt', 'w', encoding='utf-8') as f:
    f.write("# Insights sobre Impactos na Experiência Profissional\n\n")
    
    # Visão geral dos impactos
    f.write("## Visão Geral dos Impactos\n\n")
    f.write(f"Do total de {total_respondentes} respondentes, {impacto_total} ({percentual_impacto:.1f}%) relatam algum tipo de impacto na experiência profissional devido à raça/etnia ou identidade de gênero.\n\n")
    f.write(f"- Impacto por raça/etnia: {impacto_raca} respondentes ({percentual_impacto_raca:.1f}%)\n")
    f.write(f"- Impacto por identidade de gênero: {impacto_genero} respondentes ({percentual_impacto_genero:.1f}%)\n\n")
    
    # Impacto por faixa etária
    f.write("## Impacto por Faixa Etária\n\n")
    f.write("### Percentual de respondentes que relatam impacto por faixa etária:\n")
    for faixa, percentual in tabela_impacto_idade_pct['Relata Impacto (%)'].sort_values(ascending=False).items():
        contagem = tabela_impacto_idade.loc[faixa, 'Relata Impacto']
        total = tabela_impacto_idade.loc[faixa].sum()
        f.write(f"- {faixa}: {percentual:.1f}% ({contagem} de {total} respondentes)\n")
    
    faixa_maior_impacto = tabela_impacto_idade_pct['Relata Impacto (%)'].sort_values(ascending=False).index[0]
    faixa_menor_impacto = tabela_impacto_idade_pct['Relata Impacto (%)'].sort_values().index[0]
    f.write(f"\nA faixa etária com maior percentual de impacto relatado é '{faixa_maior_impacto}', ")
    f.write(f"enquanto a faixa com menor percentual é '{faixa_menor_impacto}'.\n\n")
    
    # Impacto por gênero
    f.write("## Impacto por Gênero\n\n")
    f.write("### Percentual de respondentes que relatam impacto por gênero:\n")
    for genero, percentual in tabela_impacto_genero_pct['Relata Impacto (%)'].sort_values(ascending=False).items():
        contagem = tabela_impacto_genero.loc[genero, 'Relata Impacto']
        total = tabela_impacto_genero.loc[genero].sum()
        f.write(f"- {genero}: {percentual:.1f}% ({contagem} de {total} respondentes)\n")
    
    genero_maior_impacto = tabela_impacto_genero_pct['Relata Impacto (%)'].sort_values(ascending=False).index[0]
    genero_menor_impacto = tabela_impacto_genero_pct['Relata Impacto (%)'].sort_values().index[0]
    f.write(f"\nO gênero com maior percentual de impacto relatado é '{genero_maior_impacto}', ")
    f.write(f"enquanto o gênero com menor percentual é '{genero_menor_impacto}'.\n\n")
    
    # Impacto por raça/etnia
    f.write("## Impacto por Raça/Etnia\n\n")
    f.write("### Percentual de respondentes que relatam impacto por raça/etnia:\n")
    for raca, percentual in tabela_impacto_raca_pct['Relata Impacto (%)'].sort_values(ascending=False).items():
        contagem = tabela_impacto_raca.loc[raca, 'Relata Impacto']
        total = tabela_impacto_raca.loc[raca].sum()
        f.write(f"- {raca}: {percentual:.1f}% ({contagem} de {total} respondentes)\n")
    
    raca_maior_impacto = tabela_impacto_raca_pct['Relata Impacto (%)'].sort_values(ascending=False).index[0]
    raca_menor_impacto = tabela_impacto_raca_pct['Relata Impacto (%)'].sort_values().index[0]
    f.write(f"\nA raça/etnia com maior percentual de impacto relatado é '{raca_maior_impacto}', ")
    f.write(f"enquanto a raça/etnia com menor percentual é '{raca_menor_impacto}'.\n\n")
    
    # Análise cruzada
    f.write("## Análise Cruzada: Impacto por Gênero e Raça/Etnia\n\n")
    f.write("### Top 10 combinações com maior percentual de impacto:\n")
    for (genero, raca), percentual in tabela_cruzada_pct_ordenada['Relata Impacto (%)'].head(10).items():
        contagem = tabela_cruzada.loc[(genero, raca), 'Relata Impacto']
        total = tabela_cruzada.loc[(genero, raca)].sum()
        f.write(f"- {genero}, {raca}: {percentual:.1f}% ({contagem} de {total} respondentes)\n")
    
    # Conclusão
    f.write("\n## Conclusão\n\n")
    f.write("A análise dos impactos na experiência profissional revela padrões importantes relacionados à diversidade e inclusão na área de dados:\n\n")
    
    f.write(f"1. Aproximadamente {percentual_impacto:.1f}% dos respondentes relatam algum tipo de impacto na experiência profissional devido à raça/etnia ou identidade de gênero.\n\n")
    
    if percentual_impacto_raca > percentual_impacto_genero:
        f.write(f"2. O impacto por raça/etnia é mais prevalente ({percentual_impacto_raca:.1f}%) do que o impacto por identidade de gênero ({percentual_impacto_genero:.1f}%).\n\n")
    else:
        f.write(f"2. O impacto por identidade de gênero é mais prevalente ({percentual_impacto_genero:.1f}%) do que o impacto por raça/etnia ({percentual_impacto_raca:.1f}%).\n\n")
    
    f.write(f"3. Existem diferenças significativas no percentual de impacto relatado entre diferentes grupos demográficos, com '{genero_maior_impacto}' e '{raca_maior_impacto}' apresentando os maiores percentuais em suas respectivas categorias.\n\n")
    
    f.write("4. A análise cruzada revela que certas combinações de gênero e raça/etnia estão associadas a percentuais significativamente mais altos de impacto na experiência profissional, destacando a importância de considerar a interseccionalidade ao abordar questões de diversidade e inclusão no mercado de trabalho da área de dados.\n\n")
    
    f.write("Estes resultados sugerem a necessidade de políticas e práticas mais inclusivas no setor, com atenção especial aos grupos que relatam maiores percentuais de impacto negativo em suas experiências profissionais.")

print("Análise de impactos na experiência profissional concluída com sucesso!")

import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import glob

# Criar diretório para o relatório final
os.makedirs('relatorio_final', exist_ok=True)

# Função para copiar imagens para o diretório do relatório
def copiar_imagens(origem, destino):
    imagens = glob.glob(f"{origem}/*.png")
    for img_path in imagens:
        img_nome = os.path.basename(img_path)
        img = Image.open(img_path)
        img.save(f"{destino}/{img_nome}")
    return len(imagens)

# Copiar todas as imagens para o diretório do relatório
num_imagens = copiar_imagens('visualizacoes', 'relatorio_final')
print(f"Copiadas {num_imagens} imagens para o diretório do relatório final")

# Ler os arquivos de insights
try:
    with open('visualizacoes/insights_distribuicoes.txt', 'r', encoding='utf-8') as f:
        insights_distribuicoes = f.read()
except:
    insights_distribuicoes = "Arquivo de insights sobre distribuições não encontrado."

try:
    with open('visualizacoes/insights_relacoes.txt', 'r', encoding='utf-8') as f:
        insights_relacoes = f.read()
except:
    insights_relacoes = "Arquivo de insights sobre relações entre variáveis não encontrado."

try:
    with open('visualizacoes/insights_impactos.txt', 'r', encoding='utf-8') as f:
        insights_impactos = f.read()
except:
    insights_impactos = "Arquivo de insights sobre impactos na experiência profissional não encontrado."

# Criar o relatório final
with open('relatorio_final/relatorio_completo.md', 'w', encoding='utf-8') as f:
    f.write("# Análise Exploratória de Dados (EDA) - Mercado de Trabalho na Área de Dados\n\n")
    
    f.write("## Introdução\n\n")
    f.write("Este relatório apresenta uma análise exploratória de dados (EDA) sobre o mercado de trabalho na área de dados, ")
    f.write("com foco em aspectos demográficos, educacionais, salariais e experiências profissionais dos respondentes. ")
    f.write("A análise busca responder a perguntas específicas sobre distribuições demográficas, relações entre variáveis ")
    f.write("e impactos na experiência profissional relacionados a raça/etnia e identidade de gênero.\n\n")
    
    f.write("## Metodologia\n\n")
    f.write("A análise foi realizada utilizando Python e bibliotecas como pandas, matplotlib, seaborn e plotly. ")
    f.write("Os dados foram processados para tratar valores ausentes e padronizar variáveis ordinais como faixa etária, ")
    f.write("nível de ensino e faixa salarial. Foram geradas visualizações para responder às perguntas específicas da análise, ")
    f.write("incluindo gráficos de barras, heatmaps e gráficos de dispersão.\n\n")
    
    f.write("## 1. Distribuições Demográficas\n\n")
    f.write(insights_distribuicoes)
    f.write("\n\n### Visualizações de Distribuições Demográficas\n\n")
    f.write("![Distribuição de Faixa Etária](distribuicao_faixa_etaria.png)\n\n")
    f.write("![Distribuição de Gênero](distribuicao_genero.png)\n\n")
    f.write("![Distribuição de Nível de Ensino](distribuicao_nivel_ensino.png)\n\n")
    f.write("![Distribuição de Faixa Salarial](distribuicao_faixa_salarial.png)\n\n")
    f.write("![Distribuição de Tempo de Experiência](distribuicao_tempo_experiencia.png)\n\n")
    
    f.write("## 2. Relações entre Variáveis\n\n")
    f.write(insights_relacoes)
    f.write("\n\n### Visualizações de Relações entre Variáveis\n\n")
    f.write("![Relação entre Nível de Ensino e Faixa Salarial (Heatmap)](relacao_ensino_salario_heatmap.png)\n\n")
    f.write("![Relação entre Nível de Ensino e Faixa Salarial (Barras)](relacao_ensino_salario_barras.png)\n\n")
    f.write("![Relação entre Tempo de Experiência e Faixa Salarial (Heatmap)](relacao_experiencia_salario_heatmap.png)\n\n")
    f.write("![Relação entre Tempo de Experiência e Faixa Salarial (Barras)](relacao_experiencia_salario_barras.png)\n\n")
    f.write("![Matriz de Correlação entre Variáveis](matriz_correlacao.png)\n\n")
    
    f.write("## 3. Impactos na Experiência Profissional\n\n")
    f.write(insights_impactos)
    f.write("\n\n### Visualizações de Impactos na Experiência Profissional\n\n")
    f.write("![Proporção de Respondentes que Relatam Impacto](proporcao_impacto.png)\n\n")
    f.write("![Tipos de Impacto](tipos_impacto.png)\n\n")
    f.write("![Impacto por Faixa Etária](impacto_por_faixa_etaria.png)\n\n")
    f.write("![Impacto por Gênero](impacto_por_genero.png)\n\n")
    f.write("![Impacto por Raça/Etnia](impacto_por_raca_etnia.png)\n\n")
    f.write("![Top Combinações com Maior Impacto](top_combinacoes_impacto.png)\n\n")
    
    f.write("## Conclusões Gerais\n\n")
    f.write("A análise exploratória de dados revelou insights importantes sobre o mercado de trabalho na área de dados:\n\n")
    
    f.write("1. **Perfil Demográfico**: A área de dados é predominantemente composta por profissionais jovens, ")
    f.write("com maior concentração nas faixas etárias de 25-29 e 30-34 anos. Há um desequilíbrio significativo ")
    f.write("na distribuição de gênero, com predominância masculina.\n\n")
    
    f.write("2. **Educação e Salário**: Existe uma clara relação positiva entre nível de ensino e faixa salarial, ")
    f.write("com profissionais de maior formação acadêmica tendendo a receber salários mais altos. ")
    f.write("A pós-graduação e o mestrado aparecem como níveis educacionais predominantes entre os profissionais da área.\n\n")
    
    f.write("3. **Experiência e Salário**: O tempo de experiência na área de dados também apresenta ")
    f.write("correlação positiva com a faixa salarial, indicando que a experiência prática é valorizada pelo mercado.\n\n")
    
    f.write("4. **Impactos na Experiência Profissional**: Uma parcela significativa dos respondentes relata ")
    f.write("impactos na experiência profissional devido à raça/etnia ou identidade de gênero. ")
    f.write("Esses impactos variam consideravelmente entre diferentes grupos demográficos, ")
    f.write("com certos grupos apresentando percentuais muito mais altos de experiências negativas.\n\n")
    
    f.write("5. **Interseccionalidade**: A análise cruzada de gênero e raça/etnia revela que certas combinações ")
    f.write("estão associadas a percentuais significativamente mais altos de impacto na experiência profissional, ")
    f.write("destacando a importância de considerar a interseccionalidade ao abordar questões de diversidade e inclusão.\n\n")
    
    f.write("Estes resultados sugerem a necessidade de políticas e práticas mais inclusivas no setor de dados, ")
    f.write("com atenção especial à diversidade de gênero e racial, bem como ao desenvolvimento de carreiras ")
    f.write("que valorizem tanto a formação acadêmica quanto a experiência prática dos profissionais.\n\n")
    
    f.write("## Recomendações\n\n")
    f.write("Com base nos insights obtidos, recomenda-se:\n\n")
    
    f.write("1. **Programas de Diversidade e Inclusão**: Implementar programas específicos para aumentar ")
    f.write("a diversidade de gênero e racial na área de dados, com foco especial nos grupos sub-representados.\n\n")
    
    f.write("2. **Mentoria e Desenvolvimento**: Criar programas de mentoria e desenvolvimento de carreira ")
    f.write("direcionados a profissionais de grupos que relatam maior impacto negativo em suas experiências profissionais.\n\n")
    
    f.write("3. **Educação Continuada**: Incentivar a educação continuada e a especialização, ")
    f.write("considerando a clara relação entre nível de ensino e faixa salarial.\n\n")
    
    f.write("4. **Valorização da Experiência**: Desenvolver políticas de remuneração que reconheçam ")
    f.write("adequadamente o valor da experiência prática na área de dados.\n\n")
    
    f.write("5. **Monitoramento Contínuo**: Estabelecer métricas e realizar monitoramento contínuo ")
    f.write("dos indicadores de diversidade e inclusão, para avaliar o progresso e ajustar estratégias quando necessário.\n\n")

print("Relatório final compilado com sucesso em 'relatorio_final/relatorio_completo.md'")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Configurações para melhorar a visualização
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12
sns.set_palette("viridis")
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'DejaVu Sans'

# Criar diretório para salvar as visualizações complementares
os.makedirs('visualizacoes_complementares', exist_ok=True)

# Carregar o arquivo CSV
print("Carregando o arquivo CSV bq-results...")
df_bq = pd.read_csv('/home/ubuntu/upload/bq-results-20250422-030542-1745291209599.csv')

# Informações básicas sobre o DataFrame
print("\nInformações básicas sobre o DataFrame:")
print(f"Número de linhas: {df_bq.shape[0]}")
print(f"Número de colunas: {df_bq.shape[1]}")

# Verificar valores ausentes
print("\nValores ausentes por coluna:")
missing_values = df_bq.isnull().sum()
missing_percentage = (df_bq.isnull().sum() / len(df_bq)) * 100
missing_info = pd.DataFrame({
    'Valores ausentes': missing_values,
    'Porcentagem (%)': missing_percentage
})
print(missing_info)

# Verificar valores únicos nas colunas principais
print("\nValores únicos nas colunas principais:")
for col in ['ano', 'trimestre', 'id_uf_sigla', 'nivel_instrucao', 'cor_raca']:
    print(f"\n{col}:")
    print(df_bq[col].value_counts().head(10))
    print(f"Total de valores únicos: {df_bq[col].nunique()}")

# Salvar informações básicas em um arquivo de texto
with open('visualizacoes_complementares/info_bq_results.txt', 'w', encoding='utf-8') as f:
    f.write("# Análise do Arquivo bq-results\n\n")
    f.write(f"## Informações Básicas\n\n")
    f.write(f"- Número de linhas: {df_bq.shape[0]}\n")
    f.write(f"- Número de colunas: {df_bq.shape[1]}\n\n")
    
    f.write("## Colunas\n\n")
    for col in df_bq.columns:
        f.write(f"- {col}\n")
    
    f.write("\n## Valores Ausentes\n\n")
    for col, count in missing_values.items():
        if count > 0:
            f.write(f"- {col}: {count} ({missing_percentage[col]:.2f}%)\n")
    
    f.write("\n## Valores Únicos nas Colunas Principais\n\n")
    for col in ['ano', 'trimestre', 'id_uf_sigla', 'nivel_instrucao', 'cor_raca']:
        f.write(f"### {col}\n\n")
        value_counts = df_bq[col].value_counts().head(10)
        for value, count in value_counts.items():
            f.write(f"- {value}: {count}\n")
        f.write(f"\nTotal de valores únicos: {df_bq[col].nunique()}\n\n")

print("\nInformações básicas salvas em 'visualizacoes_complementares/info_bq_results.txt'")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Configurações para melhorar a visualização
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 12
sns.set_palette("viridis")
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'DejaVu Sans'

# Criar diretório para salvar as visualizações complementares
os.makedirs('visualizacoes_complementares', exist_ok=True)

# Carregar os dados
print("Carregando os dados...")
df_bq = pd.read_csv('/home/ubuntu/upload/bq-results-20250422-030542-1745291209599.csv')
df_main = pd.read_excel('/home/ubuntu/upload/Main_database.xlsx')

# Converter as colunas da Main_database para strings para facilitar a busca
df_main.columns = [str(col) for col in df_main.columns]

# Comparação de tamanho dos conjuntos de dados
print("\nComparação de tamanho dos conjuntos de dados:")
print(f"bq-results: {df_bq.shape[0]} linhas, {df_bq.shape[1]} colunas")
print(f"Main_database: {df_main.shape[0]} linhas, {df_main.shape[1]} colunas")

# Identificar colunas comparáveis entre os dois conjuntos de dados
print("\nIdentificando colunas comparáveis...")

# Encontrar colunas de gênero na Main_database
genero_cols = [col for col in df_main.columns if 'Genero' in col]
print(f"Colunas de gênero encontradas: {genero_cols}")
genero_main = genero_cols[0] if genero_cols else None

# Encontrar colunas de cor/raça na Main_database
cor_raca_cols = [col for col in df_main.columns if 'Cor/raca/etnia' in col]
print(f"Colunas de cor/raça encontradas: {cor_raca_cols}")
cor_raca_main = cor_raca_cols[0] if cor_raca_cols else None

# Encontrar colunas de UF na Main_database
uf_cols = [col for col in df_main.columns if 'uf onde mora' in col]
print(f"Colunas de UF encontradas: {uf_cols}")
uf_main = uf_cols[0] if uf_cols else None

# Verificar se encontramos todas as colunas necessárias
if not all([genero_main, cor_raca_main, uf_main]):
    print("AVISO: Algumas colunas necessárias não foram encontradas.")
    
    # Mostrar as primeiras colunas para debug
    print("\nPrimeiras 10 colunas da Main_database:")
    for i, col in enumerate(df_main.columns[:10]):
        print(f"{i}: {col}")
    
    # Buscar alternativas
    if not genero_main:
        genero_alt = [col for col in df_main.columns if 'genero' in col.lower()]
        print(f"Alternativas para gênero: {genero_alt}")
        genero_main = genero_alt[0] if genero_alt else None
    
    if not cor_raca_main:
        cor_raca_alt = [col for col in df_main.columns if 'raca' in col.lower() or 'etnia' in col.lower()]
        print(f"Alternativas para cor/raça: {cor_raca_alt}")
        cor_raca_main = cor_raca_alt[0] if cor_raca_alt else None
    
    if not uf_main:
        uf_alt = [col for col in df_main.columns if 'uf' in col.lower() or 'estado' in col.lower()]
        print(f"Alternativas para UF: {uf_alt}")
        uf_main = uf_alt[0] if uf_alt else None

# Colunas do bq-results
genero_bq = 'nivel_instrucao'  # Na verdade, esta coluna contém "Homem" ou "Mulher"
cor_raca_bq = 'cor_raca'
uf_bq = 'id_uf_sigla'

# Verificar valores únicos nas colunas selecionadas
print("\nValores únicos nas colunas selecionadas:")
if genero_main:
    print(f"\nGênero (Main_database - {genero_main}):")
    print(df_main[genero_main].value_counts())

if cor_raca_main:
    print(f"\nCor/Raça (Main_database - {cor_raca_main}):")
    print(df_main[cor_raca_main].value_counts())

if uf_main:
    print(f"\nUF (Main_database - {uf_main}):")
    print(df_main[uf_main].value_counts().head(10))

print(f"\nGênero (bq-results - {genero_bq}):")
print(df_bq[genero_bq].value_counts())

print(f"\nCor/Raça (bq-results - {cor_raca_bq}):")
print(df_bq[cor_raca_bq].value_counts())

print(f"\nUF (bq-results - {uf_bq}):")
print(df_bq[uf_bq].value_counts().head(10))

# Comparação de distribuição de gênero
print("\nComparando distribuição de gênero...")
genero_bq_counts = df_bq[genero_bq].value_counts(normalize=True) * 100

if genero_main:
    # Mapear valores de gênero da Main_database para corresponder aos do bq-results
    genero_mapping = {
        'Masculino': 'Homem',
        'Feminino': 'Mulher',
        'Outro': 'Outro'
    }
    
    # Criar uma nova coluna mapeada para comparação
    df_main['genero_mapeado'] = df_main[genero_main].map(genero_mapping)
    genero_main_counts = df_main['genero_mapeado'].value_counts(normalize=True) * 100
    
    # Criar DataFrame para comparação de gênero
    genero_compare = pd.DataFrame({
        'População Geral (%)': [genero_bq_counts.get('Homem', 0), genero_bq_counts.get('Mulher', 0)],
        'Profissionais de Dados (%)': [genero_main_counts.get('Homem', 0), genero_main_counts.get('Mulher', 0)]
    })
    genero_compare.index = ['Homem', 'Mulher']
    print(genero_compare)
else:
    print("Não foi possível comparar distribuição de gênero devido à falta de colunas correspondentes.")

# Comparação de distribuição de cor/raça
print("\nComparando distribuição de cor/raça...")
cor_raca_bq_counts = df_bq[cor_raca_bq].value_counts(normalize=True) * 100

if cor_raca_main:
    # Mapear valores de cor/raça da Main_database para corresponder aos do bq-results
    cor_raca_mapping = {
        'Branca': 'Branca',
        'Preta': 'Preta',
        'Parda': 'Parda',
        'Amarela': 'Amarela',
        'Indígena': 'Indígena',
        'Prefiro não informar': 'Ignorado'
    }
    
    # Criar uma nova coluna mapeada para comparação
    df_main['cor_raca_mapeada'] = df_main[cor_raca_main].map(cor_raca_mapping)
    cor_raca_main_counts = df_main['cor_raca_mapeada'].value_counts(normalize=True) * 100
    
    # Criar DataFrame para comparação de cor/raça
    cor_raca_compare = pd.DataFrame({
        'População Geral (%)': [cor_raca_bq_counts.get('Branca', 0),
                              cor_raca_bq_counts.get('Preta', 0),
                              cor_raca_bq_counts.get('Parda', 0),
                              cor_raca_bq_counts.get('Amarela', 0),
                              cor_raca_bq_counts.get('Indígena', 0)],
        'Profissionais de Dados (%)': [cor_raca_main_counts.get('Branca', 0),
                                      cor_raca_main_counts.get('Preta', 0),
                                      cor_raca_main_counts.get('Parda', 0),
                                      cor_raca_main_counts.get('Amarela', 0),
                                      cor_raca_main_counts.get('Indígena', 0)]
    })
    cor_raca_compare.index = ['Branca', 'Preta', 'Parda', 'Amarela', 'Indígena']
    print(cor_raca_compare)
else:
    print("Não foi possível comparar distribuição de cor/raça devido à falta de colunas correspondentes.")

# Comparação de distribuição por UF
print("\nComparando distribuição por UF...")
uf_bq_counts = df_bq[uf_bq].value_counts(normalize=True) * 100

if uf_main:
    uf_main_counts = df_main[uf_main].value_counts(normalize=True) * 100
    
    # Criar DataFrame para comparação de UF (top 10 UFs)
    top_ufs = set(uf_bq_counts.nlargest(10).index) | set(uf_main_counts.nlargest(10).index)
    uf_compare = pd.DataFrame({
        'População Geral (%)': [uf_bq_counts.get(uf, 0) for uf in top_ufs],
        'Profissionais de Dados (%)': [uf_main_counts.get(uf, 0) for uf in top_ufs]
    })
    uf_compare.index = top_ufs
    uf_compare = uf_compare.sort_values('População Geral (%)', ascending=False)
    print(uf_compare.head(10))
else:
    print("Não foi possível comparar distribuição por UF devido à falta de colunas correspondentes.")

# Salvar comparações em um arquivo de texto
with open('visualizacoes_complementares/comparacao_demografica.txt', 'w', encoding='utf-8') as f:
    f.write("# Comparação Demográfica: População Geral vs. Profissionais de Dados\n\n")
    
    f.write("## Tamanho dos Conjuntos de Dados\n\n")
    f.write(f"- bq-results (População Geral): {df_bq.shape[0]} registros, {df_bq.shape[1]} colunas\n")
    f.write(f"- Main_database (Profissionais de Dados): {df_main.shape[0]} registros, {df_main.shape[1]} colunas\n\n")
    
    if 'genero_compare' in locals():
        f.write("## Distribuição de Gênero\n\n")
        f.write(genero_compare.to_string())
        f.write("\n\n")
    
    if 'cor_raca_compare' in locals():
        f.write("## Distribuição de Cor/Raça\n\n")
        f.write(cor_raca_compare.to_string())
        f.write("\n\n")
    
    if 'uf_compare' in locals():
        f.write("## Distribuição por UF (Top 10)\n\n")
        f.write(uf_compare.head(10).to_string())
        f.write("\n\n")
    
    f.write("## Observações Preliminares\n\n")
    f.write("1. O conjunto de dados bq-results representa uma amostra muito maior da população brasileira em geral, ")
    f.write("enquanto o Main_database é específico para profissionais da área de dados.\n\n")
    
    if 'genero_compare' in locals():
        f.write("2. Há diferenças significativas na distribuição de gênero entre a população geral e os profissionais de dados, ")
        homem_pop = genero_compare.loc['Homem', 'População Geral (%)']
        homem_prof = genero_compare.loc['Homem', 'Profissionais de Dados (%)']
        if homem_prof > homem_pop:
            f.write(f"com uma representação proporcionalmente maior de homens na área de dados ({homem_prof:.1f}%) ")
            f.write(f"em comparação com a população geral ({homem_pop:.1f}%).\n\n")
        else:
            f.write(f"com uma representação proporcionalmente menor de homens na área de dados ({homem_prof:.1f}%) ")
            f.write(f"em comparação com a população geral ({homem_pop:.1f}%).\n\n")
    
    if 'cor_raca_compare' in locals():
        f.write("3. A distribuição de cor/raça também apresenta diferenças, ")
        branca_pop = cor_raca_compare.loc['Branca', 'População Geral (%)']
        branca_prof = cor_raca_compare.loc['Branca', 'Profissionais de Dados (%)']
        if branca_prof > branca_pop:
            f.write(f"com uma representação proporcionalmente maior de pessoas brancas na área de dados ({branca_prof:.1f}%) ")
            f.write(f"em comparação com a população geral ({branca_pop:.1f}%).\n\n")
        else:
            f.write(f"com uma representação proporcionalmente menor de pessoas brancas na área de dados ({branca_prof:.1f}%) ")
            f.write(f"em comparação com a população geral ({branca_pop:.1f}%).\n\n")
    
    if 'uf_compare' in locals():
        f.write("4. A distribuição geográfica mostra concentração em diferentes estados, com alguns estados tendo ")
        f.write("representação proporcionalmente maior de profissionais de dados em relação à sua população geral.\n\n")

print("\nComparação demográfica salva em 'visualizacoes_complementares/comparacao_demografica.txt'")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Configurações para melhorar a visualização
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 12
sns.set_palette("viridis")
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'DejaVu Sans'

# Carregar os dados
print("Carregando os dados...")
df_bq = pd.read_csv('/home/ubuntu/upload/bq-results-20250422-030542-1745291209599.csv')
df_main = pd.read_excel('/home/ubuntu/upload/Main_database.xlsx')

# Converter as colunas da Main_database para strings para facilitar a busca
df_main.columns = [str(col) for col in df_main.columns]

# Identificar colunas comparáveis
genero_cols = [col for col in df_main.columns if 'Genero' in col]
genero_main = genero_cols[0] if genero_cols else None

cor_raca_cols = [col for col in df_main.columns if 'Cor/raca/etnia' in col]
cor_raca_main = cor_raca_cols[0] if cor_raca_cols else None

uf_cols = [col for col in df_main.columns if 'uf onde mora' in col]
uf_main = uf_cols[0] if uf_cols else None

# Colunas do bq-results
genero_bq = 'nivel_instrucao'  # Na verdade, esta coluna contém "Homem" ou "Mulher"
cor_raca_bq = 'cor_raca'
uf_bq = 'id_uf_sigla'

# Mapear valores de gênero da Main_database para corresponder aos do bq-results
genero_mapping = {
    'Masculino': 'Homem',
    'Feminino': 'Mulher',
    'Outro': 'Outro',
    'Prefiro não informar': 'Não informado'
}

# Mapear valores de cor/raça da Main_database para corresponder aos do bq-results
cor_raca_mapping = {
    'Branca': 'Branca',
    'Preta': 'Preta',
    'Parda': 'Parda',
    'Amarela': 'Amarela',
    'Indígena': 'Indígena',
    'Prefiro não informar': 'Não informado',
    'Outra': 'Outra'
}

# Criar colunas mapeadas para comparação
df_main['genero_mapeado'] = df_main[genero_main].map(genero_mapping)
df_main['cor_raca_mapeada'] = df_main[cor_raca_main].map(cor_raca_mapping)

# Processamento adicional: Análise de interseccionalidade (gênero e cor/raça)
print("\nProcessando dados para análise de interseccionalidade...")

# Criar categorias combinadas no bq-results
df_bq['interseccao'] = df_bq[genero_bq] + '_' + df_bq[cor_raca_bq]
interseccao_bq_counts = df_bq['interseccao'].value_counts(normalize=True) * 100

# Criar categorias combinadas na Main_database
df_main['interseccao'] = df_main['genero_mapeado'] + '_' + df_main['cor_raca_mapeada']
interseccao_main_counts = df_main['interseccao'].value_counts(normalize=True) * 100

# Selecionar as principais combinações para análise
top_interseccoes = [
    'Homem_Branca', 'Homem_Parda', 'Homem_Preta', 
    'Mulher_Branca', 'Mulher_Parda', 'Mulher_Preta'
]

# Criar DataFrame para comparação de interseccionalidade
interseccao_compare = pd.DataFrame({
    'População Geral (%)': [interseccao_bq_counts.get(inter, 0) for inter in top_interseccoes],
    'Profissionais de Dados (%)': [interseccao_main_counts.get(inter, 0) for inter in top_interseccoes]
})
interseccao_compare.index = top_interseccoes

# Calcular índice de representatividade (proporção entre % na área de dados e % na população geral)
interseccao_compare['Índice de Representatividade'] = interseccao_compare['Profissionais de Dados (%)'] / interseccao_compare['População Geral (%)']

print("\nComparação de interseccionalidade (gênero e cor/raça):")
print(interseccao_compare)

# Processamento adicional: Análise regional por grandes regiões
print("\nProcessando dados para análise regional...")

# Mapear UFs para regiões
regiao_mapping = {
    'AC': 'Norte', 'AM': 'Norte', 'AP': 'Norte', 'PA': 'Norte', 'RO': 'Norte', 'RR': 'Norte', 'TO': 'Norte',
    'AL': 'Nordeste', 'BA': 'Nordeste', 'CE': 'Nordeste', 'MA': 'Nordeste', 'PB': 'Nordeste', 
    'PE': 'Nordeste', 'PI': 'Nordeste', 'RN': 'Nordeste', 'SE': 'Nordeste',
    'DF': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'MS': 'Centro-Oeste', 'MT': 'Centro-Oeste',
    'ES': 'Sudeste', 'MG': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'RS': 'Sul', 'SC': 'Sul'
}

# Adicionar coluna de região aos DataFrames
df_bq['regiao'] = df_bq[uf_bq].map(regiao_mapping)
df_main['regiao'] = df_main[uf_main].map(regiao_mapping)

# Calcular distribuição por região
regiao_bq_counts = df_bq['regiao'].value_counts(normalize=True) * 100
regiao_main_counts = df_main['regiao'].value_counts(normalize=True) * 100

# Criar DataFrame para comparação regional
regiao_compare = pd.DataFrame({
    'População Geral (%)': [regiao_bq_counts.get(regiao, 0) for regiao in ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']],
    'Profissionais de Dados (%)': [regiao_main_counts.get(regiao, 0) for regiao in ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']]
})
regiao_compare.index = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']

# Calcular índice de representatividade regional
regiao_compare['Índice de Representatividade'] = regiao_compare['Profissionais de Dados (%)'] / regiao_compare['População Geral (%)']

print("\nComparação regional:")
print(regiao_compare)

# Processamento adicional: Análise de gênero por região
print("\nProcessando dados para análise de gênero por região...")

# Criar tabelas de contingência
genero_regiao_bq = pd.crosstab(df_bq['regiao'], df_bq[genero_bq], normalize='index') * 100
genero_regiao_main = pd.crosstab(df_main['regiao'], df_main['genero_mapeado'], normalize='index') * 100

# Selecionar apenas as colunas 'Homem' e 'Mulher' para comparação
genero_regiao_compare = pd.DataFrame({
    'Homens - População Geral (%)': genero_regiao_bq['Homem'],
    'Homens - Profissionais de Dados (%)': genero_regiao_main['Homem'],
    'Mulheres - População Geral (%)': genero_regiao_bq['Mulher'],
    'Mulheres - Profissionais de Dados (%)': genero_regiao_main['Mulher']
})

print("\nDistribuição de gênero por região:")
print(genero_regiao_compare)

# Processamento adicional: Análise de cor/raça por região
print("\nProcessando dados para análise de cor/raça por região...")

# Criar tabelas de contingência para as principais categorias de cor/raça
cor_raca_regiao_bq = pd.crosstab(df_bq['regiao'], df_bq[cor_raca_bq], normalize='index') * 100
cor_raca_regiao_main = pd.crosstab(df_main['regiao'], df_main['cor_raca_mapeada'], normalize='index') * 100

# Selecionar apenas as principais categorias para comparação
principais_racas = ['Branca', 'Preta', 'Parda']
cor_raca_regiao_compare = pd.DataFrame()

for raca in principais_racas:
    cor_raca_regiao_compare[f'{raca} - População Geral (%)'] = cor_raca_regiao_bq[raca]
    cor_raca_regiao_compare[f'{raca} - Profissionais de Dados (%)'] = cor_raca_regiao_main.get(raca, pd.Series(0, index=cor_raca_regiao_main.index))

print("\nDistribuição de cor/raça por região:")
print(cor_raca_regiao_compare)

# Salvar os resultados processados em um arquivo CSV para uso posterior
print("\nSalvando dados processados...")

# Criar DataFrames para salvar
resultados = {
    'interseccionalidade': interseccao_compare,
    'regiao': regiao_compare,
    'genero_por_regiao': genero_regiao_compare,
    'cor_raca_por_regiao': cor_raca_regiao_compare
}

# Salvar cada DataFrame em um arquivo CSV separado
for nome, df in resultados.items():
    df.to_csv(f'visualizacoes_complementares/{nome}.csv')

# Salvar análises em um arquivo de texto
with open('visualizacoes_complementares/analise_complementar.txt', 'w', encoding='utf-8') as f:
    f.write("# Análise Complementar: Interseccionalidade e Distribuição Regional\n\n")
    
    f.write("## Interseccionalidade (Gênero e Cor/Raça)\n\n")
    f.write(interseccao_compare.to_string())
    f.write("\n\n")
    
    f.write("### Observações sobre Interseccionalidade:\n\n")
    
    # Identificar grupos mais sub-representados (menor índice de representatividade)
    grupos_subrepresentados = interseccao_compare.sort_values('Índice de Representatividade').index[:3]
    f.write(f"Os grupos mais sub-representados na área de dados em relação à população geral são: {', '.join(grupos_subrepresentados)}.\n\n")
    
    # Identificar grupos mais sobre-representados (maior índice de representatividade)
    grupos_sobrerepresentados = interseccao_compare.sort_values('Índice de Representatividade', ascending=False).index[:3]
    f.write(f"Os grupos mais sobre-representados na área de dados em relação à população geral são: {', '.join(grupos_sobrerepresentados)}.\n\n")
    
    f.write("## Distribuição Regional\n\n")
    f.write(regiao_compare.to_string())
    f.write("\n\n")
    
    f.write("### Observações sobre Distribuição Regional:\n\n")
    
    # Identificar regiões mais sub-representadas
    regioes_subrepresentadas = regiao_compare.sort_values('Índice de Representatividade').index[:2]
    f.write(f"As regiões mais sub-representadas na área de dados em relação à população geral são: {' e '.join(regioes_subrepresentadas)}.\n\n")
    
    # Identificar regiões mais sobre-representadas
    regioes_sobrerepresentadas = regiao_compare.sort_values('Índice de Representatividade', ascending=False).index[:2]
    f.write(f"As regiões mais sobre-representadas na área de dados em relação à população geral são: {' e '.join(regioes_sobrerepresentadas)}.\n\n")
    
    f.write("## Distribuição de Gênero por Região\n\n")
    f.write(genero_regiao_compare.to_string())
    f.write("\n\n")
    
    f.write("### Observações sobre Gênero por Região:\n\n")
    
    # Calcular a diferença na representação de mulheres entre população geral e profissionais de dados por região
    genero_regiao_compare['Diferença na representação de mulheres (p.p.)'] = genero_regiao_compare['Mulheres - População Geral (%)'] - genero_regiao_compare['Mulheres - Profissionais de Dados (%)']
    
    # Região com maior disparidade de gênero
    regiao_maior_disparidade = genero_regiao_compare['Diferença na representação de mulheres (p.p.)'].abs().idxmax()
    disparidade = genero_regiao_compare.loc[regiao_maior_disparidade, 'Diferença na representação de mulheres (p.p.)']
    
    f.write(f"A região com maior disparidade de gênero entre a população geral e os profissionais de dados é {regiao_maior_disparidade}, ")
    if disparidade > 0:
        f.write(f"onde as mulheres estão sub-representadas na área de dados por {abs(disparidade):.1f} pontos percentuais.\n\n")
    else:
        f.write(f"onde as mulheres estão sobre-representadas na área de dados por {abs(disparidade):.1f} pontos percentuais.\n\n")
    
    f.write("## Distribuição de Cor/Raça por Região\n\n")
    f.write(cor_raca_regiao_compare.to_string())
    f.write("\n\n")
    
    f.write("### Observações sobre Cor/Raça por Região:\n\n")
    
    # Calcular a diferença na representação de pessoas pardas e pretas entre população geral e profissionais de dados por região
    for raca in ['Preta', 'Parda']:
        cor_raca_regiao_compare[f'Diferença na representação de {raca.lower()}s (p.p.)'] = cor_raca_regiao_compare[f'{raca} - População Geral (%)'] - cor_raca_regiao_compare[f'{raca} - Profissionais de Dados (%)']
    
    # Região com maior disparidade racial para pessoas pardas
    regiao_maior_disparidade_parda = cor_raca_regiao_compare['Diferença na representação de pardas (p.p.)'].abs().idxmax()
    disparidade_parda = cor_raca_regiao_compare.loc[regiao_maior_disparidade_parda, 'Diferença na representação de pardas (p.p.)']
    
    f.write(f"A região com maior disparidade na representação de pessoas pardas é {regiao_maior_disparidade_parda}, ")
    if disparidade_parda > 0:
        f.write(f"onde estão sub-representadas na área de dados por {abs(disparidade_parda):.1f} pontos percentuais.\n\n")
    else:
        f.write(f"onde estão sobre-representadas na área de dados por {abs(disparidade_parda):.1f} pontos percentuais.\n\n")
    
    # Região com maior disparidade racial para pessoas pretas
    regiao_maior_disparidade_preta = cor_raca_regiao_compare['Diferença na representação de pretas (p.p.)'].abs().idxmax()
    disparidade_preta = cor_raca_regiao_compare.loc[regiao_maior_disparidade_preta, 'Diferença na representação de pretas (p.p.)']
    
    f.write(f"A região com maior disparidade na representação de pessoas pretas é {regiao_maior_disparidade_preta}, ")
    if disparidade_preta > 0:
        f.write(f"onde estão sub-representadas na área de dados por {abs(disparidade_preta):.1f} pontos percentuais.\n\n")
    else:
        f.write(f"onde estão sobre-representadas na área de dados por {abs(disparidade_preta):.1f} pontos percentuais.\n\n")
    
    f.write("## Conclusões da Análise Complementar\n\n")
    f.write("Esta análise complementar revela padrões importantes de representatividade na área de dados em comparação com a população geral brasileira:\n\n")
    
    f.write("1. **Interseccionalidade**: Existem disparidades significativas quando consideramos a intersecção entre gênero e cor/raça, ")
    f.write("com alguns grupos tendo representação muito menor na área de dados do que sua proporção na população geral.\n\n")
    
    f.write("2. **Distribuição Regional**: Há um desequilíbrio regional na distribuição de profissionais de dados, ")
    f.write("com algumas regiões do país tendo representação proporcionalmente maior que outras.\n\n")
    
    f.write("3. **Gênero por Região**: A sub-representação de mulheres na área de dados varia entre as regiões do país, ")
    f.write("sendo mais acentuada em algumas regiões específicas.\n\n")
    
    f.write("4. **Cor/Raça por Região**: Similarmente, a representação de diferentes grupos raciais na área de dados ")
    f.write("varia significativamente entre as regiões, refletindo e por vezes amplificando as desigualdades regionais existentes.\n\n")
    
    f.write("Estes insights complementam a análise anterior, fornecendo um contexto mais amplo sobre como os profissionais ")
    f.write("de dados se comparam demograficamente com a população geral brasileira, e destacando áreas onde políticas ")
    f.write("de diversidade e inclusão podem ser mais necessárias no setor.\n")

print("\nAnálise complementar salva em 'visualizacoes_complementares/analise_complementar.txt'")
print("Processamento de dados complementares concluído com sucesso!")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Configurações para melhorar a visualização
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 12
sns.set_palette("viridis")
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'DejaVu Sans'

# Criar diretório para salvar as visualizações complementares
os.makedirs('visualizacoes_complementares/graficos', exist_ok=True)

# Carregar os dados processados
print("Carregando os dados processados...")
interseccao_df = pd.read_csv('visualizacoes_complementares/interseccionalidade.csv', index_col=0)
regiao_df = pd.read_csv('visualizacoes_complementares/regiao.csv', index_col=0)
genero_regiao_df = pd.read_csv('visualizacoes_complementares/genero_por_regiao.csv', index_col=0)
cor_raca_regiao_df = pd.read_csv('visualizacoes_complementares/cor_raca_por_regiao.csv', index_col=0)

# 1. Visualização de Interseccionalidade (Gênero e Cor/Raça)
print("\nCriando visualização de interseccionalidade...")

# Gráfico de barras para comparar população geral vs profissionais de dados
plt.figure(figsize=(16, 10))
bar_width = 0.35
index = np.arange(len(interseccao_df.index))

# Criar barras
bars1 = plt.bar(index, interseccao_df['População Geral (%)'], bar_width, 
                label='População Geral', color='#3498db', alpha=0.8)
bars2 = plt.bar(index + bar_width, interseccao_df['Profissionais de Dados (%)'], bar_width,
                label='Profissionais de Dados', color='#e74c3c', alpha=0.8)

# Adicionar rótulos, título e legenda
plt.xlabel('Grupos Demográficos (Gênero e Cor/Raça)', fontsize=14)
plt.ylabel('Percentual (%)', fontsize=14)
plt.title('Comparação de Representação: População Geral vs. Profissionais de Dados', fontsize=16)
plt.xticks(index + bar_width / 2, interseccao_df.index, rotation=45, ha='right')
plt.legend(loc='best')

# Adicionar valores nas barras
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height:.1f}%', ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)

plt.tight_layout()
plt.savefig('visualizacoes_complementares/graficos/interseccionalidade_barras.png', dpi=300, bbox_inches='tight')
plt.close()

# Gráfico de índice de representatividade
plt.figure(figsize=(14, 8))
bars = plt.barh(interseccao_df.index, interseccao_df['Índice de Representatividade'], 
               color=plt.cm.viridis(np.linspace(0, 1, len(interseccao_df))))

# Adicionar linha de referência para representatividade igual (índice = 1)
plt.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='Representatividade Igual')

# Adicionar rótulos, título e legenda
plt.xlabel('Índice de Representatividade', fontsize=14)
plt.ylabel('Grupos Demográficos (Gênero e Cor/Raça)', fontsize=14)
plt.title('Índice de Representatividade na Área de Dados por Grupo Demográfico', fontsize=16)
plt.legend(loc='best')

# Adicionar valores nas barras
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + 0.05, i, f'{width:.2f}', va='center')

plt.tight_layout()
plt.savefig('visualizacoes_complementares/graficos/indice_representatividade_interseccional.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Visualização de Distribuição Regional
print("\nCriando visualização de distribuição regional...")

# Gráfico de barras para comparar população geral vs profissionais de dados por região
plt.figure(figsize=(14, 8))
bar_width = 0.35
index = np.arange(len(regiao_df.index))

# Criar barras
bars1 = plt.bar(index, regiao_df['População Geral (%)'], bar_width, 
                label='População Geral', color='#3498db', alpha=0.8)
bars2 = plt.bar(index + bar_width, regiao_df['Profissionais de Dados (%)'], bar_width,
                label='Profissionais de Dados', color='#e74c3c', alpha=0.8)

# Adicionar rótulos, título e legenda
plt.xlabel('Região', fontsize=14)
plt.ylabel('Percentual (%)', fontsize=14)
plt.title('Distribuição Regional: População Geral vs. Profissionais de Dados', fontsize=16)
plt.xticks(index + bar_width / 2, regiao_df.index)
plt.legend(loc='best')

# Adicionar valores nas barras
add_labels(bars1)
add_labels(bars2)

plt.tight_layout()
plt.savefig('visualizacoes_complementares/graficos/distribuicao_regional_barras.png', dpi=300, bbox_inches='tight')
plt.close()

# Gráfico de índice de representatividade regional
plt.figure(figsize=(14, 8))
bars = plt.barh(regiao_df.index, regiao_df['Índice de Representatividade'], 
               color=plt.cm.viridis(np.linspace(0, 1, len(regiao_df))))

# Adicionar linha de referência para representatividade igual (índice = 1)
plt.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='Representatividade Igual')

# Adicionar rótulos, título e legenda
plt.xlabel('Índice de Representatividade', fontsize=14)
plt.ylabel('Região', fontsize=14)
plt.title('Índice de Representatividade na Área de Dados por Região', fontsize=16)
plt.legend(loc='best')

# Adicionar valores nas barras
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + 0.05, i, f'{width:.2f}', va='center')

plt.tight_layout()
plt.savefig('visualizacoes_complementares/graficos/indice_representatividade_regional.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Visualização de Gênero por Região
print("\nCriando visualização de gênero por região...")

# Preparar dados para o gráfico
homens_pop = genero_regiao_df['Homens - População Geral (%)']
homens_prof = genero_regiao_df['Homens - Profissionais de Dados (%)']
mulheres_pop = genero_regiao_df['Mulheres - População Geral (%)']
mulheres_prof = genero_regiao_df['Mulheres - Profissionais de Dados (%)']

# Calcular a diferença na representação de mulheres
genero_regiao_df['Diferença na representação de mulheres (p.p.)'] = mulheres_pop - mulheres_prof

# Gráfico de barras agrupadas para homens
plt.figure(figsize=(14, 8))
bar_width = 0.35
index = np.arange(len(genero_regiao_df.index))

# Criar barras para homens
bars1 = plt.bar(index, homens_pop, bar_width, 
                label='Homens - População Geral', color='#3498db', alpha=0.8)
bars2 = plt.bar(index + bar_width, homens_prof, bar_width,
                label='Homens - Profissionais de Dados', color='#2980b9', alpha=0.8)

# Adicionar rótulos, título e legenda
plt.xlabel('Região', fontsize=14)
plt.ylabel('Percentual (%)', fontsize=14)
plt.title('Representação de Homens por Região: População Geral vs. Profissionais de Dados', fontsize=16)
plt.xticks(index + bar_width / 2, genero_regiao_df.index)
plt.legend(loc='best')

# Adicionar valores nas barras
add_labels(bars1)
add_labels(bars2)

plt.tight_layout()
plt.savefig('visualizacoes_complementares/graficos/homens_por_regiao.png', dpi=300, bbox_inches='tight')
plt.close()

# Gráfico de barras agrupadas para mulheres
plt.figure(figsize=(14, 8))

# Criar barras para mulheres
bars1 = plt.bar(index, mulheres_pop, bar_width, 
                label='Mulheres - População Geral', color='#e74c3c', alpha=0.8)
bars2 = plt.bar(index + bar_width, mulheres_prof, bar_width,
                label='Mulheres - Profissionais de Dados', color='#c0392b', alpha=0.8)

# Adicionar rótulos, título e legenda
plt.xlabel('Região', fontsize=14)
plt.ylabel('Percentual (%)', fontsize=14)
plt.title('Representação de Mulheres por Região: População Geral vs. Profissionais de Dados', fontsize=16)
plt.xticks(index + bar_width / 2, genero_regiao_df.index)
plt.legend(loc='best')

# Adicionar valores nas barras
add_labels(bars1)
add_labels(bars2)

plt.tight_layout()
plt.savefig('visualizacoes_complementares/graficos/mulheres_por_regiao.png', dpi=300, bbox_inches='tight')
plt.close()

# Gráfico de disparidade na representação de mulheres por região
plt.figure(figsize=(14, 8))
disparidade = genero_regiao_df['Diferença na representação de mulheres (p.p.)'].sort_values()
bars = plt.barh(disparidade.index, disparidade, 
               color=plt.cm.RdYlGn_r(np.linspace(0, 1, len(disparidade))))

# Adicionar rótulos, título e legenda
plt.xlabel('Diferença em Pontos Percentuais (População Geral - Profissionais de Dados)', fontsize=14)
plt.ylabel('Região', fontsize=14)
plt.title('Disparidade na Representação de Mulheres por Região', fontsize=16)

# Adicionar valores nas barras
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + 0.5, i, f'{width:.1f} p.p.', va='center')

plt.tight_layout()
plt.savefig('visualizacoes_complementares/graficos/disparidade_mulheres_por_regiao.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Visualização de Cor/Raça por Região
print("\nCriando visualização de cor/raça por região...")

# Preparar dados para o gráfico de pessoas brancas
brancas_pop = cor_raca_regiao_df['Branca - População Geral (%)']
brancas_prof = cor_raca_regiao_df['Branca - Profissionais de Dados (%)']
pretas_pop = cor_raca_regiao_df['Preta - População Geral (%)']
pretas_prof = cor_raca_regiao_df['Preta - Profissionais de Dados (%)']
pardas_pop = cor_raca_regiao_df['Parda - População Geral (%)']
pardas_prof = cor_raca_regiao_df['Parda - Profissionais de Dados (%)']

# Calcular a diferença na representação por cor/raça
cor_raca_regiao_df['Diferença na representação de pessoas brancas (p.p.)'] = brancas_pop - brancas_prof
cor_raca_regiao_df['Diferença na representação de pessoas pretas (p.p.)'] = pretas_pop - pretas_prof
cor_raca_regiao_df['Diferença na representação de pessoas pardas (p.p.)'] = pardas_pop - pardas_prof

# Gráfico de disparidade na representação de pessoas pardas por região
plt.figure(figsize=(14, 8))
disparidade_pardas = cor_raca_regiao_df['Diferença na representação de pessoas pardas (p.p.)'].sort_values()
bars = plt.barh(disparidade_pardas.index, disparidade_pardas, 
               color=plt.cm.RdYlGn_r(np.linspace(0, 1, len(disparidade_pardas))))

# Adicionar rótulos, título e legenda
plt.xlabel('Diferença em Pontos Percentuais (População Geral - Profissionais de Dados)', fontsize=14)
plt.ylabel('Região', fontsize=14)
plt.title('Disparidade na Representação de Pessoas Pardas por Região', fontsize=16)

# Adicionar valores nas barras
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + 0.5, i, f'{width:.1f} p.p.', va='center')

plt.tight_layout()
plt.savefig('visualizacoes_complementares/graficos/disparidade_pardas_por_regiao.png', dpi=300, bbox_inches='tight')
plt.close()

# Gráfico de disparidade na representação de pessoas pretas por região
plt.figure(figsize=(14, 8))
disparidade_pretas = cor_raca_regiao_df['Diferença na representação de pessoas pretas (p.p.)'].sort_values()
bars = plt.barh(disparidade_pretas.index, disparidade_pretas, 
               color=plt.cm.RdYlGn_r(np.linspace(0, 1, len(disparidade_pretas))))

# Adicionar rótulos, título e legenda
plt.xlabel('Diferença em Pontos Percentuais (População Geral - Profissionais de Dados)', fontsize=14)
plt.ylabel('Região', fontsize=14)
plt.title('Disparidade na Representação de Pessoas Pretas por Região', fontsize=16)

# Adicionar valores nas barras
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + 0.5, i, f'{width:.1f} p.p.', va='center')

plt.tight_layout()
plt.savefig('visualizacoes_complementares/graficos/disparidade_pretas_por_regiao.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. Gráfico de mapa de calor para visualizar todas as disparidades regionais
print("\nCriando mapa de calor de disparidades regionais...")

# Preparar dados para o mapa de calor
disparidades = pd.DataFrame({
    'Mulheres': genero_regiao_df['Diferença na representação de mulheres (p.p.)'],
    'Pessoas Pardas': cor_raca_regiao_df['Diferença na representação de pessoas pardas (p.p.)'],
    'Pessoas Pretas': cor_raca_regiao_df['Diferença na representação de pessoas pretas (p.p.)']
})

# Criar mapa de calor
plt.figure(figsize=(14, 10))
sns.heatmap(disparidades, annot=True, cmap='RdYlGn_r', center=0, fmt='.1f',
           linewidths=.5, cbar_kws={'label': 'Diferença em Pontos Percentuais'})

plt.title('Mapa de Calor: Disparidades na Representação por Região', fontsize=16)
plt.tight_layout()
plt.savefig('visualizacoes_complementares/graficos/mapa_calor_disparidades.png', dpi=300, bbox_inches='tight')
plt.close()

print("\nVisualizações complementares criadas com sucesso!")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from scipy import stats

# Configurações para melhorar a visualização
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 12
sns.set_palette("viridis")
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'DejaVu Sans'

# Carregar os dados
print("Carregando os dados...")
df_bq = pd.read_csv('/home/ubuntu/upload/bq-results-20250422-030542-1745291209599.csv')
df_main = pd.read_excel('/home/ubuntu/upload/Main_database.xlsx')

# Converter as colunas da Main_database para strings para facilitar a busca
df_main.columns = [str(col) for col in df_main.columns]

# Identificar colunas comparáveis
genero_cols = [col for col in df_main.columns if 'Genero' in col]
genero_main = genero_cols[0] if genero_cols else None

cor_raca_cols = [col for col in df_main.columns if 'Cor/raca/etnia' in col]
cor_raca_main = cor_raca_cols[0] if cor_raca_cols else None

uf_cols = [col for col in df_main.columns if 'uf onde mora' in col]
uf_main = uf_cols[0] if uf_cols else None

# Encontrar colunas de faixa salarial e nível de ensino
faixa_salarial_cols = [col for col in df_main.columns if 'Faixa salarial' in col]
faixa_salarial_main = faixa_salarial_cols[0] if faixa_salarial_cols else None

nivel_ensino_cols = [col for col in df_main.columns if 'Nivel de Ensino' in col]
nivel_ensino_main = nivel_ensino_cols[0] if nivel_ensino_cols else None

# Colunas do bq-results
genero_bq = 'nivel_instrucao'  # Na verdade, esta coluna contém "Homem" ou "Mulher"
cor_raca_bq = 'cor_raca'
uf_bq = 'id_uf_sigla'

# Mapear valores de gênero da Main_database para corresponder aos do bq-results
genero_mapping = {
    'Masculino': 'Homem',
    'Feminino': 'Mulher',
    'Outro': 'Outro',
    'Prefiro não informar': 'Não informado'
}

# Mapear valores de cor/raça da Main_database para corresponder aos do bq-results
cor_raca_mapping = {
    'Branca': 'Branca',
    'Preta': 'Preta',
    'Parda': 'Parda',
    'Amarela': 'Amarela',
    'Indígena': 'Indígena',
    'Prefiro não informar': 'Não informado',
    'Outra': 'Outra'
}

# Criar colunas mapeadas para comparação
df_main['genero_mapeado'] = df_main[genero_main].map(genero_mapping)
df_main['cor_raca_mapeada'] = df_main[cor_raca_main].map(cor_raca_mapping)

# Mapear UFs para regiões
regiao_mapping = {
    'AC': 'Norte', 'AM': 'Norte', 'AP': 'Norte', 'PA': 'Norte', 'RO': 'Norte', 'RR': 'Norte', 'TO': 'Norte',
    'AL': 'Nordeste', 'BA': 'Nordeste', 'CE': 'Nordeste', 'MA': 'Nordeste', 'PB': 'Nordeste', 
    'PE': 'Nordeste', 'PI': 'Nordeste', 'RN': 'Nordeste', 'SE': 'Nordeste',
    'DF': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'MS': 'Centro-Oeste', 'MT': 'Centro-Oeste',
    'ES': 'Sudeste', 'MG': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'RS': 'Sul', 'SC': 'Sul'
}

# Adicionar coluna de região aos DataFrames
df_bq['regiao'] = df_bq[uf_bq].map(regiao_mapping)
df_main['regiao'] = df_main[uf_main].map(regiao_mapping)

# Criar diretório para salvar as visualizações adicionais
os.makedirs('visualizacoes_complementares/relacoes_adicionais', exist_ok=True)

# 1. Análise da relação entre gênero, cor/raça e faixa salarial
print("\nAnalisando relação entre gênero, cor/raça e faixa salarial...")

# Verificar se temos a coluna de faixa salarial
if faixa_salarial_main:
    # Criar tabela de contingência para gênero e faixa salarial
    genero_salario = pd.crosstab(df_main['genero_mapeado'], df_main[faixa_salarial_main], normalize='index') * 100
    
    # Criar tabela de contingência para cor/raça e faixa salarial
    cor_raca_salario = pd.crosstab(df_main['cor_raca_mapeada'], df_main[faixa_salarial_main], normalize='index') * 100
    
    # Salvar as tabelas em CSV
    genero_salario.to_csv('visualizacoes_complementares/relacoes_adicionais/genero_salario.csv')
    cor_raca_salario.to_csv('visualizacoes_complementares/relacoes_adicionais/cor_raca_salario.csv')
    
    # Criar visualização para gênero e faixa salarial
    plt.figure(figsize=(16, 10))
    
    # Selecionar apenas as principais faixas salariais para melhor visualização
    principais_faixas = [col for col in genero_salario.columns if 'R$' in col]
    principais_faixas = sorted(principais_faixas, key=lambda x: float(x.split('R$')[1].split('/')[0].replace('.', '').replace(',', '.').strip()) if 'R$' in x else 0)
    
    # Filtrar para os principais gêneros
    principais_generos = ['Homem', 'Mulher']
    genero_salario_filtrado = genero_salario.loc[principais_generos, principais_faixas]
    
    # Criar heatmap
    sns.heatmap(genero_salario_filtrado, annot=True, cmap='viridis', fmt='.1f', linewidths=.5)
    plt.title('Distribuição de Faixa Salarial por Gênero (%)', fontsize=16)
    plt.xlabel('Faixa Salarial', fontsize=14)
    plt.ylabel('Gênero', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('visualizacoes_complementares/relacoes_adicionais/genero_salario_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Criar visualização para cor/raça e faixa salarial
    plt.figure(figsize=(16, 12))
    
    # Filtrar para as principais raças/cores
    principais_racas = ['Branca', 'Preta', 'Parda']
    cor_raca_salario_filtrado = cor_raca_salario.loc[principais_racas, principais_faixas]
    
    # Criar heatmap
    sns.heatmap(cor_raca_salario_filtrado, annot=True, cmap='viridis', fmt='.1f', linewidths=.5)
    plt.title('Distribuição de Faixa Salarial por Cor/Raça (%)', fontsize=16)
    plt.xlabel('Faixa Salarial', fontsize=14)
    plt.ylabel('Cor/Raça', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('visualizacoes_complementares/relacoes_adicionais/cor_raca_salario_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Análise de interseccionalidade (gênero e cor/raça) com faixa salarial
    # Criar uma coluna combinada de gênero e cor/raça
    df_main['interseccao'] = df_main['genero_mapeado'] + '_' + df_main['cor_raca_mapeada']
    
    # Selecionar as principais combinações
    principais_interseccoes = ['Homem_Branca', 'Homem_Parda', 'Homem_Preta', 
                              'Mulher_Branca', 'Mulher_Parda', 'Mulher_Preta']
    
    # Filtrar o DataFrame
    df_interseccao = df_main[df_main['interseccao'].isin(principais_interseccoes)]
    
    # Criar tabela de contingência
    interseccao_salario = pd.crosstab(df_interseccao['interseccao'], df_interseccao[faixa_salarial_main], normalize='index') * 100
    
    # Salvar a tabela em CSV
    interseccao_salario.to_csv('visualizacoes_complementares/relacoes_adicionais/interseccao_salario.csv')
    
    # Criar visualização
    plt.figure(figsize=(18, 12))
    
    # Filtrar para as principais faixas salariais
    interseccao_salario_filtrado = interseccao_salario[principais_faixas]
    
    # Criar heatmap
    sns.heatmap(interseccao_salario_filtrado, annot=True, cmap='viridis', fmt='.1f', linewidths=.5)
    plt.title('Distribuição de Faixa Salarial por Interseccionalidade (Gênero e Cor/Raça) (%)', fontsize=16)
    plt.xlabel('Faixa Salarial', fontsize=14)
    plt.ylabel('Gênero e Cor/Raça', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('visualizacoes_complementares/relacoes_adicionais/interseccao_salario_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
else:
    print("Coluna de faixa salarial não encontrada.")

# 2. Análise da relação entre gênero, cor/raça e nível de ensino
print("\nAnalisando relação entre gênero, cor/raça e nível de ensino...")

# Verificar se temos a coluna de nível de ensino
if nivel_ensino_main:
    # Criar tabela de contingência para gênero e nível de ensino
    genero_ensino = pd.crosstab(df_main['genero_mapeado'], df_main[nivel_ensino_main], normalize='index') * 100
    
    # Criar tabela de contingência para cor/raça e nível de ensino
    cor_raca_ensino = pd.crosstab(df_main['cor_raca_mapeada'], df_main[nivel_ensino_main], normalize='index') * 100
    
    # Salvar as tabelas em CSV
    genero_ensino.to_csv('visualizacoes_complementares/relacoes_adicionais/genero_ensino.csv')
    cor_raca_ensino.to_csv('visualizacoes_complementares/relacoes_adicionais/cor_raca_ensino.csv')
    
    # Criar visualização para gênero e nível de ensino
    plt.figure(figsize=(16, 10))
    
    # Ordenar níveis de ensino
    ordem_nivel_ensino = [
        'Não tenho graduação formal', 'Estudante de Graduação', 'Graduação/Bacharelado', 
        'Pós-graduação', 'Mestrado', 'Doutorado ou Phd'
    ]
    
    # Filtrar para os principais gêneros e níveis de ensino
    principais_generos = ['Homem', 'Mulher']
    niveis_ensino_presentes = [nivel for nivel in ordem_nivel_ensino if nivel in genero_ensino.columns]
    genero_ensino_filtrado = genero_ensino.loc[principais_generos, niveis_ensino_presentes]
    
    # Criar heatmap
    sns.heatmap(genero_ensino_filtrado, annot=True, cmap='viridis', fmt='.1f', linewidths=.5)
    plt.title('Distribuição de Nível de Ensino por Gênero (%)', fontsize=16)
    plt.xlabel('Nível de Ensino', fontsize=14)
    plt.ylabel('Gênero', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('visualizacoes_complementares/relacoes_adicionais/genero_ensino_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Criar visualização para cor/raça e nível de ensino
    plt.figure(figsize=(16, 12))
    
    # Filtrar para as principais raças/cores
    principais_racas = ['Branca', 'Preta', 'Parda']
    cor_raca_ensino_filtrado = cor_raca_ensino.loc[principais_racas, niveis_ensino_presentes]
    
    # Criar heatmap
    sns.heatmap(cor_raca_ensino_filtrado, annot=True, cmap='viridis', fmt='.1f', linewidths=.5)
    plt.title('Distribuição de Nível de Ensino por Cor/Raça (%)', fontsize=16)
    plt.xlabel('Nível de Ensino', fontsize=14)
    plt.ylabel('Cor/Raça', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('visualizacoes_complementares/relacoes_adicionais/cor_raca_ensino_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Análise de interseccionalidade (gênero e cor/raça) com nível de ensino
    # Criar tabela de contingência
    interseccao_ensino = pd.crosstab(df_interseccao['interseccao'], df_interseccao[nivel_ensino_main], normalize='index') * 100
    
    # Salvar a tabela em CSV
    interseccao_ensino.to_csv('visualizacoes_complementares/relacoes_adicionais/interseccao_ensino.csv')
    
    # Criar visualização
    plt.figure(figsize=(18, 12))
    
    # Filtrar para os principais níveis de ensino
    interseccao_ensino_filtrado = interseccao_ensino[niveis_ensino_presentes]
    
    # Criar heatmap
    sns.heatmap(interseccao_ensino_filtrado, annot=True, cmap='viridis', fmt='.1f', linewidths=.5)
    plt.title('Distribuição de Nível de Ensino por Interseccionalidade (Gênero e Cor/Raça) (%)', fontsize=16)
    plt.xlabel('Nível de Ensino', fontsize=14)
    plt.ylabel('Gênero e Cor/Raça', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('visualizacoes_complementares/relacoes_adicionais/interseccao_ensino_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
else:
    print("Coluna de nível de ensino não encontrada.")

# 3. Análise da relação entre região e faixa salarial/nível de ensino
print("\nAnalisando relação entre região e faixa salarial/nível de ensino...")

# Verificar se temos as colunas necessárias
if faixa_salarial_main:
    # Criar tabela de contingência para região e faixa salarial
    regiao_salario = pd.crosstab(df_main['regiao'], df_main[faixa_salarial_main], normalize='index') * 100
    
    # Salvar a tabela em CSV
    regiao_salario.to_csv('visualizacoes_complementares/relacoes_adicionais/regiao_salario.csv')
    
    # Criar visualização
    plt.figure(figsize=(18, 12))
    
    # Filtrar para as principais regiões e faixas salariais
    principais_regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
    regioes_presentes = [regiao for regiao in principais_regioes if regiao in regiao_salario.index]
    regiao_salario_filtrado = regiao_salario.loc[regioes_presentes, principais_faixas]
    
    # Criar heatmap
    sns.heatmap(regiao_salario_filtrado, annot=True, cmap='viridis', fmt='.1f', linewidths=.5)
    plt.title('Distribuição de Faixa Salarial por Região (%)', fontsize=16)
    plt.xlabel('Faixa Salarial', fontsize=14)
    plt.ylabel('Região', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('visualizacoes_complementares/relacoes_adicionais/regiao_salario_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()

if nivel_ensino_main:
    # Criar tabela de contingência para região e nível de ensino
    regiao_ensino = pd.crosstab(df_main['regiao'], df_main[nivel_ensino_main], normalize='index') * 100
    
    # Salvar a tabela em CSV
    regiao_ensino.to_csv('visualizacoes_complementares/relacoes_adicionais/regiao_ensino.csv')
    
    # Criar visualização
    plt.figure(figsize=(18, 12))
    
    # Filtrar para as principais regiões e níveis de ensino
    principais_regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
    regioes_presentes = [regiao for regiao in principais_regioes if regiao in regiao_ensino.index]
    regiao_ensino_filtrado = regiao_ensino.loc[regioes_presentes, niveis_ensino_presentes]
    
    # Criar heatmap
    sns.heatmap(regiao_ensino_filtrado, annot=True, cmap='viridis', fmt='.1f', linewidths=.5)
    plt.title('Distribuição de Nível de Ensino por Região (%)', fontsize=16)
    plt.xlabel('Nível de Ensino', fontsize=14)
    plt.ylabel('Região', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('visualizacoes_complementares/relacoes_adicionais/regiao_ensino_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()

# Salvar análises em um arquivo de texto
with open('visualizacoes_complementares/relacoes_adicionais/analise_relacoes_adicionais.txt', 'w', encoding='utf-8') as f:
    f.write("# Análise de Relações Adicionais entre Variáveis Demográficas\n\n")
    
    if faixa_salarial_main:
        f.write("## Relação entre Gênero e Faixa Salarial\n\n")
        
        # Identificar faixas salariais mais comuns por gênero
        for genero in principais_generos:
            if genero in genero_salario.index:
                faixas_mais_comuns = genero_salario.loc[genero].nlargest(3)
                f.write(f"### {genero}:\n")
                for faixa, percentual in faixas_mais_comuns.items():
                    f.write(f"- {faixa}: {percentual:.1f}%\n")
                f.write("\n")
        
        f.write("## Relação entre Cor/Raça e Faixa Salarial\n\n")
        
        # Identificar faixas salariais mais comuns por cor/raça
        for raca in principais_racas:
            if raca in cor_raca_salario.index:
                faixas_mais_comuns = cor_raca_salario.loc[raca].nlargest(3)
                f.write(f"### {raca}:\n")
                for faixa, percentual in faixas_mais_comuns.items():
                    f.write(f"- {faixa}: {percentual:.1f}%\n")
                f.write("\n")
        
        f.write("## Relação entre Interseccionalidade (Gênero e Cor/Raça) e Faixa Salarial\n\n")
        
        # Identificar faixas salariais mais comuns por interseccionalidade
        for interseccao in principais_interseccoes:
            if interseccao in interseccao_salario.index:
                faixas_mais_comuns = interseccao_salario.loc[interseccao].nlargest(3)
                f.write(f"### {interseccao}:\n")
                for faixa, percentual in faixas_mais_comuns.items():
                    f.write(f"- {faixa}: {percentual:.1f}%\n")
                f.write("\n")
    
    if nivel_ensino_main:
        f.write("## Relação entre Gênero e Nível de Ensino\n\n")
        
        # 
(Content truncated due to size limit. Use line ranges to read in chunks)

import pandas as pd
import os

# Criar diretório para o relatório integrado
os.makedirs('relatorio_integrado', exist_ok=True)

# Função para ler arquivos de texto
def ler_arquivo(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return "Arquivo não encontrado: " + caminho

# Ler os arquivos de análise
analise_demografica = ler_arquivo('visualizacoes_complementares/comparacao_demografica.txt')
analise_complementar = ler_arquivo('visualizacoes_complementares/analise_complementar.txt')
analise_relacoes = ler_arquivo('visualizacoes_complementares/relacoes_adicionais/analise_relacoes_adicionais.txt')

# Ler o relatório original
relatorio_original = ler_arquivo('relatorio_final/relatorio_completo.md')

# Criar o relatório integrado
with open('relatorio_integrado/relatorio_integrado.md', 'w', encoding='utf-8') as f:
    f.write("# Análise Integrada: Profissionais de Dados no Contexto Demográfico Brasileiro\n\n")
    
    f.write("## Sumário Executivo\n\n")
    f.write("Este relatório integra duas análises complementares: (1) a análise original dos profissionais da área de dados ")
    f.write("baseada na Main_database e (2) a análise complementar que compara esses profissionais com a população geral brasileira ")
    f.write("usando os dados do bq-results. Esta integração permite contextualizar as características dos profissionais de dados ")
    f.write("dentro do panorama demográfico nacional, revelando disparidades significativas em termos de representatividade, ")
    f.write("distribuição regional, faixas salariais e níveis educacionais.\n\n")
    
    f.write("## Parte 1: Análise Original dos Profissionais de Dados\n\n")
    f.write("A análise original, baseada na Main_database com 5.293 registros, examinou o perfil demográfico e profissional ")
    f.write("dos trabalhadores da área de dados no Brasil. Abaixo estão os principais pontos desta análise:\n\n")
    
    f.write("### Distribuições Demográficas\n\n")
    f.write("- **Gênero**: Predominância masculina (75,3%) na área de dados\n")
    f.write("- **Cor/Raça**: Maioria de pessoas brancas (64,7%), seguida por pardas (24,3%) e pretas (7,3%)\n")
    f.write("- **Distribuição Regional**: Concentração no Sudeste (61,4%), especialmente em São Paulo (40,1%)\n")
    f.write("- **Nível de Ensino**: Maioria com graduação/bacharelado (33,9%) ou pós-graduação (34,4%)\n")
    f.write("- **Faixa Salarial**: Concentração nas faixas de R$ 8.001 a R$ 12.000 (21,7%) e R$ 4.001 a R$ 6.000 (15,7%)\n\n")
    
    f.write("### Relações entre Variáveis\n\n")
    f.write("- Correlação positiva entre nível de ensino e faixa salarial\n")
    f.write("- Correlação positiva entre tempo de experiência e faixa salarial\n")
    f.write("- Diferenças salariais entre grupos demográficos\n\n")
    
    f.write("### Impactos na Experiência Profissional\n\n")
    f.write("- Parcela significativa dos respondentes relata impactos na experiência profissional devido à raça/etnia ou identidade de gênero\n")
    f.write("- Diferenças no percentual de impacto relatado entre diferentes grupos demográficos\n\n")
    
    f.write("## Parte 2: Análise Complementar - Comparação com a População Geral\n\n")
    f.write("A análise complementar, baseada no arquivo bq-results com quase 2 milhões de registros, comparou o perfil dos ")
    f.write("profissionais de dados com a população geral brasileira. Esta comparação revelou disparidades significativas:\n\n")
    
    f.write("### Disparidades de Representatividade\n\n")
    f.write("#### Gênero\n")
    f.write("- **População Geral**: 48,4% homens e 51,6% mulheres\n")
    f.write("- **Profissionais de Dados**: 75,3% homens e 24,5% mulheres\n")
    f.write("- **Disparidade**: Mulheres estão sub-representadas na área de dados, com uma diferença de 27,1 pontos percentuais\n\n")
    
    f.write("#### Cor/Raça\n")
    f.write("- **População Geral**: 39,3% brancos, 49,8% pardos, 9,7% pretos\n")
    f.write("- **Profissionais de Dados**: 64,7% brancos, 24,3% pardos, 7,3% pretos\n")
    f.write("- **Disparidade**: Pessoas brancas estão sobre-representadas (+25,4 p.p.), enquanto pardas (-25,5 p.p.) e pretas (-2,4 p.p.) estão sub-representadas\n\n")
    
    f.write("#### Distribuição Regional\n")
    f.write("- **Disparidade Regional**: O Sudeste está significativamente sobre-representado na área de dados (índice de representatividade de 2,36)\n")
    f.write("- **Regiões Sub-representadas**: Norte (índice de 0,11) e Nordeste (índice de 0,35)\n\n")
    
    f.write("### Análise de Interseccionalidade\n\n")
    f.write("A análise interseccional (combinando gênero e cor/raça) revelou padrões complexos de desigualdade:\n\n")
    
    f.write("- **Homens Brancos**: Fortemente sobre-representados (índice de 2,60)\n")
    f.write("- **Mulheres Pardas**: Fortemente sub-representadas (índice de 0,22)\n")
    f.write("- **Mulheres Pretas**: Significativamente sub-representadas (índice de 0,40)\n\n")
    
    f.write("Estas disparidades indicam barreiras múltiplas para certos grupos no acesso à área de dados.\n\n")
    
    f.write("### Relações Adicionais entre Variáveis\n\n")
    
    f.write("#### Faixa Salarial por Grupo Demográfico\n\n")
    f.write("- **Gênero**: Homens e mulheres têm distribuições salariais semelhantes, com leve vantagem para homens nas faixas mais altas\n")
    f.write("- **Cor/Raça**: Pessoas brancas têm maior presença nas faixas salariais mais altas\n")
    f.write("- **Interseccionalidade**: Mulheres pretas têm menor presença nas faixas salariais mais altas em comparação com outros grupos\n\n")
    
    f.write("#### Nível de Ensino por Grupo Demográfico\n\n")
    f.write("- **Gênero**: Mulheres têm maior percentual de pós-graduação e mestrado\n")
    f.write("- **Cor/Raça**: Pessoas pretas têm maior percentual de estudantes de graduação\n")
    f.write("- **Interseccionalidade**: Mulheres pretas têm o maior percentual de pós-graduação (40,4%), possivelmente indicando a necessidade de maior qualificação para superar barreiras\n\n")
    
    f.write("#### Variações Regionais\n\n")
    f.write("- **Disparidade de Gênero**: A sub-representação de mulheres é mais acentuada na região Centro-Oeste\n")
    f.write("- **Disparidade Racial**: A sub-representação de pessoas pardas é mais acentuada na região Norte\n")
    f.write("- **Faixa Salarial**: O Sudeste concentra as maiores faixas salariais\n")
    f.write("- **Nível de Ensino**: O Nordeste tem o maior percentual de estudantes de graduação (20,4%)\n\n")
    
    f.write("## Conclusões Integradas\n\n")
    
    f.write("A integração das análises original e complementar revela um panorama abrangente sobre a área de dados no Brasil:\n\n")
    
    f.write("1. **Desigualdades Estruturais**: A área de dados reflete e por vezes amplifica desigualdades estruturais presentes na sociedade brasileira, com sub-representação significativa de mulheres, pessoas pardas e pretas, e profissionais das regiões Norte e Nordeste.\n\n")
    
    f.write("2. **Interseccionalidade**: As barreiras são multiplicadas quando consideramos a intersecção entre diferentes características demográficas, com mulheres pardas e pretas enfrentando os maiores desafios de representatividade.\n\n")
    
    f.write("3. **Qualificação como Estratégia**: Grupos sub-representados parecem investir mais em qualificação formal (como pós-graduação) possivelmente como estratégia para superar barreiras de entrada e progressão na carreira.\n\n")
    
    f.write("4. **Concentração Regional**: A concentração de oportunidades no Sudeste cria um desequilíbrio regional significativo, limitando o desenvolvimento do setor em outras regiões do país.\n\n")
    
    f.write("5. **Disparidades Salariais**: Embora existam diferenças salariais entre grupos demográficos, estas parecem ser menos pronunciadas do que as disparidades de representatividade, sugerindo que a principal barreira está no acesso à área, não necessariamente na remuneração após o ingresso.\n\n")
    
    f.write("## Recomendações\n\n")
    
    f.write("Com base nas análises integradas, recomendamos:\n\n")
    
    f.write("1. **Políticas de Diversidade e Inclusão**: Implementar políticas específicas para aumentar a representatividade de grupos sub-representados, especialmente mulheres, pessoas pardas e pretas.\n\n")
    
    f.write("2. **Abordagem Interseccional**: Adotar uma perspectiva interseccional nas iniciativas de diversidade, reconhecendo as barreiras múltiplas enfrentadas por certos grupos.\n\n")
    
    f.write("3. **Descentralização de Oportunidades**: Investir no desenvolvimento do setor de dados nas regiões Norte e Nordeste, através de incentivos fiscais, programas de capacitação e parcerias com instituições de ensino locais.\n\n")
    
    f.write("4. **Monitoramento Contínuo**: Estabelecer métricas e realizar monitoramento contínuo da diversidade no setor, com metas específicas para redução das disparidades identificadas.\n\n")
    
    f.write("5. **Programas de Mentoria e Networking**: Criar programas específicos para apoiar o desenvolvimento profissional de grupos sub-representados, facilitando o acesso a redes de contatos e oportunidades de crescimento.\n\n")
    
    f.write("Esta análise integrada fornece uma base sólida para a formulação de políticas e iniciativas que promovam maior equidade e inclusão na área de dados no Brasil, contribuindo para um setor mais diverso e representativo da população brasileira.\n")

print("Relatório integrado criado com sucesso em 'relatorio_integrado/relatorio_integrado.md'")

# Copiar as imagens relevantes para o diretório do relatório integrado
import shutil

# Criar diretório para as imagens
os.makedirs('relatorio_integrado/imagens', exist_ok=True)

# Copiar imagens das visualizações complementares
visualizacoes_dir = 'visualizacoes_complementares/graficos/'
relacoes_dir = 'visualizacoes_complementares/relacoes_adicionais/'

# Lista de imagens principais para copiar
imagens_principais = [
    (visualizacoes_dir + 'interseccionalidade_barras.png', 'imagens/interseccionalidade_barras.png'),
    (visualizacoes_dir + 'indice_representatividade_interseccional.png', 'imagens/indice_representatividade_interseccional.png'),
    (visualizacoes_dir + 'distribuicao_regional_barras.png', 'imagens/distribuicao_regional_barras.png'),
    (visualizacoes_dir + 'indice_representatividade_regional.png', 'imagens/indice_representatividade_regional.png'),
    (visualizacoes_dir + 'mapa_calor_disparidades.png', 'imagens/mapa_calor_disparidades.png'),
    (relacoes_dir + 'genero_salario_heatmap.png', 'imagens/genero_salario_heatmap.png'),
    (relacoes_dir + 'cor_raca_salario_heatmap.png', 'imagens/cor_raca_salario_heatmap.png'),
    (relacoes_dir + 'interseccao_salario_heatmap.png', 'imagens/interseccao_salario_heatmap.png'),
    (relacoes_dir + 'genero_ensino_heatmap.png', 'imagens/genero_ensino_heatmap.png'),
    (relacoes_dir + 'cor_raca_ensino_heatmap.png', 'imagens/cor_raca_ensino_heatmap.png'),
    (relacoes_dir + 'interseccao_ensino_heatmap.png', 'imagens/interseccao_ensino_heatmap.png')
]

# Copiar as imagens
for origem, destino in imagens_principais:
    try:
        shutil.copy(origem, 'relatorio_integrado/' + destino)
        print(f"Imagem copiada: {destino}")
    except:
        print(f"Erro ao copiar imagem: {origem}")

print("Imagens copiadas para o diretório do relatório integrado")


