## Explicação do Código: Notebook de Modelo GBM com Árvore e Interpretação

Este notebook implementa um pipeline completo de ciência de dados para análise de disparidade salarial, utilizando o algoritmo Gradient Boosting Machine (GBM) com LightGBM, incluindo visualização de árvore individual e interpretação com SHAP [1]. A seguir, está a explicação detalhada das principais etapas do código, organizada por blocos e funções.

---

### **1. Configuração do Ambiente e Upload dos Dados**

-   **Importação de Bibliotecas**: Importa pacotes essenciais para manipulação de dados (`pandas`, `numpy`), visualização (`matplotlib`, `seaborn`, `graphviz`), pré-processamento (`sklearn`), modelagem (`lightgbm`), interpretação (`shap`) e manipulação de arquivos no Colab [1].
-   **Upload de Arquivos**: Utiliza `google.colab.files.upload()` para solicitar ao usuário o upload dos arquivos de dados (`survey_cleaned.csv` e, opcionalmente, um arquivo de microdados) [1].
-   **Leitura dos Dados**: Os arquivos são lidos diretamente da memória (`io.BytesIO`) e carregados em DataFrames do pandas (`pd.read_csv`) [1].
-   **Limpeza dos Nomes das Colunas**: Uma função `clean_col_names` padroniza e limpa os nomes das colunas, removendo caracteres especiais, espaços e tratando possíveis duplicatas, facilitando o uso posterior [1].

---

### **2. Seleção de Features Relevantes**

-   **Definição de Variáveis**: Define a coluna alvo (`target_column`) e uma lista de colunas de interesse (`feature_columns`) que serão usadas como preditoras [1].
-   **Verificação das Colunas**: Confere se todas as colunas selecionadas existem no DataFrame e alerta caso alguma esteja ausente [1].
-   **Criação do DataFrame do Modelo**: Seleciona apenas as colunas relevantes (`existing_feature_columns` e `target_column`) para análise, criando `df_model` [1].

---

### **3. Pré-processamento dos Dados**

-   **Tratamento da Variável Alvo (Salário)**: Função `get_salary_midpoint` transforma faixas salariais (texto) em valores numéricos, usando o ponto médio de cada faixa ou tratando valores específicos como "Menos de R$ 1.000" [1].
-   **Identificação e Tratamento de Nulos**:
    -   Para variáveis numéricas: preenche valores nulos (`NaN`) com a mediana ou zero, dependendo da coluna [1].
    -   Para variáveis categóricas: preenche nulos com a string 'Desconhecido' e converte a coluna para o tipo `category` do pandas [1].
-   **Codificação de Variáveis Categóricas**: Utiliza `OrdinalEncoder` da biblioteca `sklearn.preprocessing` para transformar variáveis categóricas nominais em valores numéricos ordinais, o que é adequado para modelos baseados em árvores como o LightGBM [1].

---

### **4. Split dos Dados (Treino/Teste)**

-   **Divisão dos Dados**: Usa `train_test_split` da `sklearn.model_selection` para separar os dados (`X`, `y`) em conjuntos de treino e teste, usando uma proporção definida (`test_size`) e uma semente aleatória (`random_state`) para reprodutibilidade [1].

---

### **5. Treinamento do Modelo LightGBM (GBM)**

-   **Configuração do Dataset**: Cria objetos `lgb.Dataset` específicos para o LightGBM, contendo os dados de treino e validação (teste), e especificando quais colunas são categóricas [1].
-   **Parâmetros do Modelo**: Define um dicionário `params` com hiperparâmetros para o LightGBM, como:
    -   `objective`: 'regression_l1' (MAE - Mean Absolute Error)
    -   `metric`: 'l1' (MAE)
    -   `n_estimators`: Número máximo de árvores (boosting rounds).
    -   `learning_rate`: Taxa de aprendizado.
    -   `feature_fraction`, `bagging_fraction`, `bagging_freq`: Parâmetros de regularização para evitar overfitting.
    -   `verbose`: Nível de log.
    -   `n_jobs`: Número de threads.
    -   `seed`: Semente aleatória.
    -   `boosting_type`: 'gbdt' (Gradient Boosting Decision Tree) [1].
