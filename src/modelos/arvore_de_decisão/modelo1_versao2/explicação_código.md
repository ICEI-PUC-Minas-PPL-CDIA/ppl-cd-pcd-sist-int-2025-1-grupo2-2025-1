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

---

    # 3.2 Tratamento de Valores Nulos (ANTES DA CODIFICAÇÃO)
    print("\nTratando valores nulos...")
    numeric_cols_pre_encoding = []
    categorical_cols_pre_encoding = []
    
    for col in valid_feature_columns_final:
        # ... (lógica para detectar flags binárias vs outras colunas) ...
        numeric_col = pd.to_numeric(df_model[col], errors='coerce')
        if not numeric_col.isnull().all(): # Se conseguiu converter para número
            if is_binary_flag:
                df_model[col] = numeric_col.fillna(0).astype(int) # Flags NaN -> 0
            else:
                # df_model[col] = numeric_col.fillna(numeric_col.median()) # Outras numéricas NaN -> Mediana (se houvesse)
            numeric_cols_pre_encoding.append(col)
        else: # Se era string ou falhou conversão numérica
            df_model[col] = df_model[col].astype(str).fillna('Desconhecido') # Categóricas NaN -> 'Desconhecido'
            categorical_cols_pre_encoding.append(col)
## Explicação (Preprocess - Nulls):

### Objetivo: Lidar com valores ausentes (NaN) nas colunas de features, pois a maioria dos modelos não os aceita.

### Estratégia: Itera sobre as features válidas:
- Flags Binárias (P4d..., P2o...): Tenta converter para número. Se for flag binária e tiver NaN, preenche com 0 (assumindo que NaN significa "não usa" ou "não considera").
- Outras Numéricas (se existissem): Preencheria NaN com a mediana da coluna (medida robusta a outliers).
- Categóricas (Strings): Preenche NaN com a string literal 'Desconhecido', criando uma nova categoria explícita para valores ausentes. Converte toda a coluna para string (.astype(str)) para garantir consistência antes da codificação.

### Listas de Rastreio: 
- Mantém listas separadas (numeric_cols_pre_encoding, categorical_cols_pre_encoding) para saber quais colunas tratar como numéricas ou categóricas na próxima etapa.

---

    # 3.3 Codificação de Variáveis Categóricas (Ordinal e Nominal - CORRIGIDA)
    # ... (definição dos nomes limpos das colunas ordinais: edu_col_clean, exp_col_clean, nivel_col_clean) ...
    
    # Definir colunas ordinais e suas ordens EXATAS (valores limpos)
    ordinal_cols_mapping = {
        edu_col_clean: ['nao_tenho_graduacao_formal', 'estudante_de_graduacao', ...],
        exp_col_clean: ['nao_tenho_experiencia_na_area_de_dados', 'menos_de_1_ano', ...],
        nivel_col_clean: ['junior', 'pleno', 'senior']
    }
    
    # --- Verificação Dinâmica e Aplicação do OrdinalEncoder ---
    # ... (código que limpa valores nas colunas, compara com a ordem predefinida,
    #      cria 'final_order' com categorias válidas, e popula 'ordinal_cols_to_encode',
    #      'ordinal_categories_final', 'processed_categoricals') ...
    
    # Aplicar OrdinalEncoder
    if ordinal_cols_to_encode:
        encoder_ordinal = OrdinalEncoder(
            categories=ordinal_categories_final,
            handle_unknown='use_encoded_value',
            unknown_value=-1 # Atribui -1 a valores desconhecidos/extras
        )
        df_model[ordinal_cols_to_encode] = encoder_ordinal.fit_transform(df_model[ordinal_cols_to_encode])
        # ... (atualiza lista de colunas numéricas) ...
    
    # Identificar colunas nominais (categóricas não ordinais)
    nominal_cols_to_encode = [ ... ]
    
    # Aplicar One-Hot Encoding (get_dummies) APENAS nas nominais
    if nominal_cols_to_encode:
        df_model = pd.get_dummies(df_model, columns=nominal_cols_to_encode, dummy_na=False, drop_first=False)
        # ... (prints informativos) ...
    
    # Atualizar lista de features finais
    features_final = [ ... ]
    print(f"Número final de features: {len(features_final)}")

## Explicação (Preprocess - Encoding - Correção Principal):

### Objetivo: 
- Converter as colunas categóricas (texto) em números para que o LightGBM possa processá-las, respeitando a natureza de cada variável (ordinal vs. nominal).

