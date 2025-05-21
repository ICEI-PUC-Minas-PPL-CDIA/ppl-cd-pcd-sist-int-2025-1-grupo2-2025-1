# Explicação Detalhada do Código 

Este script Python realiza um processo completo de machine learning, desde o carregamento e pré-processamento de dados até o treinamento, otimização, avaliação de um modelo Random Forest e visualização dos resultados.

---

### Importação de Bibliotecas

    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, roc_curve, auc
    import matplotlib.pyplot as plt
    from sklearn.tree import plot_tree
    import seaborn as sns
    import os


*   `import pandas as pd`: Importa a biblioteca Pandas, essencial para manipulação e análise de dados tabulares (DataFrames). É apelidada como `pd`.
*   `import numpy as np`: Importa a biblioteca NumPy, fundamental para computação numérica, especialmente para trabalhar com arrays e matrizes. É apelidada como `np`.
*   `from sklearn.model_selection import train_test_split, GridSearchCV`: Do submódulo `model_selection` da Scikit-learn:
    *   `train_test_split`: Função para dividir dados em conjuntos de treinamento e teste.
    *   `GridSearchCV`: Ferramenta para otimizar hiperparâmetros de modelos usando busca em grade com validação cruzada.
*   `from sklearn.ensemble import RandomForestClassifier`: Do submódulo `ensemble` da Scikit-learn, importa o `RandomForestClassifier`, um algoritmo de classificação baseado em múltiplas árvores de decisão.
*   `from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, roc_curve, auc`: Do submódulo `metrics` da Scikit-learn, importa funções para avaliação de modelos:
    *   `confusion_matrix`: Calcula a matriz de confusão.
    *   `accuracy_score`: Calcula a acurácia.
    *   `classification_report`: Gera um relatório com precisão, recall, F1-score.
    *   `roc_curve`: Calcula pontos para a curva ROC.
    *   `auc`: Calcula a Área Sob a Curva ROC.
*   `import matplotlib.pyplot as plt`: Importa o `pyplot` da Matplotlib, usado para criar gráficos e visualizações. É apelidado como `plt`.
*   `from sklearn.tree import plot_tree`: Do submódulo `tree` da Scikit-learn, importa `plot_tree` para visualizar árvores de decisão individuais.
*   `import seaborn as sns`: Importa a biblioteca Seaborn, baseada no Matplotlib, para criar gráficos estatísticos mais atraentes. É apelidada como `sns`.
*   `import os`: Importa o módulo `os`, que fornece funcionalidades para interagir com o sistema operacional (ex: manipulação de arquivos e diretórios).

---

### Etapa 0: Configuração

  --- Etapa 0: Configuração ---
  Criar diretório para salvar os gráficos, se não existir
    
    output_dir = '/kaggle/working/'
    if not os.path.exists(output_dir):
    os.makedirs(output_dir)


*   `# --- Etapa 0: Configuração ---`: Comentário de seção.
*   `# Criar diretório para salvar os gráficos, se não existir`: Comentário explicativo.
*   `output_dir = '/kaggle/working/'`: Define a variável `output_dir` com o caminho `/kaggle/working/`, um diretório padrão para salvar arquivos de saída em ambientes Kaggle.
*   `if not os.path.exists(output_dir):`: Verifica se o diretório especificado em `output_dir` **não** existe.
*   `os.makedirs(output_dir)`: Se o diretório não existir, esta linha o cria. `makedirs` também cria diretórios pais necessários no caminho.

---
    
### Etapa 1: Carregamento e Pré-processamento dos Dados
    
    --- Etapa 1: Carregamento e Pré-processamento dos Dados ---
    Carregar o dataset
    try:
    df = pd.read_csv('/kaggle/input/dataset-clean/dados_limpos.csv')
    print("Dataset carregado do caminho Kaggle.")
    except FileNotFoundError:
    try:
    df = pd.read_csv('dados_limpos.csv')
    print("Dataset carregado localmente.")
    except FileNotFoundError:
    print("Arquivo 'dados_limpos.csv' não encontrado no caminho Kaggle nem localmente.")
    print("Por favor, certifique-se de que o arquivo está no diretório correto ou ajuste o caminho.")


