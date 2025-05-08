### Este código Python realiza uma análise exploratória de dados (EDA) em um conjunto de dados sobre docentes, utilizando bibliotecas como Pandas para manipulação de dados, Matplotlib e Seaborn para visualizações estáticas, e Plotly para visualizações interativas.

## Instalação de Dependências (Opcional)

    !pip install -U kaleido
*   `!pip install -U kaleido`: Esta linha é um comando de shell (executado diretamente no ambiente do notebook) que instala ou atualiza (`-U`) a biblioteca `kaleido`. Kaleido é um motor usado pela biblioteca Plotly para exportar gráficos interativos como imagens estáticas (por exemplo, .png).

## Importação de Bibliotecas

    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.express as px
    import plotly.graph_objects as go
    import os
    
*   `import pandas as pd`: Importa a biblioteca Pandas, fundamental para manipulação e análise de dados tabulares, e a apelida de `pd`.
*   `import matplotlib.pyplot as plt`: Importa o módulo `pyplot` da biblioteca Matplotlib, usado para criar gráficos estáticos, e o apelida de `plt`.
*   `import seaborn as sns`: Importa a biblioteca Seaborn, que é construída sobre o Matplotlib e oferece uma interface de mais alto nível para criar gráficos estatísticos atraentes. É apelidada de `sns`.
*   `import plotly.express as px`: Importa o módulo `express` da biblioteca Plotly, que fornece uma interface concisa e de alto nível para criar figuras interativas. É apelidado de `px`.
*   `import plotly.graph_objects as go`: Importa o módulo `graph_objects` da biblioteca Plotly, que oferece mais controle e personalização para criar figuras interativas. É apelidado de `go`.
*   `import os`: Importa o módulo `os`, que fornece funcionalidades para interagir com o sistema operacional, como criar diretórios.

## Configuração do Diretório de Saída
    output_dir = '/kaggle/working/graficos'
    os.makedirs(output_dir, exist_ok=True)
*   `output_dir = '/kaggle/working/graficos'`: Define uma variável `output_dir` que armazena o caminho do diretório onde os gráficos gerados serão salvos.
*   `os.makedirs(output_dir, exist_ok=True)`: Cria o diretório especificado em `output_dir`. O argumento `exist_ok=True` garante que o código não gere um erro se o diretório já existir.

## Configuração de Estilo dos Gráficos

    plt.style.use('ggplot')
    sns.set_palette("husl")
    
*   `plt.style.use('ggplot')`: Define o estilo dos gráficos gerados pelo Matplotlib para 'ggplot', que é um estilo popular originário da biblioteca ggplot2 do R, conhecido por sua estética agradável.
*   `sns.set_palette("husl")`: Define a paleta de cores padrão para os gráficos gerados pelo Seaborn como "husl", que é uma paleta com cores uniformemente espaçadas no espaço de cores HUSL (Hue, Saturation, Lightness).

## 1. Carregamento dos Dados

    df = pd.read_csv('/kaggle/input/dataset-microdados-agrupados-por-uf-cleaned/microdados_agrupados_por_uf.csv')

*   `df = pd.read_csv(...)`: Carrega os dados de um arquivo CSV localizado no caminho especificado para um DataFrame do Pandas chamado `df`. O arquivo CSV contém microdados agrupados por Unidade Federativa (UF).

## 2. Pré-processamento dos Dados

    degree_cols = ['Docentes_Graduacao', 'Docentes_Especializacao',
    'Docentes_Mestrado', 'Docentes_Doutorado']
    age_cols = [col for col in df.columns if 'Idade' in col]
    
    df['Total_Docentes'] = df[degree_cols].sum(axis=1)
    df_melted = df.melt(id_vars='UF', value_vars=degree_cols,
    var_name='Formação', value_name='Quantidade')

*   `degree_cols = [...]`: Cria uma lista chamada `degree_cols` contendo os nomes das colunas que representam os diferentes níveis de formação dos docentes (Graduação, Especialização, Mestrado, Doutorado).
*   `age_cols = [col for col in df.columns if 'Idade' in col]`: Cria uma lista chamada `age_cols` usando uma compreensão de lista. Ela seleciona todos os nomes de colunas do DataFrame `df` que contêm a substring 'Idade'.
*   `df['Total_Docentes'] = df[degree_cols].sum(axis=1)`: Cria uma nova coluna no DataFrame `df` chamada 'Total\_Docentes'. O valor de cada linha nesta coluna é a soma dos valores das colunas listadas em `degree_cols` para aquela respectiva linha (`axis=1` indica que a soma é feita horizontalmente, ou seja, ao longo das colunas).
*   `df_melted = df.melt(...)`: Transforma (ou "derrete") o DataFrame `df` de um formato largo para um formato longo, o que pode ser útil para algumas visualizações.
    *   `id_vars='UF'`: Especifica que a coluna 'UF' deve ser mantida como um identificador.
    *   `value_vars=degree_cols`: Especifica que as colunas em `degree_cols` são as colunas cujos valores serão "derretidos".
    *   `var_name='Formação'`: O nome da nova coluna que conterá os nomes das colunas originais de `degree_cols`.
    *   `value_name='Quantidade'`: O nome da nova coluna que conterá os valores correspondentes das colunas de `degree_cols`.

