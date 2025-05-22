# Indução de modelos

# Modelo 4: Rede Neural com Embeddings e Otimização via Ray Tune (RNA v2)

## 1. Justificativa e Objetivo

O objetivo deste modelo é classificar a faixa salarial de indivíduos em duas categorias: "Salário Baixo" e "Salário Alto", utilizando uma abordagem de rede neural artificial (RNA)[cite: 2]. A intenção é explorar se uma arquitetura de RNA, com capacidade de aprender interações complexas e representações ricas para features categóricas (via embeddings), pode oferecer um desempenho comparável ou superior aos modelos baseados em árvores (como o LightGBM anteriormente explorado) para a mesma pergunta orientada a dados[cite: 1].

A classificação binária ("Salário Baixo" vs. "Salário Alto") visa simplificar o problema e potencialmente melhorar a distinção entre os grupos salariais[cite: 3]. O modelo busca um equilíbrio na distribuição das amostras entre as classes definidas por um ponto de corte específico[cite: 3]. Na última execução do modelo de referência (LightGBM), um ponto de corte fixo de R$ 7.500,00 foi utilizado para a variável `salary_numeric_lower_bound` para realizar essa divisão[cite: 4, 41]. Este mesmo ponto de corte é mantido para a RNA.

## 2. Processo de Amostragem de Dados (Particionamento e Validação Interna para HPO e Treino Final)

O processo de amostragem e validação do modelo de rede neural é crucial para garantir sua generalização e evitar overfitting[cite: 5].

### 2.1. Particionamento Inicial (Treino HPO e Teste Final)

* **Método**: `train_test_split` da biblioteca `sklearn.model_selection`[cite: 6].
* **Divisão**: O conjunto de dados processado (`X_initial_nn`, `y_full_nn` - que já passou por limpeza, tratamento de outliers e mapeamento de features) é dividido em:
    * Conjunto de Treinamento para HPO e posterior treino final (`X_train_nn_full`, `y_train_nn_full`): 75% dos dados[cite: 7].
    * Conjunto de Teste Final (`X_test_nn_full`, `y_test_nn_full`): 25% dos dados[cite: 8].
* **Parâmetros Utilizados**:
    * `test_size=0.25`: Reserva 25% dos dados para o conjunto de teste final[cite: 9].
    * `random_state=42`: Garante a reprodutibilidade da divisão[cite: 10].
    * `stratify=y_full_nn`: Realiza uma divisão estratificada, mantendo a proporção das classes da variável alvo em ambas as partições[cite: 11].

### 2.2. Particionamento Interno para Otimização de Hiperparâmetros com Ray Tune (Keras)

* **Método**: `train_test_split` para criar um conjunto de validação interna a partir do `X_train_nn_full`.
* **Divisão**: O `X_train_nn_full` (75% do total) é novamente dividido:
    * Conjunto de Treinamento Interno para HPO (`X_train_hpo_nn_list_for_tune`, `y_train_hpo_nn_arr_for_tune`): 80% de `X_train_nn_full`.
    * Conjunto de Validação Interno para HPO (`X_val_hpo_nn_list_for_tune`, `y_val_hpo_nn_arr_for_tune`): 20% de `X_train_nn_full`.
* **Objetivo**: Este conjunto de validação interno é usado por cada *trial* do Ray Tune para avaliar o desempenho do modelo Keras com uma dada combinação de hiperparâmetros. O callback `EarlyStopping` do Keras monitora a `val_accuracy` neste conjunto, e o `ReportCheckpointCallback` reporta essa métrica ao Ray Tune.

### 2.3. Particionamento Interno para Early Stopping no Treinamento Final da RNA

* **Método**: `train_test_split` para criar um conjunto de validação interna a partir do `X_train_nn_full` (que corresponde a `X_train_nn_inputs_final_list` e `y_train_nn_final_arr` no código da RNA v2).
* **Divisão**: O conjunto `X_train_nn_full` (75% do total) é dividido novamente para o treinamento do *modelo final* com os melhores hiperparâmetros:
    * Conjunto de Treinamento Final Efetivo (`X_final_train_list`, `y_final_train_arr`): 85% de `X_train_nn_full`.
    * Conjunto de Validação para Early Stopping Final (`X_final_val_list`, `y_final_val_arr`): 15% de `X_train_nn_full`.