*   `# --- Etapa 1: Carregamento e Pré-processamento dos Dados ---`: Comentário de seção.
*   `# Carregar o dataset`: Comentário explicativo.
*   `try:`: Inicia um bloco para tratamento de exceções.
*   `df = pd.read_csv('/kaggle/input/dataset-clean/dados_limpos.csv')`: Tenta carregar o arquivo CSV `dados_limpos.csv` de um caminho típico do Kaggle para um DataFrame Pandas chamado `df`.
*   `print("Dataset carregado do caminho Kaggle.")`: Mensagem de sucesso se carregado do Kaggle.
*   `except FileNotFoundError:`: Se o arquivo não for encontrado no caminho do Kaggle, este bloco é executado.
*   `try:`: Bloco aninhado para tentar carregar localmente.
*   `df = pd.read_csv('dados_limpos.csv')`: Tenta carregar o arquivo CSV do diretório atual.
*   `print("Dataset carregado localmente.")`: Mensagem de sucesso se carregado localmente.
*   `except FileNotFoundError:`: Se o arquivo também não for encontrado localmente.
*   `print(...)`: Mensagens informando que o arquivo não foi encontrado.
*   `exit()`: Encerra o script, pois os dados são essenciais.

  Selecionar colunas relevantes
    
        colunas_features = ['Nível de ensino alcançado', 'Tempo de experiência na área de dados']
        coluna_target = 'Faixa salarial mensal'
        colunas_necessarias = colunas_features + [coluna_target]


*   `# Selecionar colunas relevantes`: Comentário explicativo.
*   `colunas_features = [...]`: Define uma lista com os nomes das colunas que serão usadas como *features* (variáveis preditoras).
*   `coluna_target = 'Faixa salarial mensal'`: Define o nome da coluna que contém a informação original do salário (antes da transformação).
*   `colunas_necessarias = colunas_features + [coluna_target]`: Cria uma lista combinada com todas as colunas importantes para esta fase inicial.

  Remover linhas com valores ausentes nas colunas cruciais
    
        df_limpo = df[colunas_necessarias].copy()
        df_limpo.dropna(subset=colunas_necessarias, inplace=True)
            exit()


*   `# Remover linhas com valores ausentes nas colunas cruciais`: Comentário explicativo.
*   `df_limpo = df[colunas_necessarias].copy()`: Cria um novo DataFrame `df_limpo` contendo apenas as `colunas_necessarias`. O `.copy()` evita `SettingWithCopyWarning` e garante uma cópia independente.
*   `df_limpo.dropna(subset=colunas_necessarias, inplace=True)`: Remove linhas de `df_limpo` que tenham qualquer valor ausente (NaN) nas colunas especificadas em `subset`. `inplace=True` modifica `df_limpo` diretamente.

---
    
### Etapa 2: Engenharia de Features e Criação da Variável Alvo
    
    --- Etapa 2: Engenharia de Features e Criação da Variável Alvo ---
    Mapeamento ordinal para 'Nível de ensino alcançado'
    nivel_ensino_map = {
    'Estudante de Graduação': 0,
    'Graduação/Bacharelado': 1,
    'Pós-graduação': 2,
    'Mestrado': 3,
    'Doutorado ou Phd': 4
    }
    df_limpo['formacao_academica_encoded'] = df_limpo['Nível de ensino alcançado'].map(nivel_ensino_map)


*   `# --- Etapa 2: Engenharia de Features e Criação da Variável Alvo ---`: Comentário de seção.
*   `# Mapeamento ordinal para 'Nível de ensino alcançado'`: Comentário explicativo.
*   `nivel_ensino_map = { ... }`: Define um dicionário para mapear categorias textuais de nível de ensino para valores numéricos ordinais (0 a 4).
*   `df_limpo['formacao_academica_encoded'] = df_limpo['Nível de ensino alcançado'].map(nivel_ensino_map)`: Cria uma nova coluna `formacao_academica_encoded` aplicando o mapeamento à coluna 'Nível de ensino alcançado'.
        
   Mapeamento ordinal para 'Tempo de experiência na área de dados'
    
        experiencia_map = {
        'Menos de 1 ano': 0,
        'de 1 a 2 anos': 1,
        'de 3 a 4 anos': 2,
        'de 4 a 6 anos': 3, # Note: mesmo valor que 'de 5 a 6 anos'
        'de 5 a 6 anos': 3,
        'de 7 a 10 anos': 4,
        'Mais de 10 anos': 5
        }
        df_limpo['experiencia_profissional_encoded'] = df_limpo['Tempo de experiência na área de dados'].map(experiencia_map)


