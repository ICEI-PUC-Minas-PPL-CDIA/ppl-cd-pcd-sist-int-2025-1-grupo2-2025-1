# Análise Detalhada do Código: Análise Exploratória de Dados

Este documento fornece uma explicação passo a passo do código Python contido no notebook `analise-exploratoria-de-dados-dataset-state.ipynb`. O objetivo do script é realizar uma análise exploratória em um conjunto de dados, com ênfase na criação de visualizações para entender as relações entre diferentes variáveis, particularmente aquelas relacionadas a salários.

## 1. Importação de Bibliotecas e Configurações Iniciais

O script começa importando as bibliotecas necessárias e definindo algumas configurações globais para as visualizações.

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.express as px
    import plotly.graph_objects as go
### Configurações iniciais
    plt.style.use('ggplot')
    sns.set_palette("pastel")

**Explicação:**
*   `pandas` (pd): Usado para manipulação e análise de dados, principalmente para trabalhar com DataFrames.
*   `numpy` (np): Fornece suporte para arrays e matrizes multidimensionais, além de funções matemáticas.
*   `matplotlib.pyplot` (plt): Uma biblioteca para criar visualizações estáticas, animadas e interativas.
*   `seaborn` (sns): Baseado no Matplotlib, fornece uma interface de alto nível para desenhar gráficos estatísticos atraentes e informativos.
*   `plotly.express` (px) e `plotly.graph_objects` (go): Bibliotecas para criar gráficos interativos, incluindo gráficos 3D e outros tipos de visualizações complexas.
*   `plt.style.use('ggplot')`: Define o estilo visual dos gráficos Matplotlib para emular o estilo 'ggplot' do R, conhecido por sua estética agradável.
*   `sns.set_palette("pastel")`: Define a paleta de cores padrão para os gráficos Seaborn como "pastel", que utiliza cores suaves.

### 2. Carregamento dos Dados

O script tenta carregar os dados de um arquivo CSV.

## Carregar os dados (certifique-se que 'dados_limpos.csv' está no mesmo diretório ou forneça o caminho completo)
    try:
    df = pd.read_csv('dados_limpos.csv')
    except FileNotFoundError:
    print("Erro: O arquivo 'dados_limpos.csv' não foi encontrado. Verifique o caminho do arquivo.")
    exit()


**Explicação:**
*   `pd.read_csv('dados_limpos.csv')`: Tenta ler o arquivo `dados_limpos.csv` e carregá-lo em um DataFrame do pandas chamado `df`.
*   `try-except FileNotFoundError`: Este bloco lida com a possibilidade de o arquivo CSV não ser encontrado no caminho especificado. Se o arquivo não for encontrado, uma mensagem de erro é impressa e o script é encerrado (`exit()`).

## 3. Pré-processamento dos Salários

    Uma função é definida para converter faixas salariais textuais em valores numéricos, e então aplicada ao DataFrame.
    
    ### Pré-processamento dos salários
    def convert_salary(salary_range):
    if isinstance(salary_range, str): # Adicionado para tratar possíveis NaNs que podem ser float
    if 'Acima' in salary_range:
    return 40001 # Considerando como mínimo do último intervalo
    ranges = {
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
    'Acima de R$ 40.001/mês': 40001 # Chave específica para o valor mais alto
    }
    return ranges.get(salary_range, np.nan)
    return np.nan # Retorna NaN se não for string (ex: já é NaN)
    
    df['Faixa_salarial_num'] = df['Faixa salarial mensal'].apply(convert_salary)


