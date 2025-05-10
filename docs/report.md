# Disparidade Salarial dos Profissionais de Dados no Brasil


**Pedro Dias Soares, [pdsoares@sga.pucminas.br]** 

**Gabriel Chaves Nascimento, [gabriel.nascimento.1483087@sga.pucminas.br]**

**Gian Henrique Ticon e Silva Carvalho , [ghtscarvalho@sga.pucminas.br]**

**Rafael Hashimoto Sanches Barbosa, [rafael.barbosa.1593862@sga.pucminas.br]**

**Enzo Alves Barcelos Gripp, [eabgripp@sga.pucminas.br]**

---

Professores:

**Hugo Bastos de Paula**

**Hayala Nepomuceno Curto**


---

_Curso de Ciência de Dados, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---
## Sumário

*   [Resumo](#resumo)
*   [Introdução](#introdução)
    *   [Contextualização](#contextualização)
    *   [Problema](#problema)
    *   [Objetivo geral](#objetivo-geral)
    *   [Justificativas](#justificativas)
*   [Público alvo](#público-alvo)
*   [Dicionário de dados](#dicionário-de-dados)
*   [Descrição de dados](#descrição-de-dados)
*   [Preparação dos dados](#preparação-dos-dados)
*   [Enriquecimento de dados](#enriquecimento-de-dados)
*   [Analises exploratorias de dados](#analises-exploratorias-de-dados) 
    *   [1º Pergunta Orientada a Dados](#1º-pergunta-orientada-a-dados)
    *   [2º Pergunta Orientada a Dados](#2º-pergunta-orientada-a-dados)
    *   [3º Pergunta Orientada a Dados](#3º-pergunta-orientada-a-dados)
    *   [4º Pergunta Orientada a Dados](#3º-pergunta-orientada-a-dados)
*   [Indução de modelos](#indução-de-modelos)
    *   [Modelo 1 Análise de Disparidade Salarial de Profissionais de Dados no Brasil Utilizando o Modelo Random Forest](#modelo-1-análise-de-disparidade-salarial-de-profissionais-de-dados-no-brasil-utilizando-o-modelo-random-forest)
    *   [Modelo 2: ](#modelo-2-algoritmo)
    *   [Modelo 3: modelo-baseado-em-árvore-de-decisão](#modelo-3-algoritmo)
    *   [Modelo 4: ](#modelo-4-algoritmo)
*   [Resultados](#resultados)
    *   [Resultados obtidos com o modelo 1.](#resultados-obtidos-com-o-modelo-1)
    *   [Resultados obtidos com o modelo 2.](#resultados-obtidos-com-o-modelo-2)
    *   [Resultados obtidos com o modelo 2.](#resultados-obtidos-com-o-modelo-3)
    *   [Resultados obtidos com o modelo 2.](#resultados-obtidos-com-o-modelo-4)
*   [Interpretação do modelo](#interpretação-do-modelo)
    *   [Interpretação do modelo 1](#interpretação-do-modelo-1)
    *   [Interpretação do modelo 2](#interpretação-do-modelo-2)
    *   [Interpretação do modelo 3](#interpretação-do-modelo-3)
    *   [Interpretação do modelo 4](#interpretação-do-modelo-4)
*   [Análise comparativa dos modelos](#análise-comparativa-dos-modelos)
*   [Conclusão](#8-conclusão)
*   [REFERÊNCIAS](#referências)
*   [APÊNDICES](#apêndices)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Resumo

A disparidade salarial entre profissionais de dados no Brasil é influenciada por diversos fatores pessoais, educacionais e de mercado. Este estudo busca identificar quais variáveis impactam a remuneração desses profissionais, analisando dados da pesquisa State of Data Brazil 2023 e de bases auxiliares. Para isso, são exploradas características como experiência, formação acadêmica, setor de atuação, localização e habilidades técnicas. Através de modelagem preditiva, os resultados indicam que experiência, nível de senioridade e setor da empresa são os fatores com maior impacto na variação salarial. Esses insights podem auxiliar profissionais e empresas na tomada de decisões estratégicas sobre carreira e políticas de remuneração.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Introdução

O Brasil experimentou um crescimento exponencial na indústria de dados devido à transformação digital do país e à crescente necessidade de trabalhadores qualificados. Embora as oportunidades sejam abundantes, os salários variam amplamente entre os trabalhadores, com fatores como experiência, gênero, educação, localização geográfica e tipo de empresa influenciando essa disparidade.

O objetivo deste estudo é identificar os principais fatores associados à disparidade na remuneração dos profissionais de dados no Brasil, utilizando informações coletadas de uma ampla pesquisa setorial.

As disparidades salariais entre os profissionais de dados no Brasil são influenciadas por diversos fatores como idade, gênero dos profissionais de dados, do setor de emprego ou modelo de contratação e ainda o seu histórico educacional e experiência profissional.

Este estudo investiga os principais elementos que estão associados à variação de salários no campo de dados ao utilizar o conjunto de dados State of Data Brazil 2023 e outras bases para complementar a pesquisa. Empregando métodos da ciência de dados, busca-se identificar padrões salariais e oferecer insights relevantes para profissionais e empresas. Espera-se que os resultados tragam um maior entendimento das disparidades salariais no campo, ajudando a desenvolver estratégias que incentivem a igualdade no mercado de tecnologia e ciência de dados.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

###    Contextualização

A desigualdade salarial é um desafio enfrentado no mercado de trabalho brasileiro, impactando diversos setores da economia.

Estudos do IBGE apontam que gênero, etnia e escolaridade são fatores cruciais na determinação dos salários. De acordo com as pesquisas de 2022 do instituto, o rendimento médio por hora dos trabalhadores brancos foi de R$ 20,00, enquanto para pretos ou pardos foi de R$ 12,40, representando uma diferença de 61,4%. Além disso, pesquisas do mesmo em 2021 indicam que as taxas de desocupação foram de 11,3% para brancos, 16,5% para pretos e 16,2% para pardos, evidenciando a influência desses aspectos na disparidade salarial na atualidade.

No setor de tecnologia, essas disparidades têm características particulares, especialmente devido ao desenvolvimento acelerado da área e à necessidade contínua de atualização profissional. Na ciência de dados, as diferenças salariais são significativas e influenciadas por fatores como a experiência, formação acadêmica, setor de atuação e habilidades técnicas.

De acordo com o relatório State of Data Brazil 2023, profissionais que possuem certificações específicas em grandes empresas costumam receber remunerações mais altas, enquanto mulheres e grupos minoritários ainda encontram barreiras para alcançar igualdade salarial. 

Diante do exposto, buscamos por meio desta análise de dados, investigar os fatores determinantes para a variação salarial entre os profissionais de dados no Brasil, visando compreender melhor as desigualdades no setor e identificar caminhos para um mercado mais equitativo.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

###    Problema

O agente em questão busca estabelecer quais são os fatores determinantes para a variação salarial entre profissionais de dados no Brasil. Constantemente, empresas brasileiras enfrentam dificuldades em determinar um salário justo ao profissional de dados por não considerarem os requisitos e as variáveis necessárias para isso. Nesse contexto, a análise busca entender o papel de fatores como experiência e nível educacional nas diferenças salariais, visando fornecer um padrão para que o mercado profissional da área seja mais equilibrado no país.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

###    Objetivo geral

**Desenvolver um sistema inteligente para compreender os fatores que influenciam a variação salarial dos profissionais de dados no Brasil, e para auxiliar na equiparação salarial desses, utilizando técnicas de ciência de dados para identificar padrões e tendências.**

####    Objetivos específicos

1. **Exploração e Análise dos Dados:**
    - Extrair da base de dados State of Data Brazil 2023 e bases auxiliares, dados suficientes para identificar variáveis relevantes associadas aos salários.
      
2. **Identificação de Fatores Relevantes:**
    - Analisar variáveis e compreender o papel de cada uma na carreira profissional do cientista de dados brasileiro, como o nível de experiência, o setor de atuação, o nível educacional, as habilidades técnicas, o gênero e a etnia.
      
3. **Aplicação de Modelos Preditivos:**
    - Aplicar por meio de algoritmos de aprendizado de máquina, a previsão da variação salarial com base nos fatores identificados.
      
4. **Interpretação dos Resultados:**
    - Aplicar por meio de algoritmos de aprendizado de máquina, a previsão da variação salarial com base nos fatores identificados.
      
5. **Geração de Insights para o Mercado:**
    - Fornecer recomendações baseadas nos achados, para auxiliar profissionais de dados e empresas na atribuição de salários aos profissionais da área.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

###    Justificativas

A desigualdade salarial na área de dados é um tema relevante, impactando profissionais e empresas. Este estudo busca identificar os principais fatores associados aos salários, com foco na experiência, senioridade e setor de atuação. O estudo se destina a profissionais da área que podem utilizar os resultados para planejar suas carreiras, e às empresas, que podem aprimorar suas políticas salariais com base em dados concretos. A pesquisa se apoia em bases de dados reconhecidas, como a State of Data Brazil 2023 da Data Hackers, garantindo a validade e confiabilidade das análises realizadas.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##    Público alvo

Os principais perfis de usuários da aplicação são:

Profissionais de dados: Os quais possuem conhecimento técnico variado. Estão familiarizados com ferramentas de análise e visualização de dados, além de linguagens como Python e SQL. No ambiente corporativo, ocupam cargos que vão de analistas a cientistas de dados sêniores.

Gestores e recrutadores de RH: Estes utilizam plataformas de análise salarial para embasar decisões estratégicas. Eles ocupam posições hierárquicas que incluem gerentes, diretores e especialistas em aquisição de talentos.

Pesquisadores e acadêmicos: Aqueles que têm conhecimento analítico e estatístico. Utilizam tecnologias para explorar padrões e tendências em dados salariais e estão inseridos em universidades, centros de pesquisa e órgãos governamentais.

Órgãos governamentais e associações da indústria: Esses utilizam a aplicação para obter informações detalhadas sobre o mercado de trabalho e salários, visando formular políticas públicas, regulamentações e padrões da indústria. Estão envolvidos com dados que ajudam a orientar legislações e relatórios sobre tendências econômicas e de emprego.

A aplicação será útil para esses grupos ao oferecer maneiras de visualizar intuitivas, comparações salariais e insights baseados em machine learning.

## 🎯 Público-alvo da aplicação

A aplicação tem como objetivo fornecer insights sobre disparidade salarial na área de dados no Brasil, ajudando diferentes perfis de usuários a tomar decisões estratégicas. 

## 🏢 Stakeholders e seus papéis

| **Stakeholder**                 | **Nível de Interesse** | **Influência** | **Objetivos** |
|---------------------------------|----------------------|--------------|--------------|
| **Profissionais de Dados**          | Alto                 | Média        | Avaliar sua posição no mercado e planejar crescimento. |
| **Gestores e Recrutadores de RH**   | Alto                 | Alta         | Ajustar faixas salariais e estruturar políticas de retenção. |
| **Pesquisadores e Acadêmicos**      | Médio                | Média        | Explorar padrões e desigualdades no mercado. |
| **Órgãos Governamentais**           | Médio                | Alta         | Criar regulamentações e políticas de inclusão. |

## 👥 Perfis de usuários (Personas)

### **1️⃣ Persona: Analista de Dados Júnior**
- **Nome:** Lucas Mendes  
- **Idade:** 25 anos  
- **Objetivo:** Comparar sua faixa salarial com o mercado para planejar seu crescimento profissional.  
- **Desafios:** Não sabe quais habilidades influenciam no aumento salarial.  

### **2️⃣ Persona: Gerente de RH em Tecnologia**
- **Nome:** Mariana Costa  
- **Idade:** 38 anos  
- **Objetivo:** Definir pacotes salariais competitivos para atrair talentos na área de dados.  
- **Desafios:** Falta de dados estruturados sobre o mercado e diferenças regionais.  

### **3️⃣ Persona: Pesquisador de Mercado de Trabalho**
- **Nome:** Dr. João Ribeiro  
- **Idade:** 45 anos  
- **Objetivo:** Estudar desigualdades salariais no setor de tecnologia.  
- **Desafios:** Precisa de dados confiáveis e ferramentas estatísticas para análise.  

### **4️⃣ Persona: Regulador de Políticas Públicas**
- **Nome:** Ana Beatriz Oliveira  
- **Idade:** 50 anos  
- **Objetivo:** Criar diretrizes para reduzir a disparidade salarial na tecnologia.  
- **Desafios:** Necessita de informações claras e de fácil interpretação.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

###    Dicionário de dados

O banco de dados "State of Data Brazil 2023" é o resultado de uma pesquisa conduzida pela comunidade Data Hackers em parceria com a Bain & Company, que visa mapear o mercado brasileiro de dados. A pesquisa contou com a participação de mais de 5.200 profissionais da área, que responderam a perguntas sobre diversos temas, por exemplo:

- **Fatores Pessoais e Demográficos:** Idade, gênero; Perfil racial e diversidade dentro do setor de dados; Contexto social e fatores que podem influenciar a carreira na área de dados.

- **Experiência profissional prejudicada (discriminação):** 

- **Experiência e Carreira:** Tempo de atuação no mercado de dados; Cargos ocupados e progressão na carreira; Transições de carreira para a área de dados.

- **Empresa e Ambiente de Trabalho:**  Tipo e porte da empresa em que os profissionais trabalham; Modelo de trabalho (remoto, híbrido ou presencial); Cultura organizacional e satisfação no ambiente de trabalho.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

###    Descrição de dados
1. State_of_Data_BR_2023
A pesquisa State_of_Data_BR_2023 é realizada anualmente com o objetivo de mapear o perfil dos profissionais de dados no Brasil. Ela abrange informações como salários, ferramentas utilizadas, nível de experiência, formação acadêmica e outros aspectos relevantes.

**Salários Médio por Gênero:**  
gênero  
Feminino           R$ 7.000,00  
Masculino         R$ 10.000,00  
Não Informado      R$ 7.000,00  
Nome: salary_midpoint, dtype: object  

**Salários Médio por Etnia:**  
etnia  
Asiático          R$ 10.000,00  
Negro              R$ 7.000,00  
Indígena           R$ 5.000,00  
Pardo              R$ 7.000,00  
Não Informado      R$ 7.000,00  
Branco            R$ 10.000,00  
Nome: salary_midpoint, dtype: object  

**Salários Médio por Nível de Educação:**  
nível_educacional  
Graduação                  R$ 7.000,00  
Mestrado                  R$ 10.000,00  
Sem Educação Formal        R$ 5.000,00  
Doutorado                 R$ 14.000,00  
Pós-graduação             R$ 10.000,00  
Estudante de Graduação     R$ 3.500,00  
Nome: salary_midpoint, dtype: object  

**Salários Médio por Senioridade:**  
senioridade  
Júnior         R$ 3.500,00  
Pleno          R$ 7.000,00  
Sênior        R$ 10.000,00  
Nome: salary_midpoint, dtype: object  

**Salários Médio por Função:**  
função_atual  
Engenheiro de Analytics       R$ 10.000,00  
Engenheiro/Arquiteto de Dados R$ 10.000,00  
Professor/Pesquisador         R$ 10.000,00  
Economista                    R$ 10.000,00  
Cientista de Dados            R$ 10.000,00  
Analista de Negócios           R$ 7.000,00  
Analista de Dados              R$ 7.000,00  
Desenvolvedor de Software      R$ 7.000,00  
Analista de BI                 R$ 5.000,00  
Nome: salary_midpoint, dtype: object  

**Salários Médio por Indústria:**  
indústria  
Finanças/Bancos          R$ 10.000,00  
Indústria                R$ 10.000,00  
Internet/E-commerce      R$ 10.000,00  
Tecnologia/Software      R$ 10.000,00  
Varejo                   R$ 10.000,00  
Educação                  R$ 7.000,00  
Setor Público             R$ 7.000,00  
Marketing                 R$ 5.000,00  
Nome: salary_midpoint, dtype: object  

**Salários Médio por Região:**  
região  
Centro-oeste    R$ 10.000,00  
Sudeste         R$ 10.000,00  
Nordeste         R$ 7.000,00  
Norte            R$ 7.000,00  
Sul              R$ 7.000,00  
Nome: salary_midpoint, dtype: object  

**Diferença Salarial por Gênero:** 42,86% (Mediana Masculino: R$ 10.000,00; Mediana Feminino: R$ 7.000,00)  

**Diferença Salarial Branco-Negro:** 42,86% (Mediana Branco: R$ 10.000,00; Mediana Negro: R$ 7.000,00)   
**Diferença Salarial Branco-Pardo:** 42,86% (Mediana Branco: R$ 10.000,00; Mediana Pardo: R$ 7.000,00)  

**Correlação entre Experiência Total e Salário:** 0,54   
**Correlação entre Nível Educacional e Salário:** 0,32

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## Preparação dos dados



### Atributos relevantes da base de dados principal para 1ºpergunta orientada
**Pergunta orientada a dados:** *Como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?*


| Atributo                                         | Nome                                      | Tipo         | Subtipo                             | Descrição                                                                                     | Relevância |
|--------------------------------------------------|-------------------------------------------|--------------|-------------------------------------|-----------------------------------------------------------------------------------------------|------------|
| P0                                               | id                 		       | Qualitativo  | Nominal                             | Para identificação da resposta                                    		            | Alta       |
| P1l                                              | Nível de ensino alcançado                 | Qualitativo  | Ordinal                             | Nível de ensino do respondente (graduação, mestrado, etc.)                                    | Alta       |
| P1m                                              | Área de formação acadêmica                | Qualitativo  | Nominal (Multivalorado)             | Área de formação acadêmica do respondente (TI, Economia, etc.)                                | Alta       |
| P2h                                              | Faixa salarial mensal                     | Qualitativo  | Ordinal                             | Faixa salarial mensal do respondente                                                          | Alta       |
| P2i                                              | Tempo de experiência na área de dados     | Quantitativo | Discreto                            | Tempo de experiência do respondente na área de dados (em anos)                                | Alta       |
| P2g                                              | Nível de senioridade                      | Qualitativo  | Ordinal                             | Nível de senioridade do respondente (Júnior, Pleno, Sênior)                                   | Alta       |
| P1b                                              | Gênero do profissional                    | Qualitativo  | Nominal (Multivalorado)             | Identidade de gênero do respondente                                                           | Alta       |
| P1c                                              | Cor/Raça/Etnia                            | Qualitativo  | Nominal (Multivalorado)             | Cor ou raça do respondente                                                                    | Alta       |
| P2b                                              | Setor de atuação da empresa               | Qualitativo  | Nominal (Multivalorado)             | Setor em que a empresa do respondente atua (Tecnologia, Finanças, etc.)                       | Alta       |
| P1i1                                             | UF onde mora                              | Qualitativo  | Nominal (Multivalorado)             | Unidade Federativa onde o respondente reside                                                  | Alta       |
| P2f                                              | Cargo atual                               | Qualitativo  | Nominal (Multivalorado)             | Cargo atual ocupado pelo respondente                                                          | Alta       |
| P2o6                                             | Oportunidade de aprendizado               | Qualitativo  | Nominal (Multivalorado)             | Valorização das oportunidades de aprendizado e crescimento profissional                       | Alta       |
| P2o10                                            | Reputação da empresa                      | Qualitativo  | Nominal (Multivalorado)             | Valorização da reputação que a empresa tem no mercado                                         | Alta       |

---

### Atributos relevantes da base de dados principal para 2ª pergunta orientada
**Pergunta orientada a dados:** *Qual é a relação entre o tempo de experiência na área de dados, o nível de senioridade e a faixa salarial dos profissionais no Brasil?*

| Atributo | Nome | Tipo | Subtipo | Descrição | Relevância |
|----------|------|------|---------|-----------|------------|
| P2i      | Tempo de Experiência | Quantitativo | Discreto | Anos de atuação na área de dados | Alta |
| P2g      | Nível de Senioridade | Qualitativo | Ordinal | Nível profissional alcançado (Júnior, Pleno, Sênior, etc.) | Alta |
| P2h      | Faixa Salarial | Qualitativo | Ordinal | Classificação salarial em faixas | Alta |


---

### Atributos relevantes da base de dados principal para 3ª pergunta orientada
**Pergunta orientada a dados::** *Como fatores como  formalidade no emprego e características demográficas (gênero e raça) interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?*

| Atributo                                           | Código de Referência | Tipo         | Subtipo                             | Descrição                                                                                     | Relevância  |
|----------------------------------------------------|-----------------------|--------------|-------------------------------------|-----------------------------------------------------------------------------------------------|------------|
| Faixa etária                                       | P1a1                  | Qualitativo  | Ordinal                             | Faixa etária do respondente                                                                   | Alta       |
| Gênero                                             | P1b                   | Qualitativo  | Nominal (Multivalorado)             | Identidade de gênero do respondente                                                           | Alta       |
| Raca                      |      P1c                                       | Qualitativo  | Nominal (Multivalorado)             | Indentificacao da raca do respondente          | Alta
| Não acredito que minha experiência profissional seja afetada     | P1e1                  | Qualitativo  | Nominal (Binário)                   | Resposta indicando que o respondente não acredita que sua experiência foi afetada             | Alta       |
| Experiência prejudicada devido à minha Cor/Raça/Etnia            | P1e2                  | Qualitativo  | Nominal (Binário)                   | Indicação de prejuízo na experiência profissional devido à cor, raça ou etnia                 | Alta       |
| Experiência prejudicada devido à minha identidade de gênero      | P1e3                  | Qualitativo  | Nominal (Binário)                   | Indicação de prejuízo na experiência profissional devido à identidade de gênero               | Alta       |
| Nivel de ensino alcançado                                                | P1l            | Qualitativo | Ordinal               | Nível de ensino do respondente (graduação, mestrado, etc.)                                     | Alta       |
| Faixa salarial mensal                                              | P2h                     | Qualitativo  | Ordinal                             | Faixa salarial mensal do respondente                                                          | Alta       |
| Tempo de experiência na área de dados                                              | P2i     | Quantitativo | Discreto                            | Tempo de experiência do respondente na área de dados (em anos)                                | Alta       |

---

### Atributos relevantes da base de dados principal para 4ª pergunta orientada
**Pergunta orientada a dados:** *Como o domínio de diferentes linguagens de programação influencia a disparidade salarial entre os
profissionais de tecnologia?*

| Atributo                                         | Nome                                      | Tipo         | Subtipo                             | Descrição                                                                                     | Relevância |
|--------------------------------------------------|-------------------------------------------|--------------|-------------------------------------|-----------------------------------------------------------------------------------------------|------------|
| P2h      | Faixa Salarial | Qualitativo | Ordinal | Classificação salarial em faixas | Alta |
| P1l                                              | Nível de ensino alcançado                 | Qualitativo  | Ordinal                             | Nível de ensino do respondente (graduação, mestrado, etc.)                                    | Alta       |
| P1m                                              | Área de formação acadêmica                | Qualitativo  | Nominal (Multivalorado)             | Área de formação acadêmica do respondente (TI, Economia, etc.)                                | Alta       |
| P2h                                              | Faixa salarial mensal                     | Qualitativo  | Ordinal                             | Faixa salarial mensal do respondente                                                          | Alta       |
| P2i                                              | Tempo de experiência na área de dados     | Quantitativo | Discreto                            | Tempo de experiência do respondente na área de dados (em anos)                                | Alta       |
| P2g                                              | Nível de senioridade                      | Qualitativo  | Ordinal             
| P4d1                                             | SQL                                       | Qualitativo  | Nominal (Multivalorado)             | Linguagem de programação utilizada no trabalho                                                | Alta       |
| P4d2                                             | R                                         | Qualitativo  | Nominal (Multivalorado)             | Linguagem de programação utilizada no trabalho                                                | Alta       |
| P4d3                                             | Python                                    | Qualitativo  | Nominal (Multivalorado)             | Linguagem de programação utilizada no trabalho                                                | Alta       |
| P4d4                                             | C/C++/C#                                  | Qualitativo  | Nominal (Multivalorado)             | Linguagem de programação utilizada no trabalho                                                | Média      |
| P4d5                                             | .NET                                      | Qualitativo  | Nominal (Multivalorado)             | Linguagem de programação utilizada no trabalho                                                | Média      |
| P4d6                                             | Java                                      | Qualitativo  | Nominal (Multivalorado)             | Linguagem de programação utilizada no trabalho                                                | Média      |
| P4d7                                             | Julia                                     | Qualitativo  | Nominal (Multivalorado)             | Linguagem de programação utilizada no trabalho                                                | Baixa      |
| P4d8                                             | SAS/Stata                                 | Qualitativo  | Nominal (Multivalorado)             | Linguagem de programação utilizada no trabalho                                                | Média      |
| P4d9                                             | Visual Basic/VBA                          | Qualitativo  | Nominal (Multivalorado)             | Linguagem de programação utilizada no trabalho                                                | Baixa      |
| P4d10                                            | Scala                                     | Qualitativo  | Nominal (Multivalorado)             | Linguagem de programação utilizada no trabalho                                                | Média      |
| P4d11                                            | Matlab                                    | Qualitativo  | Nominal (Multivalorado)             | Linguagem de programação utilizada no trabalho                                                | Baixa      |
| P4d12                                            | Rust                                      | Qualitativo  | Nominal (Multivalorado)             | Linguagem de programação utilizada no trabalho                                                | Baixa      |
| P4d13                                            | PHP                                       | Qualitativo  | Nominal (Multivalorado)             | Linguagem de programação utilizada no trabalho                                                | Baixa      |
| P4d14                                            | JavaScript                                | Qualitativo  | Nominal (Multivalorado)             | Linguagem de programação utilizada no trabalho                                                | Alta       |
| P4d15                                            | Não utilizo nenhuma linguagem             | Qualitativo  | Nominal (Binário)                   | Indicação se o respondente não utiliza nenhuma linguagem de programação                       | Média      |  

---

### Atributos relevantes da base de dados principal para 5ª pergunta orientada
**Pergunta orientada a dados:** *De que forma a especialização em áreas de dados, como inteligência artificial ou engenharia de dados, considerando graduações e pós-graduaçōes, pode influenciar na desigualdade salarial entre os profissionais da área?*

| Atributo | Nome                  | Tipo         | Subtipo                         | Descrição                                                             | Relevância |
|----------|-----------------------|-------------|---------------------------------|------------------------------------------------------------------------|------------|
| P1a      | Idade                 | Quantitativo | Contínuo                        | Idade dos respondentes em anos completos.                             | Alta       |
| P2i      | Tempo de experiência  | Quantitativo | Contínuo                        | Tempo de atuação na área de dados, geralmente em anos.                | Alta       |
| P1m      | Área de formação      | Qualitativo  | Nominal (Multivalorado)         | Curso ou campo de estudo principal (ex: Ciência da Computação, Estatística). | Alta       |
| P2o1     | Salário               | Quantitativo | Contínuo                        | Renda mensal declarada, geralmente em reais.                          | Alta       |


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## Enriquecimento de dados

### Base de dados auxiliar para 1º pergunta orientada a dados
**Pergunta orientada a dados:** *Como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?*
- Microdados do Censo da Educação Superior
- Link: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-da-educacao-superior
  
- [Base de dados](/assets/data/bases_principais/bases_auxiliar/1_pergunta_orientada_a_dados/MICRODADOS_ED_SUP_IES_2023.CSV)


### Base de dados auxiliar para 2º pergunta orientada a dados
**Pergunta orientada a dados:** *Qual é a relação entre o tempo de experiência na área de dados, o nível de senioridade e a faixa salarial dos profissionais no Brasil?*
- Relatórios de Transparência Salarial e Critérios Remuneratórios
- Link: [https://relatoriodetransparenciasalarial.trabalho.gov.br/](https://relatoriodetransparenciasalarial.trabalho.gov.br/)
  
- [Base de dados](/assets/data/bases_principais/bases_auxiliar/2_pergunta_orientada_a_dados/)

### Base de dados auxiliar para a 3º pergunta orientada a dados
**Pergunta orientada a dados:** *Como fatores como formalidade no emprego e características demográficas (gênero e raça) interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?*
- Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD-C)
- Link: https://basedosdados.org/dataset/9fa532fb-5681-4903-b99d-01dc45fd527a?table=a04fc85d-908a-4393-b51d-1bd517a40210
  
- [Base de dados](/assets/data/bases_principais/bases_auxiliar/3_pergunta_orientada_a_dados/bq-results-20250422-030542-1745291209599.zip)

### Base de dados auxiliar para 4º pergunta orientada a dados
**Pergunta orientada a dados:** Como o domínio de diferentes linguagens de programação influencia a disparidade salarial entre os
profissionais de tecnologia?*
  
- [Base de dados](/assets/data/bases_principais/bases_auxiliar/)

### Base de dados auxiliar para 5º pergunta orientada a dados
**Pergunta orientada a dados:** *De que forma a especialização em áreas de dados, como inteligência artificial ou engenharia de dados, considerando graduações e pós-graduaçōes, pode influenciar na desigualdade salarial entre os profissionais da área?*
- Escolaridade, Especialização e Remuneração de Profissionais da Área de Dados no Brasil
- Link: https://www.salario.com.br/
  
- [Base de dados](/assets/data/bases_principais/bases_auxiliar/)


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Analises exploratorias de dados 

# 1º Pergunta orientada a dados 
**Pergunta Orientada a Dados:** *Como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?*

## Analise exploratoria de dados base de dados State of Data 2023

---

## Grafico Distribuição de Salários Mensais
![__results___0_1](https://github.com/user-attachments/assets/6204cac8-9875-4db3-b6d7-6bf52b038d49)
## Explicação do Gráfico: Distribuição de Salários Mensais

O gráfico apresentado é um histograma que ilustra a **Distribuição de Salários Mensais** de profissionais de dados no Brasil, com uma curva de estimativa de densidade do kernel (KDE) sobreposta para suavizar a representação da distribuição.

**Eixos do Gráfico:**
*   **Eixo X (Horizontal):** Representa o "Salário Médio (R$)", indicando as faixas salariais mensais em Reais. A escala varia de R$ 0 até valores próximos ou superiores a R$ 40.000.
*   **Eixo Y (Vertical):** Indica a "Contagem", ou seja, o número de profissionais que se enquadram em cada faixa salarial representada pelas barras do histograma. A contagem máxima observada no gráfico aproxima-se de 800 profissionais em uma determinada faixa salarial.

**Interpretação da Distribuição:**
*   **Concentração de Salários:** A maior concentração de profissionais encontra-se nas faixas salariais mais baixas. Observa-se um pico principal (a barra mais alta) na faixa de aproximadamente R$ 9.000 a R$ 10.000, onde cerca de 800 profissionais estão localizados.
*   **Múltiplos Picos (Multimodalidade):** A distribuição aparenta ser multimodal, sugerida pela curva KDE e pelas barras do histograma. Além do pico principal, há outras concentrações notáveis:
    *   Uma concentração significativa entre R$ 4.000 e R$ 6.000, com mais de 600 profissionais.
    *   Outro pico menor ao redor de R$ 13.000 a R$ 14.000, com quase 300 profissionais.
    *   Pequenas elevações em faixas salariais mais altas, como em torno de R$ 17.000-R$18.000 e R$ 22.000-R$23.000, indicando grupos menores de profissionais nesses níveis salariais.
*   **Assimetria à Direita (Right-Skewed):** A distribuição é assimétrica à direita. Isso significa que, embora a maioria dos salários esteja concentrada nas faixas mais baixas e médias, existe uma "cauda" longa para a direita, indicando que um número menor de profissionais recebe salários consideravelmente mais altos (acima de R$ 20.000, R$ 30.000, e chegando a R$ 40.000 ou mais). Essa assimetria é comum em distribuições de renda e salário.
*   **Dispersão:** Há uma grande dispersão nos salários, variando desde valores abaixo de R$ 5.000 até mais de R$ 40.000, o que reflete a diversidade de remuneração na área de dados no Brasil.

Em resumo, o gráfico mostra que a maioria dos profissionais de dados no Brasil, conforme o dataset analisado, possui salários concentrados nas faixas inferiores a R$ 15.000, com picos importantes em torno de R$ 4.000-R$6.000 e R$ 9.000-R$10.000. No entanto, existe uma parcela de profissionais que alcança remunerações significativamente mais elevadas, estendendo a distribuição para a direita.

## Grafico Relação entre Salário e Tempo de Experiência
![__results___0_2](https://github.com/user-attachments/assets/5b842f17-cbc8-46af-8bf5-7c8bf30bc7e7)
## Explicação do Gráfico: Relação entre Salário e Tempo de Experiência

O gráfico de boxplot intitulado "Relação entre Salário e Tempo de Experiência" ilustra como a faixa salarial numérica ("Faixa_salarial_num") varia conforme o "Tempo de experiência na área de dados" no Brasil.

**Como ler este gráfico de Boxplot:**
*   **Caixa (Box):** Representa o intervalo interquartil (IQR), onde se concentram 50% dos salários. A linha inferior da caixa é o primeiro quartil (Q1 - 25º percentil), e a linha superior é o terceiro quartil (Q3 - 75º percentil).
*   **Linha dentro da Caixa:** Indica a mediana (Q2 - 50º percentil), que é o valor salarial central para cada grupo de experiência.
*   **Hastess/"Bigodes" (Whiskers):** As linhas que se estendem a partir da caixa mostram o alcance dos dados, geralmente até 1,5 vezes o IQR. Pontos além dessas hastes são considerados outliers.
*   **Outliers:** São pontos individuais (losangos no gráfico) que representam salários atípicos, muito acima ou abaixo da maioria dos salários para aquele grupo de experiência.
*   **Eixo Y (Vertical):** "Faixa\_salarial\_num" representa os salários em Reais (R$), variando de R$ 0 a R$ 40.000.
*   **Eixo X (Horizontal):** "Tempo de experiência na área de dados" categoriza os profissionais em diferentes faixas de anos de experiência: "Menos de 1 ano", "de 1 a 2 anos", "de 3 a 4 anos", "de 4 a 6 anos", "de 5 a 6 anos", e "de 7 a 10 anos". As categorias no eixo X do gráfico original não estão em ordem crescente de experiência.

**Interpretação das Tendências Observadas:**

Ao analisar os boxplots para cada faixa de experiência (considerando-os em ordem crescente de experiência):

*   **Tendência Geral de Aumento Salarial com a Experiência:**
    *   **Menos de 1 ano:** Este grupo apresenta a menor mediana salarial, situando-se em torno de R$ 3.500 - R$ 4.000. A maioria dos salários (IQR) está entre aproximadamente R$ 2.000 e R$ 5.000.
    *   **De 1 a 2 anos:** A mediana salarial sobe para cerca de R$ 5.000. O IQR varia de R$ 3.500 a R$ 7.000.
    *   **De 3 a 4 anos:** Observa-se um aumento mais significativo na mediana, que se localiza em torno de R$ 8.000 - R$ 8.500. O IQR está entre R$ 5.000 e R$ 10.000.
    *   **De 4 a 6 anos / De 5 a 6 anos / De 7 a 10 anos:** Estes grupos com maior experiência apresentam medianas salariais consideravelmente mais altas e bastante próximas entre si.
        *   A mediana para "de 4 a 6 anos" e "de 5 a 6 anos" (que parecem muito similares no gráfico) está em torno de R$ 11.000 - R$ 12.000, com IQR entre R$ 10.000 e R$ 14.000.
        *   Para "de 7 a 10 anos", a mediana é ligeiramente superior, em torno de R$ 12.000 - R$ 13.000, com um IQR similar (R$ 10.000 a R$ 14.000).

*   **Variabilidade Salarial (Dispersão):**
    *   A dispersão salarial (representada pela altura da caixa e o comprimento das hastes) tende a aumentar com a experiência. Profissionais nos níveis iniciais de carreira ("Menos de 1 ano") apresentam uma faixa salarial mais concentrada em comparação com aqueles com mais experiência, onde a variabilidade é maior.
    *   Os grupos com mais experiência ("de 4 a 6 anos" em diante) mostram uma dispersão salarial maior, indicando que, embora a média seja mais alta, há uma gama mais ampla de salários sendo pagos.

*   **Outliers:**
    *   Outliers (salários muito acima do comum para o grupo) são observados em todas as categorias de experiência.
    *   Nos grupos com mais experiência (a partir de "de 3 a 4 anos"), alguns profissionais atingem salários de até R$ 40.000, indicando um potencial de alta remuneração para os mais experientes ou em posições de destaque.
    *   Mesmo no grupo com "Menos de 1 ano", existe um outlier próximo a R$ 14.000.

**Conclusão do Gráfico:**
O gráfico demonstra uma clara correlação positiva entre o tempo de experiência na área de dados e o nível salarial. Profissionais com mais anos de atuação tendem a ter salários medianos mais altos e também uma maior variabilidade salarial, com alguns indivíduos alcançando remunerações substancialmente elevadas. A progressão salarial parece ser mais acentuada nos primeiros anos de carreira, estabilizando-se em um patamar mais elevado para profissionais com 4 ou mais anos de experiência.

## Grafico Distribuição Salarial por Nível de Ensino
![__results___0_3](https://github.com/user-attachments/assets/45da8bf1-dfcc-4fac-911f-96af9f6a8b34)
## Explicação do Gráfico: Distribuição Salarial por Nível de Ensino

O gráfico de violino apresentado, intitulado "Distribuição Salarial por Nível de Ensino", exibe como a faixa salarial numérica ("Faixa\_salarial\_num") se distribui entre diferentes níveis de escolaridade alcançados por profissionais de dados no Brasil.

**Como ler este gráfico de Violino:**
*   **Forma do Violino:** A largura do violino em diferentes pontos representa a densidade dos dados naquela faixa salarial. Onde o violino é mais largo, há uma maior concentração de profissionais com salários naquele nível.
*   **Caixa Interna (Box Plot):** Dentro de cada violino, há um box plot:
    *   A **linha branca grossa** no centro da caixa indica a **mediana** salarial (o valor central).
    *   A **caixa retangular** representa o **intervalo interquartil (IQR)**, contendo 50% dos dados (do 25º ao 75º percentil).
    *   As **linhas/hastes (whiskers)** que se estendem da caixa mostram o alcance principal dos dados, e pontos além delas podem ser considerados outliers (embora o violino em si mostre a forma completa da distribuição, incluindo os extremos).
*   **Eixo Y (Vertical):** "Faixa\_salarial\_num" representa os salários em Reais (R$), variando de R$ 0 até mais de R$ 40.000.
*   **Eixo X (Horizontal):** "Nível de ensino alcançado" categoriza os profissionais pelos seguintes níveis de educação:
    *   Doutorado ou Phd
    *   Graduação/Bacharelado
    *   Estudante de Graduação
    *   Pós-graduação
    *   Mestrado

**Interpretação das Distribuições Salariais por Nível de Ensino:**

*   **Estudante de Graduação (Verde):**
    *   Apresenta a **menor mediana salarial**, localizada em torno de R$ 4.000 - R$ 5.000.
    *   A distribuição é mais concentrada em salários baixos, com a parte mais larga do violino nessa região. A maioria dos salários está abaixo de R$ 10.000, embora a cauda superior se estenda até cerca de R$ 25.000.

*   **Graduação/Bacharelado (Laranja):**
    *   A mediana salarial sobe para aproximadamente R$ 8.000 - R$ 9.000.
    *   A distribuição é mais ampla, com uma concentração significativa de salários entre R$ 5.000 e R$ 15.000. Apresenta uma cauda superior longa, indicando que alguns profissionais com esta formação atingem salários bem elevados, chegando até R$ 40.000 ou mais.

*   **Pós-graduação (Vermelho):**
    *   A mediana salarial é ligeiramente superior à de "Graduação/Bacharelado", situando-se em torno de R$ 10.000 - R$ 11.000.
    *   A forma da distribuição é semelhante à de "Graduação/Bacharelado", com uma concentração principal e uma cauda longa para salários mais altos, também atingindo valores acima de R$ 40.000. O violino parece ter uma ligeira "cintura" indicando uma menor densidade entre a concentração mais baixa e a mediana.

*   **Mestrado (Roxo):**
    *   Este grupo apresenta uma das **medianas salariais mais altas**, em torno de R$ 11.000 - R$ 13.000.
    *   A maior parte da densidade salarial está concentrada em uma faixa mais elevada em comparação com "Graduação/Bacharelado" e "Pós-graduação". A cauda superior também é proeminente, indicando potencial para altos salários.

*   **Doutorado ou Phd (Azul):**
    *   A mediana salarial é comparável à de "Mestrado" ou ligeiramente inferior, em torno de R$ 10.000 - R$ 12.000.
    *   A distribuição é bastante dispersa, com o corpo do violino sendo largo, indicando maior variabilidade nos salários para este grupo. A cauda superior é extensa, mostrando que profissionais com doutorado também podem alcançar os salários mais altos do dataset.

**Conclusões Gerais do Gráfico:**
*   Há uma tendência geral de **aumento da mediana salarial com o avanço no nível de ensino**, sendo mais notável a diferença entre "Estudante de Graduação" e os demais níveis.
*   Profissionais com **Mestrado** e **Doutorado/PhD** tendem a ter as medianas salariais mais elevadas, embora a diferença entre eles e "Pós-graduação" (lato sensu, especializações) possa não ser tão acentuada em termos de mediana, mas sim na forma da distribuição e potencial para salários muito altos.
*   Todos os níveis de ensino, a partir da graduação, mostram uma **assimetria à direita** (cauda longa para salários altos), indicando que em todos os níveis há profissionais que conseguem remunerações significativamente acima da média do seu grupo.
*   A **variabilidade salarial** (largura do violino e comprimento das caudas) também é considerável em todos os níveis, especialmente para aqueles com formação superior completa em diante.

## Grafico Interação entre Escolaridade, Experiência e Salário
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/99901a7169839052f5473ff6f4b57242/raw/6c71c7167850cb50f4e98432a646db7c69f2ffa1/grafico_3d_interativo.html)

![newplot](https://github.com/user-attachments/assets/5bb94b6a-aa5d-416d-be48-9bac9d9d01c0)
## Explicação do Gráfico 3D Interativo: Interação entre Escolaridade, Experiência e Salário

O gráfico apresentado é uma visualização 3D interativa que tem como objetivo investigar a interação entre o nível de escolaridade, o tempo de experiência e o salário dos profissionais de dados no Brasil. Gráficos de superfície ou dispersão 3D são úteis para investigar como uma variável de resposta (neste caso, o salário) se relaciona com duas variáveis preditoras (escolaridade e experiência).

**Eixos do Gráfico:**
*   **Eixo X (Horizontal, profundidade):** "Tempo de Experiência (anos)" – Representa os anos de experiência profissional na área de dados. A escala parece variar de 0 a aproximadamente 10 anos.
*   **Eixo Y (Horizontal, largura):** "Nível de Escolaridade (numérico)" – Representa o nível de escolaridade, que foi convertido para uma escala numérica para permitir a plotagem. A legenda indica a correspondência:
    *   0: Doutorado ou PhD
    *   1: Estudante de Graduação
    *   2: Graduação/Bacharelado
    *   3: Mestrado
    *   4: Pós-graduação
*   **Eixo Z (Vertical):** "Salário (R$)" – Representa a remuneração mensal em Reais. A escala vai de R$0 até valores superiores a R$35.000.

**Interpretação dos Dados e Visualização:**
*   **Pontos de Dados (Scatter Plot 3D):** Cada ponto no gráfico representa um profissional de dados, posicionado de acordo com seu tempo de experiência, nível de escolaridade (numérico) e salário.
*   **Cores por Nível de Escolaridade:** Os pontos são coloridos de acordo com o nível de escolaridade, facilitando a distinção e a análise de como cada grupo educacional se distribui em relação à experiência e ao salário.
    *   **Doutorado ou PhD (Azul Escuro/Roxo):** Pontos para este grupo.
    *   **Estudante de Graduação (Azul Claro/Ciano):** Pontos para este grupo.
    *   **Graduação/Bacharelado (Verde):** Pontos para este grupo.
    *   **Mestrado (Laranja/Amarelo):** Pontos para este grupo.
    *   **Pós-graduação (Vermelho):** Pontos para este grupo.
*   **Interatividade:** A natureza interativa do gráfico permite ao usuário girar a visualização, alterar o ângulo de visão e dar zoom. Isso é crucial para explorar as relações complexas em um espaço tridimensional, identificando padrões, concentrações de pontos e outliers que poderiam não ser evidentes em gráficos 2D.

**Observações Gerais e Tendências (Inferidas pela Exploração Visual):**
*   **Impacto da Experiência:** Geralmente, observa-se que, para todos os níveis de escolaridade, um aumento no tempo de experiência (movimento ao longo do eixo X) tende a estar associado a salários mais altos (pontos mais elevados no eixo Z).
*   **Impacto da Escolaridade:**
    *   **Estudantes de Graduação (cor Azul Claro/Ciano):** Tendem a se concentrar na parte inferior da escala salarial e com menor tempo de experiência.
    *   **Graduação/Bacharelado (cor Verde) e Pós-graduação (cor Vermelho):** Mostram uma dispersão maior, com salários aumentando com a experiência. Muitos pontos se situam em faixas salariais intermediárias, mas com potencial de alcançar salários mais altos com mais experiência.
    *   **Mestrado (cor Laranja/Amarelo) e Doutorado/PhD (cor Azul Escuro/Roxo):** Estes grupos tendem a ter pontos que alcançam os níveis salariais mais altos, especialmente quando combinados com maior tempo de experiência. Pode-se observar se há uma "elevação" geral dos pontos dessas cores no eixo Z.
*   **Interação entre Escolaridade e Experiência:** O objetivo principal deste gráfico é visualizar como a combinação específica de um nível de escolaridade e anos de experiência influencia o salário. Por exemplo, pode-se tentar observar se o "retorno" (aumento salarial) por ano adicional de experiência é diferente para quem tem um Mestrado em comparação com quem tem apenas Graduação. A densidade de pontos em certas regiões do gráfico (por exemplo, alta experiência e alto nível de escolaridade resultando em altos salários) pode indicar essas interações. Picos e vales na distribuição dos pontos podem corresponder a combinações que produzem valores máximos ou mínimos de salário.

**Como Explorar o Gráfico Interativo:**
*   **Girar:** Clique e arraste para mudar o ponto de vista e observar a nuvem de pontos de diferentes ângulos. Isso ajuda a entender a profundidade e a sobreposição dos dados.
*   **Zoom:** Use o scroll do mouse para aproximar ou afastar, permitindo focar em áreas específicas de interesse (por exemplo, a distribuição salarial para um nível de escolaridade específico com muitos anos de experiência).
*   **Observar Agrupamentos:** Procure por concentrações de pontos de uma mesma cor em determinadas regiões do espaço 3D.

Este tipo de gráfico é uma ferramenta poderosa na análise exploratória de dados (EDA) para identificar relações multivariadas e gerar hipóteses sobre as interações entre diferentes fatores.

## Grafico Mapa de Calor de Correlações
![__results___0_5](https://github.com/user-attachments/assets/5cf1cb29-6d4c-46dc-bc80-b9b32d679b12)
## Explicação do Gráfico: Mapa de Calor de Correlações

O gráfico apresentado é um **Mapa de Calor de Correlações** (heatmap) que visualiza a força e a direção das relações lineares entre três variáveis numéricas: "Faixa\_salarial\_num", "Oportunidade de aprendizado" e "Reputação da empresa".

**Como ler este Mapa de Calor:**
*   **Variáveis:** As variáveis analisadas estão listadas tanto nas linhas (eixo Y) quanto nas colunas (eixo X) da matriz.
*   **Células Coloridas:** Cada célula na interseção de duas variáveis mostra o coeficiente de correlação entre elas. A cor da célula representa visualmente esse coeficiente.
*   **Barra de Cores (Escala):** Localizada à direita do gráfico, a barra de cores indica como os valores de correlação mapeiam para as cores. Nesta visualização:
    *   Cores quentes (como vermelho intenso) indicam correlações positivas fortes, aproximando-se de +1.0.
    *   Cores frias (como azul intenso/roxo) indicam correlações negativas fortes (aproximando-se de -1.0) ou, como neste caso, correlações muito fracas ou próximas de zero.
    *   Cores neutras ou claras no meio da escala (se presentes) indicariam correlações próximas de 0. A escala no gráfico vai de 0.0 (azul escuro) a 1.0 (vermelho escuro).
*   **Valores Numéricos:** Dentro de cada célula, o valor numérico exato do coeficiente de correlação é exibido. Estes coeficientes variam de -1 (correlação negativa perfeita) a +1 (correlação positiva perfeita), com 0 indicando ausência de correlação linear.

**Interpretação das Correlações Exibidas:**

1.  **Diagonal Principal (de cima para baixo, da esquerda para a direita):**
    *   As células na diagonal principal mostram a correlação de cada variável consigo mesma. Esses valores são sempre **1.00** (vermelho intenso), indicando uma correlação positiva perfeita, o que é esperado.
        *   Faixa\_salarial\_num com Faixa\_salarial\_num: 1.00
        *   Oportunidade de aprendizado com Oportunidade de aprendizado: 1.00
        *   Reputação da empresa com Reputação da empresa: 1.00

2.  **Correlações entre Variáveis Distintas:**
    *   **Faixa\_salarial\_num e Oportunidade de aprendizado:**
        *   Coeficiente: **-0.04**.
        *   Cor: Azul escuro.
        *   Interpretação: Existe uma correlação linear negativa muito fraca, praticamente inexistente, entre a faixa salarial e a oportunidade de aprendizado. Um valor tão próximo de zero sugere que não há uma tendência clara de aumento ou diminuição salarial associada diretamente a maiores ou menores oportunidades de aprendizado, conforme os dados analisados.

    *   **Faixa\_salarial\_num e Reputação da empresa:**
        *   Coeficiente: **0.00**.
        *   Cor: Azul escuro.
        *   Interpretação: Não há correlação linear entre a faixa salarial e a reputação da empresa. Isso indica que, neste conjunto de dados, a reputação da empresa não está linearmente associada a salários mais altos ou mais baixos.

    *   **Oportunidade de aprendizado e Reputação da empresa:**
        *   Coeficiente: **-0.05**.
        *   Cor: Azul escuro.
        *   Interpretação: Há uma correlação linear negativa muito fraca, quase nula, entre a oportunidade de aprendizado e a reputação da empresa. Isso sugere que não há uma relação linear significativa onde empresas com melhor reputação ofereçam consistentemente mais (ou menos) oportunidades de aprendizado, ou vice-versa, de acordo com os dados.

**Conclusão Geral do Mapa de Calor:**
Este mapa de calor indica que as três variáveis analisadas ("Faixa\_salarial\_num", "Oportunidade de aprendizado" e "Reputação da empresa") não possuem correlações lineares fortes entre si no contexto dos dados utilizados para esta análise. Todos os coeficientes de correlação entre pares de variáveis distintas são muito próximos de zero, sugerindo que essas variáveis são, em grande medida, linearmente independentes umas das outras. É importante notar que a correlação mede apenas relações lineares; podem existir relações não lineares que não seriam capturadas por este tipo de análise.

## Grafico Distribuição por Gênero e Raça/Etnia
![__results___0_6](https://github.com/user-attachments/assets/46d749b3-6293-46b5-bca7-021d3843a544)
## Explicação dos Gráficos: Distribuição por Gênero e Raça/Etnia

A imagem anexa exibe dois gráficos de barras que ilustram a distribuição demográfica dos profissionais no conjunto de dados analisado, um por gênero e outro por raça/etnia.

### Gráfico 1: Distribuição por Gênero

*   **Título:** "Distribuição por Gênero"
*   **Tipo de Gráfico:** Gráfico de barras verticais.
*   **Eixo Y (Vertical):** "count" (Contagem) – Indica o número de profissionais. A escala vai de 0 a 2500.
*   **Eixo X (Horizontal):** "Gênero do profissional" – Apresenta as categorias de gênero.
*   **Observações:**
    *   **Masculino:** É a categoria predominante, com uma contagem de aproximadamente 2500 profissionais. Esta é a barra mais alta no gráfico.
    *   **Feminino:** A segunda maior categoria, com uma contagem significativamente menor, em torno de 800 profissionais.
    *   **Outro:** Representa uma contagem muito pequena, quase insignificante visualmente no gráfico.
    *   **Prefiro não informar:** Também representa uma contagem muito pequena, similar à categoria "Outro".
*   **Conclusão:** O gráfico demonstra uma expressiva maioria de profissionais do gênero masculino no conjunto de dados analisado.

### Gráfico 2: Distribuição por Raça/Etnia

*   **Título:** "Distribuição por Raça/Etnia"
*   **Tipo de Gráfico:** Gráfico de barras verticais.
*   **Eixo Y (Vertical):** "count" (Contagem) – Indica o número de profissionais. A escala vai de 0 a mais de 2000.
*   **Eixo X (Horizontal):** "Cor/Raça/Etnia" – Apresenta as categorias de raça ou etnia.
*   **Observações:**
    *   **Branca:** É a categoria com a maior contagem, superando 2000 profissionais. Esta é a barra mais alta.
    *   **Parda:** A segunda categoria mais representada, com uma contagem de aproximadamente 800 profissionais.
    *   **Preta:** Apresenta uma contagem de cerca de 250 profissionais.
    *   **Amarela:** Possui uma contagem menor, em torno de 100 profissionais.
    *   **Prefiro não informar:** Representa uma contagem muito pequena, inferior a 50 profissionais.
    *   **Outra:** Contagem visualmente insignificante.
    *   **Indígena:** Contagem visualmente insignificante.
*   **Conclusão:** O gráfico indica que a maioria dos profissionais no conjunto de dados se identifica como Branca, seguida pela categoria Parda. Outras categorias raciais/étnicas têm representação consideravelmente menor.

**Resumo Geral:**
Ambos os gráficos mostram desequilíbrios significativos nas distribuições. Há uma predominância de profissionais do gênero masculino e de profissionais que se identificam como da cor/raça Branca no dataset utilizado para a análise exploratória de dados.

## Grafico Distribuição Geográfica dos Profissionais
![__results___0_8](https://github.com/user-attachments/assets/b1f41cbe-9705-44ac-8b50-9407b5b07dd2)
## Explicação do Gráfico: Distribuição Geográfica dos Profissionais

O gráfico de barras verticais intitulado "Distribuição Geográfica dos Profissionais" ilustra a contagem de profissionais de dados distribuídos pelos diferentes estados (Unidades Federativas - UF) do Brasil, conforme o conjunto de dados analisado.

**Eixos do Gráfico:**
*   **Eixo Y (Vertical):** "Contagem" – Representa o número de profissionais em cada estado. A escala varia de 0 a mais de 1200.
*   **Eixo X (Horizontal):** "Estado (UF)" – Apresenta as siglas dos estados brasileiros.

**Interpretação da Distribuição Geográfica:**

*   **Concentração em São Paulo (SP):** O estado de São Paulo (SP) destaca-se com a maior concentração de profissionais, com uma contagem que ultrapassa 1200. Esta é, de longe, a barra mais alta no gráfico, indicando que uma parcela muito significativa dos profissionais no dataset está localizada em SP.
*   **Estados com Representação Significativa:** Após São Paulo, alguns outros estados apresentam contagens notáveis, embora consideravelmente menores:
    *   **Minas Gerais (MG):** É o segundo estado com maior número de profissionais, com uma contagem próxima de 400 (especificamente, cerca de 380).
    *   **Paraná (PR):** Apresenta uma contagem um pouco acima de 300 profissionais.
    *   **Rio de Janeiro (RJ):** Também com uma contagem em torno de 300 profissionais.
    *   **Rio Grande do Sul (RS):** Possui cerca de 200 profissionais.
    *   **Santa Catarina (SC):** Apresenta uma contagem um pouco abaixo de 200, em torno de 180 profissionais.
*   **Demais Estados:**
    *   **Distrito Federal (DF), Bahia (BA), Ceará (CE), Pernambuco (PE), Espírito Santo (ES), Goiás (GO), Paraíba (PB):** Estes estados formam um grupo com contagens menores, variando aproximadamente entre 50 e 100 profissionais cada.
    *   **Outros Estados (MT, RN, AM, PA, SE, AL, MS, MA, PI, RO, AP, TO):** A grande maioria dos demais estados brasileiros apresenta contagens muito baixas, com barras quase insignificantes em comparação com os estados mais populosos em termos de profissionais de dados. Muitos desses estados têm menos de 50 profissionais representados no dataset.

**Conclusão Geral do Gráfico:**
O gráfico evidencia uma forte concentração geográfica dos profissionais de dados no Brasil, com o estado de São Paulo dominando expressivamente. A região Sudeste (com SP, MG, RJ, ES) e a região Sul (com PR, RS, SC) concentram a maior parte desses profissionais. As demais regiões e estados possuem uma representação significativamente menor no conjunto de dados analisado.

## Grafico Salário por Nível de Senioridade
![__results___0_9](https://github.com/user-attachments/assets/4cb778a5-1f36-40a9-b815-b0e97c02d2c8)
## Explicação do Gráfico: Salário por Nível de Senioridade

O gráfico de boxplot intitulado "Salário por Nível de Senioridade" ilustra a distribuição da faixa salarial numérica ("Faixa\_salarial\_num") entre diferentes níveis de senioridade profissional: Júnior, Pleno e Sênior.

**Como ler este gráfico de Boxplot:**
*   **Caixa (Box):** Representa o intervalo interquartil (IQR), onde se concentram 50% dos salários. A linha inferior da caixa é o primeiro quartil (Q1 - 25º percentil), e a linha superior é o terceiro quartil (Q3 - 75º percentil).
*   **Linha dentro da Caixa:** Indica a mediana (Q2 - 50º percentil), que é o valor salarial central para cada nível de senioridade.
*   **Hastess/"Bigodes" (Whiskers):** As linhas que se estendem a partir da caixa mostram o alcance dos dados, geralmente até 1,5 vezes o IQR. Pontos além dessas hastes são considerados outliers.
*   **Outliers:** São pontos individuais (representados por losangos no gráfico) que indicam salários atípicos, significativamente mais altos ou mais baixos do que a maioria dos salários para aquele nível de senioridade.
*   **Eixo Y (Vertical):** "Faixa\_salarial\_num" representa os salários em Reais (R$), com a escala variando de R$0 a R$40.000.
*   **Eixo X (Horizontal):** "Nível de senioridade" categoriza os profissionais em "Júnior", "Pleno" e "Sênior".

**Interpretação das Distribuições Salariais por Nível de Senioridade:**

*   **Júnior (Caixa Verde):**
    *   **Mediana Salarial:** É a mais baixa entre os três níveis, situando-se em torno de R$3.500 - R$4.000.
    *   **Intervalo Interquartil (IQR):** A maioria dos salários (50% centrais) está concentrada entre aproximadamente R$2.500 e R$5.000.
    *   **Dispersão e Outliers:** A faixa salarial típica (incluindo os "bigodes") vai de perto de R$0 até cerca de R$7.000. Observam-se alguns outliers com salários mais altos, chegando até aproximadamente R$18.000.

*   **Pleno (Caixa Laranja):**
    *   **Mediana Salarial:** Apresenta um aumento significativo em relação ao nível Júnior, localizando-se em torno de R$7.000.
    *   **Intervalo Interquartil (IQR):** Os 50% centrais dos salários estão entre aproximadamente R$5.000 e R$10.000.
    *   **Dispersão e Outliers:** A faixa salarial típica se estende de cerca de R$1.000 até aproximadamente R$14.000. Este nível possui vários outliers com salários mais elevados, incluindo valores próximos a R$18.000, R$22.500 e até um ponto próximo a R$40.000.

*   **Sênior (Caixa Azul):**
    *   **Mediana Salarial:** É a mais alta dos três níveis, posicionando-se em torno de R$11.500 - R$12.000.
    *   **Intervalo Interquartil (IQR):** A maior parte dos salários (50% centrais) varia entre R$10.000 e R$14.000.
    *   **Dispersão e Outliers:** A faixa salarial típica vai de aproximadamente R$5.000 até cerca de R$18.500. Assim como o nível Pleno, o nível Sênior também apresenta outliers com salários significativamente altos, com pontos próximos a R$22.500 e um próximo a R$40.000. Existem também alguns outliers inferiores, indicando salários mais baixos que o usual para esta senioridade.

**Conclusões Gerais do Gráfico:**
*   **Progressão Salarial Clara:** O gráfico demonstra uma clara progressão salarial à medida que o nível de senioridade aumenta. Profissionais Sênior têm a maior mediana salarial, seguidos por Pleno e depois Júnior.
*   **Aumento da Dispersão:** A variabilidade salarial (altura da caixa e extensão dos "bigodes") tende a aumentar com a senioridade, indicando uma gama mais ampla de salários pagos nos níveis Pleno e Sênior em comparação com o Júnior.
*   **Potencial de Altos Salários:** Embora os outliers existam em todos os níveis, eles atingem valores mais altos e são mais frequentes nos níveis Pleno e Sênior, sugerindo que profissionais com maior senioridade têm maior potencial para alcançar remunerações excepcionalmente elevadas.

Em resumo, o nível de senioridade é um fator importante na determinação da faixa salarial, com um aumento consistente na remuneração e na variabilidade salarial à medida que os profissionais progridem de Júnior para Pleno e Sênior.

## Grafico Análise Multivariada das Relações entre Variáveis Selecionadas (Pair Plot)
![__results___0_11](https://github.com/user-attachments/assets/f8a270d1-8bb7-4612-9c54-0c083f46936a)
## Explicação do Gráfico: Análise Multivariada das Relações entre Variáveis Selecionadas (Pair Plot)

O gráfico apresentado é uma **matriz de gráficos de dispersão (pair plot)**, intitulada "Análise Multivariada das Relações entre Variáveis Selecionadas". Este tipo de visualização é utilizado para mostrar as relações entre pares de múltiplas variáveis simultaneamente, bem como a distribuição individual de cada variável.

As variáveis analisadas são:
*   "Faixa\_salarial\_num" (Salário)
*   "Oportunidade de aprendizado"
*   "Reputação da empresa"

**Estrutura do Gráfico:**

*   **Diagonal Principal:** Os gráficos ao longo da diagonal (do canto superior esquerdo ao canto inferior direito) mostram a **distribuição de cada variável individualmente**, geralmente através de um histograma ou, como neste caso, uma estimativa de densidade do kernel (KDE).
*   **Fora da Diagonal:** Os gráficos fora da diagonal são **gráficos de dispersão (scatter plots)** que mostram a relação entre duas variáveis diferentes. Cada gráfico de dispersão (i,j) mostra a variável do eixo i contra a variável do eixo j.

**Interpretação dos Gráficos Individuais:**

1.  **Distribuições Individuais (Diagonal):**
    *   **Faixa\_salarial\_num (Topo Esquerdo):** A distribuição dos salários é multimodal (apresenta múltiplos picos) e assimétrica à direita. Há uma concentração maior em salários mais baixos (em torno de R$5.000-R$10.000), com picos menores em salários mais altos e uma cauda que se estende até R$40.000.
    *   **Oportunidade de aprendizado (Meio):** Esta variável parece ser binária ou categórica, com a grande maioria dos dados concentrada em dois valores principais (provavelmente 0 e 1, representando, por exemplo, baixa/alta oportunidade ou sim/não). Há um pico maior em um dos valores e um pico menor no outro.
    *   **Reputação da empresa (Inferior Direito):** Similar à "Oportunidade de aprendizado", esta variável também parece ser binária ou categórica, com a maioria dos dados concentrados em dois valores principais. Um dos valores tem uma densidade muito maior que o outro.

2.  **Relações entre Pares de Variáveis (Fora da Diagonal):**

    *   **Oportunidade de aprendizado vs. Faixa\_salarial\_num (Linha 1, Coluna 2 e Linha 2, Coluna 1):**
        *   Os pontos estão concentrados em duas faixas horizontais (ou verticais, dependendo da orientação do par), correspondentes aos dois principais valores da variável "Oportunidade de aprendizado".
        *   Visualmente, não há uma tendência clara (ascendente ou descendente) que sugira uma forte correlação linear entre salário e oportunidade de aprendizado. Os salários parecem variar amplamente para ambos os níveis de oportunidade de aprendizado.

    *   **Reputação da empresa vs. Faixa\_salarial\_num (Linha 1, Coluna 3 e Linha 3, Coluna 1):**
        *   Similar ao par anterior, os pontos se agrupam em duas faixas horizontais (ou verticais) correspondentes aos valores da "Reputação da empresa".
        *   Não se observa uma relação linear forte. Os salários variam amplamente independentemente do nível de reputação da empresa exibido.

    *   **Reputação da empresa vs. Oportunidade de aprendizado (Linha 2, Coluna 3 e Linha 3, Coluna 2):**
        *   Este gráfico mostra como os dois valores de "Oportunidade de aprendizado" se distribuem em relação aos dois valores de "Reputação da empresa". Os pontos se agrupam nos quatro cantos possíveis (0,0; 0,1; 1,0; 1,1), se as variáveis forem binárias 0/1. A densidade de pontos em cada um desses "cantos" indicaria a frequência dessas combinações.
        *   Visualmente, parece não haver um padrão forte de associação. Por exemplo, não parece que empresas com alta reputação consistentemente oferecem alta oportunidade de aprendizado, ou vice-versa.

**Conclusão Geral do Gráfico:**
O pair plot reforça visualmente a ausência de correlações lineares fortes entre "Faixa\_salarial\_num", "Oportunidade de aprendizado" e "Reputação da empresa", o que já havia sido sugerido pelo mapa de calor de correlações anteriormente. As variáveis "Oportunidade de aprendizado" e "Reputação da empresa" apresentam distribuições que sugerem natureza binária ou categórica com poucos níveis. As relações entre os pares de variáveis não exibem padrões lineares claros, indicando que esses fatores, isoladamente ou em pares diretos, não explicam de forma linear e significativa a variação salarial ou uns aos outros neste conjunto de dados.

## Grafico Sunburst da Distribuição de Profissionais de Dados
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/11ec6c319fd644ad08f61cff87cc702c/raw/392be6308934280602be52c7a1ec9cab21e1ad03/sunburst_chart.html)
![newplot (1)](https://github.com/user-attachments/assets/fc4076b1-1a10-48d1-89b2-3f76a107321b)

## Explicação do Gráfico Interativo: Sunburst da Distribuição de Profissionais de Dados

O gráfico apresentado é um **gráfico de explosão solar (sunburst chart)** interativo. Este tipo de visualização é ideal para exibir dados hierárquicos, mostrando como um grupo principal se divide em subgrupos e assim por diante, em uma série de anéis concêntricos.

**Como Ler Este Gráfico Sunburst:**

*   **Círculos Concêntricos (Anéis):** Cada anel representa um nível na hierarquia dos dados.
    *   **Centro do Gráfico:** O círculo mais interno representa o topo da hierarquia, neste caso, o total de "Profissionais de Dados" no dataset analisado.
    *   **Anéis Subsequentes:** Cada anel externo subdivide as categorias do anel interno adjacente.
*   **Segmentos (Fatias):** Cada anel é dividido em segmentos. O tamanho (ângulo ou área) de cada segmento é proporcional à sua participação ou contagem dentro da categoria pai no anel interno.
*   **Cores:** Cores diferentes são usadas para distinguir as categorias em cada nível, ajudando na visualização das proporções e relações.
*   **Interatividade:**
    *   **Hover (Passar o Mouse):** Ao passar o mouse sobre um segmento, ele é destacado, e geralmente uma dica de ferramenta (tooltip) exibe informações detalhadas, como o caminho hierárquico completo e o valor (contagem de profissionais) para aquele segmento específico.
    *   **Clique:** Clicar em um segmento geralmente "foca" ou "dá zoom" naquela categoria, tornando-a o novo centro do gráfico e exibindo suas subdivisões com mais detalhes. Clicar no centro do gráfico retorna ao nível hierárquico anterior.

**Hierarquia e Interpretação dos Dados Neste Gráfico Específico:**

Observando o gráfico interativo:

1.  **Nível Central (Raiz):**
    *   Representa o total de "Profissionais de Dados" considerados na análise.

2.  **Primeiro Anel (Nível de Escolaridade):**
    *   Subdivide os profissionais de dados pelo "Nível de Escolaridade".
    *   As categorias visíveis são: "Graduação/Bacharelado", "Pós-graduação", "Mestrado", "Estudante de Graduação" e "Doutorado ou PhD".
    *   O tamanho de cada segmento neste anel indica a proporção de profissionais com aquele nível de escolaridade. Por exemplo, "Graduação/Bacharelado" parece ser a maior fatia, indicando o nível de escolaridade mais comum.

3.  **Segundo Anel (Tempo de Experiência):**
    *   Subdivide cada categoria de "Nível de Escolaridade" pelo "Tempo de experiência na área de dados".
    *   As faixas de experiência incluem: "de 1 a 2 anos", "de 3 a 4 anos", "Menos de 1 ano", "de 4 a 6 anos", "de 7 a 10 anos" e "de 5 a 6 anos".
    *   O tamanho de um segmento neste anel mostra, por exemplo, quantos profissionais com "Graduação/Bacharelado" têm "de 1 a 2 anos" de experiência.

4.  **Terceiro Anel (Faixa Salarial Média):**
    *   Subdivide cada combinação de "Nível de Escolaridade" e "Tempo de Experiência" pela "Faixa Salarial Média (R$)".
    *   As faixas salariais incluem: "0-5000", "5001-10000", "10001-15000", "15001-20000", etc.
    *   O tamanho de um segmento neste anel mais externo indica, por exemplo, quantos profissionais com "Graduação/Bacharelado" e "de 1 a 2 anos" de experiência se enquadram na faixa salarial de "5001-10000". Os números dentro dos segmentos representam a contagem de profissionais.

**Como Extrair Insights:**

*   **Proporções Dominantes:** Identifique rapidamente os níveis de escolaridade mais comuns, as faixas de experiência predominantes dentro de cada nível de escolaridade e as faixas salariais mais frequentes para cada combinação de escolaridade e experiência.
*   **Relações Hierárquicas:** Entenda como os grupos se subdividem. Por exemplo, pode-se explorar se profissionais com "Mestrado" e "de 7 a 10 anos" de experiência tendem a se concentrar em faixas salariais mais altas em comparação com aqueles com "Graduação/Bacharelado" e a mesma experiência.
*   **Exploração Interativa:** Use o clique para focar em segmentos de interesse. Por exemplo, clicando em "Mestrado", o gráfico se reorganizará para mostrar apenas as subdivisões de experiência e salário para mestres, permitindo uma análise mais detalhada desse subgrupo específico.

Este gráfico sunburst oferece uma visão rica e interativa da composição da força de trabalho de profissionais de dados no Brasil, de acordo com o dataset, permitindo a exploração de como a escolaridade, a experiência e os salários se inter-relacionam em diferentes níveis.

---

## Analise exploratoria de dados base de dados Microdados

---

## Grafico Distribuição Nacional de Níveis de Formação dos Docentes
![01_distribuicao_formacao_nacional](https://github.com/user-attachments/assets/0052b7ec-4124-4e90-a500-8abd26d0ccc8)
## Explicação do Gráfico: Distribuição Nacional de Níveis de Formação dos Docentes

O gráfico de pizza ilustra a proporção dos docentes em nível nacional, classificados de acordo com seu nível de formação acadêmica. Os dados são provenientes do arquivo `microdados_agrupados_por_uf.csv`.

**Principais observações do gráfico:**

*   **Docentes com Doutorado:** Este grupo constitui a maior fatia, representando **52,3%** do total de docentes analisados. Isso indica que mais da metade dos docentes possui o título acadêmico mais elevado.
*   **Docentes com Mestrado:** Correspondem a **33,3%** do corpo docente. Somados aos doutores, os docentes com pós-graduação *stricto sensu* (mestrado ou doutorado) são a grande maioria.
*   **Docentes com Especialização:** Representam **13,9%** dos docentes. Este grupo possui pós-graduação *lato sensu*.
*   **Docentes com Graduação:** Apenas **0,6%** dos docentes possuem somente a graduação como nível de formação mais alto. Este é o menor grupo, sugerindo que a progressão para níveis de pós-graduação é comum na carreira docente.

**Contextualização para a Análise Exploratória de Dados:**

Este gráfico de pizza fornece uma visão geral do perfil educacional dos docentes no Brasil, com base nos dados disponíveis. Ele demonstra uma alta qualificação acadêmica, com a maioria possuindo títulos de mestre ou doutor.

Para a pergunta de pesquisa original sobre "como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil", este gráfico oferece um panorama da variável "formação acadêmica" para o grupo de "docentes". No entanto, conforme discutido anteriormente, para analisar a disparidade salarial, seriam necessários dados de remuneração e uma clara identificação de "profissionais de dados", que não estão presentes no dataset atual.

A predominância de altos níveis de escolaridade é um fator importante, mas sua interação com a experiência profissional e o impacto na disparidade salarial demandariam um conjunto de dados mais completo.


## Grafico Top 10 Estados por Nível de Formação de Docentes
![02_top10_estados_formacao](https://github.com/user-attachments/assets/4513d6de-20bd-4e5b-9b93-1cd10b819ad5)
## Explicação do Gráfico: Top 10 Estados por Nível de Formação de Docentes

O gráfico de barras empilhadas ilustra o número total de docentes nos 10 estados com maior contingente, detalhando a distribuição desses profissionais conforme seu nível de formação acadêmica. O eixo vertical ("Número de Docentes") quantifica o total de docentes, enquanto o eixo horizontal ("Estado") lista as siglas dos respectivos estados. Cada barra é segmentada por cores que representam os diferentes níveis de formação:

*   **Rosa:** Docentes com Graduação
*   **Dourado/Marrom:** Docentes com Especialização
*   **Verde:** Docentes com Mestrado
*   **Azul-petróleo (Teal):** Docentes com Doutorado

**Principais observações do gráfico:**

*   **Liderança de São Paulo (SP):** O estado de São Paulo (SP) destaca-se com o maior número absoluto de docentes, ultrapassando 70.000 profissionais. Dentro deste total, a maior parcela é composta por docentes com doutorado, seguida por mestrado e especialização.
*   **Minas Gerais (MG) e Rio de Janeiro (RJ):** Minas Gerais (MG) ocupa a segunda posição, com aproximadamente 40.000 docentes, seguido pelo Rio de Janeiro (RJ), com pouco mais de 30.000. Ambos os estados também apresentam uma predominância de docentes com doutorado e mestrado.
*   **Demais Estados no Top 10:** Os estados do Paraná (PR), Rio Grande do Sul (RS), Bahia (BA), Santa Catarina (SC), Pernambuco (PE), Ceará (CE) e Goiás (GO) completam o ranking dos 10 estados com mais docentes. Em todos eles, a tendência de maior concentração nos níveis de doutorado e mestrado se mantém, embora em menor escala absoluta comparado a SP, MG e RJ.
*   **Proporção dos Níveis de Formação:** Em todos os estados visualizados, a formação de doutorado (azul-petróleo) representa a maior ou uma das maiores parcelas do total de docentes. Em seguida, geralmente aparecem os docentes com mestrado (verde). Docentes com apenas especialização (dourado/marrom) formam um grupo menor, e aqueles com apenas graduação (rosa) são a menor fração, quase imperceptível em alguns estados, indicando um alto nível de qualificação formal do corpo docente nesses estados.

**Contextualização para a Análise Exploratória de Dados:**

Este gráfico permite uma comparação visual da quantidade e do perfil de formação dos docentes entre os principais estados brasileiros. Ele reforça a observação de que o corpo docente, especialmente nos estados com maior número de profissionais, possui elevada qualificação acadêmica, com forte presença de doutores e mestres.

Para a pergunta de pesquisa sobre a influência da formação acadêmica e experiência profissional na disparidade salarial entre profissionais de dados, este gráfico detalha a variável "formação acadêmica" em um nível geográfico (estadual) para "docentes". A análise da disparidade salarial, contudo, ainda dependeria da inclusão de dados de remuneração e da identificação específica de "profissionais de dados" dentro desse universo de docentes ou em um dataset complementar. Observar onde se concentram os docentes mais qualificados pode ser um ponto de partida para investigar se há correlação com polos de desenvolvimento em ciência de dados, mas a relação direta com salários não pode ser inferida apenas com este gráfico.

## Grafico Distribuição Etária Nacional dos Docentes
![03_distribuicao_etaria_nacional](https://github.com/user-attachments/assets/38b315e0-7eb6-4c40-820f-3b0281b1b1d8)
## Explicação do Gráfico: Distribuição Etária Nacional dos Docentes

O gráfico de barras verticais, intitulado "Distribuição Etária Nacional dos Docentes", exibe a quantidade de docentes em nível nacional, agrupados por diferentes faixas etárias. O eixo vertical ("Quantidade") indica o número de docentes, enquanto o eixo horizontal ("Faixa Etária") categoriza os docentes em grupos de idade.

**Principais observações do gráfico:**

*   **Pico na Faixa de 40-44 anos:** A faixa etária com o maior número de docentes é a de "Docentes\_Idade\_40\_44", com quase 70.000 profissionais. Isso sugere que o maior contingente de docentes se encontra nessa fase da carreira.
*   **Concentração entre 35 e 49 anos:** As faixas etárias "Docentes\_Idade\_35\_39" (pouco mais de 60.000 docentes) e "Docentes\_Idade\_45\_49" (pouco menos de 60.000 docentes) também apresentam um número elevado de profissionais, indicando que uma parcela significativa do corpo docente nacional está entre 35 e 49 anos.
*   **Presença Significativa em Faixas Mais Elevadas:** A faixa "Docentes\_Idade\_60\_mais" também mostra um número considerável de docentes, com mais de 45.000 profissionais. Isso indica uma retenção de docentes mais experientes no sistema ou um envelhecimento da força de trabalho docente.
*   **Menor Quantidade nas Faixas Mais Jovens e Intermediárias Superiores:** As faixas "Docentes\_Idade\_30\_34" (pouco menos de 40.000), "Docentes\_Idade\_50\_54" (aproximadamente 45.000) e "Docentes\_Idade\_55\_59" (pouco menos de 40.000) apresentam quantidades menores em comparação com o pico, mas ainda representam um número substancial de docentes. A distribuição geral se assemelha a uma curva que atinge seu pico na faixa dos 40-44 anos e depois declina gradualmente, com uma leve recuperação na faixa de 60 anos ou mais.

**Contextualização para a Análise Exploratória de Dados:**

Este gráfico fornece um panorama da distribuição etária dos docentes no Brasil. No contexto da pergunta de pesquisa sobre "como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil", a idade pode ser utilizada como um *proxy* (uma aproximação) para a experiência profissional. Geralmente, espera-se que profissionais mais velhos tenham acumulado mais anos de experiência.

A concentração de docentes em faixas etárias mais maduras (40-49 anos) e a presença significativa de docentes com 60 anos ou mais podem indicar um corpo docente experiente. Para analisar a disparidade salarial, seria necessário cruzar esses dados etários (como proxy de experiência) com informações sobre a formação acadêmica (analisada em gráficos anteriores) e, crucialmente, com dados de remuneração específicos para "profissionais de dados", os quais não estão presentes no dataset atual. Este gráfico ajuda a caracterizar uma dimensão da "experiência profissional" de forma agregada para o grupo de docentes.


## Grafico Matriz de Correlação entre Formação e Faixa Etária
![04_heatmap_correlacao](https://github.com/user-attachments/assets/18c3148a-1e19-49af-bc4e-bbc1b61910bf)
## Explicação do Gráfico: Matriz de Correlação entre Formação e Faixa Etária

O gráfico apresentado é uma **matriz de correlação**, visualizada como um *heatmap* (mapa de calor). Ele exibe a força e a direção da relação linear entre diferentes níveis de formação acadêmica dos docentes e suas faixas etárias, com base nos dados agregados por Unidade da Federação (UF).

**Como interpretar o gráfico:**

*   **Eixos:** Tanto o eixo horizontal quanto o vertical listam as mesmas variáveis: os diferentes níveis de formação (`Docentes_Graduacao`, `Docentes_Especializacao`, `Docentes_Mestrado`, `Docentes_Doutorado`) e as diferentes faixas etárias (`Docentes_Idade_30_34`, ..., `Docentes_Idade_60_mais`).
*   **Células e Valores:** Cada célula na interseção de duas variáveis mostra o coeficiente de correlação de Pearson entre elas. Este coeficiente varia de -1 a +1:
    *   **+1:** Correlação positiva perfeita (quando uma variável aumenta, a outra também aumenta proporcionalmente).
    *   **0:** Nenhuma correlação linear.
    *   **-1:** Correlação negativa perfeita (quando uma variável aumenta, a outra diminui proporcionalmente).
*   **Cores:** A barra de cores à direita indica a intensidade da correlação:
    *   **Cores quentes (vermelho intenso):** Correlação positiva forte (próxima de +1).
    *   **Cores frias (azul intenso):** Correlação negativa forte (próxima de -1).
    *   **Cores neutras (próximo ao branco/cinza claro):** Correlação fraca (próxima de 0).
*   **Diagonal Principal:** A diagonal de cima para baixo, da esquerda para a direita, sempre mostra o valor 1.00 (vermelho intenso), pois representa a correlação de cada variável consigo mesma, que é sempre perfeita.

**Principais observações e correlações:**

1.  **Alta Correlação entre Níveis de Pós-Graduação:**
    *   Há correlações muito fortes e positivas entre os diferentes níveis de pós-graduação. Por exemplo, `Docentes_Mestrado` e `Docentes_Doutorado` têm uma correlação de 0.98. Similarmente, `Docentes_Especializacao` e `Docentes_Mestrado` também apresentam 0.98.
    *   Isso sugere que as UFs que possuem um alto número de docentes com um tipo de pós-graduação (ex: mestrado) tendem a ter também um alto número de docentes com outros tipos de pós-graduação (ex: doutorado, especialização).

2.  **Alta Correlação entre Faixas Etárias Adjacentes e Próximas:**
    *   As faixas etárias demonstram correlações positivas muito altas entre si, especialmente as adjacentes. Por exemplo, `Docentes_Idade_35_39` e `Docentes_Idade_40_44` têm correlação de 0.99.
    *   Isso indica que UFs com muitos docentes em uma faixa etária específica tendem a ter também muitos docentes nas faixas etárias vizinhas.

3.  **Forte Correlação entre Níveis de Pós-Graduação e a Maioria das Faixas Etárias:**
    *   Os níveis de pós-graduação (`Docentes_Especializacao`, `Docentes_Mestrado`, `Docentes_Doutorado`) mostram correlações positivas consistentemente altas (geralmente acima de 0.90) com a maioria das faixas etárias, especialmente as intermediárias e mais velhas (a partir de `Docentes_Idade_35_39` até `Docentes_Idade_55_59`).
    *   Por exemplo, `Docentes_Mestrado` tem correlação de 1.00 com `Docentes_Idade_45_49`, e `Docentes_Doutorado` tem 0.99 com `Docentes_Idade_40_44` e `Docentes_Idade_45_49`.
    *   Isso sugere que UFs com um grande número de docentes pós-graduados tendem a ter um grande número de docentes distribuídos por diversas faixas etárias, refletindo um corpo docente qualificado e maduro.

4.  **Correlações Mais Baixas com `Docentes_Graduacao`:**
    *   A variável `Docentes_Graduacao` (que representa docentes apenas com graduação) apresenta correlações consideravelmente mais baixas com todos os outros níveis de formação e com todas as faixas etárias (valores variando de 0.26 a 0.40).
    *   Por exemplo, a correlação entre `Docentes_Graduacao` e `Docentes_Doutorado` é de 0.38, e entre `Docentes_Graduacao` e `Docentes_Idade_35_39` é de 0.40.
    *   Isso pode indicar que a distribuição de docentes apenas com graduação pelas UFs não segue o mesmo padrão da distribuição de docentes pós-graduados ou das diferentes faixas etárias de forma tão intensa.

5.  **Correlações Ligeiramente Menores nas Faixas Etárias Extremas com Formação:**
    *   Para a faixa etária mais jovem (`Docentes_Idade_30_34`), as correlações com os níveis mais altos de formação (Mestrado e Doutorado) são um pouco menores (0.95 e 0.94, respectivamente) em comparação com faixas etárias intermediárias. Isso é esperado, pois leva tempo para obter esses títulos.
    *   Da mesma forma, para a faixa `Docentes_Idade_60_mais`, as correlações com os níveis de pós-graduação também são um pouco menores, embora ainda altas (ex: 0.96 com Doutorado, 0.89 com `Docentes_Idade_35_39`).

**Contextualização para a Análise Exploratória de Dados:**

Esta matriz de correlação revela que, em nível estadual, a presença de docentes com alta qualificação (mestrado, doutorado) está fortemente associada à presença de docentes em diversas faixas etárias, especialmente as mais experientes. Indica também que estados com um forte contingente em um nível de pós-graduação tendem a ser fortes nos outros.

Para a pergunta de pesquisa sobre como formação e experiência (proxy pela idade) interagem para influenciar a disparidade salarial, esta análise mostra que, nos estados, há uma coocorrência significativa de alta formação e diversas faixas etárias. No entanto, a matriz não inclui dados salariais. Se dados salariais fossem adicionados, poderíamos investigar se UFs com alta correlação entre formação e idade (experiência) apresentam padrões específicos de disparidade salarial para "profissionais de dados". A ausência de uma forte correlação da variável `Docentes_Graduacao` com as demais sugere que este grupo pode ter características distintas que precisariam ser exploradas separadamente.


## Grafico Mapa Interativo de Bolhas - Distribuição de Docentes por Nível de Formação e UF
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/9d708a6e00717a471ed00ab3e3742a40/raw/c1f0d385f7c9ad6f156de6d78dfcc9d245c68c99/06_mapa_bolhas_interativo.html)
![06_mapa_bolhas](https://github.com/user-attachments/assets/8a39d31d-a20f-4e3a-a51a-010005ad43b1)
## Explicação do Gráfico: Mapa Interativo de Bolhas - Distribuição de Docentes por Nível de Formação e UF

O gráfico apresentado é um **mapa de bolhas interativo** que visualiza a distribuição do número de docentes em cada Unidade da Federação (UF) do Brasil, segmentado por nível de formação acadêmica. Este tipo de gráfico utiliza círculos (bolhas) de tamanhos variados sobre um mapa para representar a magnitude de uma variável em diferentes regiões geográficas.

**Como interpretar o gráfico:**

*   **Base Geográfica:** O mapa do Brasil serve como plano de fundo, com as bolhas posicionadas sobre os respectivos estados.
*   **Bolhas:** Cada bolha no mapa representa um nível de formação específico dentro de um estado.
    *   **Cor da Bolha:** A cor da bolha indica o nível de formação acadêmica, conforme a legenda fornecida no gráfico:
        *   **Azul:** Docentes com Doutorado
        *   **Verde:** Docentes com Mestrado
        *   **Laranja/Amarelo:** Docentes com Especialização
        *   **Vermelho:** Docentes com Graduação
    *   **Tamanho da Bolha:** O tamanho da bolha é diretamente proporcional ao **número de docentes** com aquele nível de formação específico naquela UF. Bolhas maiores indicam um número maior de docentes.
    *   **Interatividade:** Ao passar o cursor do mouse sobre uma bolha, uma caixa de informações (tooltip) aparece, exibindo detalhes como a sigla da UF, o nível de formação representado pela bolha e o número exato de docentes correspondente.

**Principais observações do gráfico:**

*   **Concentração Regional de Alta Qualificação:** Observa-se visualmente que estados como São Paulo (SP), Minas Gerais (MG), Rio de Janeiro (RJ), Paraná (PR) e Rio Grande do Sul (RS) tendem a apresentar bolhas azuis (Doutorado) e verdes (Mestrado) proeminentes, indicando uma concentração significativa de docentes com alta qualificação nessas regiões.
*   **Predominância de Doutorado e Mestrado:** Em muitos estados, as bolhas azuis (Doutorado) e verdes (Mestrado) são as de maior tamanho, reforçando a constatação de gráficos anteriores sobre a alta qualificação (pós-graduação *stricto sensu*) do corpo docente na maioria das UFs.
*   **Variações Estaduais:** O mapa permite uma rápida comparação entre os estados. Alguns estados, especialmente nas regiões Norte e Nordeste, podem apresentar um volume total de docentes menor (bolhas geralmente menores) ou uma distribuição proporcional diferente entre os níveis de formação quando comparados aos estados do Sul e Sudeste.
*   **Baixa Representatividade da Graduação:** As bolhas vermelhas (Graduação), que representam docentes com apenas graduação, são consistentemente as menores em todos os estados, muitas vezes quase imperceptíveis, confirmando o baixo número de docentes que não possuem pós-graduação.

**Contextualização para a Análise Exploratória de Dados:**

Este mapa de bolhas interativo oferece uma dimensão geográfica à análise da formação acadêmica dos docentes. Ele permite identificar visualmente "hotspots" ou áreas de maior concentração de docentes por nível de formação.

No contexto da pergunta de pesquisa sobre "como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil", este gráfico contribui ao:
*   Mapear a distribuição da **formação acadêmica** dos docentes (o grupo disponível no dataset) pelo território nacional.
*   Permitir a identificação de estados com maior ou menor concentração de docentes altamente qualificados.

Para avançar na resposta à pergunta de pesquisa, seria necessário cruzar essas informações geográficas de formação com dados de experiência profissional (que poderiam ser agregados por UF) e, fundamentalmente, com dados salariais específicos para "profissionais de dados" em cada estado. O mapa atual é uma ferramenta exploratória valiosa para entender a distribuição da qualificação docente, mas não contém, por si só, informações sobre salários ou experiência para analisar diretamente a disparidade salarial de profissionais de dados.


## Grafico Gráfico de Dispersão 3D Interativo - Mestrado, Doutorado e Média de Idade dos Docentes por UF
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/5edbfdc4c69d324455e65eef06c591b6/raw/d304db3742f4839c7bf4360c2ed75a06bce75bbe/07_3d_interativo.html)
![07_3d_interativo](https://github.com/user-attachments/assets/7b396546-3b72-4dc2-9897-0f6af9600cc7)
## Explicação do Gráfico: Gráfico de Dispersão 3D Interativo - Mestrado, Doutorado e Média de Idade dos Docentes por UF

O gráfico apresentado é um **gráfico de dispersão 3D interativo**. Ele visualiza a relação entre três variáveis para cada Unidade da Federação (UF) do Brasil: o número de docentes com mestrado, o número de docentes com doutorado e a média de idade dos docentes.

**Como interpretar o gráfico:**

*   **Eixos:** O gráfico possui três eixos, cada um representando uma variável quantitativa:
    *   **Eixo X (horizontal, profundidade):** `Docentes_Mestrado` - Número de docentes com título de Mestre na UF.
    *   **Eixo Y (horizontal, largura):** `Docentes_Doutorado` - Número de docentes com título de Doutor na UF.
    *   **Eixo Z (vertical, altura):** `Media_Idade_Docentes` - Média de idade dos docentes na UF.
*   **Pontos:** Cada ponto (esfera) no espaço 3D representa uma Unidade da Federação (UF). A posição do ponto é determinada pelos valores das três variáveis para aquela UF.
*   **Cores dos Pontos:** No gráfico visualizado, os pontos parecem ter uma cor azulada uniforme. A legenda ou interatividade poderiam revelar se a cor representa alguma outra variável, mas com base na imagem estática, ela parece ser apenas para visualização dos pontos.
*   **Interatividade:** Por ser um gráfico interativo (geralmente criado com bibliotecas como Plotly):
    *   **Rotação:** É possível girar o gráfico para visualizar a dispersão dos pontos de diferentes ângulos, ajudando a perceber padrões e relações espaciais.
    *   **Zoom:** Pode-se aproximar ou afastar para focar em regiões específicas do gráfico.
    *   **Hover (Passar o mouse):** Ao passar o cursor sobre um ponto, informações adicionais sobre aquela UF (como o nome da UF e os valores exatos das três variáveis) são tipicamente exibidas.

**Principais observações (baseadas na estrutura visual):**

*   **Relação entre Mestrado e Doutorado:** Observa-se uma tendência geral de que UFs com um alto número de docentes com mestrado (valores mais altos no eixo X) também tendem a ter um alto número de docentes com doutorado (valores mais altos no eixo Y). Isso é indicado pela dispersão dos pontos que tende a se estender diagonalmente no plano XY.
*   **Variação na Média de Idade:** Os pontos se distribuem em diferentes alturas ao longo do eixo Z, indicando variação na média de idade dos docentes entre as UFs.
*   **Identificação de Clusters e Outliers:**
    *   Pode haver agrupamentos (clusters) de UFs com características semelhantes (por exemplo, UFs com muitos mestres, muitos doutores e alta média de idade).
    *   Alguns pontos podem estar mais isolados (outliers), representando UFs com combinações menos comuns dessas três variáveis. Por exemplo, um ponto no canto superior direito do plano XY e alto no eixo Z representaria uma UF com muitos mestres, muitos doutores e uma alta média de idade dos docentes.
*   **Concentração de UFs:** A maioria dos pontos parece se concentrar em uma região onde os números de docentes com mestrado e doutorado não são os máximos observados, e a média de idade varia. Estados com grandes contingentes de docentes (como São Paulo, visualizado em gráficos anteriores) provavelmente se destacariam nas extremidades superiores dos eixos X e Y.

**Contextualização para a Análise Exploratória de Dados:**

Este gráfico 3D permite uma análise simultânea da **formação acadêmica** (níveis de mestrado e doutorado) e de um proxy para a **experiência profissional** (média de idade dos docentes) em nível estadual.

Para a pergunta de pesquisa ("Como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?"):
*   Este gráfico visualiza diretamente a coocorrência de altos níveis de formação (mestrado e doutorado) e diferentes médias de idade (experiência) nas UFs.
*   Ele ajuda a identificar se UFs com um perfil específico de formação e idade (ex: alta formação e alta média de idade) se agrupam.

Contudo, assim como os gráficos anteriores, este não inclui dados salariais. Para analisar a disparidade salarial, seria necessário integrar informações de remuneração a essa análise tridimensional, possivelmente usando a cor ou o tamanho dos pontos para representar uma variável salarial, ou realizando análises estatísticas subsequentes com dados mais completos. Este gráfico é uma ferramenta exploratória poderosa para entender a inter-relação das variáveis de formação e idade dos docentes entre os estados.


---

## Analise exploratoria de dados bases integradas

---

## Grafico Salário Médio Estimado e Total de Docentes por UF
![bar_line_salario_medio_total_docentes_uf](https://github.com/user-attachments/assets/6060f457-2f9f-4c68-9839-82f9f4ac9312)
## Análise do Gráfico: Salário Médio Estimado e Total de Docentes por UF

O gráfico apresentado é uma visualização combinada que utiliza barras para representar o "Salário Médio Estimado (R$)" dos profissionais de dados e uma linha para mostrar o "Total de Docentes na UF" (Unidade Federativa) onde esses profissionais residem.

**Elementos do Gráfico:**

*   **Eixo X (Horizontal):** Apresenta as Unidades Federativas (UF onde mora), ordenadas da esquerda para a direita, aparentemente pela ordem decrescente do salário médio estimado.
*   **Eixo Y Esquerdo (Vertical):** Indica o "Salário Médio Estimado (R$)" e corresponde às barras vermelhas. A escala varia de R$0 a R$14.000.
*   **Eixo Y Direito (Vertical):** Representa o "Total de Docentes na UF" e corresponde à linha azul tracejada com marcadores. A escala vai de 0 a aproximadamente 70.000.
*   **Barras Vermelhas (Salário Médio):** Cada barra mostra o salário médio estimado dos profissionais de dados para uma UF específica.
*   **Linha Azul Tracejada (Total Docentes):** A linha indica o número total de docentes em cada UF.

**Observações e Interpretações:**

*   **Salário Médio Estimado:**
    *   Tocantins (TO) exibe o maior salário médio estimado, superando os R$14.000.
    *   O Distrito Federal (DF) e São Paulo (SP) aparecem em seguida, com salários médios entre R$9.000 e R$10.000 para o DF e um pouco acima de R$9.000 para SP.
    *   Observa-se uma tendência de diminuição do salário médio ao se mover da esquerda para a direita do gráfico. UFs como Piauí (PI) e Rondônia (RO) apresentam os menores salários médios, em torno de R$4.000.

*   **Total de Docentes:**
    *   São Paulo (SP) possui, de longe, o maior número de docentes, ultrapassando 70.000.
    *   Minas Gerais (MG) e Rio de Janeiro (RJ) também têm um volume expressivo de docentes (MG entre 30.000 e 40.000, RJ acima de 30.000).
    *   Muitas outras UFs, incluindo aquelas com salários médios mais baixos e algumas com salários mais altos como TO e DF, têm um número consideravelmente menor de docentes (frequentemente abaixo de 10.000 ou 20.000).

*   **Relação entre Salário Médio e Total de Docentes:**
    *   **Não se observa uma correlação direta e simples** entre o salário médio dos profissionais de dados e o número total de docentes na UF.
        *   Por exemplo, TO tem o salário médio mais alto, mas um número relativamente baixo de docentes.
        *   SP combina um salário médio alto (terceiro maior) com o maior número de docentes.
        *   DF possui o segundo maior salário médio, mas um número de docentes bem inferior ao de SP, MG ou RJ.
    *   Isso sugere que o salário médio dos profissionais de dados em cada estado é influenciado por um conjunto de fatores que vai além da quantidade de docentes (que poderia ser um indicador da oferta de formação ou do tamanho do sistema educacional). Fatores como a demanda do mercado de trabalho local, o custo de vida, a concentração de empresas de tecnologia e o nível de desenvolvimento econômico da UF provavelmente desempenham papéis cruciais.

**Conclusão do Gráfico:**

O gráfico demonstra que não há uma relação causal direta entre o número de docentes em uma UF e o salário médio dos profissionais de dados nessa mesma UF. Enquanto São Paulo apresenta um alto volume de docentes e um alto salário médio, o caso de Tocantins (alto salário médio, poucos docentes) exemplifica que outros fatores são determinantes para a remuneração na área de dados. A dinâmica salarial é complexa e moldada por múltiplas variáveis, não sendo explicada isoladamente pela infraestrutura educacional em termos de quantidade de docentes.

## Grafico Salário Estimado por Área de Formação (Top 5)
![boxplot_salario_por_area_formacao_top5](https://github.com/user-attachments/assets/521f1e12-e4bb-445e-982d-733d52142401)
## Análise do Gráfico: Salário Estimado por Área de Formação (Top 5)

O gráfico apresentado é um boxplot que ilustra a distribuição do "Salário Estimado (R$)" para as cinco principais áreas de formação dos profissionais de dados. Cada boxplot resume a distribuição salarial para uma área específica, permitindo comparações entre elas.

**Elementos do Gráfico:**

*   **Eixo Y (Vertical):** "Área de Formação", listando as cinco categorias de formação mais comuns ou relevantes.
    *   Computação / Engenharia de Software / Sistemas de Informação/ TI
    *   Outras Engenharias
    *   Economia/ Administração / Contabilidade / Finanças/ Negócios
    *   Estatística/ Matemática / Matemática Computacional/ Ciências Atuariais
    *   Outra opção
*   **Eixo X (Horizontal):** "Salário Estimado (R$)", variando de R$0 até mais de R$40.000.
*   **Boxplot (Caixa e Bigodes):** Para cada área de formação:
    *   A **linha central** dentro da caixa representa a **mediana** salarial (o valor que divide os salários em 50% abaixo e 50% acima).
    *   A **caixa** em si abrange o **intervalo interquartil (IQR)**, ou seja, os 50% centrais dos salários (do primeiro quartil - Q1 - ao terceiro quartil - Q3). A largura da caixa indica a dispersão desses salários centrais.
    *   Os **"bigodes"** (linhas que se estendem a partir da caixa) mostram o alcance dos salários, geralmente até 1.5 vezes o IQR a partir da caixa.
    *   Os **pontos individuais** (losangos) fora dos bigodes são considerados **outliers**, indicando salários atipicamente altos ou baixos em relação ao restante do grupo.

**Observações e Interpretações por Área de Formação:**

1.  **Computação / Engenharia de Software / Sistemas de Informação/ TI:**
    *   **Mediana Salarial:** Parece ser a mais alta entre as áreas, situada próxima a R$10.000.
    *   **Dispersão (IQR):** A caixa é relativamente compacta, sugerindo que a maioria dos profissionais dessa área tem salários concentrados em torno da mediana.
    *   **Alcance e Outliers:** Apresenta um alcance considerável nos bigodes e múltiplos outliers indicando salários bem elevados, alguns ultrapassando R$40.000.

2.  **Outras Engenharias:**
    *   **Mediana Salarial:** Ligeiramente inferior à de Computação/TI, talvez em torno de R$8.000 - R$9.000.
    *   **Dispersão (IQR):** Similar ou um pouco maior que Computação/TI.
    *   **Alcance e Outliers:** Também possui um bom alcance e múltiplos outliers com salários altos.

3.  **Economia/ Administração / Contabilidade / Finanças/ Negócios:**
    *   **Mediana Salarial:** Parece estar na faixa de R$7.000 - R$8.000.
    *   **Dispersão (IQR):** A caixa aparenta ser um pouco mais larga, indicando uma maior variabilidade nos salários do grupo central em comparação com Computação/TI.
    *   **Alcance e Outliers:** Presença de outliers com salários elevados.

4.  **Estatística/ Matemática / Matemática Computacional/ Ciências Atuariais:**
    *   **Mediana Salarial:** Próxima à área de Economia/Negócios, possivelmente entre R$7.000 e R$8.000.
    *   **Dispersão (IQR):** A caixa parece ter uma dispersão considerável.
    *   **Alcance e Outliers:** Também exibe outliers significativos.

5.  **Outra opção:**
    *   **Mediana Salarial:** Aparenta ter a menor mediana entre as cinco categorias, talvez em torno de R$6.000 - R$7.000.
    *   **Dispersão (IQR):** A caixa parece ser relativamente larga, sugerindo uma variabilidade salarial significativa dentro deste grupo.
    *   **Alcance e Outliers:** Possui outliers, incluindo um que se destaca próximo a R$40.000.

**Comparações e Conclusões Gerais:**

*   Profissionais com formação na área de **Computação / Engenharia de Software / Sistemas de Informação/ TI** tendem a ter a mediana salarial mais alta.
*   Todas as áreas de formação apresentam uma dispersão salarial considerável, evidenciada pelos tamanhos das caixas e, principalmente, pela presença de outliers com salários significativamente altos. Isso sugere que, dentro de cada área, há profissionais que conseguem remunerações bem acima da média do seu grupo.
*   A categoria "Outra opção" apresenta a menor mediana salarial, o que é esperado, pois agrupa diversas formações menos diretamente ligadas às habilidades centrais da área de dados.
*   As áreas de "Outras Engenharias", "Economia/Administração/etc." e "Estatística/Matemática/etc." apresentam medianas salariais intermediárias e relativamente próximas entre si, mas com variações na dispersão dos salários.

Este gráfico é útil para entender como a área de formação inicial se relaciona com os níveis salariais no campo de dados, destacando que, embora formações em TI/Computação pareçam ter uma vantagem na mediana, todas as áreas analisadas possuem profissionais alcançando altos patamares salariais.


## Grafico Salário Estimado por Tempo de Experiência
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/a62a1fa0a659e7a351b966759dafa417/raw/4b807c1571bb235ffa8469985f8f14d4f3c80d74/boxplot_salario_por_experiencia_plotly.html)
![newplot](https://github.com/user-attachments/assets/3733a3c3-9327-497c-87db-1550f799e558)
## Análise do Gráfico: Salário Estimado por Tempo de Experiência

O gráfico visualizado é um boxplot que demonstra a distribuição do "Salário Estimado (R$)" para diferentes níveis de "Tempo de Experiência na Área de Dados (Anos Estimados)". Essa representação gráfica permite comparar como a remuneração varia conforme os profissionais acumulam mais anos de experiência na área.

**Elementos do Gráfico:**

*   **Eixo Y (Vertical):** Representa as categorias de "Tempo de Experiência na Área de Dados (Anos Estimados)". As categorias são:
    *   Menos de 1 ano (Rotulado como 0.5 no gráfico)
    *   de 1 a 2 anos (Rotulado como 1.5)
    *   de 3 a 4 anos (Rotulado como 3.5)
    *   de 4 a 6 anos (Rotulado como 5.0)
    *   de 6 a 10 anos (Rotulado como 8.0)
    *   Mais de 10 anos (Rotulado como 10.0)
*   **Eixo X (Horizontal):** Indica o "Salário Estimado (R$)", com valores que vão de R$0 até mais de R$30.000.
*   **Boxplot (Diagrama de Caixa):** Para cada faixa de experiência, o boxplot exibe:
    *   A **linha central** na caixa: Representa a **mediana** salarial (50º percentil), o valor que divide os salários em duas metades iguais.
    *   A **caixa**: Abrange o **intervalo interquartil (IQR)**, que contém os 50% centrais dos dados salariais (do primeiro quartil, Q1 ou 25º percentil, ao terceiro quartil, Q3 ou 75º percentil). A altura da caixa indica a dispersão dos salários nesse intervalo central.
    *   Os **"bigodes" (whiskers)**: Linhas que se estendem da caixa para mostrar o alcance dos dados salariais, geralmente até 1.5 vezes o IQR. Valores além dos bigodes podem ser outliers.
    *   **Outliers**: Pontos individuais (neste gráfico, parecem pequenos círculos) que se localizam fora dos bigodes, indicando salários atipicamente altos ou baixos em comparação com o restante do grupo para aquela faixa de experiência.

**Observações e Interpretações por Faixa de Experiência:**

1.  **Menos de 1 ano (0.5):**
    *   **Mediana Salarial:** A mais baixa entre todas as faixas, situando-se em torno de R$2.000 - R$3.000.
    *   **Dispersão (IQR):** A caixa é relativamente compacta, mas há uma concentração na parte inferior da faixa salarial.
    *   **Outliers:** Apresenta alguns outliers, indicando que mesmo com pouca experiência, alguns profissionais conseguem salários acima da média do grupo.

2.  **de 1 a 2 anos (1.5):**
    *   **Mediana Salarial:** Aumenta visivelmente em relação à faixa anterior, provavelmente entre R$4.000 e R$5.000.
    *   **Dispersão (IQR):** A caixa se expande, mostrando maior variabilidade salarial.
    *   **Outliers:** Mais outliers presentes, e com valores mais altos.

3.  **de 3 a 4 anos (3.5):**
    *   **Mediana Salarial:** Continua a crescer, situando-se talvez em torno de R$7.000 - R$8.000.
    *   **Dispersão (IQR):** A dispersão dos 50% centrais dos salários aumenta.
    *   **Outliers:** Número significativo de outliers, alcançando salários mais elevados.

4.  **de 4 a 6 anos (5.0):**
    *   **Mediana Salarial:** Apresenta um salto expressivo, posicionando-se próximo ou acima de R$10.000.
    *   **Dispersão (IQR):** A caixa é mais ampla, refletindo uma maior diversidade salarial.
    *   **Outliers:** Muitos outliers, com alguns ultrapassando R$30.000.

5.  **de 6 a 10 anos (8.0):**
    *   **Mediana Salarial:** Continua a tendência de alta, possivelmente entre R$12.000 e R$14.000.
    *   **Dispersão (IQR):** Grande dispersão salarial, com a caixa sendo bastante longa.
    *   **Outliers:** Vários outliers com salários muito altos.

6.  **Mais de 10 anos (10.0):**
    *   **Mediana Salarial:** Atinge o patamar mais alto, superando R$15.000 e aproximando-se de R$18.000 - R$20.000.
    *   **Dispersão (IQR):** A maior dispersão entre todas as faixas, indicando uma ampla gama de salários para os profissionais mais experientes.
    *   **Outliers:** Presença marcante de outliers com os salários mais altos do dataset, muitos acima de R$30.000.

**Conclusões Gerais:**

*   **Impacto Positivo da Experiência:** Há uma clara e consistente tendência de aumento da mediana salarial à medida que o tempo de experiência na área de dados aumenta. Profissionais com mais anos de atuação tendem a receber salários significativamente maiores.
*   **Aumento da Dispersão Salarial com a Experiência:** Não apenas a mediana, mas também a dispersão dos salários (representada pelo tamanho da caixa e pelo alcance dos bigodes e outliers) tende a aumentar com a experiência. Isso sugere que, entre os profissionais mais experientes, há uma variação salarial maior – alguns podem ter salários excepcionalmente altos, enquanto outros podem permanecer em faixas mais modestas em comparação com os "top earners" do mesmo nível de experiência.
*   **Potencial de Altos Salários:** Em todas as faixas de experiência, a presença de outliers superiores indica que existem oportunidades para alcançar salários acima da média do respectivo grupo, mas essa possibilidade se torna mais pronunciada e os valores mais altos com o aumento da experiência.

Este gráfico reforça a noção de que a experiência profissional é um fator crucial na progressão salarial dentro da área de dados no Brasil, com os profissionais mais experientes não apenas alcançando medianas salariais mais altas, mas também apresentando uma gama mais ampla de possibilidades de remuneração.


## Grafico Salário Estimado por Tempo de Experiência em Dados
![boxplot_salario_por_experiencia_seaborn](https://github.com/user-attachments/assets/1ae56e9f-614e-490c-9cea-c70402bd333c)
## Análise do Gráfico: Salário Estimado por Tempo de Experiência em Dados

O gráfico de boxplot anexado ilustra a relação entre o "Tempo de Experiência" dos profissionais de dados e o "Salário Estimado (R$)". Cada caixa no gráfico representa a distribuição salarial para uma faixa específica de anos de experiência.

**Elementos do Gráfico:**

*   **Eixo Y (Vertical):** "Tempo de Experiência", dividido nas seguintes categorias:
    *   Menos de 1 ano
    *   de 1 a 2 anos
    *   de 3 a 4 anos
    *   de 5 a 6 anos
    *   de 7 a 10 anos
    *   Mais de 10 anos
*   **Eixo X (Horizontal):** "Salário Estimado (R$)", com escala de R$0 até mais de R$40.000.
*   **Boxplot (Diagrama de Caixa):** Para cada categoria de experiência:
    *   A **linha vertical dentro da caixa** indica a **mediana** salarial (o valor central que divide os salários em 50% abaixo e 50% acima).
    *   A **caixa (box)** representa o **intervalo interquartil (IQR)**, contendo os 50% centrais dos salários (do primeiro quartil - Q1 - ao terceiro quartil - Q3). A largura da caixa mostra a dispersão desses salários centrais.
    *   Os **"bigodes" (whiskers)** são as linhas horizontais que se estendem da caixa, mostrando o alcance principal dos salários (tipicamente 1.5 vezes o IQR).
    *   Os **pontos individuais (losangos)** fora dos bigodes são considerados **outliers**, representando salários atipicamente altos ou baixos em relação ao grosso dos dados para aquela faixa de experiência.

**Observações e Interpretações por Faixa de Experiência:**

1.  **Menos de 1 ano:**
    *   **Mediana Salarial:** A mais baixa, em torno de R$4.000.
    *   **Dispersão (IQR):** Relativamente concentrada, com a maioria dos salários entre aproximadamente R$2.000 e R$6.000.
    *   **Outliers:** Alguns outliers superiores, chegando até cerca de R$20.000.

2.  **de 1 a 2 anos:**
    *   **Mediana Salarial:** Aumenta para cerca de R$6.000.
    *   **Dispersão (IQR):** A caixa se alarga um pouco, com salários centrais entre R$4.000 e R$8.000, aproximadamente.
    *   **Outliers:** Mais outliers e com valores mais altos, alguns ultrapassando R$30.000.

3.  **de 3 a 4 anos:**
    *   **Mediana Salarial:** Um salto significativo, posicionando-se em torno de R$9.000 - R$10.000.
    *   **Dispersão (IQR):** Maior variabilidade, com a caixa indo de cerca de R$6.000 a R$12.000.
    *   **Outliers:** Vários outliers, com alguns alcançando e ultrapassando R$40.000.

4.  **de 5 a 6 anos:**
    *   **Mediana Salarial:** Continua a crescer, situando-se em torno de R$12.000.
    *   **Dispersão (IQR):** A caixa é ampla, indicando diversidade salarial, aproximadamente entre R$8.000 e R$16.000.
    *   **Outliers:** Presença de outliers tanto superiores (ultrapassando R$40.000) quanto inferiores (próximos a R$0).

5.  **de 7 a 10 anos:**
    *   **Mediana Salarial:** Aumenta para cerca de R$14.000 - R$15.000.
    *   **Dispersão (IQR):** A caixa se estende de aproximadamente R$10.000 a R$20.000.
    *   **Outliers:** Similar à faixa anterior, com outliers em ambas as extremidades.

6.  **Mais de 10 anos:**
    *   **Mediana Salarial:** A mais alta, em torno de R$16.000 - R$18.000.
    *   **Dispersão (IQR):** A maior dispersão dos salários centrais, com a caixa indo de cerca de R$12.000 a R$25.000. Isso indica uma grande variação salarial entre os profissionais mais experientes.
    *   **Outliers:** Numerosos outliers, especialmente na extremidade superior, indicando que profissionais com vasta experiência podem alcançar remunerações muito elevadas. Também há outliers inferiores.

**Conclusões Gerais:**

*   **Progressão Salarial com Experiência:** O gráfico demonstra claramente que a mediana salarial tende a aumentar consistentemente com o aumento do tempo de experiência na área de dados.
*   **Aumento da Variabilidade Salarial:** À medida que a experiência aumenta, não só a mediana salarial cresce, mas também a dispersão dos salários (indicada pela largura da caixa e pela presença de outliers). Isso sugere que, com mais experiência, as faixas salariais se tornam mais amplas.
*   **Potencial de Alta Remuneração:** Em todos os níveis de experiência, existem profissionais (outliers) que ganham significativamente mais do que a mediana do seu grupo. Esse potencial para salários muito altos é particularmente evidente nas faixas de maior experiência.
*   **Outliers Inferiores:** A presença de outliers na extremidade inferior, especialmente nas faixas de maior experiência, pode indicar diversos cenários, como transições de carreira, atuação em setores ou regiões com menor remuneração, ou outros fatores não capturados apenas pela variável "tempo de experiência".

Este gráfico é uma ferramenta visual eficaz para entender como a remuneração na área de dados evolui com a experiência, destacando a valorização progressiva dos profissionais à medida que acumulam mais anos de atuação.


## Grafico Salário Estimado por Nível de Ensino
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/d4a35514b072e73dcb602e3c936f3324/raw/da8b4afe7bd6ce83a87a646bfc6e978bee28b69a/gistfile1.txt)
![newplot(1)](https://github.com/user-attachments/assets/933aba1b-01fa-45fe-b4ad-6380af43469e)
## Análise do Gráfico: Salário Estimado por Nível de Ensino

O gráfico visualizado é um boxplot que ilustra a distribuição do "Salário Estimado (R$)" para diferentes categorias de "Nível de Ensino" alcançado pelos profissionais de dados. Este tipo de gráfico é uma ferramenta eficaz na análise exploratória de dados para comparar a tendência central, dispersão e identificar valores atípicos entre diferentes grupos.

**Elementos do Gráfico:**

*   **Eixo Y (Vertical):** "Nível de Ensino", apresentando as seguintes categorias:
    *   Estudante de Graduação
    *   Graduação/Bacharelado
    *   Pós-graduação
    *   Mestrado
    *   Doutorado ou Phd
*   **Eixo X (Horizontal):** "Salário Estimado (R$)", com a escala variando de R$0 até mais de R$30.000.
*   **Boxplot (Diagrama de Caixa):** Para cada nível de ensino, o boxplot resume a distribuição salarial da seguinte forma:
    *   A **linha vertical dentro da caixa** representa a **mediana** salarial (o 50º percentil), que é o valor central dividindo os salários em duas metades iguais.
    *   A **caixa (box)** delimita o **intervalo interquartil (IQR)**, que contém os 50% centrais dos dados salariais (do primeiro quartil, Q1 ou 25º percentil, ao terceiro quartil, Q3 ou 75º percentil). A largura da caixa indica a dispersão dos salários neste intervalo.
    *   Os **"bigodes" (whiskers)** são as linhas horizontais que se estendem a partir da caixa, mostrando o alcance dos dados salariais considerados típicos (geralmente até 1.5 vezes o IQR a partir da caixa).
    *   Os **pontos individuais (losangos)** localizados fora dos bigodes são considerados **outliers**, indicando salários que são atipicamente altos ou baixos em comparação com o restante dos profissionais naquele nível de ensino.

**Observações e Interpretações por Nível de Ensino:**

1.  **Estudante de Graduação:**
    *   **Mediana Salarial:** A mais baixa entre todos os níveis, situando-se em torno de R$2.000 - R$3.000.
    *   **Dispersão (IQR):** A caixa é relativamente compacta, indicando que a maioria dos estudantes de graduação tem salários próximos a essa mediana baixa.
    *   **Outliers:** Apresenta alguns outliers superiores, sugerindo que alguns estudantes já conseguem remunerações mais elevadas.

2.  **Graduação/Bacharelado:**
    *   **Mediana Salarial:** Aumenta consideravelmente em relação aos estudantes, posicionando-se em torno de R$7.000 - R$8.000.
    *   **Dispersão (IQR):** A caixa é mais ampla, mostrando uma maior variabilidade nos salários dos graduados.
    *   **Outliers:** Presença significativa de outliers, com alguns salários ultrapassando R$30.000.

3.  **Pós-graduação:**
    *   **Mediana Salarial:** Ligeiramente superior à da graduação, talvez em torno de R$8.000 - R$9.000.
    *   **Dispersão (IQR):** A dispersão parece similar ou um pouco maior que a dos graduados.
    *   **Outliers:** Muitos outliers, alcançando patamares salariais elevados.

4.  **Mestrado:**
    *   **Mediana Salarial:** Apresenta um aumento notável em relação à pós-graduação, situando-se acima de R$10.000, talvez próximo a R$12.000.
    *   **Dispersão (IQR):** A caixa é relativamente ampla, indicando uma boa variabilidade salarial.
    *   **Outliers:** Muitos outliers com salários altos, alguns bem acima de R$30.000.

5.  **Doutorado ou Phd:**
    *   **Mediana Salarial:** A mais alta entre todos os níveis de ensino, superando a do mestrado e posicionando-se em torno de R$14.000 - R$15.000.
    *   **Dispersão (IQR):** A caixa é bastante extensa, refletindo uma grande dispersão salarial entre os doutores.
    *   **Outliers:** Presença marcante de outliers com os salários mais elevados do conjunto de dados, indicando um alto potencial de ganhos para este grupo.

**Conclusões Gerais:**

*   **Impacto Positivo do Nível de Ensino:** O gráfico demonstra uma tendência clara de aumento da mediana salarial à medida que o nível de ensino aumenta. Profissionais com níveis de formação mais elevados (Mestrado, Doutorado) tendem a ter medianas salariais significativamente maiores.
*   **Aumento da Dispersão Salarial em Níveis Mais Altos:** Nos níveis de ensino mais elevados, especialmente Doutorado, não apenas a mediana é maior, mas também a dispersão dos salários (o tamanho da caixa e o alcance dos outliers). Isso sugere uma gama mais ampla de remunerações, com alguns profissionais alcançando salários excepcionalmente altos.
*   **Valor da Graduação:** Há um salto salarial expressivo ao se completar a graduação em comparação com o nível de estudante.
*   **Outliers Significativos:** Em todos os níveis a partir da graduação, a presença de outliers superiores indica que, independentemente do nível de formação específico (pós-graduação, mestrado), existem oportunidades para alcançar salários bem acima da média do grupo.

Este gráfico reforça a ideia de que o investimento em educação formal, especialmente em níveis mais avançados como mestrado e doutorado, está associado a um maior potencial de remuneração na área de dados no Brasil.


## Grafico Salário Estimado por Nível de Ensino
![boxplot_salario_por_nivel_ensino_seaborn](https://github.com/user-attachments/assets/320b22fc-43fb-40af-be93-e02572699fec)
## Análise do Gráfico: Salário Estimado por Nível de Ensino

O gráfico anexado é um boxplot que exibe a distribuição do "Salário Estimado (R$)" para diferentes níveis de escolaridade ("Nível de Ensino") alcançados pelos profissionais de dados. Esta visualização permite comparar como a remuneração varia entre os diferentes graus de formação acadêmica.

**Elementos do Gráfico:**

*   **Eixo Y (Vertical):** "Nível de Ensino", com as seguintes categorias (de cima para baixo):
    *   Estudante de Graduação
    *   Graduação/Bacharelado
    *   Pós-graduação
    *   Mestrado
    *   Doutorado ou Phd
*   **Eixo X (Horizontal):** "Salário Estimado (R$)", com uma escala que se estende de R$0 até mais de R$40.000.
*   **Boxplot (Diagrama de Caixa):** Para cada nível de ensino, o boxplot mostra:
    *   A **linha vertical dentro da caixa**: Indica a **mediana** salarial (o valor que divide a distribuição dos salários em duas metades iguais).
    *   A **caixa**: Representa o **intervalo interquartil (IQR)**, que contém os 50% centrais dos salários (entre o primeiro quartil - Q1 - e o terceiro quartil - Q3). A largura da caixa reflete a dispersão desses salários centrais.
    *   Os **"bigodes" (whiskers)**: Linhas horizontais que se estendem da caixa para mostrar o alcance dos salários considerados típicos.
    *   Os **pontos individuais (losangos)**: Representam **outliers**, ou seja, salários que são atipicamente altos (ou baixos) em comparação com a maioria dos profissionais daquele nível de ensino.

**Observações e Interpretações por Nível de Ensino:**

1.  **Estudante de Graduação:**
    *   **Mediana Salarial:** É a mais baixa de todas as categorias, situando-se em torno de R$4.000 - R$5.000.
    *   **Dispersão (IQR):** A caixa é relativamente estreita, indicando que a maioria dos estudantes de graduação tem salários concentrados em uma faixa menor, aproximadamente entre R$2.500 e R$6.000.
    *   **Outliers:** Apresenta alguns outliers superiores, com salários chegando a cerca de R$15.000, e um outlier próximo a R$20.000.

2.  **Graduação/Bacharelado:**
    *   **Mediana Salarial:** Aumenta significativamente em relação aos estudantes, localizando-se em torno de R$8.000 - R$9.000.
    *   **Dispersão (IQR):** A caixa é consideravelmente mais larga, com os 50% centrais dos salários variando aproximadamente de R$5.000 a R$12.000, indicando maior variabilidade salarial.
    *   **Outliers:** Numerosos outliers superiores, com vários profissionais alcançando salários acima de R$20.000, R$30.000 e até R$40.000.

3.  **Pós-graduação:**
    *   **Mediana Salarial:** Um pouco superior à da graduação, possivelmente em torno de R$9.000 - R$10.000.
    *   **Dispersão (IQR):** Semelhante ou ligeiramente maior que a da graduação, com salários centrais entre aproximadamente R$6.000 e R$14.000.
    *   **Outliers:** Também apresenta muitos outliers com salários elevados, ultrapassando R$40.000 em alguns casos.

4.  **Mestrado:**
    *   **Mediana Salarial:** Demonstra um novo aumento, situando-se em torno de R$10.000 - R$12.000.
    *   **Dispersão (IQR):** A caixa é ampla, indicando uma variabilidade salarial considerável, com os 50% centrais entre aproximadamente R$7.000 e R$15.000.
    *   **Outliers:** Vários outliers superiores, incluindo salários acima de R$20.000, R$30.000 e alguns próximos ou acima de R$40.000.

5.  **Doutorado ou Phd:**
    *   **Mediana Salarial:** A mais alta entre todos os níveis de ensino, posicionando-se em torno de R$12.000 - R$14.000.
    *   **Dispersão (IQR):** A caixa é bastante larga, indicando uma grande dispersão salarial. Os 50% centrais dos salários parecem estar entre R$8.000 e R$20.000.
    *   **Outliers:** Presença marcante de outliers com salários elevados, com vários profissionais superando R$30.000 e R$40.000. Há também um outlier inferior, próximo a R$0.

**Conclusões Gerais:**

*   **Valorização da Educação:** O gráfico evidencia uma tendência geral de aumento da mediana salarial conforme o nível de ensino aumenta. Profissionais com níveis de formação mais avançados, como Mestrado e Doutorado, tendem a ter medianas salariais mais altas.
*   **Aumento da Dispersão com Níveis Mais Altos:** A variabilidade salarial (largura da caixa e presença de outliers) também tende a ser maior nos níveis de ensino mais elevados. Isso sugere que, embora a mediana aumente, a faixa de salários possíveis também se amplia, especialmente para cima.
*   **Salto Salarial Pós-Graduação (Lato Sensu e Stricto Sensu):** Completar uma graduação representa um salto salarial significativo em relação ao status de estudante. Pós-graduações (incluindo especializações, mestrado e doutorado) continuam essa tendência de aumento na mediana salarial.
*   **Potencial de Alta Remuneração:** Em todos os níveis a partir da Graduação/Bacharelado, a existência de múltiplos outliers superiores indica que há profissionais que alcançam remunerações consideravelmente acima da média de seus respectivos grupos de escolaridade. Esse potencial parece se acentuar com o Doutorado.

Este gráfico sugere que o investimento em educação formal, particularmente em níveis mais avançados, está associado a um maior potencial de ganhos na área de dados.


## Grafico Salário Estimado por Experiência, Agrupado por Nível de Ensino
![catplot_salario_exp_facet_nivel_ensino](https://github.com/user-attachments/assets/71164ccd-585b-4354-8473-631eac8a4f02)
## Análise do Gráfico: Salário Estimado por Experiência, Agrupado por Nível de Ensino

O gráfico apresentado é um conjunto de boxplots (diagramas de caixa) que visualiza a interação entre "Tempo de Experiência" e "Nível de Ensino" na determinação do "Salário Estimado (R$)" dos profissionais de dados. O gráfico é facetado por "Nível de Ensino", o que significa que para cada nível de escolaridade, há uma série de boxplots mostrando a distribuição salarial para diferentes faixas de tempo de experiência.

**Elementos do Gráfico:**

*   **Título Principal:** "Salário Estimado por Experiência, Agrupado por Nível de Ensino".
*   **Facetas (Subgráficos):** Cada subgráfico representa um "Nível de Ensino" específico:
    *   Estudante de Graduação
    *   Graduação/Bacharelado
    *   Pós-graduação
    *   Mestrado
    *   Doutorado ou Phd
*   **Eixo Y (Vertical) de cada subgráfico:** "Salário Estimado (R$)", com escala de R$0 a R$40.000.
*   **Eixo X (Horizontal) de cada subgráfico:** "Tempo de Experiência". Embora as categorias exatas não estejam rotuladas individualmente no eixo x de cada faceta, a progressão das caixas da esquerda para a direita (e as cores distintas das caixas) dentro de cada subgráfico representa o aumento do tempo de experiência. Podemos inferir que são as mesmas faixas de experiência usadas em gráficos anteriores (ex: <1 ano, 1-2 anos, 3-4 anos, 5-6 anos, 7-10 anos, Mais de 10 anos).
*   **Boxplot (Diagrama de Caixa):** Para cada combinação de nível de ensino e faixa de experiência:
    *   A **linha horizontal dentro da caixa** indica a **mediana** salarial.
    *   A **caixa** representa o **intervalo interquartil (IQR)**, contendo os 50% centrais dos salários.
    *   Os **"bigodes" (whiskers)** mostram o alcance dos salários considerados típicos.
    *   Os **pontos individuais (losangos)** são **outliers**, indicando salários atipicamente altos ou baixos.

**Observações e Interpretações:**

**Tendência Geral Dentro de Cada Nível de Ensino:**

*   **Progressão Salarial com Experiência:** Em *todos* os níveis de ensino, há uma clara tendência de aumento da mediana salarial (a linha dentro da caixa) à medida que o tempo de experiência aumenta (movendo-se da esquerda para a direita dentro de cada subgráfico). Isso é visível pela subida geral das caixas.
*   **Aumento da Dispersão com Experiência:** Frequentemente, a dispersão salarial (altura da caixa e alcance dos bigodes/outliers) também aumenta com mais experiência. Isso significa que, entre os mais experientes, há uma variação salarial maior.

**Comparações Entre Níveis de Ensino para Faixas de Experiência Similares:**

1.  **Início de Carreira (Faixas de Menor Experiência - caixas à esquerda):**
    *   **Estudantes de Graduação:** Apresentam as menores medianas salariais em todas as faixas de experiência que participam.
    *   **Graduação/Bacharelado e Pós-graduação:** Para pouca experiência, as medianas salariais são semelhantes e mais altas que as dos estudantes. A pós-graduação parece oferecer uma ligeira vantagem inicial sobre apenas a graduação.
    *   **Mestrado e Doutorado:** Mesmo com pouca experiência, profissionais com mestrado e, especialmente, doutorado, tendem a ter medianas salariais iniciais mais altas em comparação com os níveis de ensino inferiores.

2.  **Meio de Carreira (Faixas de Experiência Intermediárias - caixas centrais):**
    *   A diferença salarial entre os níveis de ensino torna-se mais pronunciada.
    *   **Graduação/Bacharelado e Pós-graduação:** A pós-graduação continua a mostrar uma vantagem sobre a graduação.
    *   **Mestrado e Doutorado:** Apresentam medianas salariais consistentemente mais altas. Profissionais com doutorado, com experiência intermediária, já alcançam patamares salariais elevados.

3.  **Final de Carreira (Faixas de Maior Experiência - caixas à direita):**
    *   **Estudantes de Graduação:** Mesmo com mais experiência (se aplicável dentro do status de estudante), os salários permanecem os mais baixos.
    *   **Graduação/Bacharelado e Pós-graduação:** A progressão continua, mas as medianas tendem a ser superadas pelos níveis de mestrado e doutorado.
    *   **Mestrado:** Profissionais com mestrado e vasta experiência alcançam salários significativamente altos.
    *   **Doutorado ou Phd:** Este grupo, com alta experiência, apresenta as maiores medianas salariais e também uma dispersão muito grande, com outliers indicando salários excepcionalmente altos (alguns acima de R$40.000). A caixa para o maior nível de experiência em Doutorado é notavelmente alta.

**Interação entre Experiência e Nível de Ensino:**

*   **Benefício da Experiência é Universal:** A experiência aumenta o potencial salarial em todos os níveis de ensino.
*   **Nível de Ensino Potencializa o Efeito da Experiência:** O "retorno" da experiência parece ser maior para níveis de ensino mais altos. Ou seja, um ano adicional de experiência pode resultar em um aumento salarial proporcionalmente maior para quem tem mestrado ou doutorado em comparação com quem tem apenas graduação. Isso é visualizado pela inclinação mais acentuada da progressão salarial com a experiência nos níveis de ensino mais altos.
*   **Teto Salarial Mais Alto com Maior Escolaridade e Experiência:** Os salários mais altos no dataset (outliers superiores) são geralmente encontrados entre profissionais com níveis de ensino mais elevados (Mestrado, Doutorado) *e* mais tempo de experiência.

**Conclusões Gerais:**

Este gráfico é particularmente elucidativo ao mostrar que tanto a formação acadêmica quanto a experiência profissional são fatores cruciais na determinação salarial, e eles interagem de forma positiva.
*   Para alcançar os patamares salariais mais elevados na área de dados, a combinação de um alto nível de ensino (especialmente Mestrado ou Doutorado) com uma experiência profissional substancial parece ser o caminho mais promissor.
*   Enquanto a experiência por si só eleva os salários em todos os níveis de formação, o nível de formação parece definir diferentes "faixas" ou "tetos" potenciais de remuneração que são então explorados e alcançados através da experiência.


## Grafico Distribuição de Profissionais por Área de Formação Acadêmica
![distribuicao_area_formacao](https://github.com/user-attachments/assets/fd0d4cb9-5e30-4f52-8a7e-9cd074ee04c5)
## Análise do Gráfico: Distribuição de Profissionais por Área de Formação Acadêmica

O gráfico em anexo é um gráfico de barras horizontais que ilustra a "Distribuição de Profissionais por Área de Formação Acadêmica". Ele mostra a contagem de profissionais de dados provenientes de diferentes campos de estudo.

**Elementos do Gráfico:**

*   **Título:** "Distribuição de Profissionais por Área de Formação Acadêmica".
*   **Eixo Y (Vertical):** "Área de Formação". Lista as diversas áreas de formação acadêmica dos profissionais.
*   **Eixo X (Horizontal):** "Contagem". Indica o número de profissionais correspondente a cada área de formação, com a escala variando de 0 a mais de 1200.
*   **Barras Horizontais:** O comprimento de cada barra é proporcional à quantidade de profissionais com formação naquela área específica. As áreas estão ordenadas da maior para a menor contagem, de cima para baixo.

**Observações e Interpretações:**

1.  **Computação / Engenharia de Software / Sistemas de Informação/ TI:**
    *   Esta é, de longe, a área de formação mais comum entre os profissionais de dados no dataset, com uma contagem superior a 1200 profissionais. Isso indica uma forte predominância de backgrounds técnicos diretamente relacionados à computação e tecnologia da informação na área de dados.

2.  **Outras Engenharias:**
    *   A segunda área mais representativa, com aproximadamente 800 profissionais. Isso sugere que as habilidades analíticas e de resolução de problemas desenvolvidas em diversas engenharias são transferíveis e valorizadas no campo de dados.

3.  **Economia/ Administração / Contabilidade / Finanças/ Negócios:**
    *   Esta categoria ocupa a terceira posição, com cerca de 450 profissionais. Profissionais com formação em negócios e áreas correlatas trazem uma perspectiva de aplicação e valor de negócio para a análise de dados.

4.  **Estatística/ Matemática / Matemática Computacional/ Ciências Atuariais:**
    *   Com pouco mais de 200 profissionais, esta área, que possui fundamentos quantitativos essenciais para a ciência de dados, aparece em quarto lugar em termos de volume.

5.  **Outra opção:**
    *   Uma categoria genérica que agrupa formações não especificadas nas demais, com pouco menos de 200 profissionais.

6.  **Áreas Menos Representadas:**
    *   As demais áreas listadas apresentam contagens significativamente menores (abaixo de 100 profissionais cada):
        *   Química / Física
        *   Ciências Biológicas/ Farmácia/ Medicina/ Área da Saúde
        *   Marketing / Publicidade / Comunicação / Jornalismo
        *   Ciências Sociais
    *   Isso indica que, embora profissionais dessas áreas também atuem no campo de dados, eles representam uma parcela menor do total.

**Conclusões Gerais:**

*   **Predominância de Formações Técnicas e Quantitativas:** As áreas de Computação/TI, Engenharias e, em menor grau, Estatística/Matemática, dominam o cenário de formação dos profissionais de dados, o que é esperado dada a natureza técnica e analítica da área.
*   **Relevância de Formações em Negócios:** A presença significativa de profissionais com background em Economia, Administração e áreas afins destaca a importância do entendimento do contexto de negócios para a aplicação eficaz de técnicas de dados.
*   **Multidisciplinaridade Crescente, Mas Concentrada:** Embora a área de dados seja conhecida por sua multidisciplinaridade, este gráfico mostra que a maioria dos profissionais ainda provém de um conjunto relativamente concentrado de formações mais tradicionais para o setor de tecnologia e análise.
*   **Oportunidades para Diversas Formações:** A presença, mesmo que minoritária, de profissionais de áreas como Ciências Sociais, Saúde e Comunicação sugere que há espaço para diferentes perspectivas e habilidades no campo de dados, embora a transição possa ser menos comum ou exigir aquisição de habilidades técnicas adicionais.

Este gráfico oferece um panorama claro sobre as origens acadêmicas mais comuns dos profissionais que atualmente trabalham com dados, ressaltando a forte base em tecnologia e engenharias.


## Grafico Distribuição de Profissionais por Faixa Salarial Mensal
![distribuicao_faixa_salarial](https://github.com/user-attachments/assets/29688dff-55fd-492f-a897-ad9a4e89a657)
## Análise do Gráfico: Distribuição de Profissionais por Faixa Salarial Mensal

O gráfico apresentado é um gráfico de barras horizontais que ilustra a "Distribuição de Profissionais por Faixa Salarial Mensal". Ele mostra quantas pessoas se enquadram em cada faixa salarial.

**Elementos do Gráfico:**

*   **Título:** "Distribuição de Profissionais por Faixa Salarial Mensal".
*   **Eixo Y (Vertical):** "Faixa Salarial Mensal". Lista as diferentes faixas de salários mensais.
*   **Eixo X (Horizontal):** "Contagem". Indica o número de profissionais em cada faixa salarial, variando de 0 a 800.
*   **Barras Horizontais:** O comprimento de cada barra representa o número de profissionais naquela faixa salarial. As barras são organizadas verticalmente, com as faixas salariais mais baixas na parte superior e as mais altas na parte inferior.

**Observações e Interpretações:**

1.  **de R$8.001/mês a R$12.000/mês:**
    *   Esta é a faixa salarial com o maior número de profissionais, com uma contagem próxima a 800. Isso sugere que a maioria dos profissionais de dados no conjunto de dados ganha entre R$8.001 e R$12.000 por mês.

2.  **de R$12.001/mês a R$16.000/mês:**
    *   A segunda maior concentração está nesta faixa salarial, com uma contagem em torno de 400. Isso indica que muitos profissionais também ganham entre R$12.001 e R$16.000 por mês.

3.  **de R$6.001/mês a R$8.000/mês:**
    *   A terceira maior concentração está nesta faixa salarial, com uma contagem também em torno de 550.

4.  **de R$3.001/mês a R$4.000/mês:**
    *   A contagem é aproximadamente 300.

5.  **de R$4.001/mês a R$6.000/mês:**
    *   A contagem é aproximadamente 300.

6.  **de R$2.001/mês a R$3.000/mês:**
    *   A contagem é aproximadamente 200.

7.  **de R$1.001/mês a R$2.000/mês:**
    *   A contagem é pouco acima de 100.

8.  **Faixas Salariais Mais Altas (de R$16.001/mês a Acima de R$40.001/mês):**
    *   As faixas salariais mais altas apresentam contagens progressivamente menores. Isso indica que há menos profissionais ganhando salários mais elevados.
    *   As faixas de R$16.001/mês a R$20.000/mês e de R$20.001/mês a R$25.000/mês são as mais representadas entre as faixas salariais mais altas.

9.  **Menos de R$1.000/mês:**
    *   A menor contagem é para essa categoria, indicando que poucos profissionais ganham menos de R$1.000 por mês.

**Conclusões Gerais:**

*   **Concentração em Faixas Salariais Intermediárias:** A maioria dos profissionais de dados neste conjunto de dados se concentra nas faixas salariais entre R$6.001 e R$16.000 por mês.
*   **Distribuição Assimétrica:** A distribuição salarial é assimétrica, com uma cauda longa para a direita, indicando que, embora a maioria ganhe entre R$6.001 e R$16.000, alguns profissionais ganham significativamente mais.
*   **Minoria nas Faixas Mais Baixas:** Poucos profissionais relatam ganhar menos de R$2.000 por mês.

Este gráfico fornece uma visão geral da distribuição de salários entre os profissionais de dados, mostrando onde a maioria se concentra e como os salários se distribuem nas faixas mais altas e mais baixas.


## Grafico Distribuição de Profissionais por Nível de Ensino
![distribuicao_nivel_ensino](https://github.com/user-attachments/assets/044e5446-b6bd-474d-86d4-3c8a94ca44c7)
## Análise do Gráfico: Distribuição de Profissionais por Nível de Ensino

O gráfico anexado é um gráfico de barras horizontais que mostra a "Distribuição de Profissionais por Nível de Ensino". Ele quantifica o número de profissionais de dados em diferentes estágios de sua formação acadêmica.

**Elementos do Gráfico:**

*   **Título:** "Distribuição de Profissionais por Nível de Ensino".
*   **Eixo Y (Vertical):** "Nível de Ensino". Lista as categorias de escolaridade dos profissionais:
    *   Estudante de Graduação
    *   Graduação/Bacharelado
    *   Pós-graduação
    *   Mestrado
    *   Doutorado ou Phd
*   **Eixo X (Horizontal):** "Contagem". Indica o número de profissionais correspondente a cada nível de ensino, com a escala variando de 0 a 1200.
*   **Barras Horizontais:** O comprimento de cada barra é proporcional à quantidade de profissionais com aquele nível de ensino. As categorias estão ordenadas de cima para baixo, aparentemente refletindo uma progressão no nível educacional.

**Observações e Interpretações:**

1.  **Graduação/Bacharelado:**
    *   Esta é a categoria com o maior número de profissionais, ultrapassando a marca de 1200. Isso indica que a maioria dos profissionais de dados no dataset possui, no mínimo, um diploma de graduação completo.

2.  **Pós-graduação:**
    *   A segunda maior concentração de profissionais está neste nível, com uma contagem superior a 1000, mas inferior à da graduação (aproximadamente 1050). Este grupo inclui provavelmente especializações e MBAs (pós-graduação lato sensu).

3.  **Estudante de Graduação:**
    *   Este grupo representa a terceira maior contagem, com aproximadamente 450 profissionais. Isso mostra uma presença significativa de indivíduos que ainda estão cursando a graduação, mas já atuam na área de dados.

4.  **Mestrado:**
    *   Profissionais com mestrado (pós-graduação stricto sensu) somam cerca de 350, representando o quarto maior grupo.

5.  **Doutorado ou Phd:**
    *   Este é o grupo com a menor representatividade, com uma contagem de aproximadamente 100 profissionais. Embora seja o nível de ensino mais alto, é o menos comum entre os profissionais de dados no dataset.

**Conclusões Gerais:**

*   **Base Educacional Sólida:** A grande maioria dos profissionais de dados possui pelo menos uma graduação completa, com um número expressivo também tendo concluído algum tipo de pós-graduação (lato sensu ou stricto sensu).
*   **Entrada Precoce no Mercado:** A presença considerável de estudantes de graduação sugere que muitos iniciam suas carreiras na área de dados antes mesmo de concluir a formação universitária inicial.
*   **Funil Educacional:** Observa-se um afunilamento no número de profissionais à medida que o nível de ensino se torna mais avançado (Mestrado e, especialmente, Doutorado). Isso é comum em diversas áreas, refletindo o menor número de pessoas que prosseguem para os níveis mais altos de qualificação acadêmica.
*   **Valorização de Diferentes Níveis:** O gráfico demonstra que há profissionais de dados em todos os principais níveis de ensino, desde estudantes até doutores, indicando que o mercado absorve talentos com diferentes graus de formação.

Este gráfico oferece uma visão clara do perfil educacional dos profissionais de dados, destacando a importância da graduação e da pós-graduação, ao mesmo tempo que mostra a participação de estudantes e o menor, porém qualificado, contingente de mestres e doutores.


## Grafico Distribuição do Salário Estimado (R$)
![distribuicao_salario_estimado](https://github.com/user-attachments/assets/cb8d3675-ed41-4fcb-bf09-7f1c8b69cda4)
## Análise do Gráfico: Distribuição do Salário Estimado (R$)

O gráfico anexado é um histograma que representa a "Distribuição do Salário Estimado (R$)" dos profissionais de dados. Ele mostra a frequência de profissionais em diferentes intervalos de salário estimado.

**Elementos do Gráfico:**

*   **Título:** "Distribuição do Salário Estimado (R$)".
*   **Eixo Y (Vertical):** "Frequência". Indica o número de profissionais (contagem) para cada intervalo de salário. A escala vai de 0 a mais de 800.
*   **Eixo X (Horizontal):** "Salário Estimado (R$)". Representa os valores dos salários estimados em Reais, agrupados em intervalos (bins). A escala vai de R$0 a mais de R$40.000.
*   **Barras (Histograma):** A altura de cada barra corresponde à frequência (número de profissionais) cujo salário estimado cai dentro do intervalo (bin) que a barra representa.
*   **Linha Azul (Estimativa de Densidade do Kernel - KDE):** Sobreposta às barras, há uma linha curva suave que representa uma estimativa da função de densidade de probabilidade da distribuição dos salários. Ela ajuda a visualizar a forma geral da distribuição.

**Observações e Interpretações:**

1.  **Picos Principais (Modas):**
    *   O gráfico exibe uma distribuição multimodal, com pelo menos dois picos proeminentes.
    *   O primeiro pico, e o mais alto, ocorre na faixa salarial em torno de R$4.000 - R$6.000 (aproximadamente), onde a frequência ultrapassa 900 profissionais.
    *   O segundo pico significativo está na faixa de R$10.000 - R$12.000 (aproximadamente), com uma frequência em torno de 800 profissionais.
    *   Um terceiro pico menor, mas notável, aparece em torno de R$14.000 - R$16.000, com frequência próxima a 400.

2.  **Concentração de Salários:**
    *   A maioria dos profissionais parece se concentrar nas faixas salariais abaixo de R$16.000, com as maiores concentrações nos dois primeiros picos mencionados.

3.  **Cauda à Direita (Assimetria Positiva):**
    *   A distribuição é assimétrica à direita (ou positivamente assimétrica). Isso significa que, embora a maioria dos salários esteja concentrada nas faixas mais baixas e médias, há uma "cauda" de profissionais que recebem salários consideravelmente mais altos, estendendo-se para além de R$20.000, R$30.000 e até R$40.000. As frequências nessas faixas mais altas são progressivamente menores.

4.  **Intervalos de Salário:**
    *   A primeira barra, de R$0 a aproximadamente R$2.500, tem uma frequência em torno de 400.
    *   Após o pico principal em torno de R$5.000, há uma queda na frequência antes de subir novamente para o segundo pico em torno de R$11.000.
    *   Depois do terceiro pico em torno de R$15.000, as frequências diminuem consideravelmente, indicando que menos profissionais se encontram nas faixas salariais mais elevadas.

**Conclusões Gerais:**

*   **Distribuição Salarial Heterogênea:** A presença de múltiplos picos sugere que pode haver subgrupos distintos dentro da população de profissionais de dados com diferentes níveis salariais predominantes. Isso pode ser influenciado por fatores como nível de experiência, área de atuação, nível de ensino, região geográfica, etc.
*   **Maioria em Faixas Médias-Baixas:** Uma grande proporção dos profissionais aufere salários nas faixas que vão até aproximadamente R$16.000, com picos notáveis em torno de R$5.000 e R$11.000.
*   **Potencial para Altos Salários:** A cauda longa à direita indica que, embora menos comuns, existem salários significativamente altos na área de dados, ultrapassando R$40.000.
*   **Necessidade de Análise Multivariada:** A forma multimodal do histograma sugere que analisar apenas a distribuição geral do salário pode não contar a história completa. Seria interessante investigar quais fatores contribuem para os diferentes picos observados, como feito nas análises anteriores que segmentaram por experiência e nível de ensino.

Este histograma fornece uma visão geral da estrutura salarial dos profissionais de dados, destacando as faixas de remuneração mais comuns e a existência de um segmento com ganhos consideravelmente mais altos.


## Grafico Distribuição de Profissionais por Tempo de Experiência em Dados
![distribuicao_tempo_experiencia](https://github.com/user-attachments/assets/986f2138-2838-4ff8-ae15-8495f36f0728)
## Análise do Gráfico: Distribuição de Profissionais por Tempo de Experiência em Dados

O gráfico anexado é um gráfico de barras horizontais que ilustra a "Distribuição de Profissionais por Tempo de Experiência em Dados". Ele mostra o número de profissionais de dados classificados em diferentes faixas de tempo de experiência na área.

**Elementos do Gráfico:**

*   **Título:** "Distribuição de Profissionais por Tempo de Experiência em Dados".
*   **Eixo Y (Vertical):** "Tempo de Experiência". Apresenta as seguintes categorias de tempo de atuação profissional na área de dados:
    *   Menos de 1 ano
    *   de 1 a 2 anos
    *   de 3 a 4 anos
    *   de 5 a 6 anos
    *   de 7 a 10 anos
    *   Mais de 10 anos
*   **Eixo X (Horizontal):** "Contagem". Indica o número de profissionais correspondente a cada faixa de experiência, com a escala variando de 0 a mais de 1000.
*   **Barras Horizontais:** O comprimento de cada barra é proporcional à quantidade de profissionais naquela faixa de experiência específica. As barras estão ordenadas de cima para baixo, começando com a menor experiência e progredindo para a maior.

**Observações e Interpretações por Faixa de Experiência:**

1.  **de 1 a 2 anos:**
    *   Esta é a faixa com o maior número de profissionais, com uma contagem superior a 1000 (aproximadamente 1050-1100). Isso sugere que uma grande parcela dos profissionais de dados no dataset possui uma experiência relativamente inicial, mas já consolidada, na área.

2.  **de 3 a 4 anos:**
    *   A segunda maior concentração de profissionais está nesta faixa, com uma contagem próxima a 950. Juntamente com a faixa anterior, indica que a maioria dos profissionais tem entre 1 e 4 anos de experiência.

3.  **Menos de 1 ano:**
    *   Profissionais com menos de um ano de experiência representam o terceiro maior grupo, com uma contagem em torno de 400. Isso mostra um contingente significativo de recém-chegados à área.

4.  **de 5 a 6 anos:**
    *   A contagem de profissionais nesta faixa é de aproximadamente 250-280, indicando um número menor de profissionais com este nível de experiência intermediária mais longa.

5.  **de 7 a 10 anos:**
    *   Esta faixa possui uma contagem similar à anterior, em torno de 250-280 profissionais.

6.  **Mais de 10 anos:**
    *   Este é o grupo com a menor representatividade, com uma contagem visivelmente inferior às demais, parecendo ser inferior a 100 (talvez em torno de 50-80). Isso indica que profissionais com vasta experiência (mais de uma década) na área de dados são menos comuns no dataset, o que pode refletir a relativa novidade da área de "dados" como um campo formalizado ou a nomenclatura utilizada.

**Conclusões Gerais:**

*   **Concentração em Níveis Iniciais e Intermediários de Experiência:** A maioria dos profissionais de dados no dataset possui entre 1 e 4 anos de experiência, com um número também considerável de iniciantes (menos de 1 ano).
*   **Menor Representatividade de Profissionais Altamente Experientes:** Há um declínio no número de profissionais à medida que o tempo de experiência aumenta, sendo que aqueles com mais de 10 anos de experiência são os menos numerosos.
*   **Perfil da Área de Dados:** A distribuição pode sugerir que a área de dados, como campo profissional distinto, tem crescido rapidamente nos últimos anos, resultando em muitos profissionais com menos anos de experiência específica "em dados". Também pode indicar uma alta rotatividade ou transição para outras funções após alguns anos.
*   **Formato de Funil:** A distribuição se assemelha a um funil, onde muitos entram na área, mas o número de profissionais diminui nas faixas de experiência mais longas.

Este gráfico fornece uma visão clara do perfil de experiência dos profissionais de dados, destacando uma concentração maior nos estágios iniciais e intermediários da carreira na área.


## Grafico Top 10 UF de Residência dos Profissionais de Dados
![distribuicao_top10_uf](https://github.com/user-attachments/assets/1cf90782-fb39-475d-b70e-ac4b18bb3f7d)
## Análise do Gráfico: Top 10 UF de Residência dos Profissionais de Dados

O gráfico em anexo é um gráfico de barras verticais que apresenta o "Top 10 UF de Residência dos Profissionais de Dados". Ele mostra a contagem de profissionais de dados que residem nas dez Unidades Federativas (estados) com maior representatividade no dataset.

**Elementos do Gráfico:**

*   **Título:** "Top 10 UF de Residência dos Profissionais de Dados".
*   **Eixo Y (Vertical):** "Contagem". Indica o número de profissionais de dados, com a escala variando de 0 a mais de 1200.
*   **Eixo X (Horizontal):** "UF". Apresenta as siglas das Unidades Federativas. As UFs estão ordenadas da esquerda para a direita, da maior para a menor contagem de profissionais.
*   **Barras Verticais:** A altura de cada barra é proporcional ao número de profissionais de dados que residem naquela UF. As barras possuem diferentes tonalidades de azul, possivelmente para melhor distinção visual ou para indicar uma hierarquia, embora a ordenação já cumpra essa função.

**Observações e Interpretações por UF:**

1.  **SP (São Paulo):**
    *   Destaca-se como a UF com a maior concentração de profissionais de dados, com uma contagem muito superior às demais, ultrapassando 1200 (aproximadamente 1300 profissionais). Isso indica que São Paulo é o principal polo de profissionais de dados no Brasil, de acordo com este dataset.

2.  **MG (Minas Gerais):**
    *   A segunda UF com mais profissionais, com uma contagem em torno de 350-380. Embora seja um número significativo, é consideravelmente menor que o de São Paulo.

3.  **PR (Paraná):**
    *   Ocupa a terceira posição, com uma contagem próxima a 300 profissionais.

4.  **RJ (Rio de Janeiro):**
    *   Apresenta uma contagem muito similar à do Paraná, também em torno de 290-300 profissionais, posicionando-se como o quarto estado com mais profissionais de dados.

5.  **RS (Rio Grande do Sul):**
    *   A contagem de profissionais é de aproximadamente 180.

6.  **SC (Santa Catarina):**
    *   Possui uma contagem ligeiramente inferior ao RS, em torno de 160-170 profissionais.

7.  **DF (Distrito Federal):**
    *   Apresenta uma contagem próxima a 90-100 profissionais.

8.  **BA (Bahia), CE (Ceará), PE (Pernambuco):**
    *   Estas três UFs da região Nordeste encerram o top 10, com contagens menores e relativamente próximas entre si, todas abaixo de 100 (aproximadamente entre 70 e 85 profissionais cada).

**Conclusões Gerais:**

*   **Concentração Regional Sudeste-Sul:** A grande maioria dos profissionais de dados está concentrada na região Sudeste (SP, MG, RJ) e Sul (PR, RS, SC), com São Paulo liderando de forma proeminente.
*   **Disparidade Geográfica:** Existe uma notável disparidade na distribuição geográfica dos profissionais de dados, com um número muito maior de profissionais em São Paulo em comparação com todos os outros estados.
*   **Presença em Outras Regiões:** Embora em menor número, o Distrito Federal (Centro-Oeste) e estados do Nordeste (BA, CE, PE) também figuram no top 10, indicando a presença de polos de profissionais de dados nessas regiões, ainda que menos expressivos em volume.
*   **Implicações para o Mercado:** Essa concentração pode refletir onde estão as maiores oportunidades de emprego, os principais centros de formação ou os ecossistemas de inovação e tecnologia mais desenvolvidos no país.

Este gráfico fornece uma visão clara da distribuição geográfica dos profissionais de dados no Brasil, destacando a liderança de São Paulo e a importância das regiões Sudeste e Sul como principais centros para esses profissionais.


## Grafico Heatmap de Correlação entre Salário, Experiência (anos) e Nível de Ensino (ordinal)
![heatmap_correlacao_salario_exp_ensino](https://github.com/user-attachments/assets/2cd9887a-0a1d-4c89-b513-3a852d07b35c)
## Análise do Gráfico: Heatmap de Correlação entre Salário, Experiência (anos) e Nível de Ensino (ordinal)

O gráfico apresentado é um heatmap (mapa de calor) que visualiza a matriz de correlação entre três variáveis quantitativas: "Salário Estimado", "Experiência (anos) Estimados" e "Nível de Ensino (ordinal)". Este tipo de gráfico utiliza cores para representar a força e a direção das correlações lineares entre pares de variáveis.

**Elementos do Gráfico:**

*   **Título:** "Heatmap de Correlação entre Salário, Experiência (anos) e Nível de Ensino (ordinal)".
*   **Eixos (Linhas e Colunas):** As mesmas três variáveis são listadas tanto nas linhas quanto nas colunas:
    *   Salario_Estimado
    *   Experiencia_Anos_Estimados
    *   Nivel_Ensino_Ordinal
*   **Células da Matriz:** Cada célula na interseção de uma linha e uma coluna mostra o coeficiente de correlação de Pearson entre as duas variáveis correspondentes. O valor do coeficiente é exibido numericamente dentro da célula.
*   **Escala de Cores (Barra Lateral):** À direita do heatmap, uma barra de cores indica como os valores de correlação são mapeados para as cores. A escala varia de aproximadamente 0.2 (azul escuro) a 1.0 (vermelho escuro).
    *   Cores mais quentes (tendendo ao vermelho) indicam correlações positivas mais fortes.
    *   Cores mais frias (tendendo ao azul) indicam correlações positivas mais fracas (neste caso, todas as correlações são positivas).
    *   Se houvesse correlações negativas, elas normalmente seriam representadas por uma gama diferente de cores.

**Interpretação dos Coeficientes de Correlação:**

Os coeficientes de correlação variam de -1 a +1:
*   +1 indica uma correlação linear positiva perfeita.
*   -1 indica uma correlação linear negativa perfeita.
*   0 indica ausência de correlação linear.
*   Valores próximos de +1 ou -1 indicam correlações fortes, enquanto valores próximos de 0 indicam correlações fracas.

**Análise das Correlações Específicas:**

1.  **Diagonal Principal (Vermelho Escuro - Valor 1.00):**
    *   Salario_Estimado com Salario_Estimado: 1.00
    *   Experiencia_Anos_Estimados com Experiencia_Anos_Estimados: 1.00
    *   Nivel_Ensino_Ordinal com Nivel_Ensino_Ordinal: 1.00
    *   Isso é esperado, pois a correlação de qualquer variável consigo mesma é sempre perfeita e positiva.

2.  **Salario_Estimado vs. Experiencia_Anos_Estimados:**
    *   Coeficiente: 0.53
    *   Cor: Azul claro, tendendo para o centro da escala.
    *   Interpretação: Existe uma correlação positiva moderada entre o salário estimado e os anos de experiência. Isso sugere que, de forma geral, à medida que os anos de experiência aumentam, o salário estimado também tende a aumentar.

3.  **Salario_Estimado vs. Nivel_Ensino_Ordinal:**
    *   Coeficiente: 0.30
    *   Cor: Azul médio.
    *   Interpretação: Há uma correlação positiva fraca a moderada entre o salário estimado e o nível de ensino ordinal. Isso indica que, em geral, níveis de ensino mais altos estão associados a salários estimados mais altos, mas a relação é menos forte do que a observada com a experiência.

4.  **Experiencia_Anos_Estimados vs. Nivel_Ensino_Ordinal:**
    *   Coeficiente: 0.24
    *   Cor: Azul mais escuro, na parte inferior da escala de cores.
    *   Interpretação: Existe uma correlação positiva fraca entre os anos de experiência estimados e o nível de ensino ordinal. Isso pode sugerir uma leve tendência de que profissionais com níveis de ensino mais altos também possam ter um pouco mais de tempo de experiência, ou vice-versa, mas a relação é bastante tênue.

**Conclusões Gerais:**

*   **Influência da Experiência no Salário:** A experiência profissional ("Experiencia_Anos_Estimados") apresenta a correlação positiva mais forte com o salário ("Salario_Estimado") entre as variáveis analisadas (0.53), indicando que é um fator importante associado à remuneração.
*   **Influência do Nível de Ensino no Salário:** O nível de ensino ("Nivel_Ensino_Ordinal") também tem uma correlação positiva com o salário (0.30), mas essa relação é menos acentuada do que a da experiência.
*   **Relação entre Experiência e Nível de Ensino:** A correlação entre experiência e nível de ensino é a mais fraca entre os pares (0.24), sugerindo que esses dois fatores, embora ambos influenciem o salário, não estão fortemente interligados entre si no dataset.

Este heatmap fornece uma visão concisa de como essas três variáveis chave estão linearmente relacionadas, destacando a importância da experiência e, em menor grau, do nível de ensino, na determinação do salário estimado dos profissionais de dados.


## Grafico Salário Médio Estimado vs. Anos de Experiência por Nível de Ensino
![lineplot_salario_exp_por_nivel_ensino](https://github.com/user-attachments/assets/8e847b68-732a-4df6-ac5f-3abde32e4245)
## Análise do Gráfico: Salário Médio Estimado vs. Anos de Experiência por Nível de Ensino

O gráfico apresentado é um gráfico de linhas que ilustra a relação entre o "Salário Médio Estimado (R$)" e os "Anos de Experiência Estimados", segmentado por "Nível de Ensino". Cada linha representa um nível de formação acadêmica diferente, mostrando como a trajetória salarial se desenvolve com o aumento da experiência para cada grupo.

**Elementos do Gráfico:**

*   **Título:** "Salário Médio Estimado vs. Anos de Experiência por Nível de Ensino".
*   **Eixo Y (Vertical):** "Salário Médio Estimado (R$)", com a escala variando de R$2.500 a R$22.500.
*   **Eixo X (Horizontal):** "Anos de Experiência Estimados", variando de aproximadamente 0.5 (representando "Menos de 1 ano") até 8 anos (representando "de 7 a 10 anos", e possivelmente agrupando "Mais de 10 anos" no ponto final, embora a imagem corte antes de mostrar o extremo dos 10+ anos de forma explícita).
*   **Linhas Coloridas:** Cada linha representa um "Nível de Ensino" diferente, conforme a legenda:
    *   **Azul escuro/Roxo:** Estudante de Graduação
    *   **Azul médio:** Graduação/Bacharelado
    *   **Verde-azulado (Turquesa):** Pós-graduação
    *   **Verde:** Mestrado
    *   **Verde claro (Lima):** Doutorado ou Phd
*   **Pontos nas Linhas:** Marcam os valores médios de salário para faixas específicas de experiência dentro de cada nível de ensino.
*   **Áreas Sombreadas (Intervalos de Confiança):** As faixas coloridas translúcidas ao redor de cada linha provavelmente representam intervalos de confiança para o salário médio estimado. Isso indica a variabilidade ou incerteza em torno da média estimada; quanto mais larga a faixa, maior a incerteza ou dispersão dos dados.

**Observações e Interpretações:**

1.  **Progressão Salarial com Experiência (Geral):**
    *   Para *todos* os níveis de ensino, há uma clara tendência ascendente: o salário médio estimado aumenta consistentemente com o aumento dos anos de experiência. As linhas sobem da esquerda para a direita.

2.  **Impacto do Nível de Ensino no Salário Inicial (Ponto de Partida):**
    *   Mesmo com pouca ou nenhuma experiência (extrema esquerda do gráfico), os níveis de ensino mais altos tendem a começar com salários médios estimados mais elevados.
        *   "Doutorado ou Phd" e "Mestrado" iniciam com os maiores salários médios, seguidos por "Pós-graduação", "Graduação/Bacharelado", e por último "Estudante de Graduação".

3.  **Diferenças Salariais Ampliadas com a Experiência:**
    *   As linhas tendem a se divergir mais à medida que os anos de experiência aumentam. Isso significa que a diferença salarial entre os níveis de ensino se torna mais pronunciada para profissionais mais experientes.
    *   Por exemplo, a diferença salarial entre um "Doutorado ou Phd" e um "Graduado/Bacharel" com 1 ano de experiência é menor do que a diferença entre esses mesmos dois níveis com 5 ou 8 anos de experiência.

4.  **Hierarquia dos Níveis de Ensino:**
    *   Ao longo da maior parte da trajetória de experiência, a hierarquia salarial geralmente segue a ordem do nível de ensino: Doutorado > Mestrado > Pós-graduação > Graduação > Estudante de Graduação.
    *   Há um cruzamento ou proximidade muito grande entre as linhas de "Graduação/Bacharelado" e "Pós-graduação" em certos pontos, sugerindo que, para algumas faixas de experiência, a diferença salarial média entre ter apenas graduação e ter uma pós-graduação (lato sensu, provavelmente) pode não ser tão acentuada como a diferença para mestrado ou doutorado.

5.  **Retorno da Experiência por Nível de Ensino:**
    *   As inclinações das linhas sugerem que o "retorno" por ano adicional de experiência pode variar entre os níveis de ensino. As linhas para "Doutorado ou Phd" e "Mestrado" parecem ter inclinações consistentemente acentuadas, indicando um forte crescimento salarial com a experiência.

6.  **Variabilidade (Áreas Sombreadas):**
    *   As áreas sombreadas para "Doutorado ou Phd" e "Mestrado", especialmente nos níveis mais altos de experiência, parecem ser mais largas. Isso pode indicar uma maior variabilidade nos salários para esses grupos (ou seja, alguns doutores/mestres experientes ganham muito bem, enquanto outros podem ter salários mais próximos dos demais grupos, aumentando a dispersão) ou menor número de amostras nessas categorias, levando a maior incerteza na estimativa da média.
    *   A faixa para "Estudante de Graduação" é consistentemente a mais baixa e parece ter uma variabilidade relativamente menor em comparação com os níveis superiores.

**Conclusões Gerais:**

*   **Valorização da Experiência e Educação:** O gráfico demonstra claramente que tanto o tempo de experiência quanto o nível de ensino são fatores cruciais que influenciam positivamente o salário médio estimado dos profissionais de dados.
*   **Efeito Combinado:** O maior potencial salarial é observado em profissionais que combinam um alto nível de ensino (Mestrado ou Doutorado) com um volume significativo de anos de experiência.
*   **Investimento em Educação:** Níveis mais altos de educação formal tendem a proporcionar um ponto de partida salarial mais elevado e mantêm uma trajetória de crescimento salarial superior ao longo da carreira, em média.

Este gráfico sintetiza de forma eficaz como a formação acadêmica e a experiência profissional interagem para moldar a progressão salarial na área de dados, reforçando a importância de ambos os fatores para o desenvolvimento de carreira e potencial de ganhos.


## Grafico Relação 3D entre Salário, Experiência e Nível de Ensino
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/c8f65f4a0c3ba1736c5a2687f8a7c448/raw/b83fdbae94c7706b5fbc5cd2215d132558201ddb/scatter3d_salario_exp_ensino.html)
![newplot(2)](https://github.com/user-attachments/assets/ec28770a-f3a3-4129-b517-f0fc40afd8f1)
## Análise do Gráfico: Relação 3D entre Salário, Experiência e Nível de Ensino

O gráfico interativo apresentado é um gráfico de dispersão 3D (3D Scatter Plot) que visualiza a relação entre três variáveis principais: "Salário Estimado (R$)", "Experiência (Anos Estimados)" e "Nível de Ensino (Ordinal)". Cada ponto no espaço tridimensional representa um profissional de dados.

**Elementos do Gráfico:**

*   **Eixos:**
    *   **Eixo X (Horizontal, profundidade):** "Experiencia_Anos_Estimados". Este eixo representa o tempo de experiência profissional em anos, variando de aproximadamente 0.5 (menos de 1 ano) até 10.0 (mais de 10 anos).
    *   **Eixo Y (Horizontal, largura):** "Nivel_Ensino_Ordinal". Este eixo representa o nível de formação acadêmica de forma ordinal, onde valores menores indicam níveis de ensino mais básicos (0 para Estudante de Graduação) e valores maiores indicam níveis mais avançados (4 para Doutorado ou Phd).
    *   **Eixo Z (Vertical, altura):** "Salario_Estimado". Este eixo representa a remuneração estimada em Reais, variando de R$0 até mais de R$40.000.
*   **Pontos de Dados:** Cada ponto (esfera) no gráfico representa um profissional individual no dataset, posicionado de acordo com seus valores nas três variáveis mencionadas.
*   **Cor dos Pontos (Nivel_Ensino_Ordinal):** Os pontos são coloridos de acordo com o "Nivel_Ensino_Ordinal", facilitando a identificação de grupos com diferentes níveis de formação. A legenda de cores normalmente acompanha esse tipo de gráfico (embora não visível estaticamente na imagem fornecida, é um padrão em gráficos interativos como os do Plotly):
    *   Estudante de Graduação (Ordinal 0): Cor específica (ex: azul)
    *   Graduação/Bacharelado (Ordinal 1): Outra cor (ex: laranja)
    *   Pós-graduação (Ordinal 2): Outra cor (ex: verde)
    *   Mestrado (Ordinal 3): Outra cor (ex: vermelho)
    *   Doutorado ou Phd (Ordinal 4): Outra cor (ex: roxo)

**Observações e Interpretações (Baseadas na Interação Típica com Gráficos 3D):**

1.  **Concentração de Pontos:**
    *   Observa-se uma maior concentração de pontos nas regiões de menor "Salario_Estimado", especialmente para níveis de ensino mais baixos e menor tempo de experiência.
    *   À medida que o "Nivel_Ensino_Ordinal" e a "Experiencia_Anos_Estimados" aumentam (movendo-se para "cima" no eixo Y e para "frente" no eixo X), os pontos tendem a se posicionar mais alto no eixo Z ("Salario_Estimado").

2.  **Tendência Geral:**
    *   Há uma tendência visual clara de que salários mais altos (pontos mais altos no eixo Z) estão associados a combinações de maior experiência e/ou níveis de ensino mais elevados.
    *   A "nuvem" de pontos parece se inclinar para cima à medida que se avança nos eixos de experiência e nível de ensino.

3.  **Impacto Combinado de Experiência e Nível de Ensino:**
    *   **Baixa Experiência, Qualquer Nível de Ensino:** Profissionais com pouca experiência (próximo ao plano traseiro do gráfico) geralmente apresentam salários mais baixos, mesmo aqueles com níveis de ensino mais altos (ex: Doutorado com pouca experiência pode ter salário menor que um Graduado com muita experiência).
    *   **Alta Experiência, Nível de Ensino Variado:** Profissionais com muita experiência (próximo ao plano frontal) mostram uma ampla gama de salários. No entanto, dentro desse grupo de alta experiência, aqueles com níveis de ensino mais altos (cores associadas a Mestrado/Doutorado) tendem a alcançar os patamares salariais mais elevados.
    *   **Nível de Ensino Alto, Experiência Variada:** Profissionais com Doutorado (cor específica, ordinal 4), por exemplo, estão espalhados ao longo do eixo de experiência. Aqueles com mais experiência nesse grupo tendem a ter os salários mais altos do dataset.

4.  **Visualização de Outliers:**
    *   O gráfico 3D permite identificar visualmente outliers – profissionais que, por exemplo, têm um salário muito alto para seu nível de experiência e ensino, ou vice-versa. Esses pontos se destacariam da "nuvem" principal.

5.  **Interatividade:**
    *   A natureza interativa desses gráficos (possibilidade de girar, dar zoom) é crucial para uma exploração completa. Girar o gráfico permite observar a relação entre pares de variáveis, mantendo a terceira como referência, ou identificar clusters e padrões que não seriam óbvios em visualizações 2D separadas.

**Conclusões Gerais:**

*   O gráfico de dispersão 3D reforça as conclusões de análises 2D anteriores: tanto a experiência profissional quanto o nível de formação acadêmica são fatores importantes que influenciam positivamente o salário estimado dos profissionais de dados.
*   A visualização tridimensional destaca a **interação** entre esses dois fatores. Para alcançar os salários mais altos, geralmente é necessária uma combinação de alto nível de ensino *e* experiência substancial.
*   Profissionais com níveis de ensino mais baixos, mesmo com muita experiência, podem ter um "teto" salarial inferior ao de profissionais com formação mais avançada e experiência similar.
*   Da mesma forma, profissionais com alta formação, mas pouca experiência, podem não atingir os salários mais elevados até que acumulem mais tempo de atuação no mercado.

Este tipo de visualização é poderoso para entender relações multivariadas complexas, mostrando como diferentes fatores se combinam para influenciar um resultado, neste caso, o salário.


## Grafico Salário Estimado vs. Proporção de Docentes com Doutorado na UF de Residência
![scatterplot_salario_vs_prop_doc_doutorado_uf](https://github.com/user-attachments/assets/004cf9f3-3691-4536-aa8a-ae2a9ec938e9)
## Análise do Gráfico: Salário Estimado vs. Proporção de Docentes com Doutorado na UF de Residência

O gráfico apresentado é um gráfico de dispersão (scatter plot) que busca explorar a relação entre o "Salário Estimado (R$)" dos profissionais de dados e a "Proporção de Docentes com Doutorado na UF de Residência". Adicionalmente, os pontos no gráfico são codificados por cor para representar o "Nível de ensino alcançado" e por tamanho para indicar os "Experiencia_Anos_Estimados".

**Elementos do Gráfico:**

*   **Título:** "Salário Estimado vs. Proporção de Docentes com Doutorado na UF de Residência".
*   **Eixo Y (Vertical):** "Salário Estimado (R$)", com escala de R$0 até mais de R$40.000.
*   **Eixo X (Horizontal):** "Proporção de Docentes com Doutorado na UF de Residência", variando aproximadamente de 0.30 a pouco mais de 0.60. Este eixo representa a fração de docentes em uma determinada Unidade Federativa que possuem doutorado.
*   **Pontos de Dados:** Cada ponto representa um profissional de dados.
    *   **Cor (Nível de ensino alcançado):** Conforme a legenda:
        *   Verde claro/Turquesa: Estudante de Graduação
        *   Laranja: Graduação/Bacharelado
        *   Azul: Pós-graduação
        *   Roxo/Rosa: Mestrado
        *   Verde escuro: Doutorado ou Phd
    *   **Tamanho (Experiencia_Anos_Estimados):** Pontos maiores indicam maior tempo de experiência (0.5, 1.5, 3.5, 5.5, 8.5 anos estimados), conforme a legenda.

**Observações e Interpretações:**

1.  **Dispersão Geral dos Pontos:**
    *   Os pontos estão amplamente dispersos pelo gráfico, não formando um padrão linear claro (positivo ou negativo) entre a proporção de docentes com doutorado na UF e o salário estimado dos profissionais de dados.
    *   Isso sugere que, isoladamente, a proporção de docentes com doutorado em uma UF não parece ser um forte preditor direto do salário individual de um profissional de dados que reside naquela UF.

2.  **Distribuição Salarial:**
    *   Profissionais com salários muito variados (desde próximos a R$0 até acima de R$40.000) são encontrados em UFs com diferentes proporções de docentes com doutorado. Por exemplo, tanto em UFs com proporção em torno de 0.45 quanto em UFs com proporção em torno de 0.55, observa-se toda a gama de salários.

3.  **Impacto do Nível de Ensino (Cor):**
    *   **Estudantes de Graduação (Verde claro/Turquesa):** Concentram-se predominantemente nas faixas salariais mais baixas, independentemente da proporção de docentes com doutorado na UF.
    *   **Outros Níveis de Ensino:** Profissionais com Graduação (Laranja), Pós-graduação (Azul), Mestrado (Roxo/Rosa) e Doutorado (Verde escuro) estão espalhados por uma ampla faixa de salários. Os salários mais altos (acima de R$30.000) são alcançados por profissionais de diversos níveis de ensino a partir da graduação, mas frequentemente associados a maior experiência.

4.  **Impacto da Experiência (Tamanho):**
    *   Visualmente, os pontos maiores (mais experiência) tendem a se localizar nas faixas salariais mais altas. Por exemplo, muitos dos pontos com salários acima de R$20.000 são de tamanho médio a grande. Isso reforça a observação de análises anteriores de que a experiência é um fator importante na determinação salarial.
    *   Os salários mais elevados (acima de R$40.000) são consistentemente representados por pontos de tamanho médio a grande, indicando profissionais com experiência considerável (3.5 anos ou mais).

5.  **Ausência de Relação Clara com a Proporção de Docentes com Doutorado:**
    *   Não se observa que UFs com maior proporção de docentes com doutorado tenham consistentemente profissionais de dados com salários mais altos, ou vice-versa.
    *   Por exemplo, alguns dos salários mais altos (>R$40.000) aparecem em UFs com proporção de docentes com doutorado em torno de 0.45-0.50, enquanto outros salários altos também aparecem em UFs com proporção em torno de 0.55-0.60.

**Conclusões Gerais:**

*   O gráfico sugere que a proporção de docentes com doutorado na UF de residência de um profissional de dados **não é um fator determinante primário** para o salário estimado desse profissional. A qualidade do ambiente acadêmico local, se proxy pela qualificação dos docentes, não se traduz diretamente em maiores salários individuais para os profissionais de dados ali residentes.
*   Fatores individuais como **nível de ensino alcançado e, principalmente, anos de experiência**, parecem ter uma influência mais visível na determinação salarial, como indicado pela distribuição das cores e tamanhos dos pontos em relação ao eixo do salário.
*   Outros fatores não representados neste gráfico específico, como o setor de atuação da empresa, o cargo específico, as habilidades individuais, a demanda do mercado local na UF e o custo de vida, provavelmente desempenham papéis mais significativos na definição dos salários dos profissionais de dados.

Este gráfico é útil para descartar uma relação causal ou correlacional forte entre a proporção de docentes com doutorado na UF e os salários dos profissionais de dados, direcionando a atenção para outros fatores mais diretamente ligados ao perfil do profissional e ao mercado de trabalho.


## Grafico 18
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/6bdfb7fdb2be6a819758ca7b1b05d011/raw/7db0af70c340fb3c01d6a052579873f03cacbf1c/gistfile1.txt)
![newplot(3)](https://github.com/user-attachments/assets/6ebf06b9-3667-4d2f-bb06-2802e19b8949)
## Análise do Gráfico: Relação 3D entre Salário, Experiência e Nível de Ensino

O gráfico interativo apresentado é um gráfico de dispersão 3D (3D Scatter Plot) que visualiza a relação entre três variáveis principais: "Salário Estimado (R$)", "Experiência (Anos Estimados)" e "Nível de Ensino (Ordinal)". Cada ponto no espaço tridimensional representa um profissional de dados. Este tipo de análise exploratória de dados (AED) ajuda a investigar conjuntos de dados e resumir suas principais características usando métodos de visualização.

**Elementos do Gráfico:**

*   **Eixos:**
    *   **Eixo X (Horizontal, geralmente representado como profundidade ou eixo frontal):** "Experiencia_Anos_Estimados". Este eixo representa o tempo de experiência profissional em anos, variando de aproximadamente 0.5 (para "Menos de 1 ano") até 10.0 (para "Mais de 10 anos").
    *   **Eixo Y (Horizontal, geralmente representado como largura ou eixo lateral):** "Nivel_Ensino_Ordinal". Este eixo representa o nível de formação acadêmica de forma ordinal, onde valores menores indicam níveis de ensino mais básicos (0 para Estudante de Graduação) e valores maiores indicam níveis mais avançados (4 para Doutorado ou Phd).
    *   **Eixo Z (Vertical, altura):** "Salario_Estimado". Este eixo representa a remuneração estimada em Reais, variando de R$0 até valores que podem exceder R$40.000.
*   **Pontos de Dados:** Cada ponto (esfera) no gráfico representa um profissional individual no dataset, posicionado de acordo com seus valores nas três variáveis mencionadas.
*   **Cor dos Pontos (Nivel_Ensino_Ordinal):** Os pontos são coloridos de acordo com o "Nivel_Ensino_Ordinal", o que facilita a identificação visual de grupos com diferentes níveis de formação acadêmica. A legenda de cores, que tipicamente acompanha esses gráficos interativos, seria (assumindo um esquema de cores padrão para variáveis ordinais):
    *   Estudante de Graduação (Ordinal 0): Uma cor específica (ex: azul)
    *   Graduação/Bacharelado (Ordinal 1): Outra cor (ex: laranja)
    *   Pós-graduação (Ordinal 2): Outra cor (ex: verde)
    *   Mestrado (Ordinal 3): Outra cor (ex: vermelho)
    *   Doutorado ou Phd (Ordinal 4): Outra cor (ex: roxo)

**Observações e Interpretações (Baseadas na Interação Típica com Gráficos 3D):**

1.  **Concentração Geral dos Pontos:**
    *   Observa-se uma maior densidade de pontos nas regiões correspondentes a menores salários estimados (parte inferior do eixo Z), especialmente para combinações de baixo nível de ensino e pouco tempo de experiência.
    *   À medida que os valores nos eixos "Nivel_Ensino_Ordinal" e "Experiencia_Anos_Estimados" aumentam (movendo-se para valores ordinais mais altos no eixo Y e para mais anos no eixo X), os pontos tendem a se posicionar em níveis mais elevados no eixo Z ("Salario_Estimado").

2.  **Tendência Global:**
    *   Visualmente, existe uma tendência clara de que salários mais altos (pontos mais altos no eixo Z) estão associados a combinações de maior tempo de experiência e/ou níveis de ensino mais elevados. A "nuvem" de pontos parece se elevar à medida que se avança ao longo dos eixos de experiência e nível de ensino.

3.  **Impacto Combinado e Interação entre Experiência e Nível de Ensino:**
    *   **Profissionais com Baixa Experiência:** Independentemente do nível de ensino, aqueles com pouca experiência (valores baixos no eixo X) geralmente apresentam salários mais baixos. Mesmo um doutor com pouca experiência pode ter um salário menor do que um graduado com muitos anos de experiência.
    *   **Profissionais com Alta Experiência:** Aqueles com muitos anos de experiência (valores altos no eixo X) exibem uma gama mais ampla de salários. Dentro deste grupo, os profissionais com níveis de ensino mais altos (cores associadas a Mestrado/Doutorado) tendem a alcançar os patamares salariais mais elevados.
    *   **Profissionais com Nível de Ensino Elevado:** Por exemplo, indivíduos com Doutorado (ordinal 4, cor específica) estão distribuídos ao longo de diferentes faixas de experiência. Aqueles que combinam doutorado com mais anos de experiência tendem a estar entre os que recebem os salários mais altos do dataset.

4.  **Identificação de Outliers:**
    *   A visualização 3D pode ajudar a identificar outliers – por exemplo, profissionais com um salário muito alto para seu nível de experiência e ensino, ou o contrário. Esses pontos se destacariam da concentração principal de dados.

5.  **Vantagem da Interatividade:**
    *   A capacidade de girar, dar zoom e interagir com o gráfico 3D é fundamental para uma análise completa. Isso permite observar as relações entre pares de variáveis de diferentes ângulos, facilitando a identificação de padrões, clusters ou tendências que poderiam não ser evidentes em gráficos 2D estáticos.

**Conclusões Gerais:**

*   O gráfico de dispersão 3D corrobora e integra as descobertas de análises 2D anteriores: tanto a experiência profissional quanto o nível de formação acadêmica são fatores positivamente correlacionados com o salário estimado dos profissionais de dados.
*   A principal contribuição desta visualização é destacar a **interação** entre esses dois fatores. Para alcançar os salários mais elevados, geralmente é necessária uma combinação de um alto nível de ensino *e* uma experiência profissional substancial.
*   Profissionais com níveis de ensino mais baixos podem encontrar um "teto" salarial mais baixo, mesmo com muita experiência, em comparação com aqueles com formação mais avançada e experiência similar.
*   Da mesma forma, profissionais com alta qualificação acadêmica, mas pouca experiência prática, podem não atingir os salários mais altos até acumularem mais tempo de atuação no mercado.

Este tipo de gráfico é uma ferramenta poderosa para a análise exploratória de dados (AED), pois permite uma compreensão mais intuitiva de relações multivariadas complexas, mostrando como diferentes fatores se combinam para influenciar um resultado específico como o salário.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2º Pergunta orientada a dados 
**Pergunta Orientada a Dados:** *...*



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3º Pergunta orientada a dados
**Pergunta Orientada a Dados:**
*Como fatores como  formalidade no emprego e características demográficas (gênero e raça) interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?*

![cor_e_raça_ensino_heatmap](https://github.com/user-attachments/assets/f147fa83-1501-4669-b6ff-95165ed54894)

### O que o Gráfico Mostra?

O gráfico evidencia **disparidades educacionais** entre pessoas de diferentes grupos raciais:

- **Em todos os grupos** (Branca, Preta e Parda), a maioria das pessoas está concentrada nos níveis de **Graduação/Bacharelado** e **Pós-graduação** (cerca de 33-35%).
- **Pessoas pretas** apresentam um **percentual mais elevado** de "Estudante de Graduação" (18,9%) em comparação com pessoas brancas (11,6%) e pardas (14,3%), indicando uma **maior proporção de estudantes que ainda não concluíram a graduação**.
- **Pessoas pretas e pardas** possuem **percentuais menores** nos níveis de **Mestrado** e **Doutorado** em comparação às pessoas brancas:
  - Doutorado/PhD: Brancos (4,4%), Pretos (2,1%), Pardos (3,5%).
- A categoria "Não tenho graduação formal" apresenta **baixa representatividade** em todos os grupos (entre 1,9% e 2,6%).


### Como Interpretar?

Este gráfico é um **heatmap** (mapa de calor) que mostra a distribuição percentual dos níveis de ensino de pessoas segundo sua **cor/raça** (Branca, Preta e Parda).

Cada célula representa o **percentual de pessoas de uma determinada cor/raça** em um **nível de escolaridade** específico.  
As cores indicam a intensidade dos percentuais — valores mais claros correspondem a percentuais mais elevados.

Para interpretar:
- Analise cada linha que corresponde a uma cor/raça.
- Observe como os percentuais se distribuem entre os diferentes níveis de ensino.
- Compare as diferenças de distribuição entre os grupos raciais

> Em resumo: embora a maioria tenha atingido a graduação ou pós-graduação, as pessoas pretas e pardas ainda enfrentam barreiras para atingir níveis mais altos de escolaridade como mestrado e doutorado.

![distribuição_regional_barras](https://github.com/user-attachments/assets/24542e74-b49f-4edc-8ffc-0d17085c1e8f)
 
 ### O que o Gráfico Mostra?
 
 O gráfico revela **desigualdades regionais** na distribuição dos profissionais de dados em comparação com a distribuição geral da população:
 
 - **Sudeste**:
   - Concentra **61,4% dos profissionais de dados**, muito acima dos **26% da população geral**.
   - É a região com maior desequilíbrio positivo para profissionais de dados.
 
 - **Nordeste**:
   - Representa **33,2% da população**, mas apenas **11,8% dos profissionais de dados**.
   - Forte sub-representação no mercado de dados.
 
 - **Norte**:
   - Apesar de abrigar **14% da população**, apenas **1,6% dos profissionais de dados** atuam na região.
   - Grande disparidade.
 
 - **Centro-Oeste**:
   - Tem **9,9% da população** e **6,7% dos profissionais de dados**.
   - Menor diferença relativa entre população e profissionais, mas ainda assim com sub-representação.
 
 - **Sul**:
   - Apresenta **equilíbrio**: **16,9% da população** e **18,6% dos profissionais de dados**.
   - Região mais proporcional em termos de profissionais de dados versus população.
  
 ### Como Interpretar?
 
 Este gráfico de barras compara a distribuição percentual da **população geral** e dos **profissionais de dados** nas cinco grandes regiões do Brasil (Norte, Nordeste, Centro-Oeste, Sudeste e Sul).
 
 Para interpretar:
 - Observe a altura das barras para cada região.
 - As barras **azuis** representam a distribuição da **população geral**.
 - As barras **vermelhas** representam a distribuição dos **profissionais de dados**.
 - Compare o tamanho das barras para ver onde há **maior ou menor concentração de profissionais de dados** em relação à população.
 
 > Em resumo: o mercado de dados no Brasil é altamente concentrado no Sudeste, especialmente em comparação com a distribuição populacional, enquanto regiões como Norte e Nordeste são significativamente sub-representadas.

![genero_salario_heatmap](https://github.com/user-attachments/assets/1121692b-f59c-4a1e-b90f-00f3312f94e5)

### O que o Gráfico Mostra?

O gráfico revela **semelhanças e pequenas diferenças** na distribuição salarial entre homens e mulheres:

- A **maior concentração** para ambos os gêneros está na faixa de **R$12.001 a R$16.000/mês**:
  - Homens: **21,6%**
  - Mulheres: **21,8%**

- Nas faixas intermediárias (de **R$6.001 a R$12.000/mês**), homens e mulheres também têm proporções próximas:
  - Indicam uma predominância de profissionais nessa faixa de renda média-alta.

- **Faixas mais baixas** (abaixo de R$2.000/mês):
  - Pequena presença de ambos os gêneros (menos de 1%).

- **Faixas muito altas** (acima de R$30.000/mês):
  - Baixa representatividade geral, mas **homens** têm percentuais ligeiramente superiores a mulheres.

- Em geral, há uma **leve concentração maior de mulheres** nas faixas mais baixas e **um pequeno predomínio masculino** nas faixas mais altas.

### Como Interpretar?

Este gráfico é um **heatmap** que mostra a distribuição percentual de homens e mulheres em diferentes **faixas salariais**.

Para interpretar:
- Cada linha representa um gênero (Homem ou Mulher).
- Cada coluna corresponde a uma faixa salarial específica.
- As cores indicam a intensidade dos percentuais — valores mais claros indicam maior concentração de pessoas naquela faixa salarial.
- Os números dentro das células mostram o percentual exato.

> Em resumo: embora a distribuição de salários entre homens e mulheres seja bastante semelhante, pequenas diferenças persistem, principalmente nas extremidades da distribuição salarial, sugerindo desigualdades nos rendimentos mais elevados e predominio feminino nas faixas mais baixas.

![impacto_por_faixa_etaria](https://github.com/user-attachments/assets/4fa74a22-0c46-4f2f-a708-b90e0ab0fb6a)

### O que o Gráfico Mostra?

Alguns destaques importantes:

- A faixa **22-24 anos** apresenta o maior percentual de impacto (**25,2%**).
- Faixas entre **35-39 anos** (**24,0%**) e **50-54 anos** (**22,8%**) também relatam impacto elevado.
- A faixa **25-29 anos** tem o **menor percentual** de impacto (**13,9%**).
- Profissionais mais jovens (17-21 anos) e mais idosos (55+) relatam impacto em menor intensidade comparado a faixas intermediárias.

### Como Interpretar?

Este gráfico de barras horizontais mostra o percentual de profissionais de dados que relataram sentir **impacto em sua experiência profissional** em função de sua **faixa etária**.

- Cada barra representa uma faixa etária.
- O comprimento da barra indica o percentual de pessoas daquela faixa que relataram impacto.
- Valores percentuais estão anotados no final de cada barra para facilitar a comparação.

> Em resumo: o impacto na experiência profissional é mais relatado por adultos jovens e profissionais em fase de consolidação de carreira, sendo menos intenso entre os muito jovens e os mais velhos.

![impacto_por_genero](https://github.com/user-attachments/assets/104c92be-27ba-4e89-ae68-3ba12e53a374)

### O que o Gráfico Mostra?

Alguns destaques importantes:

- **Mulheres** reportaram o maior percentual de impacto (**66,7%**).
- Pessoas que se identificam como **Outro gênero** também apresentam um percentual elevado (**50,0%**).
- Pessoas que **preferiram não informar** o gênero relataram impacto em **64,8%** dos casos, valor semelhante ao das mulheres.
- **Homens** relataram impacto em apenas **9,2%** dos casos, indicando a menor percepção de impacto entre os grupos.

### Como Interpretar?

Este gráfico de barras horizontais mostra o **percentual de profissionais de dados** que relataram sentir **impacto em sua experiência profissional** em função de seu **gênero**.

- Cada barra representa um grupo de gênero.
- O comprimento da barra indica o percentual de pessoas daquele grupo que relataram impacto.
- Valores percentuais estão anotados no final de cada barra para facilitar a comparação visual.

> Em resumo: o impacto do gênero na experiência profissional é mais sentido por mulheres e minorias de gênero, enquanto homens em sua maioria relatam trajetórias profissionais menos afetadas por essa variável.

![indice_representividade_interseccional](https://github.com/user-attachments/assets/b7a0f780-f2ba-416f-8fde-1832282e05cc)

### O que o Gráfico Mostra?

Principais observações:

- O grupo **Homem_Branca** é **super-representado** na área de dados, com índice **2,60**.
- **Homem_Preta** apresenta representatividade próxima do ideal, com índice **1,10**.
- **Mulher_Branca** (**0,77**) e **Homem_Parda** (**0,76**) estão **sub-representados**, abaixo do ponto de igualdade.
- **Mulher_Preta** (**0,40**) e **Mulher_Parda** (**0,22**) são os grupos **mais sub-representados** no setor de dados.

### Como Interpretar?

Este gráfico de barras horizontais apresenta o **índice de representatividade** de diferentes grupos demográficos (considerando **gênero** e **cor/raça**) na área de dados.

- Cada barra representa um grupo (ex.: Mulher_Preta, Homem_Branca, etc.).
- O comprimento da barra indica o índice de representatividade.
- Uma linha vermelha vertical marca o ponto de **representatividade ideal** (índice = 1.0), ou seja, onde o grupo está proporcional à população geral.
- Valores numéricos estão anotados no final de cada barra para facilitar a comparação.

> Em resumo: o gráfico evidencia um cenário de desigualdade na área de dados, onde o recorte de **raça** e **gênero** é fundamental para entender os desafios de diversidade e inclusão.

![heatmap_calor_disparidae](https://github.com/user-attachments/assets/29521e78-6709-47a1-964e-fffb1d65ab09)
 
 ### O que o Gráfico Mostra?
 
 Principais observações:
 
 - **Mulheres** têm disparidades significativas em todas as regiões, com as maiores diferenças no Centro-Oeste (**29,5 pontos percentuais**) e Norte (**28,6**).
 - **Pessoas Pardas** apresentam sub-representação em todas as regiões, especialmente no Norte (**23,3**) e Nordeste (**22,2**).
 - **Pessoas Pretas** estão próximas da representatividade ideal em quase todas as regiões, com variações mínimas (por exemplo, **-0,8** no Nordeste e Centro-Oeste).
 - O **Sul** apresenta uma situação atípica: baixa disparidade para Pessoas Pardas (**6,2**) e Pessoas Pretas (**1,3**), mas ainda alta para Mulheres (**28,0**).
 
 ### Como Interpretar?
 
 Este é um **mapa de calor** que mostra a **diferença em pontos percentuais** entre a representatividade observada e a representatividade ideal de alguns grupos (Mulheres, Pessoas Pardas e Pessoas Pretas) nas diferentes **regiões do Brasil**.
 
 - As células mostram a magnitude da diferença para cada grupo e região.
 - Cores mais escuras indicam **maior disparidade** (diferença mais acentuada).
 - Diferenças positivas indicam **sub-representação** (grupo menos presente que deveria).
 - Diferenças negativas ou próximas de zero indicam **representatividade adequada**.
 
 > Em resumo: o mapa de calor revela que questões de gênero e raça impactam de maneira diferente nas regiões brasileiras, com desafios mais agudos para mulheres e pessoas pardas na área de dados.

![matriz_correlação](https://github.com/user-attachments/assets/aa66357b-c3cc-4507-a780-843303b7131f)

### O que o Gráfico Mostra?

Principais observações:

- **Anos de experiência** tem correlação **moderada** com a **faixa salarial** (**0,56**), indicando que mais experiência tende a estar associada a salários maiores.
- **Nível de ensino** também tem uma correlação positiva com **faixa salarial** (**0,31**), embora mais fraca do que anos de experiência.
- **Relato de impacto** tem forte correlação com **impacto de gênero** (**0,76**) e **impacto de raça** (**0,63**), sugerindo que quem relata impacto, frequentemente associa esse impacto a questões de gênero e raça.
- As demais correlações são fracas ou praticamente inexistentes (próximas de zero).

### Como Interpretar?

Esta é uma **matriz de correlação** que mostra a relação linear entre diferentes variáveis numéricas do estudo.

- As células indicam o **coeficiente de correlação de Pearson**, variando de **-1** (correlação negativa perfeita) a **+1** (correlação positiva perfeita).
- Cores mais próximas do vermelho indicam correlação positiva, enquanto cores azuladas indicam correlação negativa.
- Valores próximos de zero sugerem pouca ou nenhuma correlação linea

> Em resumo: a progressão de carreira é mais fortemente associada à experiência e educação, enquanto percepções de impacto estão mais conectadas a fatores de identidade como gênero e raça.

![relação_salario_ensino_heatmap](https://github.com/user-attachments/assets/ad208ee3-80cc-43fc-bd74-541c1c9ff10d)

### O que o Gráfico Mostra?

Principais observações:

- **Anos de experiência** tem correlação **moderada** com a **faixa salarial** (**0,56**), indicando que mais experiência tende a estar associada a salários maiores.
- **Nível de ensino** também tem uma correlação positiva com **faixa salarial** (**0,31**), embora mais fraca do que anos de experiência.
- **Relato de impacto** tem forte correlação com **impacto de gênero** (**0,76**) e **impacto de raça** (**0,63**), sugerindo que quem relata impacto frequentemente associa esse impacto tanto a questões de gênero quanto de raça.
- As demais correlações são fracas ou praticamente inexistentes (valores próximos de zero).

### Como Interpretar?

Esta é uma **matriz de correlação** que mostra a relação linear entre diferentes variáveis numéricas do estudo.

- As células indicam o **coeficiente de correlação de Pearson**, variando de **-1** (correlação negativa perfeita) a **+1** (correlação positiva perfeita).
- Cores mais próximas do vermelho indicam correlação positiva, enquanto cores azuladas indicam correlação negativa.
- Valores próximos de zero sugerem pouca ou nenhuma correlação linear.

> Em resumo: a progressão de carreira está mais fortemente associada à experiência e educação, enquanto as percepções de impacto estão mais conectadas a fatores de identidade como gênero e raça.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4º Pergunta orientada a dados 
**Pergunta Orientada a Dados:** *...*



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Indução de modelos

## Modelo 1 Análise de Disparidade Salarial de Profissionais de Dados no Brasil Utilizando o Modelo Random Forest
### 1º Pergunta orientada a dados
### *Justificativa*

A escolha do algoritmo Random Forest para investigar a pergunta orientada a dados "Como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?" fundamenta-se nas seguintes características e vantagens do modelo:

### - Capacidade de Capturar Interações Complexas:
A pergunta central foca na interação entre formação acadêmica e experiência profissional. O Random Forest, por ser um ensemble de árvores de decisão, é intrinsecamente capaz de modelar relações não-lineares e interações complexas entre as variáveis independentes sem a necessidade de especificá-las explicitamente no modelo. Cada árvore no Random Forest pode aprender diferentes combinações e condições das features que levam a diferentes resultados salariais.

### - Fornecimento de Importância das Features:
O Random Forest oferece uma métrica de importância das features (como a "redução média de impureza Gini", visível no gráfico de importância das features do notebook). Isso permite quantificar a contribuição relativa da formacao_academica_encoded e da experiencia_profissional_encoded na previsão da disparidade salarial, ajudando a entender quais fatores têm maior influência.

### - Robustez e Generalização:
Por agregar as previsões de múltiplas árvores de decisão (250 no modelo atual), o Random Forest tende a ser mais robusto e a generalizar melhor para novos dados do que uma única árvore de decisão, reduzindo o risco de overfitting. Parâmetros como min_samples_split=10 e min_samples_leaf=5 também auxiliam na regularização.

### - Bom Desempenho em Problemas de Classificação:
Random Forest é reconhecido por seu alto desempenho em tarefas de classificação, como a que está sendo abordada (classificar a faixa salarial em "Salário Baixo/Médio" ou "Salário Alto"). A acurácia de 0.7283 obtida é um ponto de partida razoável, com potencial de otimização.

### - Manejo de Features Categóricas e Numéricas:
As features Nível de ensino alcançado e Tempo de experiência na área de dados foram transformadas em variáveis numéricas ordinais. O Random Forest lida bem com esse tipo de dado após o pré-processamento.

| Atributo                                         | Nome                                      | Tipo         | Subtipo                             | Descrição                                                                                     | Relevância |
|--------------------------------------------------|-------------------------------------------|--------------|-------------------------------------|-----------------------------------------------------------------------------------------------|------------|
| P0                                               | id                 		       | Qualitativo  | Nominal                             | Para identificação da resposta                                    		            | Alta       |
| P1l                                              | Nível de ensino alcançado                 | Qualitativo  | Ordinal                             | Nível de ensino do respondente (graduação, mestrado, etc.)                                    | Alta       |
| P1m                                              | Área de formação acadêmica                | Qualitativo  | Nominal (Multivalorado)             | Área de formação acadêmica do respondente (TI, Economia, etc.)                                | Alta       |
| P2h                                              | Faixa salarial mensal                     | Qualitativo  | Ordinal                             | Faixa salarial mensal do respondente                                                          | Alta       |
| P2i                                              | Tempo de experiência na área de dados     | Quantitativo | Discreto                            | Tempo de experiência do respondente na área de dados (em anos)                                | Alta       |
| P2g                                              | Nível de senioridade                      | Qualitativo  | Ordinal                             | Nível de senioridade do respondente (Júnior, Pleno, Sênior)                                   | Alta       |
| P1b                                              | Gênero do profissional                    | Qualitativo  | Nominal (Multivalorado)             | Identidade de gênero do respondente                                                           | Alta       |
| P1c                                              | Cor/Raça/Etnia                            | Qualitativo  | Nominal (Multivalorado)             | Cor ou raça do respondente                                                                    | Alta       |
| P2b                                              | Setor de atuação da empresa               | Qualitativo  | Nominal (Multivalorado)             | Setor em que a empresa do respondente atua (Tecnologia, Finanças, etc.)                       | Alta       |
| P1i1                                             | UF onde mora                              | Qualitativo  | Nominal (Multivalorado)             | Unidade Federativa onde o respondente reside                                                  | Alta       |
| P2f                                              | Cargo atual                               | Qualitativo  | Nominal (Multivalorado)             | Cargo atual ocupado pelo respondente                                                          | Alta       |
| P2o6                                             | Oportunidade de aprendizado               | Qualitativo  | Nominal (Multivalorado)             | Valorização das oportunidades de aprendizado e crescimento profissional                       | Alta       |
| P2o10                                            | Reputação da empresa                      | Qualitativo  | Nominal (Multivalorado)             | Valorização da reputação que a empresa tem no mercado                                         | Alta       |


### - Interpretabilidade Parcial:
Embora um ensemble de muitas árvores possa parecer uma "caixa preta", é possível visualizar árvores individuais (como o exemplo plotado no gráfico da árvore de decisão do notebook) para entender os caminhos de decisão. Isso oferece insights sobre como o modelo toma suas decisões com base nas interações.

### - Tratamento de Classes Desbalanceadas:
O modelo utiliza o parâmetro class_weight='balanced_subsample', que ajusta os pesos das classes em cada subamostra (bootstrap), ajudando a mitigar o impacto de um possível desbalanceamento entre as classes de "Salário Baixo/Médio" e "Salário Alto" (observado no relatório de classificação como 568 vs 422 instâncias no conjunto de teste).


### *Processo de Amostragem de Dados (Particionamento e Cross-Validation)*

No modelo desenvolvido para analisar a disparidade salarial dos profissionais de dados no Brasil, o processo de amostragem de dados envolveu o particionamento do conjunto de dados em subconjuntos de treino e teste.

**A técnica específica utilizada no código do notebook Kaggle foi a divisão Holdout Simples, implementada através da função train_test_split da biblioteca sklearn.model_selection.** 

**Particionamento dos Dados (Método Holdout)**
- Divisão em Treino e Teste:

	- O conjunto de dados pré-processado, contendo as features (X: formacao_academica_encoded, experiencia_profissional_encoded) e a variável alvo (y: salario_alto), foi dividido em dois conjuntos distintos:
	
	- Conjunto de Treinamento (X_train, y_train)
	
	- Conjunto de Teste (X_test, y_test)
	
	- Esta divisão foi realizada pela linha de código:
   
		   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
   
**Parâmetros da Divisão:**
	- test_size=0.3: Este parâmetro especifica que 30% do conjunto de dados total foi reservado para o conjunto de teste, enquanto os 70% restantes foram utilizados para o treinamento do modelo. Esta é uma proporção comum para o método holdout e visa garantir que o modelo seja testado em uma quantidade significativa de dados que ele não viu durante o treinamento.
	- random_state=42: A utilização de um random_state fixo garante que a divisão dos dados seja sempre a mesma a cada execução do código. Isso é crucial para a reprodutibilidade dos resultados do modelo.
	- stratify=y: Este parâmetro é particularmente importante em problemas de classificação. Ele assegura que a proporção das classes da variável alvo (y, que no caso é 'Salário Baixo/Médio' e 'Salário Alto') seja mantida de forma equilibrada tanto no conjunto de treino quanto no de teste. Isso é vital para evitar que o modelo seja treinado ou avaliado com uma representação distorcida das classes, especialmente se houver desbalanceamento nos dados originais.

**Utilização dos Conjuntos:**
	- O conjunto de treinamento (X_train, y_train) foi utilizado para "ensinar" o modelo Random Forest, ou seja, para ajustar seus parâmetros internos e aprender os padrões presentes nos dados (rf_model.fit(X_train, y_train)).
	- O conjunto de teste (X_test, y_test) foi mantido separado durante todo o processo de treinamento e utilizado exclusivamente para avaliar o desempenho do modelo treinado em dados novos e desconhecidos. As métricas como acurácia, relatório de classificação e a matriz de confusão foram calculadas com base nas previsões feitas neste conjunto. O objetivo desta separação é verificar o desempenho do modelo em dados que ele não viu, simulando uma aplicação no "mundo real".

*Em resumo, o processo de amostragem adotado no projeto foi o particionamento dos dados em conjuntos de treino e teste (70% e 30%, respectivamente) de forma estratificada, utilizando o método holdout para a avaliação final do modelo Random Forest.*


### *Parâmetros utilizados*

- **bootstrap:** True
  
- **ccp_alpha:** 0.0
  
- **class_weight:** 'balanced_subsample'
  
- **criterion:** 'gini'
  
- **max_depth:** None
  
- **max_features:** 'sqrt'
  
- **max_leaf_nodes:** None
  
- **max_samples:** None
  
- **min_impurity_decrease:** 0.0
  
- **min_samples_leaf: 5:** 
  
- **min_samples_split:** 10
  
- **min_weight_fraction_leaf:** 0.0
  
- **n_estimators: 250:** 
  
- **n_jobs: -1:** 
  
- **oob_score:** False
  
- **random_state:** 42
  
- **verbose:** 0
  
- **warm_start:** False
  

- Esses parâmetros foram explicitamente definidos no código:

		rf_model = RandomForestClassifier(
		    n_estimators=250,
		    max_depth=None,
		    min_samples_split=10,
		    min_samples_leaf=5,
		    class_weight='balanced_subsample',
		    random_state=42,
		    n_jobs=-1
		)

- Os demais parâmetros assumiram seus valores padrão conforme listado na saída de rf_model.get_params()

 ### *Explicação do Código:*





-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Indução de modelos

## Modelo 2 
### 2º Pergunta orientada a dados
### *Justificativa*
### *Processo de Amostragem de Dados (Particionamento e Cross-Validation)*
### *Parâmetros utilizados*
### *Explicação do Código:*

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Indução de modelos

## Modelo 3 Modelo LightGBM para Previsão de Faixa Salarial para a 3º pergunta orientada a dados
### 3º Pergunta orientada a dados

# Explicação Detalhada do Modelo LightGBM para Previsão de Faixa Salarial para a 3º pergunta orientada a dados

## Relatório do Modelo LightGBM para Previsão de Experiência Profissional Prejudicada por Cor/Raça/Etnia

### Resumo do Modelo

Este relatório detalha os resultados de um modelo preditivo desenvolvido para identificar fatores associados à percepção de ter a experiência profissional prejudicada devido à cor/raça/etnia entre profissionais de dados no Brasil. Utilizamos um modelo de classificação **LightGBM (Light Gradient Boosting Machine)**, um algoritmo eficiente e robusto baseado em árvores de decisão.

O modelo foi treinado utilizando um conjunto específico de atributos, conforme solicitado:

*   Faixa etária (`P1_a_1_Faixa_idade`)
*   Gênero (`P1_b_Genero`)
*   Não acredita que a experiência profissional seja afetada (`P1_e_1_Não_acredito_que_minha_experiência_profissional_seja_afetada`)
*   Experiência prejudicada devido à identidade de gênero (`P1_e_3_Experiencia_prejudicada_devido_a_minha_identidade_de_gênero`)
*   Nível de Ensino (`P1_l_Nivel_de_Ensino`)
*   Faixa Salarial (`P2_h_Faixa_salarial`)
*   Tempo de experiência prévia em TI/Engenharia (`P2_j_Quanto_tempo_de_experiência_na_área_de_TI_Engenharia_de_Software_você_teve_antes_de_começar_a_trabalhar_na_área_de_dados`)

A variável alvo foi `P1_e_2_Experiencia_prejudicada_devido_a_minha_Cor_Raça_Etnia`, indicando se o respondente sentiu sua experiência prejudicada por este motivo (1 = Sim, 0 = Não).

O pré-processamento incluiu a limpeza dos nomes das colunas, tratamento de valores ausentes (imputação pela mediana para numéricos e criação da categoria "Missing" para categóricos) e a conversão de variáveis categóricas para um formato adequado ao LightGBM. Os dados foram divididos em conjuntos de treino (80%) e teste (20%) de forma estratificada para manter a proporção da variável alvo.

## Métricas de Desempenho

### Acurácia Global

O modelo alcançou uma **acurácia de 92.65%** no conjunto de teste. Este valor indica a proporção geral de previsões corretas realizadas pelo modelo.

### Desempenho por Classe

A tabela abaixo detalha o desempenho do modelo para cada classe da variável alvo (0: Não Prejudicada, 1: Prejudicada):

| Classe          | Precisão | Recall | F1-Score | Suporte |
|-----------------|----------|--------|----------|---------|
| 0 (Não Prej.)   | 0.94     | 0.97   | 0.95     | 434     |
| 1 (Prejudicada) | 0.85     | 0.77   | 0.81     | 110     |
| **Média Macro** | **0.90** | **0.87** | **0.88** | **544** |
| **Média Pond.** | **0.92** | **0.93** | **0.93** | **544** |

*   **Precisão (Precision):** Das vezes que o modelo previu uma classe, quantas ele acertou. O modelo acerta 94% das vezes que prevê "Não Prejudicada" e 85% das vezes que prevê "Prejudicada".
*   **Recall (Sensibilidade):** Das vezes que uma classe realmente ocorreu, quantas o modelo previu corretamente. O modelo identifica corretamente 97% dos casos "Não Prejudicada" e 77% dos casos "Prejudicada".
*   **F1-Score:** Média harmônica entre Precisão e Recall, fornecendo uma métrica balanceada.
*   **Suporte:** Número de ocorrências reais de cada classe no conjunto de teste.

Observa-se que o modelo tem um desempenho ligeiramente melhor na identificação da classe majoritária (Não Prejudicada), mas ainda apresenta boa capacidade de identificar a classe minoritária (Prejudicada), com um F1-Score de 0.81.

## Matriz de Confusão

A matriz de confusão visualiza o desempenho do modelo comparando os valores reais com as previsões:

![Matriz de Confusão](https://private-us-east-1.manuscdn.com/sessionFile/0pIzjTfZ2ej8QNlhhGhgHn/sandbox/NN8QC7oShWRzRCBMSI8ZFa-images_1746104251006_na1fn_L2hvbWUvdWJ1bnR1L3Byb2pldG8vdmlzdWFsaXphY29lcy9tYXRyaXpfY29uZnVzYW8.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvMHBJempUZloyZWo4UU5saGhHaGdIbi9zYW5kYm94L05OOFFDN29TaFdSelJDQk1TSThaRmEtaW1hZ2VzXzE3NDYxMDQyNTEwMDZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzQnliMnBsZEc4dmRtbHpkV0ZzYVhwaFkyOWxjeTl0WVhSeWFYcGZZMjl1Wm5WellXOC5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=b3Nitf5E6vr2GHFVLI-2b5p86qjAtRlX1T4CDy4ktAALfiCSEyVpMaikvFyyD5yiAXOgOKIA5C7B9WakQ8s8xlgD4lvWz2hDv3B-0zCQo8T7CYEjUQH6UOmWuNRBr8PCm-84C45YRNcZtIUKqD6VrHPS-XxEBkHKMQxRG8RDRR72OF6SvRAocby0OdB7Fm6qGlgXtNyWkC~eD9TDy0Gd1Ts~mR4YJacypqA0Zbo5zo1jUnMhGWGR2S62cXePggWZgGcEL~bHSCZ8tz1NUGHW4LtU7c8MKmD84NTfT55T4qX9JYD0AO2eDdLJEWyTBZBn2CiKdVImVrPeNS98r9aJ~g__)

*   **Verdadeiros Negativos (VN):** 419 casos onde a experiência não foi prejudicada e o modelo previu corretamente.
*   **Falsos Positivos (FP):** 15 casos onde a experiência não foi prejudicada, mas o modelo previu que foi.
*   **Falsos Negativos (FN):** 25 casos onde a experiência foi prejudicada, mas o modelo previu que não foi.
*   **Verdadeiros Positivos (VP):** 85 casos onde a experiência foi prejudicada e o modelo previu corretamente.

A matriz confirma o bom desempenho geral, com a maioria das previsões caindo na diagonal principal (previsões corretas). Os erros (FP e FN) são relativamente baixos.

## Curva ROC

A curva ROC (Receiver Operating Characteristic) ilustra o desempenho do classificador em diferentes limiares de decisão:

![Curva ROC](https://private-us-east-1.manuscdn.com/sessionFile/0pIzjTfZ2ej8QNlhhGhgHn/sandbox/NN8QC7oShWRzRCBMSI8ZFa-images_1746104251006_na1fn_L2hvbWUvdWJ1bnR1L3Byb2pldG8vdmlzdWFsaXphY29lcy9jdXJ2YV9yb2M.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvMHBJempUZloyZWo4UU5saGhHaGdIbi9zYW5kYm94L05OOFFDN29TaFdSelJDQk1TSThaRmEtaW1hZ2VzXzE3NDYxMDQyNTEwMDZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzQnliMnBsZEc4dmRtbHpkV0ZzYVhwaFkyOWxjeTlqZFhKMllWOXliMk0ucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=DCsaiz-1N10sZ2UY-8UUV9qSVW-BuCYBOHC3gDdarz6AWMBVzDHvTba6wiHSVP50ueON7qUmjZghyB~1m-aTfU8QZ3Za43u1cn9rnSq9sJrnejEXw-YpaZkvrU8p-jdZJDmNkuZmYgJ8btvYzsFEzkjRsLOTLeJkqOalfz~zN~6fNIPAQbGhsN3V5zhXCtiU54apyHIi7unOyG-ZF5zJGBQHbqzp1fe4bBDLq0qnxajQkL5fHion5cpbAKldtu3i63ZYT3Wu6C480TV0CYVH6iXqTq9jwD3Y5-5QrdS6Ts9YhjM-vwtm-Ar20EruBjziRSLh9Oiwj5bF3NvAskod8Q__)

A área sob a curva ROC (AUC) é uma medida da capacidade do modelo de distinguir entre as classes. Quanto mais próximo de 1, melhor o desempenho do modelo. Nosso modelo apresenta uma AUC elevada, indicando excelente capacidade de discriminação entre experiências prejudicadas e não prejudicadas.

## Importância das Variáveis

O gráfico abaixo mostra quais atributos mais contribuíram para as previsões do modelo LightGBM:

![Importância das Features](https://private-us-east-1.manuscdn.com/sessionFile/0pIzjTfZ2ej8QNlhhGhgHn/sandbox/NN8QC7oShWRzRCBMSI8ZFa-images_1746104251006_na1fn_L2hvbWUvdWJ1bnR1L3Byb2pldG8vdmlzdWFsaXphY29lc19jb3JyaWdpZGFzL2ltcG9ydGFuY2lhX2ZlYXR1cmVzX2NvcnJpZ2lkbw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvMHBJempUZloyZWo4UU5saGhHaGdIbi9zYW5kYm94L05OOFFDN29TaFdSelJDQk1TSThaRmEtaW1hZ2VzXzE3NDYxMDQyNTEwMDZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzQnliMnBsZEc4dmRtbHpkV0ZzYVhwaFkyOWxjMTlqYjNKeWFXZHBaR0Z6TDJsdGNHOXlkR0Z1WTJsaFgyWmxZWFIxY21WelgyTnZjbkpwWjJsa2J3LnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc2NzIyNTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=OwlBURnrp-rPr1KZw8DArD74arwcQNhz0SBxMqYMFQV0Dwa6TYuLtO9VV462pnIOZyDiywpUdp8tjadoopDYsrkOozoXB59mNLrUjfvWNkEIpqumt58oC3Jle4NuRqovCBJZom7XP4T74mgvaDn-FlxfjJLOAyh0-5vgKoRG95f6Vl3hFF7Fuw9WdTr3435D-SWfE0xwA27ww4w~eyh3ENyMwJiM~2atWKcUvzJRsIN8AvaozL8op2zma8iNNccv8Uk7PRhTG2CJCeHVP7xPYOK5RCtuPxHh8DWa9QE~DaJrw08Hs~ZDK3n6NkLexpLHolsMVnjC2ABXMY~lssrxfg__)

As variáveis mais importantes identificadas pelo modelo foram:

1.  **Gênero (`P1_b_Genero`)**: O gênero do profissional foi o fator mais influente.
2.  **Experiência prejudicada devido à identidade de gênero (`P1_e_3_...`)**: Se o profissional sentiu impacto devido à identidade de gênero.
3.  **Não acredita que a experiência profissional seja afetada (`P1_e_1_...`)**: Se o profissional acredita que sua experiência não é afetada por fatores externos.
4.  **Tempo de Experiência Prévia em TI/Engenharia (`P2_j_...`)**: O tempo de experiência em áreas correlatas antes de migrar para dados.
5.  **Faixa Salarial (`P2_h_Faixa_salarial`)**: A faixa salarial do profissional.
6.  **Nível de Ensino (`P1_l_Nivel_de_Ensino`)**: O nível educacional formal do profissional.
7.  **Faixa Etária (`P1_a_1_Faixa_idade`)**: A idade do profissional.

## Distribuição das Previsões por Gênero

O gráfico abaixo mostra como as previsões do modelo se distribuem entre os diferentes gêneros:

![Previsões por Gênero](https://private-us-east-1.manuscdn.com/sessionFile/0pIzjTfZ2ej8QNlhhGhgHn/sandbox/NN8QC7oShWRzRCBMSI8ZFa-images_1746104251006_na1fn_L2hvbWUvdWJ1bnR1L3Byb2pldG8vdmlzdWFsaXphY29lcy9wcmV2aXNvZXNfcG9yX2dlbmVybw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvMHBJempUZloyZWo4UU5saGhHaGdIbi9zYW5kYm94L05OOFFDN29TaFdSelJDQk1TSThaRmEtaW1hZ2VzXzE3NDYxMDQyNTEwMDZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzQnliMnBsZEc4dmRtbHpkV0ZzYVhwaFkyOWxjeTl3Y21WMmFYTnZaWE5mY0c5eVgyZGxibVZ5YncucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=KNWqcii8vxpGzyhjEFAGBGEqdGIdy418ImOoQY8XLhze2HTfXpYak2UcqUbCqnveK0XqoA0eXl6amrpaaZI2qx6EjbbG2jdtp02i7JZs77QDwFBBjltSYUhAvHvXeaNteVX-APITw5KM0owopnvbFqVms8NjcdfNzovPuRwMF1hkNBpe1tsdgRXC1TJTgKu4~Nw8CXJdq32-6pS3RoJFqfJwb8eLVB5zOUAv92EtE7Rcr5h0A56~4RzrhJhuujcnLWr2dAtWyh-6QJMyUo6XU3~DnAq9HjAa61V5n3rURNvARYc7C6LrRP6kjoMG3PalKGzKVXVe9qzAyVw-NUV~lg__)

Esta visualização permite identificar se há diferenças significativas na proporção de experiências prejudicadas previstas pelo modelo entre os diferentes gêneros.

## Distribuição das Previsões por Nível de Ensino

O gráfico a seguir mostra a distribuição das previsões do modelo por nível de ensino:

![Previsões por Nível de Ensino](https://private-us-east-1.manuscdn.com/sessionFile/0pIzjTfZ2ej8QNlhhGhgHn/sandbox/NN8QC7oShWRzRCBMSI8ZFa-images_1746104251006_na1fn_L2hvbWUvdWJ1bnR1L3Byb2pldG8vdmlzdWFsaXphY29lcy9wcmV2aXNvZXNfcG9yX25pdmVsX2Vuc2lubw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvMHBJempUZloyZWo4UU5saGhHaGdIbi9zYW5kYm94L05OOFFDN29TaFdSelJDQk1TSThaRmEtaW1hZ2VzXzE3NDYxMDQyNTEwMDZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzQnliMnBsZEc4dmRtbHpkV0ZzYVhwaFkyOWxjeTl3Y21WMmFYTnZaWE5mY0c5eVgyNXBkbVZzWDJWdWMybHVidy5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=C4VRDen~TPOd49nMRIjz5G3cxxIyp5CVtAp4gMxquhRl3xcLAvbKPlD08jku7Rs-zWotnjA23pWiFZkV3kZciohO-KJCD8P2yaugY2xeKNHU-4EPLOXZbngQye233BQShkpdRPlleqZ-LsZqS3zWFHWwYaZ2RsbVdSXDiXwrrqgZVlcel-6Lr02YUzlOs2WJd6YTEQ-XIk9MEnJvUqBzgXuPyl7WLhxMF~zT3J-aOESAvxX9eb6HEwVwTSU7uTSRBXQLnKLKCDMzGybfG0U34U9gUWzsFztuG4fR65gyAQSKBtM3BRhyvFYuWfZzj~8K8nYGgKqGmDDZmOQiTxcKJQ__)

Esta visualização permite analisar se o nível de ensino está relacionado com a probabilidade de ter a experiência profissional prejudicada por cor/raça/etnia, segundo as previsões do modelo.

## Principais Insights

Com base na importância das variáveis e nas análises de distribuição, podemos extrair os seguintes insights:

1.  **Impacto de Gênero e Identidade:**
    *   **Gênero:** O gênero do profissional foi o fator mais influente nas previsões do modelo, sugerindo uma forte relação entre gênero e a percepção de discriminação racial.
    *   **Percepção de Impacto por Identidade de Gênero:** A variável que mede se o profissional sentiu impacto devido à *identidade de gênero* também foi muito importante para prever o impacto devido à *cor/raça/etnia*, sugerindo uma possível interseccionalidade nas experiências de discriminação.

2.  **Crença na Neutralidade da Experiência:**
    *   A variável `P1_e_1_Não_acredito_que_minha_experiência_profissional_seja_afetada` teve uma importância significativa, indicando que a crença geral sobre a neutralidade da experiência profissional está relacionada com a percepção específica de discriminação racial.

3.  **Impacto Socioeconômico e de Carreira:**
    *   **Tempo de Experiência e Faixa Salarial:** Estas variáveis foram relevantes, sugerindo que fatores relacionados à progressão na carreira e status socioeconômico estão ligados à percepção de discriminação racial no ambiente de trabalho de dados.

4.  **Educação e Idade:**
    *   **Nível de Ensino:** O nível educacional teve um impacto moderado nas previsões do modelo.
    *   **Faixa Etária:** A idade também figura entre os fatores relevantes, indicando possíveis diferenças geracionais na percepção ou ocorrência de discriminação.

## Conclusões

O modelo LightGBM demonstrou alta capacidade (92.65% de acurácia) em prever a percepção de experiência profissional prejudicada por cor/raça/etnia, utilizando um conjunto limitado de 7 atributos.

Os fatores mais importantes estão ligados ao **gênero e à percepção de discriminação por identidade de gênero**, seguidos pela **crença na neutralidade da experiência profissional**, **posição na carreira (tempo de experiência prévia, faixa salarial)**, **educação e idade**.

A forte influência do gênero e da percepção de discriminação por identidade de gênero sugere uma importante interseccionalidade nas experiências de discriminação. Profissionais que já percebem impacto devido à sua identidade de gênero parecem ter maior probabilidade de também perceber impacto devido à sua cor/raça/etnia.

As análises de distribuição por gênero e nível de ensino fornecem insights adicionais sobre como diferentes características demográficas podem estar relacionadas à percepção de discriminação racial no campo de dados no Brasil.

Este modelo e suas análises fornecem um ponto de partida valioso para entender os complexos fatores associados à discriminação racial no campo de dados no Brasil, destacando a importância de abordagens interseccionais para compreender e combater diferentes formas de discriminação no ambiente profissional.



## Análise SHAP (SHapley Additive exPlanations)

Para uma compreensão mais profunda de como cada atributo influencia a previsão do modelo para cada observação individual, utilizamos a análise SHAP. Os valores SHAP quantificam a contribuição de cada feature para afastar a previsão da média.

### Importância Global das Features (SHAP)

O gráfico de barras SHAP mostra a importância média absoluta de cada feature nas previsões do modelo. Ele confirma a ordem de importância já vista no gráfico do LightGBM, mas com uma métrica diferente.

![Image](https://github.com/user-attachments/assets/2e0c3077-6eea-4a0e-a760-6dd9e6cc8d28)

### Sumário SHAP

O gráfico de sumário SHAP combina a importância das features com seus efeitos. Cada ponto representa um valor SHAP para uma feature e uma observação. A posição no eixo y indica a feature, no eixo x o valor SHAP, e a cor representa o valor da feature (alto ou baixo).

![Image](https://github.com/user-attachments/assets/db4a7c82-6d02-4943-9345-38d82c4a4eba)-

Esta visualização revela não apenas quais features são importantes, mas também *como* elas impactam a previsão. Por exemplo, podemos observar se valores altos ou baixos de uma feature tendem a aumentar ou diminuir a probabilidade de prever "Experiência Prejudicada".

## Análise de Interseccionalidade (Região x Nível de Ensino)

A análise de interseccionalidade explora como a combinação de diferentes atributos (neste caso, Região e Nível de Ensino) afeta a previsão do modelo.

![Image](https://github.com/user-attachments/assets/ad361844-eb17-4a9c-bb8f-bc0616c0ac9c)

Este gráfico mostra a probabilidade média prevista de ter a experiência prejudicada para diferentes combinações de Região e nível de ensino. Ele permite identificar se certos grupos interseccionais enfrentam um risco previsto maior ou menor.

## Análise por Faixa Salarial e Gênero

![Image](https://github.com/user-attachments/assets/c918d6b7-76b3-4a26-93e7-ba69d6e056b1)

Exploramos também como a faixa salarial e o gênero se relacionam com a probabilidade prevista de experiência prejudicada.

## Análise por faixa salarial por raça e cor

![Image](https://github.com/user-attachments/assets/20cdb9d1-82c6-49d6-a656-05bc42306091)

Exploramos também como a faixa salarial e o raça/cor se relacionam com a probabilidade prevista de experiência prejudicada.

## Análise de interseccionalidade de faixas salarias (Gênero x Raça e cor)

![Image](https://github.com/user-attachments/assets/a703a897-f9d7-4a4e-b857-b469584ca191)

## Análise de Casos Específicos

Analisamos a previsão do modelo para dois perfis hipotéticos:

*   **Caso 1: Profissional com Doutorado (Masculino)**
    *   Probabilidade de Experiência NÃO Prejudicada: 0.16
    *   Probabilidade de Experiência Prejudicada: 0.84
*   **Caso 2: Profissional com Graduação (Feminino)**
    *   Probabilidade de Experiência NÃO Prejudicada: 0.95
    *   Probabilidade de Experiência Prejudicada: 0.05

Esses exemplos ilustram como o modelo atribui diferentes probabilidades com base nas características de entrada, refletindo os padrões aprendidos nos dados.

## Conclusões Atualizadas

O modelo LightGBM demonstrou alta capacidade (92.65% de acurácia) em prever a percepção de experiência profissional prejudicada por cor/raça/etnia, utilizando um conjunto limitado de 7 atributos.

Os fatores mais importantes estão ligados ao **gênero e à percepção de discriminação por identidade de gênero**, seguidos pela **crença na neutralidade da experiência profissional**, **posição na carreira (tempo de experiência prévia, faixa salarial)**, **educação e idade**.

A análise SHAP aprofunda o entendimento de como cada feature contribui para as previsões individuais, enquanto a análise de interseccionalidade (Gênero x Nível de Ensino) e as análises por faixa salarial e Região revelam padrões mais complexos e interações entre os atributos.

A forte influência do gênero e da percepção de discriminação por identidade de gênero, confirmada pela análise SHAP, sugere uma importante interseccionalidade nas experiências de discriminação. Profissionais que já percebem impacto devido à sua identidade de gênero parecem ter maior probabilidade de também perceber impacto devido à sua cor/raça/etnia.

Este modelo e suas análises, incluindo as visualizações SHAP e de interseccionalidade, fornecem um ponto de partida valioso para entender os complexos fatores associados à discriminação racial no campo de dados no Brasil, destacando a importância de abordagens interseccionais para compreender e combater diferentes formas de discriminação no ambiente profissional.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Indução de modelos

## Modelo 4 
### 4º Pergunta orientada a dados
### *Justificativa*
### *Processo de Amostragem de Dados (Particionamento e Cross-Validation)*
### *Parâmetros utilizados*
### *Explicação do Código:*

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Resultados


## Resultados obtidos com o modelo 1.


| Classe          | Precisão | Recall | F1-Score | Suporte |
|-----------------|----------|--------|----------|---------|
| Salário Baixo/Médio    | 0.84     | 0.65   | 0.73     | 568     |
| Salário Alto | 0.64     | 0.84   | 0.72     | 422     |
| accuracy |  |  | **0.73** | **990** |
| macro avg | **0.74** | **0.74** | **0.73** | **990** |
| weighted avg | **0.76** | **0.73** | **0.73** | **990** |

Acurácia do Modelo: 0.7283

**Parâmetros do Modelo Random Forest Utilizado:**

	{'bootstrap': True, 'ccp_alpha': 0.0, 'class_weight': 'balanced_subsample', 'criterion': 'gini', 'max_depth': None, 'max_features': 'sqrt', 'max_leaf_nodes': None, 'max_samples': None, 'min_impurity_decrease': 0.0, 'min_samples_leaf': 5, 'min_samples_split': 10, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 250, 'n_jobs': -1, 'oob_score': False, 'random_state': 42, 'verbose': 0, 'warm_start': False}

### Matriz de confusão
 ![image](https://github.com/user-attachments/assets/ac4dc383-e6d3-4aee-b330-46cc07407dde)
 
### Interpretação dos Quadrantes:

**Verdadeiros Negativos (VN = 368):**
	- Este valor indica o número de profissionais que realmente têm "Salário Baixo/Médio" e que o modelo corretamente previu como tendo "Salário Baixo/Médio".
	- No seu caso, o modelo acertou em 368 instâncias ao classificar corretamente os salários mais baixos.

**Falsos Positivos (FP = 200):**
	- Representa o número de profissionais que realmente têm "Salário Baixo/Médio", mas que o modelo incorretamente previu como tendo "Salário Alto".
	- Isso é também conhecido como "Erro do Tipo I". O modelo errou 200 vezes, prevendo um salário alto para quem, na verdade, tem um salário baixo/médio.

**Falsos Negativos (FN = 69):**
	- Indica o número de profissionais que realmente têm "Salário Alto", mas que o modelo incorretamente previu como tendo "Salário Baixo/Médio".
	- Isso é também conhecido como "Erro do Tipo II". O modelo errou 69 vezes, prevendo um salário baixo/médio para quem, na verdade, tem um salário alto.

**Verdadeiros Positivos (VP = 353):**
	- Este valor mostra o número de profissionais que realmente têm "Salário Alto" e que o modelo corretamente previu como tendo "Salário Alto".
	- O modelo acertou em 353 instâncias ao classificar corretamente os salários mais altos.

**Insights da Matriz:**
	- O modelo parece ser melhor em identificar corretamente os casos de "Salário Alto" quando eles realmente são altos (353 VP) do que em evitar classificar erroneamente os "Salário Baixo/Médio" como altos (200 FP).
	- Da mesma forma, o modelo identifica corretamente muitos casos de "Salário Baixo/Médio" (368 VN), mas deixa de identificar 69 casos de "Salário Alto", classificando-os erroneamente como "Salário Baixo/Médio".
	- Essa matriz é crucial para calcular métricas de desempenho mais detalhadas, como precisão, recall (sensibilidade) e F1-score para cada classe, que foram apresentadas no "Relatório de Classificação" do seu notebook. Por exemplo:
	- Precisão para "Salário Alto": VP / (VP + FP) = 353 / (353 + 200) ≈ 0.637 (Consistente com o 0.64 no relatório de classificação)
	- Recall para "Salário Alto": VP / (VP + FN) = 353 / (353 + 69) ≈ 0.836 (Consistente com o 0.84 no relatório de classificação)

A análise desses valores ajuda a entender os pontos fortes e fracos do seu modelo e onde ele tende a cometer mais erros, orientando possíveis melhorias.
### Arvore de dexisão do Radom Forest
![image](https://github.com/user-attachments/assets/be82f0f2-4978-4ccd-92f4-c72bfdad8708)


### Importância das features
![image](https://github.com/user-attachments/assets/56ce356a-8f50-45f3-b03d-c89db7ccda91)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Resultados obtidos com o modelo 2.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Resultados obtidos com o modelo 3.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Resultados obtidos com o modelo 4.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Interpretação dos modelos


### Interpretação do modelo 1

Apresente os parâmetros do modelo obtido. Tentre mostrar as regras que são utilizadas no
processo de 'raciocínio' (*reasoning*) do sistema inteligente. Utilize medidas como 
o *feature importances* para tentar entender quais atributos o modelo se baseia no
processo de tomada de decisão.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Interpretação do modelo 2

Apresente os parâmetros do modelo obtido. Tentre mostrar as regras que são utilizadas no
processo de 'raciocínio' (*reasoning*) do sistema inteligente. Utilize medidas como 
o *feature importances* para tentar entender quais atributos o modelo se baseia no
processo de tomada de decisão.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


### Interpretação do modelo 3

Apresente os parâmetros do modelo obtido. Tentre mostrar as regras que são utilizadas no
processo de 'raciocínio' (*reasoning*) do sistema inteligente. Utilize medidas como 
o *feature importances* para tentar entender quais atributos o modelo se baseia no
processo de tomada de decisão.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Interpretação do modelo 4

Apresente os parâmetros do modelo obtido. Tentre mostrar as regras que são utilizadas no
processo de 'raciocínio' (*reasoning*) do sistema inteligente. Utilize medidas como 
o *feature importances* para tentar entender quais atributos o modelo se baseia no
processo de tomada de decisão.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Análise comparativa dos modelos



## Análise comparativa dos modelos

Discuta sobre as forças e fragilidades de cada modelo. Exemplifique casos em que um
modelo se sairia melhor que o outro. Nesta seção é possível utilizar a sua imaginação
e extrapolar um pouco o que os dados sugerem.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Distribuição do modelo (opcional)

Tende criar um pacote de distribuição para o modelo construído, para ser aplicado 
em um sistema inteligente.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 8. Conclusão

Apresente aqui a conclusão do seu trabalho. Discussão dos resultados obtidos no trabalho, 
onde se verifica as observações pessoais de cada aluno.

Uma conclusão deve ter 3 partes:

   * Breve resumo do que foi desenvolvido
	 * Apresenação geral dos resultados obtidos com discussão das vantagens e desvantagens do sistema inteligente
	 * Limitações e possibilidades de melhoria


# REFERÊNCIAS 

DATA HACKERS. State of Data Brazil 2023. Disponível em: https://www.kaggle.com/datasets/datahackers/state-of-data-brazil-2023. Acesso em: 5 mar. 2025.

BAIN & COMPANY; DATA HACKERS. State of Data 2024. [S.l.]: Bain & Company, 2024. Disponível em: <https://www.stateofdata.com.br/>. Acesso em: 6 mar. 2025.

H2R PESQUISAS; TOTVS. Estudo Panorama das Carreiras 2030: o que esperar das profissões até o fim da década. Setembro/2023. Acesso em: 6 mar. 2025

INSTITUTO NACIONAL DE ESTUDOS E PESQUISAS EDUCACIONAIS ANÍSIO TEIXEIRA (INEP). Censo da Educação Superior. Brasília, DF: INEP,[2022]. Disponível em: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-da-educacao-superior. Acesso em: 15 mar. 2025.


# APÊNDICES

**Colocar link:**

Do código (armazenado no repositório);

Dos artefatos (armazenado do repositório);

Da apresentação final (armazenado no repositório);

Do vídeo de apresentação (armazenado no repositório).