* **Objetivo**: Este conjunto de validação é usado para o `EarlyStopping` do Keras durante o treinamento do modelo RNA final com os melhores hiperparâmetros encontrados pelo Ray Tune, ajudando a evitar overfitting no conjunto de treinamento final[cite: 31, 32].

### Justificativa das Escolhas de Amostragem:

* **Divisão Treino/Teste Principal**: Essencial para avaliar o desempenho final do modelo em dados completamente não vistos durante o treinamento ou HPO[cite: 33]. A proporção 75/25 é comum[cite: 34].
* **Estratificação**: Crucial para problemas de classificação binária para garantir que as proporções das classes sejam mantidas nas divisões, levando a estimativas de desempenho e HPO mais confiáveis[cite: 34].
* **Conjunto de Validação Interna para HPO**: Permite que o Ray Tune avalie cada combinação de hiperparâmetros de forma justa, usando um subconjunto dos dados de treino para validação, com `EarlyStopping` para otimizar o tempo de cada trial.
* **Conjunto de Validação Interna para Treinamento Final**: Permite que o modelo final pare de treinar no momento ótimo, evitando o overfitting aos dados de treinamento final[cite: 37].

---
## 3. Parâmetros Utilizados (Principais)

### 3.1. Criação da Variável Alvo (`target_col_agrupada_name`)

* **`salary_group_labels = ["Salário Baixo", "Salário Alto"]`**: Define os nomes das duas categorias da variável alvo[cite: 38].
* **`point_of_cut_fixed = 7500.0`**: Valor monetário usado para dividir `salary_numeric_lower_bound`[cite: 39]. Salários `<= 7500.0` são "Salário Baixo", e `> 7500.0` são "Salário Alto"[cite: 40]. Este ponto de corte produziu um suporte de 2268 para "Salário Baixo" e 2485 para "Salário Alto" no dataset processado.
* A coluna alvo é codificada numericamente usando `LabelEncoder` (ex: "Salário Alto" -> 0, "Salário Baixo" -> 1).

### 3.2. Features Preditivas Utilizadas e Pré-processamento para RNA

Para o modelo de Rede Neural v2, utilizou-se diretamente o conjunto de 7 features iniciais relevantes, sem a etapa de RFECV baseada em LightGBM, para permitir que a RNA aprendesse as relações e a importância das features diretamente. As features são:

| Atributo                      | Código de Referência Original | Tipo         | Subtipo              | Descrição                                                      |
| :---------------------------- | :---------------------------- | :----------- | :------------------- | :------------------------------------------------------------- |
| Faixa etária                  | P1_a_1                        | Qualitativo  | Ordinal (tratada como cat.) | Faixa etária do respondente                                    |
| Gênero                        | P1_b                          | Qualitativo  | Nominal (tratada como cat.) | Identidade de gênero do respondente                            |
| Nível de ensino alcançado     | P1_l                          | Qualitativo  | Ordinal (tratada como cat.) | Nível de ensino do respondente (graduação, mestrado, etc.) |
| Tempo de experiência na área de dados | P2_i                       | Quantitativo | Discreto             | Tempo de experiência do respondente na área de dados (em anos) |
| Nível de senioridade          | P2_g                          | Qualitativo  | Ordinal (tratada como cat.) | Nível de senioridade do respondente (Júnior, Pleno, Sênior) |
| Cargo atual                   | P2_f                          | Qualitativo  | Nominal (tratada como cat.) | Cargo atual ocupado pelo respondente                           |
| Região Mapeada                | Derivada de P1_i_1            | Qualitativo  | Nominal (tratada como cat.) | Região do Brasil onde o respondente reside                     |

**Pré-processamento para RNA:**
* **Features Numéricas (`P2_i` - experiência):**
    * Valores ausentes imputados com a mediana.
    * Outliers identificados usando 1.5\*IQR e as linhas contendo outliers são removidas do conjunto de dados antes do split principal.
    * Escalonadas usando `StandardScaler`.
* **Features Categóricas (todas as outras listadas acima):**
    * Valores ausentes preenchidos com a string "Missing\_Val\_Cat\_NN".
    * Codificadas usando `LabelEncoder` individualmente para cada feature.
    * Para o conjunto de teste, categorias não vistas durante o ajuste do `LabelEncoder` (no treino) são mapeadas para um novo índice numérico (índice "UNK" - desconhecido).
    * Utilizadas como entrada para camadas de `Embedding` na rede neural. A `input_dim` de cada camada de Embedding é a cardinalidade da feature + 1 (para o índice UNK).

