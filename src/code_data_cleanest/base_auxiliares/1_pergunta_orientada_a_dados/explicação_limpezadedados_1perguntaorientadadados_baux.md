### 1. Importação e Configuração Inicial
    
    import pandas as pd

-   Esta linha importa a biblioteca `pandas`.
-   `pandas` é uma biblioteca Python fundamental para manipulação e análise de dados, oferecendo estruturas de dados como DataFrames.
-   A biblioteca é importada com o alias `pd`, que é a convenção padrão para se referir ao pandas no código.

        pd.set_option('display.max_columns', None)

-   Esta linha utiliza a função `set_option` da biblioteca `pandas`.
-   `'display.max_columns'` é uma opção de configuração que controla o número máximo de colunas a serem exibidas quando um DataFrame é impresso.
-   `None` como valor para esta opção significa que todas as colunas do DataFrame serão exibidas, sem truncamento. Isso é útil para inspecionar DataFrames largos.

### 2. Carregamento dos Dados

    input_file = 'MICRODADOS_ED_SUP_IES_2023.CSV'

-   Esta linha atribui a string `'MICRODADOS_ED_SUP_IES_2023.CSV'` à variável `input_file`.
-   `input_file` agora armazena o nome (e caminho, se não estiver no mesmo diretório do script) do arquivo CSV que contém os dados a serem processados.
        
        df = pd.read_csv(input_file, sep=';', encoding='latin-1', low_memory=False)
-   Esta linha lê os dados do arquivo CSV especificado pela variável `input_file` e os carrega em um DataFrame do pandas.
-   `pd.read_csv()` é a função do pandas usada para ler arquivos CSV.
-   `input_file`: O primeiro argumento é o caminho para o arquivo CSV.
-   `sep=';'`: Este parâmetro especifica que o delimitador de colunas no arquivo CSV é o ponto e vírgula (`;`).
-   `encoding='latin-1'`: Este parâmetro define a codificação de caracteres do arquivo. `'latin-1'` (ou ISO-8859-1) é comumente usado para arquivos que podem conter caracteres especiais da língua portuguesa.
-   `low_memory=False`: Este parâmetro, quando definido como `False`, pode ajudar a pandas a inferir os tipos de dados das colunas de forma mais precisa, especialmente em arquivos grandes com tipos mistos, lendo o arquivo inteiro ou em blocos maiores de uma vez, o que pode consumir mais memória inicialmente, mas evita problemas de tipos mistos.
-   O DataFrame resultante da leitura do arquivo é atribuído à variável `df`.

### 3. Seleção de Colunas Relevantes

    colunas_relevantes = [
    'SG_UF_IES', 'NO_UF_IES',
    'QT_DOC_EX_GRAD', 'QT_DOC_EX_ESP', 'QT_DOC_EX_MEST', 'QT_DOC_EX_DOUT',
    'QT_DOC_EX_FEMI', 'QT_DOC_EX_MASC',
    'QT_DOC_EX_0_29', 'QT_DOC_EX_30_34', 'QT_DOC_EX_35_39',
    'QT_DOC_EX_40_44', 'QT_DOC_EX_45_49', 'QT_DOC_EX_50_54',
    'QT_DOC_EX_55_59', 'QT_DOC_EX_60_MAIS'
    ]

-   Esta linha define uma lista Python chamada `colunas_relevantes`.
-   A lista contém strings, onde cada string é o nome de uma coluna que se deseja manter do DataFrame original para a análise subsequente.
-   As colunas selecionadas incluem identificadores de Unidade Federativa (UF), quantidades de docentes por nível de formação, por sexo e por faixas etárias.

### 4. Verificação da Existência das Colunas

    colunas_presentes = [col for col in colunas_relevantes if col in df.columns]

-   Esta linha cria uma nova lista chamada `colunas_presentes` usando uma compreensão de lista (list comprehension).
-   Ela itera sobre cada nome de coluna (`col`) na lista `colunas_relevantes`.
-   Para cada `col`, verifica se esse nome de coluna existe na lista de colunas do DataFrame `df` (acessada por `df.columns`).
-   Apenas os nomes de colunas que estão tanto em `colunas_relevantes` quanto em `df.columns` são incluídos na lista `colunas_presentes`.
        
        colunas_ausentes = [col for col in colunas_relevantes if col not in df.columns]

