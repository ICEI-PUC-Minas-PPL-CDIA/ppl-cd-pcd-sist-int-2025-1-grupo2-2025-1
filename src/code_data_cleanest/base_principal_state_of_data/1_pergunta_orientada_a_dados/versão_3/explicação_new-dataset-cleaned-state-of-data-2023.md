### Importação de Bibliotecas

    # Importar bibliotecas necessárias
    import pandas as pd

Esta linha importa a biblioteca pandas e a apelida de pd. Pandas é uma biblioteca fundamental para manipulação e análise de dados em Python, oferecendo estruturas de dados como DataFrames

    import numpy as np

Esta linha importa a biblioteca numpy e a apelida de np. Numpy é utilizada para computação numérica em Python, fornecendo suporte para arrays e matrizes multidimensionais, além de funções matemáticas para operar nesses arrays

### 1. Carregar o Arquivo CSV

    # 1. Carregar o arquivo CSV
    df = pd.read_csv('/kaggle/input/state-of-data-brazil-2023/State_of_data_BR_2023_Kaggle - df_survey_2023.csv')

Esta linha utiliza a função read_csv da biblioteca pandas para carregar os dados de um arquivo CSV especificado pelo caminho. O conteúdo do arquivo CSV é carregado em um DataFrame pandas chamado d

### 2. Renomear Colunas

    # 2. Renomear colunas para os nomes simplificados
    colunas_renomeadas = {
     "('P0', 'id')": "id",
     "('P1_l ', 'Nivel de Ensino')": "Nível de ensino alcançado",
     "('P1_m ', 'Área de Formação')": "Área de formação acadêmica",
     "('P2_h ', 'Faixa salarial')": "Faixa salarial mensal",
     "('P2_i ', 'Quanto tempo de experiência na área de dados você tem?')": "Tempo de experiência na área de dados",
     "('P2_g ', 'Nivel')": "Nível de senioridade",
     "('P1_b ', 'Genero')": "Gênero do profissional",
     "('P1_c ', 'Cor/raca/etnia')": "Cor/Raça/Etnia",
     "('P2_b ', 'Setor')": "Setor de atuação da empresa",
     "('P1_i_1 ', 'uf onde mora')": "UF onde mora",
     "('P2_f ', 'Cargo Atual')": "Cargo atual",
     "('P2_o_6 ', 'Oportunidade de aprendizado e trabalhar com referências na área')": "Oportunidade de aprendizado",
     "('P2_o_10 ', 'Reputação que a empresa tem no mercado')": "Reputação da empresa"
    }

Esta seção define um dicionário chamado colunas_renomeadas. As chaves deste dicionário são os nomes originais das colunas no DataFrame df (que parecem ser tuplas representadas como strings), e os valores são os novos nomes, mais simplificados e descritivos, que serão atribuídos a essas colunas
    
    # Renomear colunas e selecionar apenas as desejadas
    df_clean = df.rename(columns=colunas_renomeadas)[list(colunas_renomeadas.values())]

Esta linha realiza duas operações:
    
    df.rename(columns=colunas_renomeadas): Renomeia as colunas do DataFrame df de acordo com o mapeamento definido no dicionário colunas_renomeadas.
    
    [list(colunas_renomeadas.values())]: Após a renomeação, esta parte seleciona apenas as colunas cujos novos nomes estão presentes nos valores do dicionário colunas_renomeadas. O resultado é armazenado em um novo DataFrame chamado df_clean

### 3. Remover Linhas com Dados Faltantes
    
    # 3. Remover linhas com dados faltantes
    df_clean = df_clean.dropna()

Esta linha utiliza o método dropna() do DataFrame df_clean. Este método remove todas as linhas que contêm pelo menos um valor ausente (NaN) em qualquer uma de suas colunas. O DataFrame resultante, sem as linhas com dados faltantes, substitui o df_clean original

    # 4. Remover outliers (aplicado apenas em colunas numéricas)
    # Identificar colunas numéricas (exemplo: Tempo de experiência)
    if df_clean["Tempo de experiência na área de dados"].dtype == 'object':