### 3.3. Arquitetura da Rede Neural (Keras - `create_keras_model_v2`)

* **Múltiplos Inputs:** Um input para cada feature categórica (para as camadas de Embedding) e um input para todas as features numéricas concatenadas.
* **Camadas de Embedding:** Para cada feature categórica, uma camada `Embedding` transforma o índice numérico em um vetor denso. A dimensão de saída de cada embedding (`output_dim`) é um hiperparâmetro otimizado pelo Ray Tune. Regularização L2 é aplicada às embeddings.
* **Concatenação:** Os outputs achatados (`Flatten`) de todas as camadas de Embedding são concatenados com as features numéricas (já escalonadas).
* **Camadas Densas (MLP):**
    * A primeira camada densa possui um número de unidades e regularização L2 otimizados via Ray Tune, seguida por `BatchNormalization`, ativação `ReLU` e `Dropout`.
    * O modelo pode ter uma segunda camada densa opcional (controlada pelo hiperparâmetro `num_hidden_layers`), também com unidades, L2, `BatchNormalization`, `ReLU` e `Dropout` otimizados.
* **Camada de Saída:** Uma camada `Dense` com 1 neurônio e ativação `sigmoid` para classificação binária.
* **Compilação:**
    * Otimizador: O tipo de otimizador (Adam, Nadam, AdamW) e a taxa de aprendizado são hiperparâmetros.
    * Função de Perda: `binary_crossentropy`.
    * Métricas: `accuracy`.

### 3.4. Otimização de Hiperparâmetros com Ray Tune (Keras)

* **`n_ray_tune_samples_nn`**: Número de combinações de hiperparâmetros a serem testadas (ex: 75 na última execução).
* **`ray_tune_timeout_nn`**: Tempo máximo para a otimização (ex: 5400 segundos).
* **`objective_ray_tune_keras_v2`**: Função que treina e avalia um modelo Keras para uma dada configuração de hiperparâmetros, utilizando um split de validação interno e `EarlyStopping`. Reporta `val_accuracy` (como `val_accuracy_tune`) para o Ray Tune.
* **`TuneReportCallback`**: Utilizado para reportar métricas do Keras para o Ray Tune durante o treinamento de cada trial.
* **`ASHAScheduler`**: Utilizado para interromper trials menos promissores mais cedo. Configurado com `metric='val_accuracy_tune'` e `mode='max'`.
* **`HyperOptSearch`**: Utilizado como algoritmo de busca para encontrar os melhores hiperparâmetros, também configurado com `metric='val_accuracy_tune'` e `mode='max'`.
* **Espaço de Busca dos Hiperparâmetros (otimizados pelo Ray Tune):**
    * `dense_units_1`, `dense_units_2` (unidades nas camadas densas)
    * `dropout_1`, `dropout_2` (taxas de dropout)
    * `learning_rate_nn` (taxa de aprendizado)
    * `batch_size`
    * `epochs` (número máximo de épocas, controlado por EarlyStopping)
    * `num_hidden_layers` (1 ou 2 camadas densas ocultas)
    * `early_stopping_patience`
    * `l2_strength_embedding`, `l2_strength_dense` (força da regularização L2)
    * `optimizer` (tipo de otimizador: adam, nadam, adamw)
    * `weight_decay` (para AdamW)
    * `reduce_lr_patience`, `reduce_lr_factor` (para o callback `ReduceLROnPlateau`)
    * `emb_dim_{feature_name}` (dimensão de saída para cada camada de Embedding)
* **Melhores Hiperparâmetros Encontrados (exemplo da última execução):**
    * `dense_units_1`: 64, `dense_units_2`: 128 (mas `num_hidden_layers`: 1, então `dense_units_2` não foi usada)
    * `learning_rate_nn`: 0.000236...
    * `batch_size`: 32
    * `num_hidden_layers`: 1
    * Outros parâmetros específicos para dropout, L2, e dimensões de embedding também foram definidos.

### 3.5. Treinamento do Modelo Final (RNA v2)

