### 0. Importação de Bibliotecas e Configurações Iniciais
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.express as px
    import plotly.graph_objects as go
    from mpl_toolkits.mplot3d import Axes3D # Para gráficos 3D com matplotlib
    import os # Para criar diretórios

- `import pandas as pd`: Importa a biblioteca Pandas, essencial para manipulação e análise de dados tabulares (DataFrames), apelidada como `pd`.
- `import numpy as np`: Importa a biblioteca NumPy, fundamental para computação numérica, especialmente operações com arrays, apelidada como `np`.
- `import matplotlib.pyplot as plt`: Importa o submódulo `pyplot` da Matplotlib, usado para criar gráficos estáticos, apelidado como `plt`.
- `import seaborn as sns`: Importa a biblioteca Seaborn, construída sobre o Matplotlib, para gráficos estatísticos mais atraentes e informativos, apelidada como `sns`.
- `import plotly.express as px`: Importa Plotly Express, uma interface de alto nível para criar figuras complexas com Plotly de forma concisa.
- `import plotly.graph_objects as go`: Importa objetos gráficos do Plotly, permitindo um controle mais granular sobre as visualizações interativas.
- `from mpl_toolkits.mplot3d import Axes3D`: Importa a ferramenta `Axes3D` da Matplotlib, necessária para criar gráficos 3D (embora o script use mais o Plotly para 3D).
- `import os`: Importa o módulo `os` para interagir com o sistema operacional, como criar diretórios.

--- Configurações e Criação de Pasta para Gráficos ---

    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (12, 6)
    pd.set_option('display.max_columns', None)

- `sns.set_style("whitegrid")`: Define o estilo visual padrão dos gráficos Seaborn para "whitegrid", que tem um fundo branco com linhas de grade.
- `plt.rcParams['figure.figsize'] = (12, 6)`: Define o tamanho padrão (12 polegadas de largura por 6 de altura) para todas as figuras geradas pelo Matplotlib.
- `pd.set_option('display.max_columns', None)`: Configura o Pandas para exibir todas as colunas de um DataFrame ao imprimi-lo (útil para inspeção).

Criar pasta para salvar os gráficos, se não existir

    output_dir = 'graficos_analise_exploratoria'
    if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Diretório '{output_dir}' criado para salvar os gráficos.")
    else:
    print(f"Diretório '{output_dir}' já existe. Gráficos serão salvos nele.")

- `output_dir = 'graficos_analise_exploratoria'`: Define o nome do diretório onde os gráficos serão salvos.
- `if not os.path.exists(output_dir): os.makedirs(output_dir)`: Verifica se o diretório existe; se não, cria o diretório.
- `print(...)`: Informa ao usuário se o diretório foi criado ou se já existia.

Função auxiliar para salvar gráficos matplotlib/seaborn

    def save_plt_figure(filename_base, tight_layout=True):
    if tight_layout:
    plt.tight_layout()
    filepath = os.path.join(output_dir, f"{filename_base}.png")
    plt.savefig(filepath)
    print(f"Gráfico salvo em: {filepath}")
    plt.show() # Continuar mostrando o gráfico no notebook

- `def save_plt_figure(...)`: Define uma função reutilizável para salvar gráficos Matplotlib/Seaborn.
    - `if tight_layout: plt.tight_layout()`: Se `tight_layout` for verdadeiro (padrão), ajusta automaticamente os subparâmetros da plotagem para fornecer um layout compacto.
    - `filepath = os.path.join(output_dir, f"{filename_base}.png")`: Constrói o caminho completo do arquivo para salvar o gráfico como PNG.
    - `plt.savefig(filepath)`: Salva a figura atual do Matplotlib no caminho especificado.
    - `print(...)`: Informa onde o gráfico foi salvo.
    - `plt.show()`: Exibe o gráfico na saída do notebook (mesmo após salvar).

