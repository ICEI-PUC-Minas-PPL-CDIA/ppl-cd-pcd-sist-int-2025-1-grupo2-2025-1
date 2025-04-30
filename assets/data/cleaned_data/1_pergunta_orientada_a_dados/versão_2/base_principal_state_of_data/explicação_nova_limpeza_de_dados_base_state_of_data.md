## Explicação da Limpeza de Dados - State_of_data_BR_2023_cleaned_v2.csv

Este documento detalha os passos de limpeza aplicados ao dataset original `State_of_data_BR_2023_Kaggle-df_survey_2023.csv` para gerar o arquivo final `State_of_data_BR_2023_cleaned_v2.csv`. O objetivo foi refinar a base de dados, focando em colunas específicas e removendo dados inconsistentes ou extremos.

### 1. Carregamento dos Dados Originais (Implícito)

*   **Ação:** O processo iniciou carregando o dataset completo `State_of_data_BR_2023_Kaggle-df_survey_2023.csv` em um DataFrame pandas.

### 2. Seleção de Colunas Relevantes

*   **Ação:** Foi definida uma lista específica de 39 colunas consideradas importantes para a análise (incluindo dados demográficos, formação, cargo, salário, experiência, linguagens de programação e critérios de escolha de trabalho). Todas as outras colunas do dataset original foram descartadas.
*   **Resultado:** O DataFrame foi filtrado para conter **apenas** as colunas especificadas. Isso reduziu significativamente a dimensionalidade do dataset, focando nas informações essenciais definidas como relevantes.
*   **Colunas Mantidas:** As colunas presentes no arquivo `State_of_data_BR_2023_cleaned_v2.csv` são exatamente aquelas que foram selecionadas nesta etapa.

### 3. Remoção de Linhas com Dados Ausentes (NaN)

*   **Ação:** O código verificou **todas as colunas selecionadas** (as 39 mantidas) em busca de valores ausentes (representados como `NaN`, Nulo, ou Vazio).
*   **Regra:** Qualquer linha (representando um respondente da pesquisa) que contivesse **pelo menos um** valor ausente em **qualquer uma** das 39 colunas mantidas foi completamente removida do dataset.
*   **Objetivo:** Garantir que todas as linhas restantes no dataset tivessem informações completas para todas as variáveis selecionadas, aumentando a consistência e a usabilidade para análises subsequentes que exigem dados completos.

### 4. Tratamento de Outliers na Coluna de Faixa Salarial (`('P2_h ', 'Faixa salarial')`)

Este foi um processo multi-etapas, pois a coluna de salário continha texto (faixas) e precisava ser tratada numericamente para identificar outliers:

*   **4.1. Conversão para Valor Numérico:**
    *   **Desafio:** A coluna `('P2_h ', 'Faixa salarial')` continha strings como "de R$ 8.001/mês a R$ 12.000/mês" ou "Acima de R$ 40.001/mês". Métodos de detecção de outliers como o IQR exigem valores numéricos.
    *   **Ação:** Uma função específica foi aplicada para interpretar cada string de faixa salarial e convertê-la em um único valor numérico representativo. A lógica principal foi calcular o **ponto médio** da faixa.
        *   *Exemplo:* "de R$ 8.001/mês a R$ 12.000/mês" foi convertido para `(8001 + 12000) / 2 = 10000.5`.
        *   Casos como "Acima de X" foram tratados com uma estimativa (ex: `X * 1.1`).
        *   Casos como "Até X" usaram o valor limite `X`.
    *   **Resultado:** Uma coluna numérica temporária (chamada `salario_numerico` no código) foi criada contendo esses valores médios ou estimados.

*   **4.2. Remoção de Falhas na Conversão:**
    *   **Ação:** Se alguma string de faixa salarial não pôde ser convertida para um número válido pela função (devido a formato inesperado ou texto não previsto), ela resultou em um valor `NaN` na coluna numérica temporária. As linhas contendo esses `NaN`s foram removidas, pois não poderiam ser usadas na análise de outliers.