*   `# Mapeamento ordinal para 'Tempo de experiência na área de dados'`: Comentário explicativo.
*   `experiencia_map = { ... }`: Define um dicionário para mapear categorias textuais de tempo de experiência para valores numéricos ordinais (0 a 5).
*   `df_limpo['experiencia_profissional_encoded'] = df_limpo['Tempo de experiência na área de dados'].map(experiencia_map)`: Cria a coluna `experiencia_profissional_encoded` aplicando o mapeamento.

Mapeamento ordinal para 'Faixa salarial mensal' para criar a variável alvo binária

    salario_map_ordinal = {
    'Menos de R$ 1.000/mês': 0,
    'de R$ 1.001/mês a R$ 2.000/mês': 1,
    'de R$ 2.001/mês a R$ 3.000/mês': 2,
    'de R$ 3.001/mês a R$ 4.000/mês': 3,
    'de R$ 4.001/mês a R$ 6.000/mês': 4,
    'de R$ 6.001/mês a R$ 8.000/mês': 5,
    'de R$ 8.001/mês a R$ 12.000/mês': 6,
    'de R$ 12.001/mês a R$ 16.000/mês': 7,
    'de R$ 16.001/mês a R$ 20.000/mês': 8,
    'de R$ 20.001/mês a R$ 25.000/mês': 9,
    'de R$ 25.001/mês a R$ 30.000/mês': 10,
    'de R$ 30.001/mês a R$ 40.000/mês': 11,
    'Acima de R$ 40.001/mês': 12
    }
    df_limpo['faixa_salarial_encoded'] = df_limpo['Faixa salarial mensal'].map(salario_map_ordinal)


*   `# Mapeamento ordinal para 'Faixa salarial mensal' ...`: Comentário explicativo.
*   `salario_map_ordinal = { ... }`: Define um dicionário para mapear faixas salariais textuais para valores numéricos ordinais (0 a 12). Este é um passo intermediário.
*   `df_limpo['faixa_salarial_encoded'] = df_limpo['Faixa salarial mensal'].map(salario_map_ordinal)`: Cria a coluna `faixa_salarial_encoded` com os salários mapeados.

Remover NaNs que podem surgir de mapeamentos incompletos
    
    df_limpo.dropna(subset=['formacao_academica_encoded',
    'experiencia_profissional_encoded',
    'faixa_salarial_encoded'], inplace=True)


*   `# Remover NaNs que podem surgir de mapeamentos incompletos`: Comentário explicativo. Se alguma categoria original não estivesse nos dicionários de mapeamento, `.map()` geraria NaN.
*   `df_limpo.dropna(subset=[...], inplace=True)`: Remove linhas com NaN nas colunas encodadas recém-criadas.

Criar variável alvo binária: 0 para salários até R$ 8.000 (<=5), 1 para salários acima (>5)

    df_limpo['salario_alto'] = df_limpo['faixa_salarial_encoded'].apply(lambda x: 1 if x > 5 else 0)


*   `# Criar variável alvo binária ...`: Comentário explicativo.
*   `df_limpo['salario_alto'] = df_limpo['faixa_salarial_encoded'].apply(lambda x: 1 if x > 5 else 0)`: Cria a coluna alvo `salario_alto`.
    *   `.apply(lambda x: ...)`: Aplica uma função anônima a cada valor da coluna `faixa_salarial_encoded`.
    *   `1 if x > 5 else 0`: Se o valor encodado do salário (`x`) for maior que 5 (correspondendo a > R$8.000/mês), atribui 1 (salário alto); caso contrário, atribui 0.

Preparar Features (X) e Target (y)

    X = df_limpo[['formacao_academica_encoded', 'experiencia_profissional_encoded']]
    y = df_limpo['salario_alto']


*   `# Preparar Features (X) e Target (y)`: Comentário explicativo.
*   `X = df_limpo[['formacao_academica_encoded', 'experiencia_profissional_encoded']]`: Define `X` (features) como um DataFrame contendo as colunas de formação e experiência encodadas.
*   `y = df_limpo['salario_alto']`: Define `y` (variável alvo) como a Series Pandas `salario_alto`.

