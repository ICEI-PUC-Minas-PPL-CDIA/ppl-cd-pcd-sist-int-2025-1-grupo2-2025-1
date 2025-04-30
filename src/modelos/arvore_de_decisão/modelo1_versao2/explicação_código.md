# Explicação código *modelo2_remasterizado.ipynb*
### Código em pyhton:
    # --- Etapa 1: Configuração do Ambiente, Upload e Carregamento ---
    
    # Importar bibliotecas necessárias
    import pandas as pd
    import numpy as np
    import re
    import io
    from google.colab import files
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.preprocessing import OrdinalEncoder, StandardScaler
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    import lightgbm as lgb
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    
    # Instalar/Importar bibliotecas opcionais
    try:
        from unidecode import unidecode
    except ImportError:
        print("Instalando unidecode para remover acentos...")
        !pip install unidecode
        from unidecode import unidecode
        print("Unidecode instalado.")
    
    try:
        import shap
    except ImportError:
        print("Instalando shap para interpretação do modelo...")
        !pip install shap
        import shap
        print("Shap instalado.")
    
    try:
        import graphviz
    except ImportError:
        print("Instalando graphviz para visualização de árvore...")
        !apt-get install -qq graphviz > /dev/null # Instala dependência do sistema no Colab
        !pip install graphviz > /dev/null
        import graphviz
        print("Graphviz instalado.")
    
    # Ignorar warnings específicos que podem poluir a saída
    warnings.filterwarnings("ignore", category=UserWarning, module='shap')
    warnings.filterwarnings("ignore", category=FutureWarning)
## Explicação (Etapa 1 - Setup):
### Importações Principais: **Importa as bibliotecas essenciais:**
  - pandas e numpy: **Para manipulação de dados (DataFrames, arrays).**
  - re: **Para expressões regulares (usadas na limpeza).**
  - io, google.colab.files: **Para lidar com upload/leitura de arquivos no Google Colab.**
  - sklearn.model_selection: **Para dividir os dados (train_test_split) e otimizar parâmetros (GridSearchCV).**
  - sklearn.preprocessing: **Para codificar variáveis ordinais (OrdinalEncoder) e escalar dados (StandardScaler).**
  - sklearn.metrics: **Para calcular métricas de avaliação (MAE, RMSE, R²).**
  - lightgbm: **Para usar o algoritmo LightGBM (o modelo principal).**
  - matplotlib.pyplot, seaborn: **Para gerar gráficos.**

### Warnings: 
- Para suprimir mensagens de aviso não críticas.

### Importar unidecode. 
- Se falhar (não instalada), imprime uma mensagem, usa !pip install para instalá-la no ambiente Colab e depois importa. Essencial para remover acentos na limpeza de nomes/valores.

### Fazer o mesmo para shap (interpretação do modelo) e graphviz (visualização de árvore). 
- A instalação do graphviz no Colab requer também um comando de sistema (!apt-get).

### Ignorar Warnings: 
Configura para não exibir certos tipos de avisos (UserWarning do shap, FutureWarning) que podem ser informativos mas poluem a saída principal.

---

    # --- Upload dos Arquivos ---
    print("Por favor, faça o upload do arquivo survey limpo (ex: 'survey_cleaned-1.csv'):")
    uploaded_survey = files.upload()
    # ... (código de verificação e nome do arquivo) ...
    print(f"\nArquivo '{survey_filename}' carregado.")
    
    print("\n(Opcional) Por favor, faça o upload do arquivo de microdados...")
    uploaded_microdados = files.upload()
    # ... (código de verificação e nome do arquivo) ...

## Explicação (Upload):

### Solicitação de Upload: 
- Usa files.upload() do google.colab para criar um widget interativo que permite ao usuário carregar os arquivos CSV necessários diretamente no ambiente Colab.

### Verificação: 
- O código verifica se um arquivo foi realmente carregado antes de prosseguir.

---

    # --- Carregamento dos Dados ---
    try:
        # ... (lógica complexa para tentar ler CSV com diferentes separadores e formatos de cabeçalho) ...
        df = pd.read_csv(...) # ou df = pd.read_csv(..., sep=';', ...)
        print(f"\nDataset Survey carregado. Shape: {df.shape}")
    except Exception as e:
        print(f"Erro CRÍTICO ao carregar Survey: {e}")
        raise
    
    # ... (código similar para df_microdados, se carregado) ...

## Explicação (Load):

### Leitura do CSV: 
- Utiliza pd.read_csv() para carregar o arquivo CSV (uploaded_survey) em um DataFrame do pandas chamado df.

### Tratamento Flexível: 
- O bloco try-except tenta lidar com diferentes cenários:

- Verifica se o cabeçalho parece uma "tupla" (como ('P1_l ', 'Nivel de Ensino')) ou uma string normal.

- Tenta usar , como separador e, se falhar ou resultar em poucas colunas, tenta usar ;.

- Usa encoding='utf-8' para compatibilidade com caracteres diversos.

### Informação: 
- Imprime o formato (shape) do DataFrame carregado.

