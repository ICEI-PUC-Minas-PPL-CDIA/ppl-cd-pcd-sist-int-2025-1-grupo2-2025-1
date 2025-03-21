# Código do projeto

# **Estatísticas descritivas para variáveis numéricas**
print(df_selecionado[['P1_a', 'P2_i']].describe())

# **Gráficos de barras para variáveis categóricas**
for coluna in ['P1_b', 'P1_c', 'P1_d', 'P1_i_1', 'P2_f', 'P1_f_2', 'P2_g', 'P2_h']:
    plt.figure(figsize=(10, 5))
    sns.countplot(y=df_selecionado[coluna], order=df_selecionado[coluna].value_counts().index)
    plt.title(f'Distribuição de {coluna}')
    plt.show()   

# **Exemplo: Relação entre Idade e Faixa Salarial**
plt.figure(figsize=(10, 5))
sns.boxplot(x='P2_h', y='P1_a', data=df_selecionado)
plt.title('Relação entre Idade e Faixa Salarial')
plt.show()

# **Exemplo: Relação entre Gênero e Cargo Atual**
tabela_contingencia = pd.crosstab(df_selecionado['P1_b'], df_selecionado['P2_f'])
print(tabela_contingencia)
print(df_selecionado.isnull().sum()) 