Verificar se há dados suficientes

    if X.shape < 10 or len(y.unique()) < 2:
    print("Não há dados suficientes ou classes suficientes após o pré-processamento para treinar o modelo.")
    print(f"Tamanho de X: {X.shape}, Classes em y: {y.unique()}")
    exit()

 
*   `# Verificar se há dados suficientes`: Comentário explicativo.
*   `if X.shape[0] < 10 or len(y.unique()) < 2:`: Verifica se há menos de 10 amostras ou menos de 2 classes únicas na variável alvo.
*   `print(...)`: Mensagem de erro se a condição for verdadeira.
*   `exit()`: Encerra o script.

Divisão dos dados em treino e teste

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)


*   `# Divisão dos dados em treino e teste`: Comentário explicativo.
*   `X_train, X_test, y_train, y_test = train_test_split(...)`: Divide `X` e `y` em conjuntos de treino e teste.
    *   `test_size=0.3`: 30% dos dados para teste, 70% para treino.
    *   `random_state=42`: Garante reprodutibilidade da divisão.
    *   `stratify=y`: Mantém a proporção das classes de `y` nos conjuntos de treino e teste.

---

### Etapa 3: Desenvolvimento do Modelo de Machine Learning - Random Forest

Definir a grade de parâmetros para o GridSearchCV

    param_grid = {
    'n_estimators': ,
    'max_depth': [None, 10, 20],
    'min_samples_split': ,
    'min_samples_leaf': ,
    'class_weight': ['balanced_subsample', 'balanced']
    }


*   `# --- Etapa 3: Desenvolvimento do Modelo ... ---`: Comentário de seção.
*   `# Definir a grade de parâmetros para o GridSearchCV`: Comentário explicativo.
*   `param_grid = { ... }`: Define um dicionário com os hiperparâmetros do `RandomForestClassifier` e os valores a serem testados pelo `GridSearchCV`.
    *   `'n_estimators'`: Número de árvores.
    *   `'max_depth'`: Profundidade máxima das árvores.
    *   `'min_samples_split'`: Mínimo de amostras para dividir um nó.
    *   `'min_samples_leaf'`: Mínimo de amostras em um nó folha.
    *   `'class_weight'`: Pesos para as classes, útil para dados desbalanceados.

Instanciar o RandomForestClassifier

    rf_base = RandomForestClassifier(random_state=42, n_jobs=-1)


*   `# Instanciar o RandomForestClassifier`: Comentário explicativo.
*   `rf_base = RandomForestClassifier(random_state=42, n_jobs=-1)`: Cria uma instância do classificador Random Forest.
    *   `random_state=42`: Para reprodutibilidade da aleatoriedade interna do modelo.
    *   `n_jobs=-1`: Usa todos os processadores disponíveis para paralelizar o treinamento.

Instanciar o GridSearchCV
cv=3 para ser mais rápido, idealmente cv=5 ou cv=10
    
    grid_search = GridSearchCV(estimator=rf_base, param_grid=param_grid,
    cv=3, n_jobs=-1, verbose=1, scoring='accuracy')


*   `# Instanciar o GridSearchCV`: Comentário explicativo.
*   `# cv=3 ...`: Comentário sobre a escolha de `cv` (número de folds da validação cruzada).
*   `grid_search = GridSearchCV(...)`: Cria uma instância do `GridSearchCV`.
    *   `estimator=rf_base`: O modelo a ser otimizado.
    *   `param_grid=param_grid`: A grade de parâmetros.
    *   `cv=3`: Validação cruzada com 3 folds.
    *   `n_jobs=-1`: Paraleliza a busca em grade.
    *   `verbose=1`: Mostra mensagens de progresso.
    *   `scoring='accuracy'`: Métrica para avaliar as combinações de parâmetros.

            print("Iniciando a busca de hiperparâmetros com GridSearchCV...")
            grid_search.fit(X_train, y_train)


*   `print(...)`: Mensagem indicando o início da otimização.
*   `grid_search.fit(X_train, y_train)`: Executa a busca em grade nos dados de treinamento para encontrar a melhor combinação de hiperparâmetros.