### Variáveis Ordinais:
- Mapeamento: 
    - Define um dicionário (ordinal_cols_mapping) que especifica quais colunas são ordinais (nivel_de_ensino, quanto_tempo_de_experiencia..., nivel) e a ordem correta das suas categorias (ex: 'junior' < 'pleno' < 'senior'). Usa os nomes limpos das colunas e os valores esperados após a limpeza (lowercase, sem acento, com underscore).
    Verificação Dinâmica: 
    - O código crucial aqui verifica, para cada coluna ordinal definida:
    - Limpa os valores reais da coluna no DataFrame.
        - Compara com a ordem predefinida (também limpa).
        - Cria uma lista (final_order) contendo apenas as categorias predefinidas que realmente existem nos dados, mantendo a ordem. Avisa sobre categorias extras ou faltantes.

- OrdinalEncoder:
    - Instancia OrdinalEncoder passando a lista de categorias válidas e ordenadas (ordinal_categories_final). Isso garante que a codificação numérica (0, 1, 2, ...) respeite a ordem correta.
        - handle_unknown='use_encoded_value', unknown_value=-1: Garante que valores não previstos na ordem (incluindo 'Desconhecido' ou extras) recebam um valor numérico específico (-1), em vez de causar erro.
        - Aplica (.fit_transform()) o encoder às colunas ordinais identificadas.

### Variáveis Nominais:
- Identificação: 
- Seleciona as colunas que foram inicialmente marcadas como categóricas mas não foram processadas pelo OrdinalEncoder.
    - pd.get_dummies: Aplica o One-Hot Encoding apenas a essas colunas nominais. Isso cria novas colunas binárias (0/1) para cada categoria única (ex: area_de_formacao_computacao, genero_feminino, setor_financas_ou_bancos).
        - dummy_na=False: Não cria coluna extra para NaNs (já tratados como 'Desconhecido').
        - drop_first=False: Mantém todas as categorias dummy, o que geralmente é seguro para modelos de árvore.

### Resultado: 
- Todas as features agora são numéricas (originais numéricas, ordinais codificadas, dummies binárias). A lista features_final é atualizada com os nomes de todas essas colunas. O número final de features (106 neste caso) reflete essa transformação.