* Utiliza os melhores hiperparâmetros encontrados pelo Ray Tune.
* O modelo Keras é treinado no conjunto de treino HPO completo (`X_train_nn_full`, que corresponde a 75% dos dados após tratamento de outliers), com um novo split de validação (15% de `X_train_nn_full`) para `EarlyStopping` (com paciência aumentada e `ReduceLROnPlateau`).
* O número de épocas efetivas é determinado pelo `EarlyStopping`. Na última execução, o modelo final parou na época 40 (restaurando pesos da época 20).

## 4. Resultados da Avaliação (RNA v2 - Exemplo da Última Execução)

A avaliação foi realizada no conjunto de teste (25% dos dados).

* **Melhor Acurácia na Validação (HPO da RNA):** 0.8345
* **Acurácia no Teste:** 0.8377
* **F1-Score (Ponderado) no Teste:** 0.8377
* **ROC AUC no Teste:** 0.9263
* **Relatório de Classificação (Teste):**
    * Salário Alto: precision 0.85, recall 0.84, f1-score 0.84
    * Salário Baixo: precision 0.83, recall 0.84, f1-score 0.83

## 5. Explicação do Código (Fluxo Principal para RNA v2)

### Pergunta orientada a dados: Como fatores como formalidade no emprego, características demográficas e regionais se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?

O fluxo de execução do código para o modelo de Rede Neural (RNA v2) é:

1.  **Carregamento e Preparação Inicial dos Dados**:
    * Leitura do arquivo Excel.
    * Limpeza dos nomes das colunas.
    * Mapeamento de colunas importantes para nomes padronizados.
2.  **Engenharia da Variável Alvo**:
    * Extração do `salary_numeric_lower_bound`.
    * Divisão em "Salário Baixo" e "Salário Alto" usando o ponto de corte fixo de R$ 7.500,00.
    * Codificação da variável alvo com `LabelEncoder`.
3.  **Preparação das Features Iniciais para RNA**:
    * Seleção das 7 features relevantes (faixa etária, gênero, UF transformado em Região, ensino, cargo, senioridade, experiência).
    * Tratamento de valores ausentes e outliers nas features numéricas (experiência).
4.  **Divisão Treino-Teste Principal**:
    * Os dados processados (`X_initial_nn`, `y_full_nn`) são divididos em 75% para treino/HPO (`X_train_nn_full`) e 25% para teste final (`X_test_nn_full`).
5.  **Pré-processamento Específico para RNA (em `X_train_nn_full` e `X_test_nn_full`):**
    * Features numéricas são escalonadas com `StandardScaler`.
    * Features categóricas são tratadas para NaNs e codificadas com `LabelEncoder` (individualmente). Um índice UNK é reservado para categorias não vistas no teste. São coletadas informações para as camadas de `Embedding` (cardinalidade, dimensão de output).
    * Os inputs são formatados como uma lista de arrays para o modelo Keras.
6.  **Otimização de Hiperparâmetros com Ray Tune**:
    * Um subconjunto de `X_train_nn_full` é usado para criar dados de treino e validação internos para cada trial da HPO.
    * A função `objective_ray_tune_keras_v2` define como cada trial (combinação de hiperparâmetros da RNA) é treinado (com `EarlyStopping` e `ReduceLROnPlateau`) e avaliado (pela `val_accuracy`).
    * `TuneReportCallback` envia métricas para o Ray Tune.
    * `tune.run` executa a busca usando `ASHAScheduler` e `HyperOptSearch`.
7.  **Treinamento do Modelo RNA Final**:
    * O modelo Keras é instanciado com os melhores hiperparâmetros encontrados.
    * É treinado no conjunto `X_train_nn_full` (usando 85% para treino efetivo e 15% para validação do `EarlyStopping` e `ReduceLROnPlateau`).
8.  **Avaliação do Modelo RNA Final**:
    * Previsões são feitas no conjunto de teste (`X_test_nn_full`).
    * Métricas (acurácia, F1, ROC AUC, relatório de classificação, matriz de confusão) são calculadas e exibidas.
9.  **Salvamento de Resultados e Modelo**:
    * Resultados detalhados são salvos em arquivo de texto.
    * O modelo Keras treinado e os objetos de pré-processamento (scalers, encoders, informações de embedding) são salvos em arquivos (`.keras` e `.pkl`).

Este processo visa construir um modelo de rede neural otimizado e avaliado de forma robusta, fornecendo insights sobre os fatores que determinam as faixas salariais, focando na capacidade da RNA de aprender representações e interações complexas.