-   Esta linha cria uma nova lista chamada `colunas_ausentes`, também usando uma compreensão de lista.
-   Ela itera sobre cada nome de coluna (`col`) na lista `colunas_relevantes`.
-   Para cada `col`, verifica se esse nome de coluna *não* existe na lista de colunas do DataFrame `df` (`df.columns`).
-   Apenas os nomes de colunas que estão em `colunas_relevantes` mas *não* estão em `df.columns` são incluídos na lista `colunas_ausentes`.
        
        if colunas_ausentes:
        print(f"Aviso: As seguintes colunas não foram encontradas no arquivo e serão ignoradas: {colunas_ausentes}")

-   Esta é uma estrutura condicional `if`.
-   `if colunas_ausentes:`: A condição verifica se a lista `colunas_ausentes` não está vazia (ou seja, se há alguma coluna relevante que não foi encontrada no DataFrame).
-   Se a condição for verdadeira (houver colunas ausentes), a linha `print(...)` é executada.
-   `print(f"...")`: Esta função imprime uma mensagem formatada (f-string) no console.
-   A mensagem informa ao usuário quais colunas da lista `colunas_relevantes` não foram encontradas no arquivo CSV carregado e, portanto, serão ignoradas nas etapas seguintes.

### 5. Filtragem e Limpeza dos Dados

    df_filtrado = df[colunas_presentes].copy()

-   Esta linha cria um novo DataFrame chamado `df_filtrado`.
-   `df[colunas_presentes]`: Esta parte seleciona apenas as colunas do DataFrame `df` cujos nomes estão listados em `colunas_presentes`. Isso resulta em um novo DataFrame contendo apenas as colunas desejadas que de fato existem nos dados originais.
-   `.copy()`: Este método é chamado no DataFrame resultante da seleção de colunas. Ele cria uma cópia explícita dos dados, em vez de uma visualização. Isso é feito para evitar potenciais `SettingWithCopyWarning` que podem surgir ao modificar subconjuntos de DataFrames posteriormente.
-   O novo DataFrame, contendo apenas as colunas relevantes e existentes, é atribuído à variável `df_filtrado`.
        
        df_limpo = df_filtrado.dropna().drop_duplicates()

-   Esta linha realiza duas operações de limpeza de dados em `df_filtrado` e atribui o resultado a um novo DataFrame chamado `df_limpo`.
-   `df_filtrado.dropna()`: O método `dropna()` é chamado em `df_filtrado`. Por padrão (sem argumentos), ele remove todas as linhas que contêm pelo menos um valor ausente (NaN ou `None`) em qualquer uma das suas colunas.
-   `.drop_duplicates()`: Este método é chamado no DataFrame que resulta da operação `dropna()`. Ele remove linhas duplicadas, mantendo apenas a primeira ocorrência de cada conjunto de valores de linha idêntico.
-   O DataFrame resultante, após a remoção de linhas com valores ausentes e a remoção de duplicatas, é atribuído a `df_limpo`.

### 6. Agrupamento e Agregação dos Dados

    agg_dict_base = {
    'QT_DOC_EX_GRAD': 'sum', 'QT_DOC_EX_ESP': 'sum',
    'QT_DOC_EX_MEST': 'sum', 'QT_DOC_EX_DOUT': 'sum',
    'QT_DOC_EX_FEMI': 'sum', 'QT_DOC_EX_MASC': 'sum',
    'QT_DOC_EX_0_29': 'sum', 'QT_DOC_EX_30_34': 'sum', 'QT_DOC_EX_35_39': 'sum',
    'QT_DOC_EX_40_44': 'sum', 'QT_DOC_EX_45_49': 'sum', 'QT_DOC_EX_50_54': 'sum',
    'QT_DOC_EX_55_59': 'sum', 'QT_DOC_EX_60_MAIS': 'sum'
    }

-   Esta linha define um dicionário Python chamado `agg_dict_base`.
-   As chaves deste dicionário são nomes de colunas (que representam quantidades de docentes).
-   O valor associado a cada chave é a string `'sum'`, indicando que a operação de agregação a ser aplicada a estas colunas é a soma.

        colunas_para_soma = [col for col in agg_dict_base.keys() if col in df_limpo.columns]

