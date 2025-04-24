1. Configuração do Ambiente e Upload dos Dados
Importação de Bibliotecas: O notebook importa pacotes essenciais para manipulação de dados (pandas, numpy), visualização (matplotlib, seaborn, graphviz), pré-processamento (sklearn), modelagem (lightgbm), interpretação (shap) e manipulação de arquivos no Colab.

Upload de Arquivos: Utiliza google.colab.files.upload() para solicitar ao usuário o upload dos arquivos de dados principais (survey_cleaned.csv e, opcionalmente, um arquivo de microdados).

Leitura dos Dados: Os arquivos são lidos diretamente da memória e carregados em DataFrames do pandas.

Limpeza dos Nomes das Colunas: Uma função clean_col_names padroniza e limpa os nomes das colunas, removendo caracteres especiais e espaços, facilitando o uso posterior.

2. Seleção de Features Relevantes
Definição de Variáveis: Define a coluna alvo (target_column) e uma lista de colunas de interesse (feature_columns) que serão usadas como preditoras.

Verificação das Colunas: Confere se todas as colunas selecionadas existem no DataFrame e alerta caso alguma esteja ausente.

Criação do DataFrame do Modelo: Seleciona apenas as colunas relevantes para análise.

3. Pré-processamento dos Dados
Tratamento da Variável Alvo (Salário): Função get_salary_midpoint transforma faixas salariais em valores numéricos (usando o ponto médio de cada faixa).

Identificação e Tratamento de Nulos:

Para variáveis numéricas: preenche nulos com a mediana ou zero.

Para variáveis categóricas: preenche nulos com 'Desconhecido' e converte para tipo category.

Codificação de Variáveis Categóricas: Utiliza OrdinalEncoder para transformar variáveis categóricas em valores numéricos, facilitando o uso pelo LightGBM.

4. Split dos Dados (Treino/Teste)
Divisão dos Dados: Usa train_test_split para separar os dados em conjuntos de treino e teste, garantindo validação adequada do modelo.

5. Treinamento do Modelo LightGBM (GBM)
Configuração do Dataset: Cria objetos lgb.Dataset para treino e validação.

Parâmetros do Modelo: Define parâmetros como tipo de boosting, métrica de avaliação (MAE), número de árvores, taxa de aprendizado, etc.

Treinamento: Executa o treinamento do modelo com early stopping, exibindo logs do processo.

Avaliação: Calcula as métricas no conjunto de teste: MAE, RMSE e R².

6. Interpretação e Visualização do Modelo
6.1 Importância das Features
Plot de Importância: Exibe a importância das variáveis para o modelo, baseado em ganho de informação.

6.2 Visualização da Árvore Individual
Plot da Árvore: Utiliza lgb.plot_tree e graphviz para visualizar uma árvore individual do ensemble, permitindo entender as regras de decisão aprendidas.

6.3 Interpretação SHAP
Cálculo dos Valores SHAP: Calcula os valores SHAP para interpretar o impacto de cada feature na predição individual.

Plots SHAP:

Resumo (dot/bar): Mostra a influência global das variáveis.

Dependence Plots: Visualiza como o valor SHAP de uma variável varia em relação ao seu valor, colorindo por outra variável relevante.

Tratamento de Erros: Caso ocorram erros nos plots de dependência (por exemplo, devido a incompatibilidades de versões), o notebook exibe mensagens de erro amigáveis.

7. Encerramento
Mensagens de Fim: O notebook encerra com uma mensagem indicando o fim da análise.

Resumo do Fluxo
Upload e limpeza dos dados

Seleção e tratamento das variáveis

Codificação e preparação dos dados

Divisão em treino e teste

Treinamento do modelo GBM (LightGBM)

Avaliação do desempenho

Interpretação: importância das features, visualização de árvore, e análise SHAP