Função auxiliar para salvar gráficos Plotly

    def save_plotly_figure(fig, filename_base):
    # Salvar como HTML
    filepath_html = os.path.join(output_dir, f"{filename_base}.html")
    fig.write_html(filepath_html)
    print(f"Gráfico interativo salvo em: {filepath_html}")

# Tentar salvar como PNG (requer kaleido)
    try:
        filepath_png = os.path.join(output_dir, f"{filename_base}.png")
        fig.write_image(filepath_png, scale=2) # scale para melhor resolução
        print(f"Gráfico estático salvo em: {filepath_png}")
    except ValueError as e:
        print(f"Não foi possível salvar {filename_base}.png (Plotly). Erro: {e}")
        print("Certifique-se de ter a biblioteca 'kaleido' instalada: pip install kaleido")
    fig.show() # Continuar mostrando o gráfico no notebook

- `def save_plotly_figure(...)`: Define uma função para salvar gráficos Plotly.
    - `fig.write_html(filepath_html)`: Salva a figura Plotly (`fig`) como um arquivo HTML interativo.
    - `try...except ValueError`: Tenta salvar a figura como um arquivo PNG estático.
        - `fig.write_image(filepath_png, scale=2)`: Converte a figura Plotly para PNG. `scale=2` aumenta a resolução da imagem. Requer a biblioteca `kaleido`.
        - Se `kaleido` não estiver instalado ou ocorrer outro erro, uma mensagem é exibida.
    - `fig.show()`: Exibe o gráfico interativo Plotly na saída do notebook.

### 1. Carregar e Inspecionar Dados

    print("\n--- 1. Carregando e Inspecionando Dados ---")
    try:
    df_profissionais = pd.read_csv('/kaggle/input/dataset-clean/dados_limpos.csv')
    df_microdados_uf = pd.read_csv('/kaggle/input/dataset-microdados-agrupados-por-uf-cleaned/microdados_agrupados_por_uf.csv')
    except FileNotFoundError:
    print("Erro: Um ou ambos os arquivos CSV não foram encontrados. Verifique os caminhos.")
    exit()

- `print(...)`: Imprime um cabeçalho para a seção.
- `try...except FileNotFoundError`: Tenta carregar os dois datasets de arquivos CSV. Se um arquivo não for encontrado, imprime uma mensagem de erro e encerra o script (`exit()`).
    - `df_profissionais = pd.read_csv(...)`: Carrega dados de profissionais.
    - `df_microdados_uf = pd.read_csv(...)`: Carrega dados de microdados de docentes por UF.

          print("\n### Dataset de Profissionais de Dados (dados_limpos.csv):")
          print("Primeiras 5 linhas:")
          print(df_profissionais.head())
          print("\nInformações gerais:")
          df_profissionais.info()
          
          print("\n### Dataset de Microdados por UF (microdados_agrupados_por_uf.csv):")
          print("Primeiras 5 linhas:")
          print(df_microdados_uf.head())
          print("\nInformações gerais:")
          df_microdados_uf.info()
- Para cada DataFrame (`df_profissionais` e `df_microdados_uf`):
    - `print(df.head())`: Exibe as primeiras 5 linhas para uma visualização rápida dos dados.
    - `df.info()`: Exibe um resumo conciso do DataFrame, incluindo tipos de dados de cada coluna, número de valores não nulos e uso de memória. Crucial para entender a estrutura inicial e identificar possíveis problemas (ex: tipos errados, muitos nulos).

### 2. Pré-processamento de `df_profissionais`

    print("\n--- 2. Pré-processamento do Dataset de Profissionais ---")
    df_profissionais_proc = df_profissionais.copy()  

- `print(...)`: Cabeçalho da seção.
- `df_profissionais_proc = df_profissionais.copy()`: Cria uma cópia do DataFrame original. É uma boa prática para evitar modificações acidentais no DataFrame original carregado.