-   Esta linha cria uma lista chamada `colunas_para_soma` usando uma compreensão de lista.
-   `agg_dict_base.keys()`: Retorna uma visualização das chaves do dicionário `agg_dict_base` (os nomes das colunas destinadas à soma).
-   A compreensão de lista itera sobre cada nome de coluna (`col`) nas chaves de `agg_dict_base`.
-   `if col in df_limpo.columns`: Verifica se a coluna `col` realmente existe no DataFrame `df_limpo` (após filtragem e limpeza).
-   Apenas as colunas que estão em `agg_dict_base` E também presentes em `df_limpo` são incluídas na lista `colunas_para_soma`.

        agg_dict = {col: 'sum' for col in colunas_para_soma}

-   Esta linha cria um novo dicionário chamado `agg_dict` usando uma compreensão de dicionário (dict comprehension).
-   Ele itera sobre cada nome de coluna (`col`) na lista `colunas_para_soma` (que contém apenas as colunas numéricas válidas para agregação).
-   Para cada `col`, cria uma entrada no dicionário `agg_dict` onde a chave é `col` e o valor é `'sum'`.
-   Este `agg_dict` final conterá apenas as colunas que devem ser somadas e que existem no `df_limpo`.

        if 'SG_UF_IES' in df_limpo.columns:
        df_agrupado = df_limpo.groupby('SG_UF_IES').agg(agg_dict).reset_index()

-   `if 'SG_UF_IES' in df_limpo.columns:`: Esta condição verifica se a coluna `'SG_UF_IES'` (sigla da UF, usada para agrupamento) existe no DataFrame `df_limpo`.
-   Se a coluna existir, o bloco de código indentado é executado:
    -   `df_limpo.groupby('SG_UF_IES')`: Esta parte agrupa as linhas do DataFrame `df_limpo` com base nos valores únicos da coluna `'SG_UF_IES'`.
    -   `.agg(agg_dict)`: O método `agg()` é chamado no objeto agrupado. Ele aplica as operações de agregação especificadas no dicionário `agg_dict` (soma, neste caso) às colunas correspondentes para cada grupo (cada UF).
    -   `.reset_index()`: Após a agregação, a coluna de agrupamento (`'SG_UF_IES'`) torna-se o índice do DataFrame resultante. O método `reset_index()` converte este índice de volta em uma coluna regular.
    -   O DataFrame final, agrupado por UF e com as somas calculadas, é atribuído à variável `df_agrupado`.

            else:
            print("Erro: A coluna 'SG_UF_IES' é necessária para o agrupamento, mas não foi encontrada nas colunas filtradas e limpas.")
            df_agrupado = pd.DataFrame()

-   `else:`: Este bloco é executado se a condição `if 'SG_UF_IES' in df_limpo.columns:` for falsa (ou seja, a coluna `'SG_UF_IES'` não foi encontrada em `df_limpo`).
-   `print("...")`: Uma mensagem de erro é impressa, informando que a coluna de agrupamento crucial está ausente.
-   `df_agrupado = pd.DataFrame()`: Um DataFrame vazio é criado e atribuído a `df_agrupado`. Isso é feito para que as etapas subsequentes do código possam verificar se `df_agrupado` está vazio e evitar erros ao tentar operar em um DataFrame que não pôde ser criado corretamente.

### 7. Renomeação das Colunas

    if not df_agrupado.empty:
    df_agrupado = df_agrupado.rename(columns={
    'SG_UF_IES': 'UF',
    'QT_DOC_EX_GRAD': 'Docentes_Graduacao',
    'QT_DOC_EX_ESP': 'Docentes_Especializacao',
    'QT_DOC_EX_MEST': 'Docentes_Mestrado',
    'QT_DOC_EX_DOUT': 'Docentes_Doutorado',
    'QT_DOC_EX_FEMI': 'Docentes_Feminino',
    'QT_DOC_EX_MASC': 'Docentes_Masculino',
    'QT_DOC_EX_0_29': 'Docentes_0_29_Anos',
    'QT_DOC_EX_30_34': 'Docentes_30_34_Anos',
    'QT_DOC_EX_35_39': 'Docentes_35_39_Anos',
    'QT_DOC_EX_40_44': 'Docentes_40_44_Anos',
    'QT_DOC_EX_45_49': 'Docentes_45_49_Anos',
    'QT_DOC_EX_50_54': 'Docentes_50_54_Anos',
    'QT_DOC_EX_55_59': 'Docentes_55_59_Anos',
    'QT_DOC_EX_60_MAIS': 'Docentes_60_Mais_Anos'
    })

