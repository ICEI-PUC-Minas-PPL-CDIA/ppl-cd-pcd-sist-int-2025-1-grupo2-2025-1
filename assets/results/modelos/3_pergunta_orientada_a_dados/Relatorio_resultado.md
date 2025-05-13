# Relatório de Resultados e Insights: Classificação Binária de Faixa Salarial (v7)

Este relatório detalha os resultados da última execução do modelo LightGBM para classificação binária da faixa salarial ("Salário Alto" vs. "Salário Baixo"). A análise inclui métricas de desempenho, a importância das features e uma interpretação dos gráficos gerados para extrair insights.

* **Pergunta orientada a dados: Como fatores como formalidade no emprego e características demográficas (gênero e raça) interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?**

## 1. Resumo do Desempenho do Modelo

O modelo final demonstrou um desempenho robusto na classificação das faixas salariais.

* **Tipo de Classificação**: Binário
* **Classes da Variável Alvo (codificadas)**: `['Salário Alto', 'Salário Baixo']` (onde "Salário Alto" é a classe 0 e "Salário Baixo" é a classe 1 após LabelEncoding)
* **Acurácia Média no CV/Val do Optuna**: 0.8505
* **Acurácia do Modelo Final no Conjunto de Treinamento (`X_train_final`)**: 0.8583
* **Número de Árvores no Modelo Final (após early stopping)**: 105

### 1.1. Resultados da Avaliação no Conjunto de Teste

| Métrica                          | Valor  |
| :------------------------------- | :----- |
| **Acurácia no Teste** | 0.8335 |
| Precisão Média (Macro Avg)       | 0.8331 |
| Precisão Média (Weighted Avg)    | 0.8335 |
| F1-Score (Ponderado)             | 0.8335 |
| **ROC AUC (Binário)** | 0.9234 |

**Interpretação das Métricas de Teste:**
* A **Acurácia de 0.8335** indica que o modelo classificou corretamente aproximadamente 83.35% das instâncias no conjunto de teste.
* O **ROC AUC de 0.9234** é um excelente indicador da capacidade do modelo de distinguir entre as classes "Salário Alto" e "Salário Baixo". Um valor próximo de 1 sugere uma alta performance na separação das classes.
* As precisões médias e o F1-Score ponderado, todos em torno de 0.83, mostram um bom equilíbrio geral entre precisão e recall.

### 1.2. Relatório de Classificação Detalhado (Conjunto de Teste)

| Classe        | Precision | Recall | F1-score | Support |
| :------------ | :-------- | :----- | :------- | :------ |
| Salário Alto  | 0.84      | 0.84   | 0.84     | 622     |
| Salário Baixo | 0.83      | 0.83   | 0.83     | 567     |
|               |           |        |          |         |
| accuracy      |           |        | 0.83     | 1189    |
| macro avg     | 0.83      | 0.83   | 0.83     | 1189    |
| weighted avg  | 0.83      | 0.83   | 0.83     | 1189    |

**Interpretação do Relatório de Classificação:**
* **Suporte (Support)**: Indica o número de amostras reais para cada classe no conjunto de teste. "Salário Alto" teve 622 instâncias e "Salário Baixo" teve 567. A distribuição está bem equilibrada, com uma diferença de apenas 55 amostras, o que é ótimo para a confiabilidade do modelo.
* **Precisão (Precision)**:
    * Para "Salário Alto" (0.84): De todas as vezes que o modelo previu "Salário Alto", ele estava correto em 84% dos casos.
    * Para "Salário Baixo" (0.83): De todas as vezes que o modelo previu "Salário Baixo", ele estava correto em 83% dos casos.
* **Recall (Revocação)**:
    * Para "Salário Alto" (0.84): O modelo identificou corretamente 84% de todos os verdadeiros "Salário Alto".
    * Para "Salário Baixo" (0.83): O modelo identificou corretamente 83% de todos os verdadeiros "Salário Baixo".
* **F1-score**: É a média harmônica da precisão e do recall. Valores de 0.84 e 0.83 para as classes indicam um bom equilíbrio entre essas duas métricas para cada classe.
* **Macro Avg vs Weighted Avg**: Como as classes estão bem equilibradas, as médias macro (calcula a métrica independentemente para cada classe e depois tira a média) e ponderada (leva em conta o suporte de cada classe) são muito próximas, o que é um bom sinal.
