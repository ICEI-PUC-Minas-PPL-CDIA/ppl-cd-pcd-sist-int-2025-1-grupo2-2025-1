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

    plt.figure(figsize=(12,6))
    sns.boxplot(x='Tempo de experiência na área de dados', y='Faixa_salarial_num', data=df)
    plt.title('Relação entre Salário e Tempo de Experiência')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('salario_vs_experiencia.png')
    plt.show()
    plt.close()


**Explicação:**
*   `sns.boxplot(...)`: Cria um boxplot (diagrama de caixa) para visualizar a distribuição dos salários (`Faixa_salarial_num`) para cada categoria de tempo de experiência (`Tempo de experiência na área de dados`).
*   `plt.xticks(rotation=45, ha='right')`: Rotaciona os rótulos do eixo x em 45 graus e alinha-os à direita para melhor legibilidade caso sejam longos.
*   `plt.tight_layout()`: Ajusta automaticamente os parâmetros da plotagem para dar um layout compacto.

### 5.3 Salário vs Formação Acadêmica
    plt.figure(figsize=(14,7))
    sns.violinplot(x='Nível de ensino alcançado', y='Faixa_salarial_num', data=df)
    plt.title('Distribuição Salarial por Nível de Ensino')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('salario_vs_formacao.png')
    plt.show()
    plt.close()


**Explicação:**
*   `sns.violinplot(...)`: Gera um violin plot, que combina características de um boxplot com uma estimativa de densidade do kernel. Ele mostra a distribuição dos salários (`Faixa_salarial_num`) para diferentes níveis de ensino (`Nível de ensino alcançado`).

### 5.4 Gráfico 3D Interativo (Salário, Experiência, Nível Educacional)

    fig_3d = px.scatter_3d(df.dropna(subset=['Faixa_salarial_num', 'Tempo de experiência na área de dados', 'Nível de ensino alcançado']),
    x='Faixa_salarial_num',
    y='Tempo de experiência na área de dados',
    z='Nível de ensino alcançado',
    color='Área de formação acadêmica',
    hover_name='Cargo atual',
    height=800,
    title='Salário vs Experiência vs Nível Educacional')
    fig_3d.update_layout(scene = dict(
    xaxis_title='Salário (R$)',
    yaxis_title='Experiência',
    zaxis_title='Nível Educacional'))
    fig_3d.write_html('grafico_3d_interativo.html') # Modificado na conversa para full_html=False, include_plotlyjs='cdn' para incorporação
    fig_3d.show()

**Explicação:**
*   `px.scatter_3d(...)`: Cria um gráfico de dispersão 3D interativo usando Plotly Express.
    *   `df.dropna(...)`: Remove linhas com NaNs nas colunas usadas para os eixos x, y e z para evitar erros.
    *   `x`, `y`, `z`: Mapeiam as colunas `Faixa_salarial_num`, `Tempo de experiência na área de dados`, e `Nível de ensino alcançado` para os eixos do gráfico.
    *   `color='Área de formação acadêmica'`: Colore os pontos de acordo com a área de formação.
    *   `hover_name='Cargo atual'`: Define a informação que aparece quando o mouse passa sobre um ponto.
    *   `height=800`: Define a altura da figura.
*   `fig_3d.update_layout(...)`: Personaliza o layout da cena 3D, definindo os títulos dos eixos.
*   `fig_3d.write_html('grafico_3d_interativo.html')`: Salva o gráfico como um arquivo HTML interativo. (Nota: Em interações posteriores, este comando foi modificado para `fig_3d.write_html('grafico_3d_interativo.html', full_html=False, include_plotlyjs='cdn')` para facilitar a incorporação em páginas web).