---

    # --- Etapa 4: Preparação para o Modelo ---
    
    # 4.1 Definir X e y
    X = df_model[features_final]
    y = df_model['salarymidpoint']
    
    # 4.2 Dividir em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    
    # 4.3 Escalonamento das Features
    print("\nEscalonando features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Converter de volta para DataFrame para manter nomes das colunas
    X_train_scaled_df = pd.DataFrame(X_train_scaled, columns=X_train.columns, index=X_train.index)
    X_test_scaled_df = pd.DataFrame(X_test_scaled, columns=X_test.columns, index=X_test.index)
## Explicação (Split & Scale):

### Definir X e y: Separa o DataFrame df_model em:
- X: DataFrame contendo apenas as colunas de features (preditoras).
- y: Series contendo apenas a variável alvo numérica (salarymidpoint).

### Divisão Treino/Teste (train_test_split):
- Divide X e y em conjuntos de treinamento (X_train, y_train) e teste (X_test, y_test).
- test_size=0.25: Define que 25% dos dados serão usados para teste, e 75% para treino.
- random_state=42: Garante que a divisão seja sempre a mesma se o código for executado novamente (reprodutibilidade). Fundamental para comparar modelos.

### Escalonamento (StandardScaler):
- Objetivo: Transforma os dados para terem média 0 e desvio padrão 1. Embora modelos de árvore como LightGBM não exijam escalonamento, ele geralmente não prejudica e pode às vezes ajudar na convergência ou interpretação (especialmente com SHAP).
- Aplicação:
    - Cria uma instância do StandardScaler.
    - scaler.fit_transform(X_train): Aprende a média e o desvio padrão apenas do conjunto de treino e aplica a transformação a ele.
    - scaler.transform(X_test): Aplica a mesma transformação (aprendida no treino) ao conjunto de teste. É crucial não usar fit no teste para evitar data leakage.

### Reconversão para DataFrame: 
- Os dados escalados são convertidos de volta para DataFrames (X_train_scaled_df, X_test_scaled_df) para preservar os nomes das colunas, que são importantes para a interpretação posterior com SHAP.

---

    # --- Etapa 5: Treinamento e Otimização do Modelo LightGBM ---
    print("\n--- Treinamento e Otimização com GridSearchCV ---")
    
    lgbm = lgb.LGBMRegressor(objective='regression_l1', metric='mae', random_state=42, n_jobs=-1)
    
    param_grid = { # Define combinações de hiperparâmetros a testar
        'n_estimators': [200, 400],
        'learning_rate': [0.05, 0.1],
        'num_leaves': [31, 50],
        'max_depth': [-1, 10],
        'min_child_samples': [20, 30],
    }
    
    grid_search = GridSearchCV(estimator=lgbm, param_grid=param_grid,
                               cv=3, scoring='r2', verbose=2, n_jobs=-1)
    
    print("Iniciando GridSearchCV...")
    grid_search.fit(X_train_scaled_df, y_train) # Treinar com dados escalados
    print("GridSearchCV concluído.")
## Explicação (Train - Otimização):

### Instanciar Modelo Base: 
- Cria uma instância do lgb.LGBMRegressor com configurações iniciais:
- objective='regression_l1': Define o objetivo como regressão, usando o Erro Absoluto Médio (L1 loss) como função de perda a ser minimizada durante o treino.
- metric='mae': Usa MAE também como métrica de avaliação interna durante o treino (embora o GridSearchCV use R²).
- random_state=42: Para reprodutibilidade interna do algoritmo.
- n_jobs=-1: Usa todos os processadores disponíveis para acelerar.

### Definir Grid de Parâmetros (param_grid): 
- Cria um dicionário onde as chaves são nomes de hiperparâmetros do LightGBM e os valores são listas de opções a serem testadas. Isso define o espaço de busca para a otimização.
- n_estimators: Número de árvores no ensemble.
- learning_rate: Taxa de aprendizado (quão rápido o modelo aprende/corrige erros).
- num_leaves, max_depth, min_child_samples: Parâmetros que controlam a complexidade de cada árvore individual para evitar overfitting.

### Configurar GridSearchCV:

- estimator=lgbm: O modelo base a ser otimizado.
- param_grid=param_grid: O grid de parâmetros a testar.
- cv=3: Usa validação cruzada de 3 folds (divide o treino em 3 partes, treina em 2 e valida em 1, rotacionando). Isso dá uma estimativa mais robusta do desempenho de cada combinação de parâmetros.
- scoring='r2': Usa o R² como métrica para decidir qual combinação de parâmetros é a "melhor".
- verbose=2: Mostra logs detalhados durante a execução.
- n_jobs=-1: Paraleliza a busca nos folds/combinações.

### Executar a Busca (grid_search.fit): 
- Treina o LightGBM com cada combinação de parâmetros do grid, usando validação cruzada (CV) no conjunto de treinamento escalado (X_train_scaled_df, y_train). Esta etapa pode ser demorada.

---

    # --- Etapa 6: Avaliação do Modelo Otimizado ---
    print("\n--- Avaliação do Modelo Otimizado ---")
    
    print("Melhores parâmetros:", grid_search.best_params_)
    best_lgbm = grid_search.best_estimator_ # Pega o modelo treinado com os melhores params
    y_pred = best_lgbm.predict(X_test_scaled_df) # Prediz no teste escalado
    
    # Calcular Métricas
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    # Imprimir Métricas
    print(f"\nDesempenho no Teste:")
    print(f"MAE: R$ {mae:,.2f}")
    print(f"RMSE: R$ {rmse:,.2f}")
    print(f"R²: {r2:.4f} ({r2*100:.2f}%)")
## Explicação (Evaluate):

### Melhor Modelo:
- grid_search.best_params_: Acessa e imprime o dicionário com a combinação de hiperparâmetros que resultou no melhor score R² durante a validação cruzada.
- grid_search.best_estimator_: Acessa o modelo LightGBM que já foi re-treinado automaticamente pelo GridSearchCV usando os melhores parâmetros encontrados e todo o conjunto de treino.

### Predição no Teste: 
- Usa o melhor modelo (best_lgbm) para fazer previsões (.predict()) no conjunto de teste escalado (X_test_scaled_df), que o modelo nunca viu antes.

### Cálculo das Métricas: 
- Compara as previsões (y_pred) com os valores reais do conjunto de teste (y_test) usando as funções de métrica do sklearn.metrics:
- mean_absolute_error: Calcula o MAE.
- mean_squared_error: Calcula o MSE.
- np.sqrt(mse): Calcula o RMSE a partir do MSE.
- r2_score: Calcula o R².

### Apresentação: 
- Imprime as métricas calculadas de forma formatada, permitindo avaliar o desempenho final do modelo otimizado em dados não vistos.