*   **4.3. Aplicação do Método IQR (Intervalo Interquartil):**
    *   **Ação:** O método IQR foi aplicado sobre a coluna **numérica temporária** de salários (`salario_numerico`).
        *   Calculou-se o 1º Quartil (`Q1` - valor abaixo do qual 25% dos salários numéricos se encontram).
        *   Calculou-se o 3º Quartil (`Q3` - valor abaixo do qual 75% dos salários numéricos se encontram).
        *   Calculou-se o Intervalo Interquartil (`IQR = Q3 - Q1`).
    *   **Definição dos Limites:** Foram definidos os limites inferior e superior para identificar outliers, usando a regra comum de 1.5 vezes o IQR:
        *   Limite Inferior = `Q1 - 1.5 * IQR`
        *   Limite Superior = `Q3 + 1.5 * IQR`

*   **4.4. Remoção dos Outliers:**
    *   **Ação:** Todas as linhas cujo valor na coluna **numérica temporária** de salário (`salario_numerico`) estivesse **abaixo** do Limite Inferior ou **acima** do Limite Superior foram consideradas outliers e removidas do dataset.
    *   **Objetivo:** Remover respondentes cujas faixas salariais (representadas pelo ponto médio) eram estatisticamente muito discrepantes em relação à maioria dos dados. Isso ajuda a evitar que valores extremos distorçam médias, medianas ou outros resultados de análises agregadas.

*   **4.5. Remoção da Coluna Temporária:**
    *   **Ação:** Após a remoção dos outliers com base nos valores numéricos, a coluna numérica temporária (`salario_numerico`) foi descartada do DataFrame.
    *   **Resultado:** O DataFrame final manteve a coluna original `('P2_h ', 'Faixa salarial')` com as strings das faixas, mas apenas para as linhas cujos pontos médios salariais não foram considerados outliers pelo método IQR.

### 5. Salvamento do Arquivo Final

*   **Ação:** O DataFrame resultante, agora contendo apenas as 39 colunas selecionadas, sem valores ausentes (`NaN`) nessas colunas, e com os outliers de faixa salarial (conforme critério IQR no ponto médio) removidos, foi salvo como o novo arquivo CSV: `State_of_data_BR_2023_cleaned_v2.csv`.

### Conclusão

O arquivo `State_of_data_BR_2023_cleaned_v2.csv` representa uma versão mais focada e robusta do dataset original, pronta para análises mais consistentes. Ele contém um subconjunto específico de colunas, garante a completude dos dados nessas colunas para todas as linhas restantes e removeu respondentes com faixas salariais consideradas estatisticamente extremas.

## 4. Tratando Outliers na Faixa Salarial
Coluna alvo: '('P2_h ', 'Faixa salarial')'
Convertendo faixas salariais para valores numéricos (ponto médio)...

### Boxplot do Salário Numérico (Ponto Médio) ANTES da remoção de outliers:

![image](https://github.com/user-attachments/assets/33ae092d-03a4-4e85-89a5-e0d72eb3c7fd)

Detalhes do cálculo do IQR para Salário Numérico:
  Q1: 5000.50
  Q3: 10000.50
  IQR: 5000.00
  Limite Inferior (Q1 - 1.5*IQR): -2499.50
  Limite Superior (Q3 + 1.5*IQR): 17500.50

Foram removidas 308 linhas identificadas como outliers salariais.
Shape após tratamento de outliers salariais: (3323, 40)
Coluna 'salario_numerico' temporária removida.

### Boxplot do Salário Numérico (Ponto Médio) APÓS a remoção de outliers:
![image](https://github.com/user-attachments/assets/8925d992-2579-4987-b9bd-827b2cbe873a)


## 5. Limpeza de Dados Concluída
Shape inicial original: (5293, 399)
Shape final do dataset limpo: (3323, 39)
Total de linhas removidas: 1970