Melhor modelo encontrado pelo GridSearchCV

    best_rf_model = grid_search.best_estimator_
    
    print("\nMelhores Parâmetros Encontrados pelo GridSearchCV:")
    print(grid_search.best_params_)


*   `# Melhor modelo encontrado pelo GridSearchCV`: Comentário explicativo.
*   `best_rf_model = grid_search.best_estimator_`: Armazena o melhor modelo (com os melhores hiperparâmetros, já treinado) na variável `best_rf_model`.
*   `print(...)`: Imprime os melhores parâmetros encontrados.

Previsões com o melhor modelo

    y_pred_train = best_rf_model.predict(X_train)
    y_pred_test = best_rf_model.predict(X_test)
    y_pred_proba_test = best_rf_model.predict_proba(X_test)[:, 1] # Probabilidades para ROC


*   `# Previsões com o melhor modelo`: Comentário explicativo.
*   `y_pred_train = best_rf_model.predict(X_train)`: Faz previsões no conjunto de treinamento.
*   `y_pred_test = best_rf_model.predict(X_test)`: Faz previsões no conjunto de teste.
*   `y_pred_proba_test = best_rf_model.predict_proba(X_test)[:, 1]`: Obtém as probabilidades da classe positiva (1) para o conjunto de teste, usadas na curva ROC. `[:, 1]` seleciona a segunda coluna (probabilidade da classe 1).

---

### Etapa 4: Avaliação do Modelo

    accuracy_train = accuracy_score(y_train, y_pred_train)
    accuracy_test = accuracy_score(y_test, y_pred_test)
    
    print(f"\nAcurácia do Modelo no Conjunto de Treinamento: {accuracy_train:.4f}")
    print(f"Acurácia do Modelo no Conjunto de Teste: {accuracy_test:.4f}")
    print(f"Diferença de Acurácia (Treino - Teste): {accuracy_train - accuracy_test:.4f}\n")
    
    print("Relatório de Classificação no Conjunto de Teste:")
    print(classification_report(y_test, y_pred_test, target_names=['Salário Baixo/Médio', 'Salário Alto']))
    
    print("\nParâmetros do Melhor Modelo Random Forest Utilizado:")
    print(best_rf_model.get_params())


*   `# --- Etapa 4: Avaliação do Modelo ---`: Comentário de seção.
*   `accuracy_train = accuracy_score(y_train, y_pred_train)`: Calcula a acurácia no treino.
*   `accuracy_test = accuracy_score(y_test, y_pred_test)`: Calcula a acurácia no teste.
*   `print(...)`: Imprime as acurácias de treino e teste e a diferença entre elas (para verificar overfitting).
*   `print("Relatório de Classificação ...")`: Imprime o cabeçalho do relatório.
*   `print(classification_report(...))`: Gera e imprime o relatório de classificação (precisão, recall, F1-score) para o conjunto de teste, com nomes de classes personalizados.
*   `print("\nParâmetros do Melhor Modelo ...")`: Imprime o cabeçalho.
*   `print(best_rf_model.get_params())`: Imprime todos os parâmetros do melhor modelo Random Forest.

---

### Etapa 5: Geração de Gráficos

5.1. Matriz de Confusão

    cm = confusion_matrix(y_test, y_pred_test)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
    xticklabels=['Salário Baixo/Médio', 'Salário Alto'],
    yticklabels=['Salário Baixo/Médio', 'Salário Alto'])
    plt.title('Matriz de Confusão (Conjunto de Teste)')
    plt.xlabel('Previsto')
    plt.ylabel('Verdadeiro')
    plt.savefig(os.path.join(output_dir, 'matriz_confusao.png'), bbox_inches='tight')
    
    plt.show() # Comentado para evitar interrupção se rodando em script não interativo
    plt.close()


*   `# --- Etapa 5: Geração de Gráficos ---`: Comentário de seção.
*   `# 5.1. Matriz de Confusão`: Comentário específico do gráfico.
*   `cm = confusion_matrix(y_test, y_pred_test)`: Calcula a matriz de confusão.
*   `plt.figure(figsize=(8, 6))`: Cria uma nova figura Matplotlib com tamanho 8x6.
*   `sns.heatmap(...)`: Usa Seaborn para plotar a matriz de confusão como um mapa de calor.
    *   `annot=True`: Mostra os números nas células.
    *   `fmt='d'`: Formata os números como inteiros.
    *   `cmap='Blues'`: Esquema de cores.
    *   `xticklabels`, `yticklabels`: Rótulos das classes.