**Mapeamento e Conversão de Colunas Categóricas para Numéricas/Ordinais:**

    faixa_salarial_map = {
    'Menos de R$ 1.000/mês': 500, 'de R$ 1.001/mês a R$ 2.000/mês': 1500,
    # ... (outros mapeamentos de salário) ...
    'Acima de R$ 40.001/mês': 45000
    }
    df_profissionais_proc['Salario_Estimado'] = df_profissionais_proc['Faixa salarial mensal'].map(faixa_salarial_map)
    ordem_faixa_salarial = list(faixa_salarial_map.keys())
    df_profissionais_proc['Faixa salarial mensal'] = pd.Categorical(
    df_profissionais_proc['Faixa salarial mensal'], categories=ordem_faixa_salarial, ordered=True
    )

- `faixa_salarial_map`: Um dicionário que mapeia as strings de faixa salarial para um valor numérico representativo (geralmente o ponto médio ou uma estimativa).
- `df_profissionais_proc['Salario_Estimado'] = ... .map(faixa_salarial_map)`: Cria uma nova coluna `Salario_Estimado` aplicando o mapeamento à coluna `Faixa salarial mensal`.
- `ordem_faixa_salarial = list(faixa_salarial_map.keys())`: Cria uma lista com as chaves do dicionário, que define a ordem correta das faixas salariais.
- `df_profissionais_proc['Faixa salarial mensal'] = pd.Categorical(...)`: Converte a coluna `Faixa salarial mensal` original para o tipo `Categorical` do Pandas.
    - `categories=ordem_faixa_salarial`: Especifica a ordem das categorias.
    - `ordered=True`: Indica que as categorias têm uma ordem intrínseca (são ordinais). Isso é útil para plots e algumas análises.

O mesmo padrão é aplicado para `Tempo de experiência na área de dados` e `Nível de ensino alcançado`:
- `experiencia_map` e `nivel_ensino_map_num` (onde `enumerate` é usado para criar valores ordinais 0, 1, 2...): Dicionários para mapeamento.
- Criação de colunas numéricas estimadas/ordinais (`Experiencia_Anos_Estimados`, `Nivel_Ensino_Ordinal`).
- Conversão das colunas textuais originais para tipo `Categorical` ordenado.

      print("\nDataset de profissionais após pré-processamento (novas colunas e tipos):")
      print(df_profissionais_proc[['Faixa salarial mensal', 'Salario_Estimado',
      'Tempo de experiência na área de dados', 'Experiencia_Anos_Estimados',
      'Nível de ensino alcançado', 'Nivel_Ensino_Ordinal']].head())

- Exibe as primeiras linhas das colunas originais transformadas e das novas colunas numéricas criadas, para verificar o resultado do pré-processamento.

### 3. Análise Exploratória Univariada (em `df_profissionais_proc`)

Esta seção examina a distribuição de variáveis individuais.
    
    print("\n--- 3. Análise Exploratória Univariada ---")

- Cabeçalho da seção.

**Exemplo: 3.1. Distribuição da Faixa Salarial (Categórica)**
    
    plt.figure(figsize=(14, 7))
    sns.countplot(data=df_profissionais_proc, y='Faixa salarial mensal', order=ordem_faixa_salarial, palette='viridis')
    plt.title('Distribuição de Profissionais por Faixa Salarial Mensal')
    plt.xlabel('Contagem')
    plt.ylabel('Faixa Salarial Mensal')
    save_plt_figure('distribuicao_faixa_salarial')

- `plt.figure(figsize=(14, 7))`: Cria uma nova figura Matplotlib com tamanho especificado.
- `sns.countplot(...)`: Cria um gráfico de barras (contagem) usando Seaborn.
    - `data=df_profissionais_proc`: Especifica o DataFrame.
    - `y='Faixa salarial mensal'`: Define a variável do eixo Y (as faixas salariais). O gráfico será horizontal.
    - `order=ordem_faixa_salarial`: Garante que as barras sejam plotadas na ordem definida anteriormente.
    - `palette='viridis'`: Define a paleta de cores.
- `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)`: Definem título e rótulos dos eixos.
- `save_plt_figure('distribuicao_faixa_salarial')`: Salva e exibe o gráfico usando a função auxiliar.