## 3. Função Auxiliar para Salvamento de Gráficos

    def save_plot(fig, filename, formats=['png']):
    """Salva gráficos em múltiplos formatos"""
    for fmt in formats:
    full_path = f'{output_dir}/{filename}.{fmt}'
    
    if fmt == 'png':
    if isinstance(fig, go.Figure):
    fig.write_image(full_path, engine="kaleido")
    else:
    fig.savefig(full_path, bbox_inches='tight')
    
    elif fmt == 'html':
    if isinstance(fig, go.Figure):
    fig.write_html(full_path)
    else:
    print(f"Ignorando HTML para {filename} (suportado apenas para Plotly)")
    continue
    
    print(f'✓ Arquivo salvo: {full_path}')

*   `def save_plot(fig, filename, formats=['png']):`: Define uma função chamada `save_plot` que recebe um objeto de figura (`fig`), um nome de arquivo (`filename`) e uma lista de formatos (`formats`, com 'png' como padrão).
*   `"""Salva gráficos em múltiplos formatos"""`: Docstring que descreve a função.
*   `for fmt in formats:`: Itera sobre cada formato especificado na lista `formats`.
*   `full_path = f'{output_dir}/{filename}.{fmt}'`: Constrói o caminho completo do arquivo onde o gráfico será salvo, usando f-strings para formatação.
*   `if fmt == 'png':`: Verifica se o formato atual é 'png'.
    *   `if isinstance(fig, go.Figure):`: Verifica se a figura `fig` é uma instância de `plotly.graph_objects.Figure` (ou seja, um gráfico Plotly).
        *   `fig.write_image(full_path, engine="kaleido")`: Se for um gráfico Plotly, salva-o como uma imagem PNG usando o motor Kaleido.
    *   `else:`: Caso contrário (presume-se que seja um gráfico Matplotlib).
        *   `fig.savefig(full_path, bbox_inches='tight')`: Salva a figura Matplotlib. `bbox_inches='tight'` ajusta a caixa delimitadora da figura para incluir todos os elementos.
*   `elif fmt == 'html':`: Verifica se o formato atual é 'html'.
    *   `if isinstance(fig, go.Figure):`: Verifica se é um gráfico Plotly.
        *   `fig.write_html(full_path)`: Salva o gráfico Plotly como um arquivo HTML interativo.
    *   `else:`: Caso contrário.
        *   `print(f"Ignorando HTML para {filename} (suportado apenas para Plotly)")`: Informa que o salvamento em HTML é ignorado para tipos de gráficos não Plotly.
        *   `continue`: Pula para a próxima iteração do loop.
*   `print(f'✓ Arquivo salvo: {full_path}')`: Imprime uma mensagem de confirmação informando que o arquivo foi salvo.

## 4. Visualizações com Salvamento em Múltiplos Formatos

### Gráfico 1: Distribuição de Formação Acadêmica Nacional (Pizza)

    plt.figure(figsize=(10,6))
    df[degree_cols].sum().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Distribuição Nacional de Níveis de Formação dos Docentes')
    plt.ylabel('')
    plt.show()
    
    Para salvar este gráfico (exemplo, pois o código original não salva os gráficos de Matplotlib estáticos):
    fig = plt.gcf() # Pega a figura atual
    save_plot(fig, '01_distribuicao_formacao_nacional')

*   `# Gráfico 1: ...`: Comentário indicando o propósito do gráfico.
*   `plt.figure(figsize=(10,6))`: Cria uma nova figura Matplotlib com tamanho 10x6 polegadas.
*   `df[degree_cols].sum()`: Seleciona as colunas de formação (`degree_cols`) e calcula a soma total para cada nível de formação em todo o país.
*   `.plot(kind='pie', autopct='%1.1f%%')`: Gera um gráfico de pizza a partir dos dados somados. `autopct='%1.1f%%'` formata as porcentagens exibidas em cada fatia da pizza para uma casa decimal.
*   `plt.title(...)`: Define o título do gráfico.
*   `plt.ylabel('')`: Remove o rótulo do eixo y, que não é relevante para gráficos de pizza.
*   `plt.show()`: Exibe o gráfico gerado.
*   O comentário `# Para salvar este gráfico...` sugere como você poderia salvar este gráfico usando a função `save_plot`. Note que `plt.show()` geralmente limpa a figura atual, então `plt.gcf()` (Get Current Figure) deve ser chamado antes de `plt.show()` se você quiser salvar a figura diretamente após criá-la. Alternativamente, a função `plot` retorna um objeto `AxesSubplot`, e `fig = ax.get_figure()` poderia ser usado.