-   **Treinamento**: Executa o treinamento do modelo (`lgb.train`) usando os dados de treino, validando no conjunto de teste (`valid_sets`), e utilizando `early_stopping_rounds` para parar o treinamento se a métrica de validação não melhorar por um número definido de rodadas [1].
-   **Avaliação**: Após o treino, faz predições (`bst.predict`) no conjunto de teste e calcula as métricas de desempenho: MAE, RMSE (Root Mean Squared Error) e R² (R-squared) usando funções da `sklearn.metrics` [1].

---

### **6. Interpretação e Visualização do Modelo**

#### **6.1 Importância das Features**

-   **Plot de Importância**: Utiliza `lgb.plot_importance(bst, importance_type='gain', ...)` para exibir um gráfico de barras mostrando a importância das variáveis para o modelo, baseado no ganho total (redução de impureza) que cada feature proporciona ao longo de todas as árvores [1].

#### **6.2 Visualização da Árvore Individual**

-   **Plot com `lgb.plot_tree`**: Mostra uma visualização textual básica de uma árvore específica (ex: árvore 0) do ensemble [1].
-   **Plot com `graphviz`**: Gera uma visualização gráfica mais elaborada da mesma árvore usando `lgb.create_tree_digraph` e a biblioteca `graphviz`. Isso permite ver as divisões (splits), os valores nos nós e as folhas [1].
    -   *Nota*: O código também inclui comentários para usar a biblioteca `dtreeviz`, que oferece visualizações ainda mais ricas, mas está comentado [1].

#### **6.3 Interpretação SHAP**

-   **Cálculo dos Valores SHAP**: Utiliza `shap.TreeExplainer(bst)` para criar um explicador e depois `.shap_values(X_test)` para calcular os valores SHAP para o conjunto de teste. SHAP (SHapley Additive exPlanations) atribui a cada feature um valor de importância para cada predição individual [1].
-   **Plots SHAP**:
    -   **Resumo (dot/beeswarm)**: `shap.summary_plot(shap_values, X_test, plot_type='dot')` mostra a distribuição dos impactos de cada feature nas predições. Pontos à direita indicam contribuição positiva para a predição (maior salário), pontos à esquerda indicam contribuição negativa. A cor geralmente representa o valor original da feature (alto/baixo) [1].
    -   **Resumo (bar)**: `shap.summary_plot(shap_values, X_test, plot_type='bar')` mostra a importância média absoluta de cada feature [1].
    -   **Dependence Plots**: `shap.dependence_plot(feature, shap_values, X_test, interaction_index=interaction_feature)` visualiza como o valor SHAP de uma *feature* específica muda conforme o valor da própria *feature* muda. O `interaction_index` permite colorir os pontos por outra *feature* para observar interações [1].
-   **Tratamento de Erros**: O código inclui blocos `try...except` para os *dependence plots*, pois podem ocorrer erros (como o `KeyError: 'final_order'` visto nos outputs do notebook), imprimindo uma mensagem caso o plot falhe para uma feature específica [1].

---

### **7. Encerramento**

-   **Mensagem Final**: Imprime "--- Fim da Análise ---" para indicar a conclusão da execução do notebook [1].

---

## **Resumo do Fluxo**

1.  **Setup**: Importar bibliotecas.
2.  **Load**: Fazer upload e ler os arquivos CSV.
3.  **Clean**: Limpar nomes das colunas.
4.  **Select**: Escolher colunas alvo e features.
5.  **Preprocess**: Tratar salário, nulos e codificar categóricas.
6.  **Split**: Dividir dados em treino/teste.
7.  **Train**: Treinar modelo LightGBM com early stopping.
8.  **Evaluate**: Calcular MAE, RMSE, R².
9.  **Interpret**:
    -   Plotar importância das features (LGBM gain).
    -   Visualizar uma árvore individual (LGBM plot, Graphviz).
    -   Calcular e plotar valores SHAP (summary dot/bar, dependence plots).
10. **End**: Concluir a análise.