**Padrões semelhantes são usados para outras análises univariadas:**
- **3.2. Salário Estimado (Numérica):** `sns.histplot` com `kde=True` (Kernel Density Estimate) para visualizar a distribuição. `dropna()` é usado para remover NaNs antes de plotar, pois o histplot pode ter problemas com eles.
- **3.3. Nível de Ensino:** `sns.countplot` usando `ordem_nivel_ensino`.
- **3.4. Área de Formação Acadêmica:** `sns.countplot`. A ordem é definida pela contagem de valores (`value_counts().index`).
- **3.5. Tempo de Experiência:** `sns.countplot` usando `ordem_experiencia`.
- **3.6. UF onde mora (Top 10):**
    - `top_10_uf = df_profissionais_proc['UF onde mora'].value_counts().nlargest(10)`: Calcula as 10 UFs mais frequentes.
    - `sns.barplot(x=top_10_uf.index, y=top_10_uf.values, ...)`: Cria um gráfico de barras para o Top 10. `barplot` é usado aqui porque os valores (contagens) já foram calculados.
    - `plt.xticks(rotation=45)`: Rotaciona os rótulos do eixo X para evitar sobreposição.

### 4. Análise Exploratória Bivariada (em `df_profissionais_proc`)

Esta seção explora a relação entre duas variáveis.

    print("\n--- 4. Análise Exploratória Bivariada ---")[

- Cabeçalho da seção.

**Exemplo: 4.1. Formação Acadêmica vs. Salário Estimado (Matplotlib/Seaborn e Plotly)**
*   **Com Matplotlib/Seaborn:**
    ```
    plt.figure(figsize=(12, 7))
    sns.boxplot(data=df_profissionais_proc, x='Salario_Estimado', y='Nível de ensino alcançado',
                order=ordem_nivel_ensino, palette='crest')
    plt.title('Salário Estimado por Nível de Ensino')
    # ... rótulos e save_plt_figure ...
    ```
    - `sns.boxplot(...)`: Cria boxplots para mostrar a distribuição do `Salario_Estimado` para cada `Nível de ensino alcançado`.
    - `x='Salario_Estimado'`, `y='Nível de ensino alcançado'`: Define as variáveis dos eixos.
    - `order=ordem_nivel_ensino`: Garante a ordem correta das categorias no eixo Y.
*   **Com Plotly:**
    ```
    fig_box_sal_nivel = px.box(df_profissionais_proc.dropna(subset=['Salario_Estimado', 'Nível de ensino alcançado']),
                               x='Salario_Estimado', y='Nível de ensino alcançado',
                               category_orders={'Nível de ensino alcançado': ordem_nivel_ensino},
                               title='Salário Estimado por Nível de Ensino (Plotly)',
                               labels={...}, color='Nível de ensino alcançado')
    save_plotly_figure(fig_box_sal_nivel, 'boxplot_salario_por_nivel_ensino_plotly')
    ```
    - `px.box(...)`: Cria boxplots interativos com Plotly Express.
    - `dropna(subset=[...])`: Remove linhas onde o salário ou nível de ensino são NaN, pois Plotly pode não lidar bem com eles em boxplots.
    - `category_orders`: Similar ao `order` do Seaborn, para definir a ordem das categorias.
    - `color='Nível de ensino alcançado'`: Colore os boxplots de acordo com o nível de ensino.
    - `save_plotly_figure`: Salva e exibe o gráfico Plotly.

**Padrões semelhantes para outras análises bivariadas:**
- **4.2. Área de Formação vs. Salário Estimado (Top 5 áreas):** Filtra para as 5 áreas mais comuns e usa `sns.boxplot`.
- **4.3. Experiência Profissional vs. Salário Estimado:** Boxplots com Seaborn e Plotly, similar ao item 4.1.

**4.4. Heatmap de Correlação**

    cols_numericas_interesse = ['Salario_Estimado', 'Experiencia_Anos_Estimados', 'Nivel_Ensino_Ordinal']
    df_corr = df_profissionais_proc[cols_numericas_interesse].dropna()
    matriz_corr = df_corr.corr()
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Heatmap de Correlação entre Salário, Experiência (anos) e Nível de Ensino (ordinal)')

- `cols_numericas_interesse`: Seleciona colunas numéricas para calcular a correlação.
- `df_corr = ... .dropna()`: Remove linhas com qualquer valor NaN nas colunas selecionadas, pois a correlação não lida com NaNs.
- `matriz_corr = df_corr.corr()`: Calcula a matriz de correlação de Pearson.
- `sns.heatmap(...)`: Visualiza a matriz de correlação.
    - `annot=True`: Mostra os valores de correlação no mapa.
    - `cmap='coolwarm'`: Paleta de cores (azul para negativo, vermelho para positivo).
    - `fmt=".2f"`: Formata os números para duas casas decimais.
- `tight_layout=False`: Às vezes, para heatmaps, desabilitar o `tight_layout` evita que os rótulos sejam cortados.

### 5. Análise Exploratória Multivariada (Interações em `df_profissionais_proc`)

Examina a relação entre três ou mais variáveis.
    
    print("\n--- 5. Análise Exploratória Multivariada (Interações) ---")


**5.1. Interação: Salário Estimado por Experiência, segmentado por Nível de Ensino**
    
    df_lineplot = df_profissionais_proc.dropna(subset=['Experiencia_Anos_Estimados', 'Salario_Estimado', 'Nível de ensino alcançado'])
    sns.lineplot(data=df_lineplot, x='Experiencia_Anos_Estimados', y='Salario_Estimado',
    hue='Nível de ensino alcançado', hue_order=ordem_nivel_ensino,
    palette='viridis', marker='o', errorbar=('ci', 95))
    save_plt_figure('heatmap_correlacao_salario_exp_ensino', tight_layout=False)

- `df_lineplot = ... .dropna()`: Remove NaNs das colunas envolvidas para evitar problemas com `lineplot`.
- `sns.lineplot(...)`: Cria um gráfico de linha.
    - `x='Experiencia_Anos_Estimados'`, `y='Salario_Estimado'`: Variáveis principais.
    - `hue='Nível de ensino alcançado'`: Cria uma linha separada (com cor diferente) para cada categoria de nível de ensino.
    - `hue_order`: Define a ordem das categorias na legenda e para as cores.
    - `marker='o'`: Adiciona marcadores circulares aos pontos de dados.
    - `errorbar=('ci', 95)`: Mostra o intervalo de confiança de 95% em torno da média (se houver múltiplas observações por ponto x e hue).

**5.2. Boxplot: Salário por Experiência, facetado por Nível de Ensino**

    df_catplot = df_profissionais_proc.dropna(subset=[...])
    g = sns.catplot(data=df_catplot, x='Tempo de experiência na área de dados', y='Salario_Estimado',
    col='Nível de ensino alcançado', col_wrap=3, kind='box',
    order=ordem_experiencia, col_order=ordem_nivel_ensino, palette='Paired', height=5, aspect=1.2)
    g.set_titles("{col_name}")
    g.set_xticklabels(rotation=30, ha='right')

- `sns.catplot(...)`: Uma função de alto nível para desenhar gráficos categóricos em um `FacetGrid`.
    - `col='Nível de ensino alcançado'`: Cria subplots (facetas) separados para cada nível de ensino, organizados em colunas.
    - `col_wrap=3`: Quebra as colunas de facetas a cada 3 subplots.
    - `kind='box'`: Especifica que o tipo de gráfico em cada faceta será um boxplot.
    - `g.set_titles(...)`, `g.set_xticklabels(...)`: Métodos específicos do `FacetGrid` (`g`) para ajustar títulos e rótulos.
    - O salvamento é feito usando `g.savefig(...)`.

**5.3. Gráfico 3D: Salário vs. Experiência Numérica vs. Nível de Ensino Numérico (Plotly)**

    df_plot3d = df_profissionais_proc.dropna(subset=[...])
    fig_3d_scatter = px.scatter_3d(df_plot3d,
    x='Experiencia_Anos_Estimados',
    y='Nivel_Ensino_Ordinal',
    z='Salario_Estimado',
    color='Nível de ensino alcançado',
    # ... category_orders, labels, title ...
    )
    fig_3d_scatter.update_layout(scene=dict(
    yaxis = dict(
    tickmode = 'array',
    tickvals = list(nivel_ensino_map_num.values()),
    ticktext = list(nivel_ensino_map_num.keys())
    )))
    save_plotly_figure(fig_3d_scatter, 'scatter3d_salario_exp_ensino')

- `px.scatter_3d(...)`: Cria um gráfico de dispersão 3D interativo com Plotly.
    - `x`, `y`, `z`: Definem as três dimensões.
    - `color='Nível de ensino alcançado'`: Colore os pontos pela categoria de nível de ensino.
    - `fig_3d_scatter.update_layout(scene=dict(yaxis=dict(...)))`: Customiza os eixos da cena 3D. Aqui, está configurando o eixo Y (`Nivel_Ensino_Ordinal`) para mostrar os rótulos textuais (`ticktext`) correspondentes aos valores numéricos ordinais (`tickvals`).

**5.4 Gráfico de Superfície 3D (Plotly)**

    df_agg_3d = df_profissionais_proc.groupby(['Experiencia_Anos_Estimados', 'Nivel_Ensino_Ordinal'], as_index=False)['Salario_Estimado'].mean()
    df_agg_3d = df_agg_3d.dropna()
    
    if not df_agg_3d.empty and len(df_agg_3d['Experiencia_Anos_Estimados'].unique()) > 1 and len(df_agg_3d['Nivel_Ensino_Ordinal'].unique()) > 1:
    try:
    pivot_3d = df_agg_3d.pivot(index='Nivel_Ensino_Ordinal', columns='Experiencia_Anos_Estimados', values='Salario_Estimado')
    pivot_3d = pivot_3d.fillna(0) # Preencher NaNs para o plot

  X_surf = pivot_3d.columns.values
  Y_surf = pivot_3d.index.values
  Z_surf = pivot_3d.values

  fig_3d_surface = go.Figure(data=[go.Surface(z=Z_surf, x=X_surf, y=Y_surf, colorscale='Viridis')])
  # ... update_layout com títulos de eixos e customização do yaxis similar ao scatter_3d ...
  save_plotly_figure(fig_3d_surface, 'surface3d_salario_medio_exp_ensino')
except Exception as e:
    # ... tratamento de erro ...

    else:
    print("Dados insuficientes ... para gerar gráfico de superfície 3D ...")

- `df_agg_3d = ... .groupby(...).mean()`: Agrupa os dados por experiência e nível de ensino para calcular o salário médio estimado (o valor Z da superfície).
- `if not df_agg_3d.empty ...`: Verifica se há dados suficientes e variados para criar uma superfície.
- `pivot_3d = df_agg_3d.pivot(...)`: Transforma os dados agregados em um formato de grade (matriz), onde as linhas são níveis de ensino, colunas são anos de experiência, e os valores são os salários médios. Isso é necessário para o gráfico de superfície.
- `pivot_3d = pivot_3d.fillna(0)`: Preenche quaisquer NaNs restantes na grade (ex: combinações sem dados) com 0 para permitir a plotagem.
- `X_surf, Y_surf, Z_surf`: Extrai os valores dos eixos e da superfície da tabela pivotada.
- `fig_3d_surface = go.Figure(data=[go.Surface(...)])`: Cria a figura de superfície 3D usando `plotly.graph_objects`.
- A customização do eixo Y é semelhante à do gráfico de dispersão 3D.

### 6. Integração dos Dados
    
    print("\n--- 6. Integração dos Datasets ---")
    df_integrado = pd.merge(df_profissionais_proc, df_microdados_uf,
    left_on='UF onde mora', right_on='UF',
    how='left')
    print("\nDataset integrado (primeiras linhas):")
    print(df_integrado.head())

- `print(...)`: Cabeçalho da seção.
- `df_integrado = pd.merge(...)`: Combina (`merge`) os dois DataFrames (`df_profissionais_proc` e `df_microdados_uf`).
    - `left_on='UF onde mora'`: Coluna chave do DataFrame da esquerda (`df_profissionais_proc`).
    - `right_on='UF'`: Coluna chave do DataFrame da direita (`df_microdados_uf`).
    - `how='left'`: Tipo de junção. Mantém todas as linhas do DataFrame da esquerda e as colunas correspondentes do da direita. Se não houver correspondência na direita, os valores serão NaN.
- Exibe as primeiras linhas do DataFrame integrado.

### 7. Análise Exploratória com Dados Integrados

    print("\n--- 7. Análise Exploratória com Dados Integrados ---")
    if df_integrado['Docentes_Doutorado'].isnull().all():
    print("Merge não resultou em dados úteis de microdados para os profissionais.")
    else:
    # Criação de novas features no dataset integrado
    df_integrado['Total_Docentes_UF'] = df_integrado[['Docentes_Graduacao', ..., 'Docentes_Doutorado']].sum(axis=1)
    df_integrado['Prop_Docentes_Doutorado_UF'] = df_integrado['Docentes_Doutorado'] / df_integrado['Total_Docentes_UF']
    df_integrado['Prop_Docentes_Doutorado_UF'].replace([np.inf, -np.inf], np.nan, inplace=True) # Tratar divisão por zero

- `if df_integrado['Docentes_Doutorado'].isnull().all()`: Verifica se a junção foi bem-sucedida (se alguma informação de docentes foi adicionada). Se a coluna `Docentes_Doutorado` (do `df_microdados_uf`) estiver inteiramente NaN, significa que nenhuma UF correspondeu.
- `df_integrado['Total_Docentes_UF'] = ... .sum(axis=1)`: Calcula o número total de docentes em cada UF somando as colunas de diferentes titulações. `axis=1` indica soma ao longo das linhas.
- `df_integrado['Prop_Docentes_Doutorado_UF'] = ...`: Calcula a proporção de docentes com doutorado na UF.
- `.replace([np.inf, -np.inf], np.nan, inplace=True)`: Substitui valores infinitos (que podem surgir de divisão por zero se `Total_Docentes_UF` for 0) por NaN.

**7.1. Salário Estimado vs. Proporção de Docentes com Doutorado na UF**

    df_plot_integrado = df_integrado.dropna(subset=['Salario_Estimado', 'Prop_Docentes_Doutorado_UF', ...])
    if not df_plot_integrado.empty:
    plt.figure(figsize=(14, 9))
    sns.scatterplot(data=df_plot_integrado, x='Prop_Docentes_Doutorado_UF', y='Salario_Estimado',
    hue='Nível de ensino alcançado',
    size='Experiencia_Anos_Estimados',
    palette='Set2', alpha=0.7, sizes=(20, 200))
    # ... título, rótulos, legenda ajustada (bbox_to_anchor), save_plt_figure ...
    corr_sal_prop_dout = df_plot_integrado[['Salario_Estimado', 'Prop_Docentes_Doutorado_UF']].corr().iloc
    print(f"\nCorrelação entre Salário Estimado e Proporção de Docentes com Doutorado na UF: {corr_sal_prop_dout:.2f}")

- `df_plot_integrado = ... .dropna()`: Remove NaNs das colunas relevantes para o plot.
- `if not df_plot_integrado.empty`: Verifica se há dados para plotar.
- `sns.scatterplot(...)`: Cria um gráfico de dispersão.
    - `x='Prop_Docentes_Doutorado_UF'`, `y='Salario_Estimado'`.
    - `hue='Nível de ensino alcançado'`: Colore os pontos pelo nível de ensino do profissional.
    - `size='Experiencia_Anos_Estimados'`: Varia o tamanho dos pontos pela experiência do profissional.
    - `sizes=(20, 200)`: Define o intervalo de tamanhos para os pontos.
    - `plt.legend(..., bbox_to_anchor=(1.05, 1), loc='upper left')`: Ajusta a posição da legenda para fora da área do gráfico para evitar sobreposição.
- `corr_sal_prop_dout = ... .corr().iloc[0,1]`: Calcula e imprime a correlação de Pearson entre o salário estimado e a proporção de docentes com doutorado na UF.

**7.2. Média Salarial por UF e comparação com total de docentes na UF (Gráfico Combinado)**

    df_integrado_agg = df_integrado.dropna(subset=['UF onde mora', 'Salario_Estimado', 'Total_Docentes_UF'])
    media_salarial_uf = df_integrado_agg.groupby('UF onde mora')['Salario_Estimado'].mean().sort_values(ascending=False)
    total_docentes_uf_agg = df_integrado_agg.groupby('UF onde mora')['Total_Docentes_UF'].first().sort_values(ascending=False)
    
    if not media_salarial_uf.empty and not total_docentes_uf_agg.empty:
    df_comparacao_uf = pd.DataFrame({'Media_Salarial': media_salarial_uf, 'Total_Docentes': total_docentes_uf_agg}).dropna().sort_values(by='Media_Salarial', ascending=False)


if not df_comparacao_uf.empty:
    fig, ax1 = plt.subplots(figsize=(16, 9)) # Cria figura e um conjunto de eixos

    # Eixo 1 (Salário Médio - Barras)
    color = 'tab:red'
    ax1.set_xlabel('UF onde mora')
    ax1.set_ylabel('Salário Médio Estimado (R$)', color=color)
    ax1.bar(df_comparacao_uf.index, df_comparacao_uf['Media_Salarial'], color=color, alpha=0.6, label='Salário Médio')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.tick_params(axis='x', rotation=90)
    ax1.grid(False) # Remove grade para clareza

    # Eixo 2 (Total Docentes - Linha, compartilhando o eixo X)
    ax2 = ax1.twinx() # Cria um segundo eixo Y que compartilha o mesmo eixo X
    color = 'tab:blue'
    ax2.set_ylabel('Total de Docentes na UF', color=color)
    ax2.plot(df_comparacao_uf.index, df_comparacao_uf['Total_Docentes'], color=color, marker='o', linestyle='--', label='Total Docentes')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.grid(False)

    fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes) # Legenda combinada
    plt.title('Salário Médio Estimado e Total de Docentes por UF')
    save_plt_figure('bar_line_salario_medio_total_docentes_uf')