### Gráfico 2: Top 10 Estados por Formação Acadêmica (Barras Empilhadas)

    top_states = df.nlargest(10, 'Total_Docentes')
    plt.figure(figsize=(12,6)) # Criar a figura antes de plotar
    ax = top_states[degree_cols].plot(kind='bar', stacked=True,
    xlabel='Estado',
    ylabel='Número de Docentes',
    title='Top 10 Estados por Nível de Formação dos Docentes')
    plt.xticks(ticks=range(len(top_states)), labels=top_states['UF'], rotation=45, ha='right') # Ajustado para melhor visualização dos rótulos
    plt.legend(title='Formação')
    plt.tight_layout() # Ajusta o layout para evitar sobreposição
    plt.show()

Para salvar este gráfico:

    fig = ax.get_figure()
    save_plot(fig, '02_top_10_estados_formacao')

*   `top_states = df.nlargest(10, 'Total_Docentes')`: Seleciona os 10 estados (linhas) com o maior número total de docentes, com base na coluna 'Total\_Docentes', e armazena o resultado em `top_states`.
*   `plt.figure(figsize=(12,6))`: Cria a figura explicitamente para ter mais controle.
*   `ax = top_states[degree_cols].plot(kind='bar', stacked=True, ...)`: Gera um gráfico de barras empilhadas para os 10 principais estados. A função `plot` do Pandas retorna um objeto `Axes` do Matplotlib.
    *   `kind='bar'`: Especifica um gráfico de barras.
    *   `stacked=True`: Indica que as barras devem ser empilhadas.
    *   `xlabel`, `ylabel`, `title`: Definem os rótulos dos eixos e o título do gráfico.
*   `plt.xticks(ticks=range(len(top_states)), labels=top_states['UF'], rotation=45, ha='right')`: Define os rótulos do eixo x para serem os nomes das UFs dos 10 principais estados, rotacionados para melhor legibilidade.
*   `plt.legend(title='Formação')`: Adiciona uma legenda ao gráfico com o título 'Formação'.
*   `plt.tight_layout()`: Ajusta automaticamente os parâmetros do subplot para dar um layout compacto.
*   `plt.show()`: Exibe o gráfico.
*   O comentário para salvar o gráfico foi adicionado.

### Gráfico 3: Distribuição Etária Nacional (Barras)

    plt.figure(figsize=(12,6))
    ax = df[age_cols].sum().plot(kind='bar')
    plt.title('Distribuição Etária Nacional dos Docentes')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Quantidade de Docentes')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

Para salvar este gráfico:

    fig = ax.get_figure()
    save_plot(fig, '03_distribuicao_etaria_nacional')
    text

*   Este bloco gera um gráfico de barras mostrando a distribuição etária nacional dos docentes, somando os valores das colunas de faixa etária (`age_cols`).
*   `plt.xticks(rotation=45, ha='right')`: Rotaciona os rótulos do eixo x em 45 graus e alinha à direita para melhor legibilidade.
*   `plt.tight_layout()`: Ajusta o layout.
*   O comentário para salvar o gráfico foi adicionado.

### Gráfico 4: Heatmap de Correlação

    plt.figure(figsize=(12,8))
    corr_matrix = df[degree_cols + age_cols].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Matriz de Correlação entre Formação e Faixa Etária')
    plt.tight_layout()
    plt.show()

Para salvar este gráfico:

    fig = plt.gcf()
    save_plot(fig, '04_heatmap_correlacao')

*   `corr_matrix = df[degree_cols + age_cols].corr()`: Calcula a matriz de correlação entre as colunas de formação e as colunas de faixa etária.
*   `sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")`: Gera um mapa de calor (heatmap) usando Seaborn para visualizar a matriz de correlação.
    *   `annot=True`: Exibe os valores de correlação nas células do mapa.
    *   `cmap='coolwarm'`: Define o esquema de cores do mapa.
    *   `fmt=".2f"`: Formata os valores de correlação para duas casas decimais.
*   `plt.tight_layout()`: Ajusta o layout.
*   O comentário para salvar o gráfico foi adicionado.