**Explicação:**
*   `convert_salary(salary_range)`: Esta função recebe uma string representando uma faixa salarial.
    *   Primeiro, verifica se a entrada é uma string (`isinstance(salary_range, str)`). Isso é importante para lidar com valores que já podem ser NaN (que são do tipo float).
    *   Se a string contém "Acima", retorna um valor numérico fixo (40001).
    *   Um dicionário `ranges` mapeia as strings das faixas salariais para um valor numérico representativo (geralmente o ponto médio da faixa, ou um valor inicial para faixas abertas).
    *   `ranges.get(salary_range, np.nan)`: Tenta encontrar a faixa salarial no dicionário. Se encontrar, retorna o valor numérico correspondente; caso contrário (ou se a entrada não for uma string ou for uma string não mapeada), retorna `np.nan` (Not a Number).
*   `df['Faixa_salarial_num'] = df['Faixa salarial mensal'].apply(convert_salary)`: Cria uma nova coluna chamada `Faixa_salarial_num` no DataFrame `df`. Esta coluna é populada aplicando a função `convert_salary` a cada valor da coluna existente `Faixa salarial mensal`.

## 4. Preparação de Dados para Heatmap

Valores infinitos são tratados em colunas numéricas selecionadas para garantir que o heatmap de correlação possa ser gerado corretamente.

### Preparar DataFrame numérico e limpar valores infinitos para o heatmap
    numeric_cols_for_heatmap = ['Faixa_salarial_num', 'Oportunidade de aprendizado', 'Reputação da empresa']
    numeric_df_heatmap = df[numeric_cols_for_heatmap].copy()
    numeric_df_heatmap.replace([np.inf, -np.inf], np.nan, inplace=True)


**Explicação:**
*   `numeric_cols_for_heatmap`: Define uma lista com os nomes das colunas que serão usadas para calcular o heatmap de correlação.
*   `numeric_df_heatmap = df[numeric_cols_for_heatmap].copy()`: Cria uma cópia (`numeric_df_heatmap`) do DataFrame `df` contendo apenas as colunas especificadas. Usar `.copy()` evita modificar o DataFrame original ao fazer alterações.
*   `numeric_df_heatmap.replace([np.inf, -np.inf], np.nan, inplace=True)`: Substitui quaisquer valores infinitos positivos (`np.inf`) ou negativos (`-np.inf`) nas colunas selecionadas por `np.nan`. Isso é importante porque funções de correlação geralmente não lidam bem com valores infinitos. `inplace=True` modifica o DataFrame `numeric_df_heatmap` diretamente.

## 5. Visualizações Geradas

O script prossegue para gerar uma série de visualizações para explorar os dados. Cada gráfico é salvo como uma imagem (PNG para gráficos estáticos, HTML para gráficos interativos do Plotly) e exibido.

### 5.1 Distribuição Salarial

### 1. Distribuição Salarial
    plt.figure(figsize=(12,6))
    sns.histplot(df['Faixa_salarial_num'].dropna(), bins=20, kde=True)
    plt.title('Distribuição de Salários Mensais')
    plt.xlabel('Salário Médio (R$)')
    plt.ylabel('Contagem')
    plt.savefig('distribuicao_salarial.png')
    plt.show()
    plt.close()


**Explicação:**
*   `plt.figure(figsize=(12,6))`: Cria uma nova figura do Matplotlib com tamanho especificado (largura=12, altura=6 polegadas).
*   `sns.histplot(df['Faixa_salarial_num'].dropna(), bins=20, kde=True)`: Gera um histograma usando Seaborn.
    *   `df['Faixa_salarial_num'].dropna()`: Usa a coluna de salários numéricos, removendo quaisquer valores NaN antes da plotagem.
    *   `bins=20`: Divide os dados em 20 intervalos (barras) no histograma.
    *   `kde=True`: Sobrepõe uma estimativa de densidade do kernel (Kernel Density Estimate) ao histograma, que é uma forma suavizada da distribuição.
*   `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)`: Definem o título do gráfico e os rótulos dos eixos x e y.
*   `plt.savefig('distribuicao_salarial.png')`: Salva o gráfico como um arquivo PNG.
*   `plt.show()`: Exibe o gráfico.
*   `plt.close()`: Fecha a figura para liberar memória.

### 5.2 Salário vs Experiência

