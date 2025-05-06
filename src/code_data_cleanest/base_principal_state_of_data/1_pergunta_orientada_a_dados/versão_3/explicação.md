## Visão Geral do Código

O script realiza a limpeza e o pré-processamento de um conjunto de dados proveniente da pesquisa "State of Data Brazil 2023", que contém informações sobre profissionais da área de dados no Brasil. O processo inclui importação de bibliotecas, carregamento de dados, renomeação de colunas, remoção de valores ausentes, tratamento de outliers e exportação do conjunto de dados limpo.

### Importação de Bibliotecas
    import pandas as pd
    import numpy as np

Esta seção inicial importa duas bibliotecas fundamentais para análise de dados em Python. O pandas (`pd`) é utilizado para manipulação e análise de dados estruturados, oferecendo estruturas de dados flexíveis como DataFrame. O numpy (`np`) fornece suporte para arrays multidimensionais e funções matemáticas de alto desempenho, sendo especialmente útil para cálculos numéricos em grandes conjuntos de dados.

### Carregamento dos Dados

    df = pd.read_csv('/kaggle/input/state-of-data-brazil-2023/State_of_data_BR_2023_Kaggle - df_survey_2023.csv')

Nesta etapa, o código carrega o arquivo CSV contendo os dados da pesquisa "State of Data Brazil 2023" utilizando a função `read_csv()` do pandas. O arquivo está localizado no diretório de entrada do Kaggle, indicando que este notebook está sendo executado na plataforma Kaggle. O resultado é armazenado em um DataFrame chamado `df`, que é a estrutura de dados principal do pandas para manipulação de dados tabulares.

## Limpeza e Transformação dos Dados

### Renomeação de Coluna
    colunas_renomeadas = {
    "('P0', 'id')": "id",
    "('P1_l ', 'Nivel de Ensino')": "Nível de ensino alcançado",
    "('P1_m ', 'Área de Formação')": "Área de formação acadêmica",
    # ... outras colunas renomeadas (o exemplo original era mais longo)
    # Adicionei uma nota para indicar que a lista completa não está aqui
    # para manter a resposta concisa, mas o código original teria a lista completa.
    "('P2_a ', 'Qual sua situação atual de trabalho?')": "Situação atual de trabalho",
    "('P2_b ', 'Setor de atuação')": "Setor de atuação profissional",
    "('P2_c ', 'Você está satisfeito na sua empresa atual?')": "Satisfação na empresa atual",
    "('P2_d ', 'Qual o Régime de trabalho?')": "Regime de trabalho (CLT, PJ, etc.)",
    "('P2_e ', 'Você exerce cargo de liderança?')": "Exerce cargo de liderança",
    "('P2_f ', 'Quais são os principais desafios que você percebe na área de Dados atualmente?')": "Principais desafios na área de Dados",
    "('P2_g ', 'Quais são as principais oportunidades que você percebe na área de Dados atualmente?')": "Principais oportunidades na área de Dados",
    "('P2_h ', 'Em qual das opções abaixo você se enquadra?')": "Opção de enquadramento profissional",
    "('P2_i ', 'Qual sua faixa salarial atual?')": "Faixa salarial atual (R$)",
    "('P2_j ', 'Há quanto tempo você está na sua empresa atual?')": "Tempo na empresa atual",
    "('P2_k ', 'Há quanto tempo você atua na área de Dados?')": "Tempo de experiência na área de dados",
    "('P2_l ', 'Você participou de entrevistas de emprego nos últimos 6 meses?')": "Participou de entrevistas recentes",
    "('P2_m ', 'Você pretende mudar de emprego nos próximos 6 meses?')": "Pretende mudar de emprego em breve",
    "('P2_n ', 'Quais são seus principais objetivos de carreira para os próximos 5 anos?')": "Objetivos de carreira para os próximos 5 anos",
    "('P2_o ', 'Quais são as principais habilidades que você busca desenvolver nos próximos anos?')": "Habilidades a desenvolver nos próximos anos",
    "('P2_p ', 'Quais são as principais fontes de aprendizado que você utiliza para se manter atualizado na área de Dados?')": "Fontes de aprendizado na área de Dados",
    "('P2_q ', 'Você utiliza alguma ferramenta ou linguagem de programação no seu dia-a-dia de trabalho?')": "Utiliza ferramentas/linguagens de programação",
    "('P2_r ', 'Quais são as principais ferramentas e tecnologias que você utiliza no seu dia-a-dia de trabalho?')": "Principais ferramentas e tecnologias utilizadas",
    "('P2_s ', 'Quais são as principais linguagens de programação que você utiliza no seu dia-a-dia de trabalho?')": "Principais linguagens de programação utilizadas",
    "('P2_t ', 'Qual o seu nível de conhecimento em inglês?')": "Nível de conhecimento em inglês",
    "('P2_u ', 'Você possui alguma certificação na área de Dados?')": "Possui certificação na área de Dados",
    "('P2_v ', 'Quais são as principais certificações que você possui?')": "Principais certificações possuídas",
    "('P2_w ', 'Você considera que o mercado de trabalho na área de Dados está aquecido no Brasil?')": "Percepção do mercado de trabalho na área de Dados",
    "('P2_x ', 'Você acredita que a área de Dados é promissora para o futuro?')": "Perspectiva sobre o futuro da área de Dados",
    "('P2_y ', 'Você recomendaria a área de Dados para outras pessoas?')": "Recomendaria a área de Dados",
    "('P2_z ', 'Em qual cidade você mora?')": "Cidade de residência",
    "('P2_A ', 'Em qual estado você mora?')": "Estado de residência",
    "('P2_B ', 'Qual sua idade?')": "Idade do profissional",
    "('P2_C ', 'Qual seu gênero?')": "Gênero do profissional"
    }