-   `if not df_agrupado.empty:`: Esta condição verifica se o DataFrame `df_agrupado` não está vazio. A renomeação só faz sentido se `df_agrupado` foi criado com sucesso.
-   Se `df_agrupado` não estiver vazio:
    -   `df_agrupado.rename(columns={...})`: O método `rename()` é chamado em `df_agrupado` para alterar os nomes de suas colunas.
    -   `columns={...}`: O argumento `columns` recebe um dicionário onde as chaves são os nomes antigos das colunas e os valores são os novos nomes desejados.
    -   Por exemplo, `'SG_UF_IES'` é renomeada para `'UF'`, `'QT_DOC_EX_GRAD'` para `'Docentes_Graduacao'`, e assim por diante, tornando os nomes das colunas mais descritivos.
    -   O DataFrame com as colunas renomeadas substitui o `df_agrupado` original.

### 8. Salvamento e Visualização do Resultado

    output_file = 'microdados_agrupados_por_uf.csv'

-   Esta linha atribui a string `'microdados_agrupados_por_uf.csv'` à variável `output_file`.
-   `output_file` agora armazena o nome (e caminho) do arquivo CSV onde o DataFrame processado será salvo.

        if not df_agrupado.empty:
        df_agrupado.to_csv(output_file, index=False)

-   `if not df_agrupado.empty:`: Novamente, esta condição verifica se `df_agrupado` não está vazio antes de tentar salvá-lo.
-   Se `df_agrupado` não estiver vazio:
    -   `df_agrupado.to_csv(output_file, index=False)`: O método `to_csv()` é chamado em `df_agrupado` para salvar seu conteúdo em um arquivo CSV.
    -   `output_file`: O primeiro argumento é o nome do arquivo de saída.
    -   `index=False`: Este parâmetro impede que o pandas escreva o índice do DataFrame como uma coluna no arquivo CSV.

            print(f"Arquivo '{output_file}' salvo com sucesso.")

-   Esta linha (dentro do `if not df_agrupado.empty:`) imprime uma mensagem de confirmação no console, informando que o arquivo foi salvo com sucesso e especificando seu nome.

        print("\n### Amostra dos Dados Agrupados ###")

-   Esta linha (também dentro do `if`) imprime um cabeçalho no console para a amostra dos dados que será exibida a seguir. O `\n` no início adiciona uma linha em branco antes do cabeçalho.

        print(df_agrupado.head())

-   Esta linha (também dentro do `if`) imprime as primeiras linhas do DataFrame `df_agrupado`.
-   `df_agrupado.head()`: O método `head()` retorna, por padrão, as primeiras 5 linhas do DataFrame. Isso permite uma rápida visualização do resultado final do processamento.

        elif 'SG_UF_IES' in df_limpo.columns and df_agrupado.empty:
        print(f"O DataFrame agrupado está vazio após a limpeza. Nenhum arquivo foi salvo.")

-   `elif 'SG_UF_IES' in df_limpo.columns and df_agrupado.empty:`: Esta é uma condição "else if". Ela é verificada se a condição `if not df_agrupado.empty:` anterior foi falsa.
-   Ela verifica se a coluna de agrupamento `'SG_UF_IES'` *estava* presente em `df_limpo`, mas mesmo assim `df_agrupado` resultou vazio (o que pode acontecer se, por exemplo, `dropna()` removeu todas as linhas).
-   Se esta condição for verdadeira, uma mensagem é impressa informando que o DataFrame agrupado ficou vazio após a limpeza e que nenhum arquivo foi salvo.

        else:
        print("Processamento interrompido devido à ausência da coluna 'SG_UF_IES'. Nenhum arquivo foi salvo.")

-   `else:`: Este bloco final é executado se todas as condições `if` e `elif` anteriores forem falsas.
-   Isso ocorre especificamente se `df_agrupado` estava vazio porque a coluna `'SG_UF_IES'` não foi encontrada inicialmente (conforme a lógica de criação de `df_agrupado`).
-   Uma mensagem é impressa indicando que o processamento foi interrompido devido à ausência da coluna de agrupamento e que nenhum arquivo foi salvo.