### 5.5 Heatmap de Correlação

    plt.figure(figsize=(10,6))
    sns.heatmap(numeric_df_heatmap.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Mapa de Calor de Correlações')
    plt.tight_layout()
    plt.savefig('heatmap_correlacao.png')
    plt.show()
    plt.close()


**Explicação:**
*   `sns.heatmap(numeric_df_heatmap.corr(), ...)`: Gera um mapa de calor para visualizar a matriz de correlação das colunas em `numeric_df_heatmap`.
    *   `numeric_df_heatmap.corr()`: Calcula a matriz de correlação de Pearson.
    *   `annot=True`: Exibe os valores de correlação em cada célula do heatmap.
    *   `cmap='coolwarm'`: Define o mapa de cores (vermelho para correlações positivas, azul para negativas).
    *   `fmt=".2f"`: Formata os valores de correlação exibidos para duas casas decimais.

### 5.6 Distribuição por Gênero e Raça

    fig_dist_gen_raca, ax_gen_raca = plt.subplots(1,2, figsize=(18,6))
    sns.countplot(x='Gênero do profissional', data=df, ax=ax_gen_raca)
    ax_gen_raca.set_title('Distribuição por Gênero')
    ax_gen_raca.tick_params(axis='x', rotation=45)
    
    sns.countplot(x='Cor/Raça/Etnia', data=df, ax=ax_gen_raca)
    ax_gen_raca.set_title('Distribuição por Raça/Etnia')
    ax_gen_raca.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('distribuicao_genero_raca.png')
    plt.show()
    plt.close(fig_dist_gen_raca)


**Explicação:**
*   `plt.subplots(1,2, figsize=(18,6))`: Cria uma figura com 1 linha e 2 colunas de subplots (gráficos lado a lado). `fig_dist_gen_raca` é a figura inteira, e `ax_gen_raca` é um array de eixos (um para cada subplot).
*   `sns.countplot(..., ax=ax_gen_raca[0])`: Cria um gráfico de contagem para a coluna `Gênero do profissional` no primeiro subplot (`ax_gen_raca[0]`).
*   `sns.countplot(..., ax=ax_gen_raca[1])`: Cria um gráfico de contagem para a coluna `Cor/Raça/Etnia` no segundo subplot (`ax_gen_raca[1]`).
*   `.set_title(...)` e `.tick_params(...)` são usados para personalizar cada subplot.

### 5.7 Sunburst Chart Hierárquico

    sunburst_df = df.dropna(subset=['Nível de ensino alcançado', 'Área de formação acadêmica', 'Cargo atual', 'Faixa_salarial_num'])
    fig_sunburst = px.sunburst(sunburst_df,
    path=['Nível de ensino alcançado', 'Área de formação acadêmica', 'Cargo atual'],
    values='Faixa_salarial_num',
    height=800,
    title='Hierarquia: Nível de Ensino, Área de Formação, Cargo e Salário')
    fig_sunburst.write_html('sunburst_chart.html')
    fig_sunburst.show()


**Explicação:**
*   `sunburst_df = df.dropna(...)`: Cria um novo DataFrame `sunburst_df` removendo linhas com NaNs nas colunas que definirão a hierarquia (`path`) e os valores (`values`) do gráfico sunburst. Isso é crucial para a correta construção do gráfico.
*   `px.sunburst(...)`: Cria um gráfico sunburst interativo.
    *   `path=[...]`: Define a ordem hierárquica dos níveis, do centro para fora: `Nível de ensino alcançado`, depois `Área de formação acadêmica`, e por fim `Cargo atual`.
    *   `values='Faixa_salarial_num'`: O tamanho de cada setor no gráfico é proporcional à soma dos valores de `Faixa_salarial_num` para aquela categoria e seus descendentes na hierarquia.

### 5.8 Distribuição Geográfica
    
    plt.figure(figsize=(12,6))
    df['UF onde mora'].value_counts().plot(kind='bar')
    plt.title('Distribuição Geográfica dos Profissionais')
    plt.xlabel('Estado (UF)')
    plt.ylabel('Contagem')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('distribuicao_geografica.png')
    plt.show()
    plt.close()


**Explicação:**
*   `df['UF onde mora'].value_counts()`: Conta a frequência de cada estado (UF) na coluna `UF onde mora`.
*   `.plot(kind='bar')`: Plota o resultado como um gráfico de barras.

### 5.9 Senioridade vs Salário

    plt.figure(figsize=(12,6))
    sns.boxplot(x='Nível de senioridade', y='Faixa_salarial_num', data=df)
    plt.title('Salário por Nível de Senioridade')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('senioridade_vs_salario.png')
    plt.show()
    plt.close()


**Explicação:**
*   Similar ao gráfico de Salário vs Experiência, este boxplot mostra a distribuição dos salários (`Faixa_salarial_num`) para diferentes níveis de senioridade (`Nível de senioridade`).

### 5.10 Pairplot Multivariado

Preparar DataFrame para pairplot, limpando inf e NaN

    cols_for_pairplot = ['Faixa_salarial_num', 'Oportunidade de aprendizado',
    'Reputação da empresa', 'Nível de senioridade']
    pairplot_df = df[cols_for_pairplot].copy()
    pairplot_df.replace([np.inf, -np.inf], np.nan, inplace=True)
    pairplot_df.dropna(inplace=True)

Verificar se há dados suficientes após o dropna para o pairplot

    if not pairplot_df.empty:
    sns.pairplot(pairplot_df, diag_kind='kde', corner=True) # Adicionado diag_kind e corner para melhor visualização
    plt.suptitle('Análise Multivariada das Relações entre Variáveis Selecionadas', y=1.02)
    plt.tight_layout()
    plt.savefig('pairplot_multivariado.png')
    plt.show()
    plt.close()
    else:
    print("Não há dados suficientes para gerar o Pairplot após remover NaNs.")


**Explicação:**
*   `cols_for_pairplot`: Define uma lista de colunas para incluir no pairplot.
*   `pairplot_df = df[cols_for_pairplot].copy()`: Cria uma cópia do DataFrame com essas colunas.
*   `pairplot_df.replace(...)` e `pairplot_df.dropna(inplace=True)`: Limpa o DataFrame de valores infinitos e NaNs para garantir que o pairplot funcione corretamente.
*   `if not pairplot_df.empty:`: Verifica se ainda há dados após a limpeza.
*   `sns.pairplot(pairplot_df, diag_kind='kde', corner=True)`: Gera um pairplot.
    *   Mostra gráficos de dispersão para cada par de variáveis nas colunas selecionadas.
    *   `diag_kind='kde'`: Mostra estimativas de densidade do kernel (KDEs) nas diagonais (em vez de histogramas).
    *   `corner=True`: Plota apenas a parte triangular inferior da matriz de gráficos, o que é comum quando as relações são simétricas (ex: corr(A,B) == corr(B,A)).
*   `plt.suptitle(...)`: Adiciona um título principal acima de todos os subplots.
*   Se `pairplot_df` estiver vazio após a limpeza, uma mensagem é impressa.

## 6. Conclusão da Análise

O script finaliza com uma mensagem indicando que a análise foi concluída.
    
    print("Análise exploratória concluída e gráficos salvos.")


**Explicação:**
*   Uma simples instrução `print` informa ao usuário que o processo de análise e salvamento dos gráficos foi finalizado.