Esta linha verifica o tipo de dados (dtype) da coluna "Tempo de experiência na área de dados" no DataFrame df_clean. Se o tipo for 'object' (geralmente indicando strings), o bloco de código seguinte será executado para converter os dados para numérico e remover outliers

 # Converter para numérico (supondo formato como "de 3 a 4 anos")
    df_clean["Tempo_exp_num"] = (
        df_clean["Tempo de experiência na área de dados"]
        .str.extract(r'(\d+)').astype(float) # Extrair o primeiro número
    )

Este bloco de código é executado se a condição do if for verdadeira:

- df_clean["Tempo de experiência na área de dados"].str.extract(r'(\d+)'): Acessa os valores da coluna como strings (.str) e utiliza o método extract() com uma expressão regular r'(\d+)' para extrair o primeiro conjunto de dígitos (números) de cada string. Isso é útil para converter textos como "de 3 a 4 anos" para o número 3.

- .astype(float): Converte os números extraídos para o tipo de dado float (número de ponto flutuante).

- df_clean["Tempo_exp_num"] = ...: Cria uma nova coluna chamada "Tempo_exp_num" no DataFrame df_clean para armazenar esses valores numéricos convertidos


 # Calcular limites para outliers usando IQR
    Q1 = df_clean["Tempo_exp_num"].quantile(0.25)

Calcula o primeiro quartil (Q1), que é o valor abaixo do qual 25% dos dados da coluna "Tempo_exp_num" se encontram. O método quantile(0.25) é usado para isso

    Q3 = df_clean["Tempo_exp_num"].quantile(0.75)

Calcula o terceiro quartil (Q3), que é o valor abaixo do qual 75% dos dados da coluna "Tempo_exp_num" se encontram. O método quantile(0.75) é usado

    IQR = Q3 - Q1

Calcula o Intervalo Interquartil (IQR), que é a diferença entre o terceiro quartil (Q3) e o primeiro quartil (Q1). O IQR é uma medida de dispersão estatística

    lim_inf = Q1 - 1.5 * IQR

Calcula o limite inferior para a detecção de outliers. Valores abaixo deste limite são considerados outliers. A fórmula comum é Q1 - 1.5 * IQR

    lim_sup = Q3 + 1.5 * IQR

Calcula o limite superior para a detecção de outliers. Valores acima deste limite são considerados outliers. A fórmula comum é Q3 + 1.5 * IQR

 # Filtrar dados dentro dos limites
    df_clean = df_clean[
        (df_clean["Tempo_exp_num"] >= lim_inf) &
        (df_clean["Tempo_exp_num"] <= lim_sup)
    ].drop(columns="Tempo_exp_num")

Esta linha filtra o DataFrame df_clean para manter apenas as linhas onde os valores da coluna "Tempo_exp_num" estão dentro dos limites inferior (lim_inf) e superior (lim_sup) calculados.

- (df_clean["Tempo_exp_num"] >= lim_inf): Cria uma série booleana indicando se cada valor é maior ou igual ao limite inferior.

- (df_clean["Tempo_exp_num"] <= lim_sup): Cria uma série booleana indicando se cada valor é menor ou igual ao limite superior.

- &: O operador lógico "E" combina as duas condições, selecionando apenas as linhas que satisfazem ambas.

- .drop(columns="Tempo_exp_num"): Após filtrar as linhas, remove a coluna temporária "Tempo_exp_num" que foi criada para o cálculo dos outliers. O DataFrame df_clean é atualizado com os dados filtrados e sem a coluna auxiliar

### 5. Salvar o Novo Arquivo CSV
    # 5. Salvar o novo arquivo CSV
    df_clean.to_csv('dados_limpos.csv', index=False)


Esta linha salva o DataFrame df_clean (que agora contém os dados limpos) em um novo arquivo CSV chamado 'dados_limpos.csv'.

- index=False: Este argumento impede que o pandas escreva o índice do DataFrame como uma coluna no arquivo CSV

      print("Arquivo 'dados_limpos.csv' gerado com sucesso!")

  Esta linha imprime uma mensagem no console informando que o arquivo 'dados_limpos.csv' foi gerado com sucesso