### Gráfico 5: Dispersão 3D (Matplotlib)

    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111, projection='3d')
    x = df['Docentes_Mestrado']
    y = df['Docentes_Doutorado']
    z = df['Total_Docentes']
    ax.scatter(x, y, z, c='r', s=50, alpha=0.6) # Adicionado alpha para transparência
    ax.set_xlabel('Mestrado')
    ax.set_ylabel('Doutorado')
    ax.set_zlabel('Total de Docentes')
    plt.title('Relação entre Mestrado, Doutorado e Total de Docentes')
    plt.show()

Para salvar este gráfico:
    
    save_plot(fig, '05_dispersao_3d_matplotlib')

*   Este bloco cria um gráfico de dispersão 3D estático usando Matplotlib.
*   `fig = plt.figure(figsize=(12,10))`: Cria a figura.
*   `ax = fig.add_subplot(111, projection='3d')`: Adiciona um subplot 3D à figura.
*   `x`, `y`, `z`: Definem os dados para os eixos x (Docentes com Mestrado), y (Docentes com Doutorado) e z (Total de Docentes).
*   `ax.scatter(x, y, z, c='r', s=50, alpha=0.6)`: Plota os pontos de dados. `c='r'` define a cor dos pontos como vermelho, `s=50` define o tamanho dos pontos, e `alpha=0.6` adiciona um pouco de transparência.
*   `ax.set_xlabel`, `ax.set_ylabel`, `ax.set_zlabel`: Definem os rótulos dos eixos.
*   O comentário para salvar o gráfico foi adicionado.

### Gráfico 6: Mapa de Bolhas Interativo (Plotly)

    fig_plotly_bubble = px.scatter(
    df,
    x='Docentes_Mestrado',
    y='Docentes_Doutorado',
    size='Total_Docentes',
    color='UF',
    hover_name='UF',
    log_x=True,
    size_max=60,
    title='Relação entre Mestrado vs Doutorado por Estado'
    )
    fig_plotly_bubble.show() # Para exibir no notebook
    save_plot(fig_plotly_bubble, '06_mapa_bolhas_interativo', formats=['png', 'html'])

*   Este bloco cria um gráfico de dispersão interativo (mapa de bolhas) usando Plotly Express.
*   `fig_plotly_bubble = px.scatter(...)`: Cria o gráfico de dispersão.
    *   `df`: DataFrame de origem.
    *   `x='Docentes_Mestrado'`, `y='Docentes_Doutorado'`: Colunas para os eixos x e y.
    *   `size='Total_Docentes'`: A coluna 'Total\_Docentes' determina o tamanho das bolhas.
    *   `color='UF'`: A coluna 'UF' determina a cor das bolhas.
    *   `hover_name='UF'`: O nome da UF será exibido ao passar o mouse sobre uma bolha.
    *   `log_x=True`: Usa uma escala logarítmica para o eixo x.
    *   `size_max=60`: Define o tamanho máximo das bolhas.
    *   `title`: Define o título do gráfico.
*   `fig_plotly_bubble.show()`: Exibe o gráfico interativo no ambiente do notebook.
*   `save_plot(fig_plotly_bubble, '06_mapa_bolhas_interativo', formats=['png', 'html'])`: Salva o gráfico interativo como uma imagem PNG estática e como um arquivo HTML interativo usando a função `save_plot` definida anteriormente.

### Gráfico 7: Gráfico 3D Interativo (Plotly)

    fig_plotly_3d = px.scatter_3d(
    df,
    x='Docentes_Mestrado',
    y='Docentes_Doutorado',
    z='Docentes_Idade_40_44', # Exemplo de uma faixa etária para o eixo z
    color='UF',
    size='Total_Docentes',
    hover_name='UF',
    title='Relação 3D: Mestrado, Doutorado e Idade 40-44'
    )
    fig_plotly_3d.show() # Para exibir no notebook
    save_plot(fig_plotly_3d, '07_3d_interativo', formats=['png', 'html'])

*   Este bloco cria um gráfico de dispersão 3D interativo usando Plotly Express.
*   `fig_plotly_3d = px.scatter_3d(...)`: Cria o gráfico de dispersão 3D.
    *   `z='Docentes_Idade_40_44'`: A coluna 'Docentes\_Idade\_40\_44' é usada como exemplo para o eixo z.
    *   Os outros parâmetros são semelhantes ao gráfico de bolhas, adaptados para 3D.
*   `fig_plotly_3d.show()`: Exibe o gráfico interativo.
*   `save_plot(fig_plotly_3d, '07_3d_interativo', formats=['png', 'html'])`: Salva o gráfico 3D interativo como PNG e HTML.

## Conclusão do Processo

    print("\n✅ Processo concluído! Gráficos disponíveis em:", output_dir)

*   `print(...)`: Imprime uma mensagem final indicando que o processo foi concluído e onde os gráficos foram salvos (principalmente os gráficos Plotly, conforme a função `save_plot` foi chamada).