### Renomear colunas e selecionar apenas as desejadas

    df_clean = df.rename(columns=colunas_renomeadas)[list(colunas_renomeadas.values())]

Esta seção aborda um problema comum em conjuntos de dados: nomes de colunas complexos ou pouco intuitivos. O código cria um dicionário chamado `colunas_renomeadas` que mapeia os nomes originais das colunas (como "('P1_b ', 'Genero')") para nomes mais simples e descritivos (como "Gênero do profissional"). Em seguida, a função `rename()` é aplicada ao DataFrame original para renomear as colunas conforme o mapeamento definido.

Adicionalmente, ao selecionar apenas os valores do dicionário (`list(colunas_renomeadas.values())`), o código garante que apenas as colunas de interesse sejam mantidas no novo DataFrame `df_clean`. Esta abordagem combina eficientemente duas operações: renomeação de colunas e seleção de um subconjunto de colunas.

### Remoção de Valores Ausentes

    df_clean = df_clean.dropna()

Neste passo, o método `dropna()` é aplicado para remover todas as linhas que contêm valores ausentes (NaN) em qualquer coluna. Esta é uma abordagem direta para lidar com dados ausentes, embora seja importante notar que ela pode reduzir significativamente o tamanho do conjunto de dados se muitas linhas contiverem valores ausentes. Em análises mais avançadas, estratégias alternativas como imputação (substituição de valores ausentes por estimativas) poderiam ser consideradas.

### Tratamento de Outliers
    if "Tempo de experiência na área de dados" in df_clean.columns:
    if df_clean["Tempo de experiência na área de dados"].dtype == 'object':
# Converter para numérico (supondo formato como "de 3 a 4 anos" ou apenas números)
# Extrair o primeiro conjunto de dígitos
    df_clean["Tempo_exp_num"] = (
    df_clean["Tempo de experiência na área de dados"]
    .astype(str) # Garantir que é string antes de usar .str
    .str.extract(r'(\d+)', expand=False) # Extrair o primeiro número
    .astype(float)
    )

# Calcular limites para outliers usando IQR
    Q1 = df_clean["Tempo_exp_num"].quantile(0.25)
    Q3 = df_clean["Tempo_exp_num"].quantile(0.75)
    IQR = Q3 - Q1
    lim_inf = Q1 - 1.5 * IQR
    lim_sup = Q3 + 1.5 * IQR
    
# Filtrar dados dentro dos limites, tratando NaNs que podem surgir da conversão
    df_clean = df_clean[
        (df_clean["Tempo_exp_num"] >= lim_inf) &
        (df_clean["Tempo_exp_num"] <= lim_sup)
    ].drop(columns="Tempo_exp_num")
# Se já for numérica, poderia aplicar o IQR diretamente ou pular se não necessário
    elif pd.api.types.is_numeric_dtype(df_clean["Tempo de experiência na área de dados"]):
# Aplicar IQR diretamente se a coluna já for numérica
    col_num = "Tempo de experiência na área de dados"
    Q1 = df_clean[col_num].quantile(0.25)
    Q3 = df_clean[col_num].quantile(0.75)
    IQR = Q3 - Q1
    lim_inf = Q1 - 1.5 * IQR
    lim_sup = Q3 + 1.5 * IQR
    df_clean = df_clean[
        (df_clean[col_num] >= lim_inf) &
        (df_clean[col_num] <= lim_sup)
    ]
    else:
      print("Coluna 'Tempo de experiência na área de dados' não encontrada após renomeação ou remoção de NaNs.")

Esta seção implementa o tratamento de outliers utilizando o método do Intervalo Interquartil (IQR), uma técnica estatística robusta para identificação de valores extremos. O código foca especificamente na coluna "Tempo de experiência na área de dados".

Primeiro, o código verifica se a coluna existe e se é do tipo "object" (texto), indicando a necessidade de conversão para tipo numérico. Utiliza uma expressão regular para extrair o primeiro número encontrado em cada valor da coluna (assumindo que o tempo de experiência pode estar em formatos como "X anos", "de X a Y anos", etc.), armazenando o resultado em uma nova coluna chamada "Tempo_exp_num". Se a coluna já for numérica, o tratamento de outliers pode ser aplicado diretamente.

O método IQR é então aplicado para calcular os limites para identificação de outliers:
1. Calcula o primeiro quartil (Q1) e o terceiro quartil (Q3) dos dados numéricos de experiência.
2. Determina o IQR como a diferença entre Q3 e Q1.
3. Define o limite inferior como Q1 - 1.5 * IQR e o limite superior como Q3 + 1.5 * IQR.
4. Filtra o DataFrame para manter apenas as linhas cujos valores de experiência estão dentro desses limites.

Por fim, a coluna temporária "Tempo_exp_num" (se criada) é removida do DataFrame com o método `drop()`, mantendo apenas as colunas originais.

### Exportação dos Dados Limpos

    df_clean.to_csv('dados_limpos.csv', index=False)
    
    print("Arquivo 'dados_limpos.csv' gerado com sucesso!")
Na etapa final, o DataFrame limpo e processado (`df_clean`) é exportado para um novo arquivo CSV chamado 'dados_limpos.csv'. O parâmetro `index=False` garante que o índice do DataFrame não seja incluído como uma coluna adicional no arquivo CSV. Uma mensagem de confirmação é então impressa para informar que o arquivo foi gerado com sucesso.