---

    # --- Função de Limpeza REFINADA ---
    def clean_col_names_refined(df_to_clean):
        # ... (lógica para extrair nome de tupla-like ou string) ...
        # Limpeza Refinada:
        clean_name = col_str.lower() # Lowercase primeiro
        clean_name = unidecode(clean_name) # Remove acentos
        clean_name = re.sub(r'[?()/,.:#\-\[\]\'"]+', '', clean_name) # Remove pontuação
        clean_name = clean_name.replace(' ', '_') # Espaços -> underscore
        clean_name = re.sub(r'[^a-z0-9_]+', '_', clean_name) # Remove outros caracteres especiais
        clean_name = re.sub(r'_+', '_', clean_name) # Consolida underscores
        clean_name = clean_name.strip('_') # Remove do início/fim
        # ... (lógica para garantir nome único e renomear colunas) ...
        return df_cleaned
    
    # Aplicar limpeza
    df = clean_col_names_refined(df)
    print("\nNomes das colunas do Survey (APÓS LIMPEZA REFINADA):")
    # print(df.columns.tolist())

## Explicação (Clean - Nomes de Colunas):

### Objetivo: 
- Padronizar os nomes das colunas para facilitar o acesso e evitar erros.

###  Função clean_col_names_refined:

- Itera sobre cada nome de coluna original.

- Tenta extrair um nome significativo caso o original seja uma string representando uma tupla (ex: ('P1_l ', 'Nivel de Ensino') -> nivel_de_ensino).

- Aplica uma série de transformações:

    - lower(): **Converte para minúsculas.**

    - unidecode(): **Remove acentos (ex: experiência -> experiencia).**

    - re.sub(): **Usa expressões regulares para remover pontuações e caracteres especiais, substituindo-os por _ ou removendo-os.**

    - replace(' ', '_'): **Substitui espaços por underscores.**

    - **strip('_'): Remove underscores no início ou fim.**

    - **Garante que nomes não fiquem vazios e adiciona sufixos numéricos (_1, _2) se a limpeza gerar nomes duplicados.**

### Aplicação: 
- A função é chamada para limpar os nomes das colunas do DataFrame df.

---

    # --- Etapa 2: Definição da Variável Alvo e Seleção de Features ---
    
    target_column_clean_final = 'faixa_salarial' # Nome esperado após limpeza
    
    feature_columns_expected_clean = [ # Lista de nomes limpos esperados
        'nivel_de_ensino', 'area_de_formacao',
        'quanto_tempo_de_experiencia_na_area_de_dados_voce_tem', 'nivel',
        'sql', 'r', 'python', # ... etc ...
    ]
    
    # Verificação e Seleção
    # ... (código para verificar se target e features existem em df.columns) ...
    valid_feature_columns_final = [col for col in feature_columns_expected_clean if col in df.columns]
    # ... (Aviso se features esperadas não foram encontradas) ...
    
    df_model = df[valid_feature_columns_final + [target_column_clean_final]].copy()
    print(f"Shape inicial df_model: {df_model.shape}")

## Explicação (Select):

### Definição: 
- Define explicitamente o nome esperado da coluna alvo (target_column_clean_final) e uma lista com os nomes limpos esperados das colunas que serão usadas como features (feature_columns_expected_clean).

### Validação: 
- O código verifica se a coluna alvo e as features listadas realmente existem no DataFrame df (após a limpeza). Isso é importante para capturar erros de digitação ou problemas na etapa de limpeza. Avisa se alguma feature esperada não foi encontrada.

### Criação do df_model: 
- Cria um novo DataFrame (df_model) contendo apenas a coluna alvo e as features válidas encontradas. Isso foca a análise subsequente apenas nos dados relevantes. .copy() evita warnings sobre modificar o DataFrame original.

---

    # --- Etapa 3: Pré-processamento e Engenharia de Variáveis (CORRIGIDA) ---
    
    # 3.1 Tratar Salário (Variável Alvo)
    def get_salary_midpoint(salary_range):
        # ... (lógica para converter faixa ex: 'de R$ 4.001 a R$ 6.000' para 5000.5) ...
        return midpoint_value # ou np.nan se não conseguir converter
    
    df_model['salarymidpoint'] = df_model[target_column_clean_final].apply(get_salary_midpoint)
    df_model.dropna(subset=['salarymidpoint'], inplace=True)
    # ... (prints informativos) ...

## Explicação (Preprocess - Target):

### Objetivo: Converter a coluna alvo (faixa salarial, que é texto) em um valor numérico para que o modelo de regressão possa prevê-la.

### Função get_salary_midpoint:
- Recebe uma string de faixa salarial.
- Limpa a string (remove 'R$', '.', ajusta separadores).
- Trata casos especiais ('menos de 1.000', 'mais de 40.001').
- Usa expressões regulares (re.findall) para extrair os números limites da faixa.
- Calcula o ponto médio entre os limites. Considera a indicação 'ms' (mil) se presente.
- Retorna o valor numérico do ponto médio ou np.nan se a conversão falhar.

### Aplicação: 
- A função é aplicada (.apply()) à coluna alvo original (target_column_clean_final) para criar a nova coluna numérica salarymidpoint.

### Remoção de NaN: 
- Linhas onde não foi possível calcular o salarymidpoint são removidas (.dropna()) pois não podem ser usadas para treinar/avaliar o modelo.