*   `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)`: Define título e rótulos dos eixos.
*   `plt.savefig(os.path.join(output_dir, 'matriz_confusao.png'), bbox_inches='tight')`: Salva o gráfico como `matriz_confusao.png` no `output_dir`. `bbox_inches='tight'` ajusta para que tudo caiba.
*   `# plt.show()`: Comentado; se descomentado, mostraria o gráfico interativamente.
*   `plt.close()`: Fecha a figura para liberar memória.

5.2. Exemplo de uma Árvore de Decisão da Floresta

    plt.figure(figsize=(40, 20))
    plot_tree(best_rf_model.estimators_,
    feature_names=['Nível de Formação (Encoded)', 'Tempo de Experiência (Encoded)'],
    class_names=['Salário Baixo/Médio', 'Salário Alto'],
    filled=True,
    rounded=True,
    impurity=True, # Mostra a impureza (Gini)
    proportion=False, # Mostra contagens absolutas em 'value'
    fontsize=7,
    max_depth=4) # Mantém a profundidade limitada para visualização
    plt.title('Exemplo de uma Árvore de Decisão do Random Forest (Profundidade limitada para visualização)', fontsize=20)
    plt.savefig(os.path.join(output_dir, 'arvore_decisao_exemplo.png'), bbox_inches='tight', dpi=300)
    
    plt.show()


*   `# 5.2. Exemplo de uma Árvore de Decisão ...`: Comentário do gráfico.
*   `plt.figure(figsize=(40, 20))`: Cria uma figura grande para a árvore.
*   `plot_tree(best_rf_model.estimators_[0], ...)`: Plota a primeira árvore (`estimators_[0]`) do Random Forest.
    *   `feature_names`, `class_names`: Rótulos para features e classes.
    *   `filled=True`, `rounded=True`, `impurity=True`, `proportion=False`: Opções de visualização.
    *   `fontsize=7`: Tamanho da fonte nos nós.
    *   `max_depth=4`: Limita a profundidade da árvore plotada para melhor legibilidade.
*   `plt.title(...)`: Define o título.
*   `plt.savefig(..., dpi=300)`: Salva o gráfico com resolução de 300 DPI para melhor qualidade.
*   `# plt.show()`, `plt.close()`: Como antes.

5.3. Importância das Features

    importances = best_rf_model.feature_importances_
    feature_names_importances = ['Nível de Formação', 'Tempo de Experiência']
    forest_importances = pd.Series(importances, index=feature_names_importances)
    
    fig, ax = plt.subplots(figsize=(10,6))
    forest_importances.sort_values(ascending=False).plot.bar(ax=ax)
    ax.set_title("Importância das Features (Random Forest)")
    ax.set_ylabel("Redução média de impureza (Gini)")
    fig.tight_layout()
    plt.savefig(os.path.join(output_dir, 'importancia_features.png'), bbox_inches='tight')
    
    plt.show()
    plt.close()


*   `# 5.3. Importância das Features`: Comentário do gráfico.
*   `importances = best_rf_model.feature_importances_`: Obtém os scores de importância das features do modelo.
*   `feature_names_importances = [...]`: Nomes das features para o gráfico.
*   `forest_importances = pd.Series(...)`: Cria uma Series Pandas com as importâncias e os nomes como índice.
*   `fig, ax = plt.subplots(figsize=(10,6))`: Cria uma figura e eixos.
*   `forest_importances.sort_values(ascending=False).plot.bar(ax=ax)`: Plota um gráfico de barras das importâncias, ordenadas.
*   `ax.set_title(...)`, `ax.set_ylabel(...)`: Define título e rótulo do eixo y.
*   `fig.tight_layout()`: Ajusta o layout.
*   `plt.savefig(...)`, `# plt.show()`, `plt.close()`: Como antes.