- `df_integrado_agg = ... .dropna()`: Remove NaNs das colunas chave para agregação.
- `media_salarial_uf = ... .groupby(...).mean()`: Calcula o salário médio por UF.
- `total_docentes_uf_agg = ... .groupby(...).first()`: Pega o total de docentes por UF (usar `.first()` é seguro se o total de docentes for o mesmo para todas as entradas de uma mesma UF no `df_integrado`, o que deve ser o caso após o merge).
- `df_comparacao_uf = pd.DataFrame(...)`: Cria um novo DataFrame combinando as médias salariais e totais de docentes por UF.
- `fig, ax1 = plt.subplots(...)`: Cria uma figura e um conjunto de eixos (`ax1`).
- Gráfico de barras para `Media_Salarial` em `ax1`.
- `ax2 = ax1.twinx()`: Cria `ax2`, um segundo conjunto de eixos que compartilha o mesmo eixo X que `ax1`, mas tem seu próprio eixo Y no lado direito.
- Gráfico de linha para `Total_Docentes` em `ax2`.
- `fig.legend(...)`: Cria uma legenda única para os elementos de `ax1` e `ax2`.

      print("\n--- Análise Exploratória Concluída ---")
      print(f"Todos os gráficos foram salvos no diretório: {output_dir}")

- Mensagens finais indicando a conclusão da análise e onde os gráficos foram salvos.