5.4. Curva ROC

    fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba_test)
    roc_auc = auc(fpr, tpr)
    
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'Curva ROC (AUC = {roc_auc:.2f})')
    plt.plot(, , color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Taxa de Falsos Positivos (FPR)')
    plt.ylabel('Taxa de Verdadeiros Positivos (TPR)')
    plt.title('Curva ROC (Receiver Operating Characteristic)')
    plt.legend(loc="lower right")
    plt.savefig(os.path.join(output_dir, 'curva_roc.png'), bbox_inches='tight')
    
    plt.show()


    plt.close()


*   `# 5.4. Curva ROC`: Comentário do gráfico.
*   `fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba_test)`: Calcula os valores da Taxa de Falsos Positivos (FPR) e Taxa de Verdadeiros Positivos (TPR) para diferentes limiares.
*   `roc_auc = auc(fpr, tpr)`: Calcula a Área Sob a Curva ROC.
*   `plt.figure(...)`: Cria a figura.
*   `plt.plot(fpr, tpr, ...)`: Plota a curva ROC, incluindo a AUC na legenda.
*   `plt.plot([0, 1], [0, 1], ...)`: Plota a linha de referência (classificador aleatório).
*   `plt.xlim(...)`, `plt.ylim(...)`: Define os limites dos eixos.
*   `plt.xlabel(...)`, `plt.ylabel(...)`, `plt.title(...)`: Define rótulos e título.
*   `plt.legend(loc="lower right")`: Mostra a legenda.
*   `plt.savefig(...)`, `# plt.show()`, `plt.close()`: Como antes.

5.5. Gráfico de Distribuição da Variável Alvo (Salário Alto)

    plt.figure(figsize=(7, 5))
    sns.countplot(x='salario_alto', data=df_limpo, palette='viridis')
    plt.title('Distribuição da Variável Alvo (0: Salário Baixo/Médio, 1: Salário Alto)')
    plt.xlabel('Categoria Salarial')
    plt.ylabel('Contagem')
    plt.xticks(, ['Salário Baixo/Médio (<= R$8k)', 'Salário Alto (> R$8k)'])
    plt.savefig(os.path.join(output_dir, 'distribuicao_target.png'), bbox_inches='tight')
    
    plt.show()
    plt.close()


*   `# 5.5. Gráfico de Distribuição da Variável Alvo ...`: Comentário do gráfico.
*   `plt.figure(...)`: Cria a figura.
*   `sns.countplot(...)`: Cria um gráfico de barras mostrando a contagem de cada classe na variável alvo `salario_alto`.
*   `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)`: Define título e rótulos.
*   `plt.xticks([0,1], ['Salário Baixo/Médio ...', 'Salário Alto ...'])`: Define rótulos personalizados para as marcações do eixo x.
*   `plt.savefig(...)`, `# plt.show()`, `plt.close()`: Como antes.

5.6. Análise: Nível de Ensino vs. Proporção de Salário Alto
    
    nivel_ensino_map_inv = {v: k for k, v in nivel_ensino_map.items()}
    df_limpo['Nivel de ensino (labels)'] = df_limpo['formacao_academica_encoded'].map(nivel_ensino_map_inv)
    
    plt.figure(figsize=(12, 7))
    sns.barplot(
    x='Nivel de ensino (labels)',
    y='salario_alto',
    data=df_limpo,
    estimator=lambda x: sum(x==1)*100.0/len(x) if len(x) > 0 else 0.0,
    palette='coolwarm',
    order=list(nivel_ensino_map.keys()) # Garante a ordem correta das categorias
    )
    plt.title('Proporção de Profissionais com Salário Alto por Nível de Ensino')
    plt.xlabel('Nível de Ensino Alcançado')
    plt.ylabel('Proporção de Salário Alto (%)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'formacao_vs_salario_alto.png'), bbox_inches='tight')
    
    plt.show()
    plt.close()


*   `# 5.6. Análise: Nível de Ensino ...`: Comentário do gráfico.
*   `nivel_ensino_map_inv = {v: k for k, v in nivel_ensino_map.items()}`: Cria um mapa reverso para obter os rótulos textuais do nível de ensino a partir dos valores encodados.
*   `df_limpo['Nivel de ensino (labels)'] = df_limpo['formacao_academica_encoded'].map(nivel_ensino_map_inv)`: Adiciona uma coluna com os rótulos textuais ao DataFrame.
*   `plt.figure(...)`: Cria a figura.
*   `sns.barplot(...)`: Cria um gráfico de barras mostrando a proporção de "salário alto" para cada nível de ensino.
    *   `estimator=lambda ...`: Calcula a porcentagem de `salario_alto == 1` para cada grupo.
    *   `order=list(nivel_ensino_map.keys())`: Garante que as barras sejam plotadas na ordem definida pelo `nivel_ensino_map`.
*   `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)`: Define título e rótulos.
*   `plt.xticks(rotation=45, ha='right')`: Rotaciona os rótulos do eixo x para melhor legibilidade.
*   `plt.tight_layout()`: Ajusta o layout.
*   `plt.savefig(...)`, `# plt.show()`, `plt.close()`: Como antes.

5.7. Análise: Tempo de Experiência vs. Proporção de Salário Alto

experiencia_map_inv = {v: k for k, v in experiencia_map.items()}

    Lógica para obter rótulos ordenados e únicos para o gráfico, lidando com valores encodados duplicados
    ordered_experiencia_labels = sorted(experiencia_map, key=experiencia_map.get)
    unique_ordered_experiencia_labels = []
    seen_values = set()
    for label in ordered_experiencia_labels:
    encoded_val = experiencia_map[label]
    if encoded_val not in seen_values:
    # Encontra o primeiro rótulo original para este valor encodado (para garantir consistência se múltiplos rótulos mapeiam para o mesmo valor)
    original_label_for_unique_value = next(k for k,v in experiencia_map.items() if v == encoded_val and k in ordered_experiencia_labels)
    if original_label_for_unique_value not in unique_ordered_experiencia_labels:
    unique_ordered_experiencia_labels.append(original_label_for_unique_value)
    seen_values.add(encoded_val)
    
    df_limpo['Experiencia (labels)'] = df_limpo['experiencia_profissional_encoded'].map(experiencia_map_inv)

Filtra os rótulos ordenados para incluir apenas aqueles presentes nos dados

    valid_experiencia_labels_in_df = df_limpo['Experiencia (labels)'].dropna().unique()
    final_ordered_experiencia_labels = [lbl for lbl in unique_ordered_experiencia_labels if lbl in valid_experiencia_labels_in_df]
    
    plt.figure(figsize=(12, 7))
    sns.barplot(
    x='Experiencia (labels)',
    y='salario_alto',
    data=df_limpo,
    estimator=lambda x: sum(x==1)*100.0/len(x) if len(x) > 0 else 0.0,
    palette='coolwarm',
    order=final_ordered_experiencia_labels
    )
    plt.title('Proporção de Profissionais com Salário Alto por Tempo de Experiência')
    plt.xlabel('Tempo de Experiência na Área de Dados')
    plt.ylabel('Proporção de Salário Alto (%)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'experiencia_vs_salario_alto.png'), bbox_inches='tight')
    
    plt.show()
    plt.close()


*   `# 5.7. Análise: Tempo de Experiência ...`: Comentário do gráfico.
*   `experiencia_map_inv = {v: k for k, v in experiencia_map.items()}`: Cria o mapa reverso para experiência.
*   O bloco de código de `ordered_experiencia_labels` até `final_ordered_experiencia_labels` é uma lógica cuidadosa para criar uma lista ordenada de rótulos de experiência para o gráfico, especialmente para lidar com o fato de que 'de 4 a 6 anos' e 'de 5 a 6 anos' foram mapeados para o mesmo valor numérico. O objetivo é ter uma ordem consistente e representativa no gráfico.
*   `df_limpo['Experiencia (labels)'] = df_limpo['experiencia_profissional_encoded'].map(experiencia_map_inv)`: Adiciona a coluna com rótulos textuais de experiência.
*   `plt.figure(...)`: Cria a figura.
*   `sns.barplot(...)`: Cria um gráfico de barras mostrando a proporção de "salário alto" para cada faixa de tempo de experiência.
    *   `order=final_ordered_experiencia_labels`: Usa a lista de rótulos ordenada e filtrada para definir a ordem das barras.
*   `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)`, `plt.xticks(...)`, `plt.tight_layout()`: Como no gráfico anterior.
*   `plt.savefig(...)`, `# plt.show()`, `plt.close()`: Como antes.

        print(f"\nTodos os gráficos foram salvos no diretório: {output_dir}")


*   `print(...)`: Mensagem final confirmando que todos os gráficos foram salvos e indicando o diretório de saída.

