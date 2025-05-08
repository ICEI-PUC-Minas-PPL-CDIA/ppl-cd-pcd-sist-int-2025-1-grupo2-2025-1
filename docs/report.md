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
	*   [3º Pergunta Orientada a Dados](#3º-pergunta-orientada-a-dados)
*   [Indução de modelos](#indução-de-modelos)
    *   [Modelo 1 gbm (gradient boosting machines) modelo baseado em árvore de decisão](#modelo-1-gbm-gradient-boosting-machines-modelo-baseado-em-árvore-de-decisão)
    *   [Modelo 2: modelo-baseado-em-árvore-de-decisão](#modelo-2-algoritmo)
*   [Resultados](#resultados)
    *   [Resultados obtidos com o modelo 1.](#resultados-obtidos-com-o-modelo-1)
    *   [Interpretação do modelo 1](#interpretação-do-modelo-1)
    *   [Resultados obtidos com o modelo 2.](#resultados-obtidos-com-o-modelo-2)
    *   [Interpretação do modelo 2](#interpretação-do-modelo-2)
*   [Análise comparativa dos modelos](#análise-comparativa-dos-modelos)
*   [Conclusão](#8-conclusão)
*   [REFERÊNCIAS](#referências)
*   [APÊNDICES](#apêndices)

# Resumo

A disparidade salarial entre profissionais de dados no Brasil é influenciada por diversos fatores pessoais, educacionais e de mercado. Este estudo busca identificar quais variáveis impactam a remuneração desses profissionais, analisando dados da pesquisa State of Data Brazil 2023 e de bases auxiliares. Para isso, são exploradas características como experiência, formação acadêmica, setor de atuação, localização e habilidades técnicas. Através de modelagem preditiva, os resultados indicam que experiência, nível de senioridade e setor da empresa são os fatores com maior impacto na variação salarial. Esses insights podem auxiliar profissionais e empresas na tomada de decisões estratégicas sobre carreira e políticas de remuneração.

---

## Introdução

O Brasil experimentou um crescimento exponencial na indústria de dados devido à transformação digital do país e à crescente necessidade de trabalhadores qualificados. Embora as oportunidades sejam abundantes, os salários variam amplamente entre os trabalhadores, com fatores como experiência, gênero, educação, localização geográfica e tipo de empresa influenciando essa disparidade.

O objetivo deste estudo é identificar os principais fatores associados à disparidade na remuneração dos profissionais de dados no Brasil, utilizando informações coletadas de uma ampla pesquisa setorial.

As disparidades salariais entre os profissionais de dados no Brasil são influenciadas por diversos fatores como idade, gênero dos profissionais de dados, do setor de emprego ou modelo de contratação e ainda o seu histórico educacional e experiência profissional.

Este estudo investiga os principais elementos que estão associados à variação de salários no campo de dados ao utilizar o conjunto de dados State of Data Brazil 2023 e outras bases para complementar a pesquisa. Empregando métodos da ciência de dados, busca-se identificar padrões salariais e oferecer insights relevantes para profissionais e empresas. Espera-se que os resultados tragam um maior entendimento das disparidades salariais no campo, ajudando a desenvolver estratégias que incentivem a igualdade no mercado de tecnologia e ciência de dados.

###    Contextualização

A desigualdade salarial é um desafio enfrentado no mercado de trabalho brasileiro, impactando diversos setores da economia.

Estudos do IBGE apontam que gênero, etnia e escolaridade são fatores cruciais na determinação dos salários. De acordo com as pesquisas de 2022 do instituto, o rendimento médio por hora dos trabalhadores brancos foi de R$ 20,00, enquanto para pretos ou pardos foi de R$ 12,40, representando uma diferença de 61,4%. Além disso, pesquisas do mesmo em 2021 indicam que as taxas de desocupação foram de 11,3% para brancos, 16,5% para pretos e 16,2% para pardos, evidenciando a influência desses aspectos na disparidade salarial na atualidade.

No setor de tecnologia, essas disparidades têm características particulares, especialmente devido ao desenvolvimento acelerado da área e à necessidade contínua de atualização profissional. Na ciência de dados, as diferenças salariais são significativas e influenciadas por fatores como a experiência, formação acadêmica, setor de atuação e habilidades técnicas.

De acordo com o relatório State of Data Brazil 2023, profissionais que possuem certificações específicas em grandes empresas costumam receber remunerações mais altas, enquanto mulheres e grupos minoritários ainda encontram barreiras para alcançar igualdade salarial. 

Diante do exposto, buscamos por meio desta análise de dados, investigar os fatores determinantes para a variação salarial entre os profissionais de dados no Brasil, visando compreender melhor as desigualdades no setor e identificar caminhos para um mercado mais equitativo.

###    Problema

O agente em questão busca estabelecer quais são os fatores determinantes para a variação salarial entre profissionais de dados no Brasil. Constantemente, empresas brasileiras enfrentam dificuldades em determinar um salário justo ao profissional de dados por não considerarem os requisitos e as variáveis necessárias para isso. Nesse contexto, a análise busca entender o papel de fatores como experiência e nível educacional nas diferenças salariais, visando fornecer um padrão para que o mercado profissional da área seja mais equilibrado no país.



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





###    Justificativas

A desigualdade salarial na área de dados é um tema relevante, impactando profissionais e empresas. Este estudo busca identificar os principais fatores associados aos salários, com foco na experiência, senioridade e setor de atuação. O estudo se destina a profissionais da área que podem utilizar os resultados para planejar suas carreiras, e às empresas, que podem aprimorar suas políticas salariais com base em dados concretos. A pesquisa se apoia em bases de dados reconhecidas, como a State of Data Brazil 2023 da Data Hackers, garantindo a validade e confiabilidade das análises realizadas.



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


###    Dicionário de dados

O banco de dados "State of Data Brazil 2023" é o resultado de uma pesquisa conduzida pela comunidade Data Hackers em parceria com a Bain & Company, que visa mapear o mercado brasileiro de dados. A pesquisa contou com a participação de mais de 5.200 profissionais da área, que responderam a perguntas sobre diversos temas, por exemplo:

- **Fatores Pessoais e Demográficos:** Idade, gênero; Perfil racial e diversidade dentro do setor de dados; Contexto social e fatores que podem influenciar a carreira na área de dados.

- **Experiência profissional prejudicada (discriminação):** 

- **Experiência e Carreira:** Tempo de atuação no mercado de dados; Cargos ocupados e progressão na carreira; Transições de carreira para a área de dados.

- **Empresa e Ambiente de Trabalho:**  Tipo e porte da empresa em que os profissionais trabalham; Modelo de trabalho (remoto, híbrido ou presencial); Cultura organizacional e satisfação no ambiente de trabalho.


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

---


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


---


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


---

# Analises exploratorias de dados 

# 1º Pergunta orientada a dados 
**Pergunta Orientada a Dados:** *Como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?*

## Analise exploratoria de dados base de dados State of Data 2023

---

## Grafico Distribuição de Salários Mensais
![__results___0_1](https://github.com/user-attachments/assets/6204cac8-9875-4db3-b6d7-6bf52b038d49)
## Explicação do Gráfico: Distribuição de Salários Mensais

O gráfico apresentado é um histograma que ilustra a **Distribuição de Salários Mensais** de profissionais de dados no Brasil, com uma curva de estimativa de densidade do kernel (KDE) sobreposta para suavizar a representação da distribuição[1].

**Eixos do Gráfico:**
*   **Eixo X (Horizontal):** Representa o "Salário Médio (R$)", indicando as faixas salariais mensais em Reais. A escala varia de R$ 0 até valores próximos ou superiores a R$ 40.000[1].
*   **Eixo Y (Vertical):** Indica a "Contagem", ou seja, o número de profissionais que se enquadram em cada faixa salarial representada pelas barras do histograma. A contagem máxima observada no gráfico aproxima-se de 800 profissionais em uma determinada faixa salarial[1].

**Interpretação da Distribuição:**
*   **Concentração de Salários:** A maior concentração de profissionais encontra-se nas faixas salariais mais baixas. Observa-se um pico principal (a barra mais alta) na faixa de aproximadamente R$ 9.000 a R$ 10.000, onde cerca de 800 profissionais estão localizados[1].
*   **Múltiplos Picos (Multimodalidade):** A distribuição aparenta ser multimodal, sugerida pela curva KDE e pelas barras do histograma. Além do pico principal, há outras concentrações notáveis:
    *   Uma concentração significativa entre R$ 4.000 e R$ 6.000, com mais de 600 profissionais[1].
    *   Outro pico menor ao redor de R$ 13.000 a R$ 14.000, com quase 300 profissionais[1].
    *   Pequenas elevações em faixas salariais mais altas, como em torno de R$ 17.000-R$18.000 e R$ 22.000-R$23.000, indicando grupos menores de profissionais nesses níveis salariais[1].
*   **Assimetria à Direita (Right-Skewed):** A distribuição é assimétrica à direita. Isso significa que, embora a maioria dos salários esteja concentrada nas faixas mais baixas e médias, existe uma "cauda" longa para a direita, indicando que um número menor de profissionais recebe salários consideravelmente mais altos (acima de R$ 20.000, R$ 30.000, e chegando a R$ 40.000 ou mais)[1]. Essa assimetria é comum em distribuições de renda e salário.
*   **Dispersão:** Há uma grande dispersão nos salários, variando desde valores abaixo de R$ 5.000 até mais de R$ 40.000, o que reflete a diversidade de remuneração na área de dados no Brasil[1].

Em resumo, o gráfico mostra que a maioria dos profissionais de dados no Brasil, conforme o dataset analisado, possui salários concentrados nas faixas inferiores a R$ 15.000, com picos importantes em torno de R$ 4.000-R$6.000 e R$ 9.000-R$10.000. No entanto, existe uma parcela de profissionais que alcança remunerações significativamente mais elevadas, estendendo a distribuição para a direita[1].

## Grafico Relação entre Salário e Tempo de Experiência
![__results___0_2](https://github.com/user-attachments/assets/5b842f17-cbc8-46af-8bf5-7c8bf30bc7e7)
## Explicação do Gráfico: Relação entre Salário e Tempo de Experiência

O gráfico de boxplot intitulado "Relação entre Salário e Tempo de Experiência" ilustra como a faixa salarial numérica ("Faixa_salarial_num") varia conforme o "Tempo de experiência na área de dados" no Brasil[1].

**Como ler este gráfico de Boxplot:**
*   **Caixa (Box):** Representa o intervalo interquartil (IQR), onde se concentram 50% dos salários. A linha inferior da caixa é o primeiro quartil (Q1 - 25º percentil), e a linha superior é o terceiro quartil (Q3 - 75º percentil)[1].
*   **Linha dentro da Caixa:** Indica a mediana (Q2 - 50º percentil), que é o valor salarial central para cada grupo de experiência[1].
*   **Hastess/"Bigodes" (Whiskers):** As linhas que se estendem a partir da caixa mostram o alcance dos dados, geralmente até 1,5 vezes o IQR. Pontos além dessas hastes são considerados outliers[1].
*   **Outliers:** São pontos individuais (losangos no gráfico) que representam salários atípicos, muito acima ou abaixo da maioria dos salários para aquele grupo de experiência[1].
*   **Eixo Y (Vertical):** "Faixa\_salarial\_num" representa os salários em Reais (R$), variando de R$ 0 a R$ 40.000[1].
*   **Eixo X (Horizontal):** "Tempo de experiência na área de dados" categoriza os profissionais em diferentes faixas de anos de experiência: "Menos de 1 ano", "de 1 a 2 anos", "de 3 a 4 anos", "de 4 a 6 anos", "de 5 a 6 anos", e "de 7 a 10 anos". As categorias no eixo X do gráfico original não estão em ordem crescente de experiência[1].

**Interpretação das Tendências Observadas:**

Ao analisar os boxplots para cada faixa de experiência (considerando-os em ordem crescente de experiência):

*   **Tendência Geral de Aumento Salarial com a Experiência:**
    *   **Menos de 1 ano:** Este grupo apresenta a menor mediana salarial, situando-se em torno de R$ 3.500 - R$ 4.000. A maioria dos salários (IQR) está entre aproximadamente R$ 2.000 e R$ 5.000[1].
    *   **De 1 a 2 anos:** A mediana salarial sobe para cerca de R$ 5.000. O IQR varia de R$ 3.500 a R$ 7.000[1].
    *   **De 3 a 4 anos:** Observa-se um aumento mais significativo na mediana, que se localiza em torno de R$ 8.000 - R$ 8.500. O IQR está entre R$ 5.000 e R$ 10.000[1].
    *   **De 4 a 6 anos / De 5 a 6 anos / De 7 a 10 anos:** Estes grupos com maior experiência apresentam medianas salariais consideravelmente mais altas e bastante próximas entre si.
        *   A mediana para "de 4 a 6 anos" e "de 5 a 6 anos" (que parecem muito similares no gráfico) está em torno de R$ 11.000 - R$ 12.000, com IQR entre R$ 10.000 e R$ 14.000[1].
        *   Para "de 7 a 10 anos", a mediana é ligeiramente superior, em torno de R$ 12.000 - R$ 13.000, com um IQR similar (R$ 10.000 a R$ 14.000)[1].

*   **Variabilidade Salarial (Dispersão):**
    *   A dispersão salarial (representada pela altura da caixa e o comprimento das hastes) tende a aumentar com a experiência. Profissionais nos níveis iniciais de carreira ("Menos de 1 ano") apresentam uma faixa salarial mais concentrada em comparação com aqueles com mais experiência, onde a variabilidade é maior[1].
    *   Os grupos com mais experiência ("de 4 a 6 anos" em diante) mostram uma dispersão salarial maior, indicando que, embora a média seja mais alta, há uma gama mais ampla de salários sendo pagos[1].

*   **Outliers:**
    *   Outliers (salários muito acima do comum para o grupo) são observados em todas as categorias de experiência[1].
    *   Nos grupos com mais experiência (a partir de "de 3 a 4 anos"), alguns profissionais atingem salários de até R$ 40.000, indicando um potencial de alta remuneração para os mais experientes ou em posições de destaque[1].
    *   Mesmo no grupo com "Menos de 1 ano", existe um outlier próximo a R$ 14.000[1].

**Conclusão do Gráfico:**
O gráfico demonstra uma clara correlação positiva entre o tempo de experiência na área de dados e o nível salarial. Profissionais com mais anos de atuação tendem a ter salários medianos mais altos e também uma maior variabilidade salarial, com alguns indivíduos alcançando remunerações substancialmente elevadas[1]. A progressão salarial parece ser mais acentuada nos primeiros anos de carreira, estabilizando-se em um patamar mais elevado para profissionais com 4 ou mais anos de experiência[1].

## Grafico Distribuição Salarial por Nível de Ensino
![__results___0_3](https://github.com/user-attachments/assets/45da8bf1-dfcc-4fac-911f-96af9f6a8b34)
## Explicação do Gráfico: Distribuição Salarial por Nível de Ensino

O gráfico de violino apresentado, intitulado "Distribuição Salarial por Nível de Ensino", exibe como a faixa salarial numérica ("Faixa\_salarial\_num") se distribui entre diferentes níveis de escolaridade alcançados por profissionais de dados no Brasil[1].

**Como ler este gráfico de Violino:**
*   **Forma do Violino:** A largura do violino em diferentes pontos representa a densidade dos dados naquela faixa salarial. Onde o violino é mais largo, há uma maior concentração de profissionais com salários naquele nível[1].
*   **Caixa Interna (Box Plot):** Dentro de cada violino, há um box plot:
    *   A **linha branca grossa** no centro da caixa indica a **mediana** salarial (o valor central)[1].
    *   A **caixa retangular** representa o **intervalo interquartil (IQR)**, contendo 50% dos dados (do 25º ao 75º percentil)[1].
    *   As **linhas/hastes (whiskers)** que se estendem da caixa mostram o alcance principal dos dados, e pontos além delas podem ser considerados outliers (embora o violino em si mostre a forma completa da distribuição, incluindo os extremos)[1].
*   **Eixo Y (Vertical):** "Faixa\_salarial\_num" representa os salários em Reais (R$), variando de R$ 0 até mais de R$ 40.000[1].
*   **Eixo X (Horizontal):** "Nível de ensino alcançado" categoriza os profissionais pelos seguintes níveis de educação[1]:
    *   Doutorado ou Phd
    *   Graduação/Bacharelado
    *   Estudante de Graduação
    *   Pós-graduação
    *   Mestrado

**Interpretação das Distribuições Salariais por Nível de Ensino:**

*   **Estudante de Graduação (Verde):**
    *   Apresenta a **menor mediana salarial**, localizada em torno de R$ 4.000 - R$ 5.000[1].
    *   A distribuição é mais concentrada em salários baixos, com a parte mais larga do violino nessa região. A maioria dos salários está abaixo de R$ 10.000, embora a cauda superior se estenda até cerca de R$ 25.000[1].

*   **Graduação/Bacharelado (Laranja):**
    *   A mediana salarial sobe para aproximadamente R$ 8.000 - R$ 9.000[1].
    *   A distribuição é mais ampla, com uma concentração significativa de salários entre R$ 5.000 e R$ 15.000. Apresenta uma cauda superior longa, indicando que alguns profissionais com esta formação atingem salários bem elevados, chegando até R$ 40.000 ou mais[1].

*   **Pós-graduação (Vermelho):**
    *   A mediana salarial é ligeiramente superior à de "Graduação/Bacharelado", situando-se em torno de R$ 10.000 - R$ 11.000[1].
    *   A forma da distribuição é semelhante à de "Graduação/Bacharelado", com uma concentração principal e uma cauda longa para salários mais altos, também atingindo valores acima de R$ 40.000[1]. O violino parece ter uma ligeira "cintura" indicando uma menor densidade entre a concentração mais baixa e a mediana.

*   **Mestrado (Roxo):**
    *   Este grupo apresenta uma das **medianas salariais mais altas**, em torno de R$ 11.000 - R$ 13.000[1].
    *   A maior parte da densidade salarial está concentrada em uma faixa mais elevada em comparação com "Graduação/Bacharelado" e "Pós-graduação". A cauda superior também é proeminente, indicando potencial para altos salários[1].

*   **Doutorado ou Phd (Azul):**
    *   A mediana salarial é comparável à de "Mestrado" ou ligeiramente inferior, em torno de R$ 10.000 - R$ 12.000[1].
    *   A distribuição é bastante dispersa, com o corpo do violino sendo largo, indicando maior variabilidade nos salários para este grupo. A cauda superior é extensa, mostrando que profissionais com doutorado também podem alcançar os salários mais altos do dataset[1].

**Conclusões Gerais do Gráfico:**
*   Há uma tendência geral de **aumento da mediana salarial com o avanço no nível de ensino**, sendo mais notável a diferença entre "Estudante de Graduação" e os demais níveis.
*   Profissionais com **Mestrado** e **Doutorado/PhD** tendem a ter as medianas salariais mais elevadas, embora a diferença entre eles e "Pós-graduação" (lato sensu, especializações) possa não ser tão acentuada em termos de mediana, mas sim na forma da distribuição e potencial para salários muito altos[1].
*   Todos os níveis de ensino, a partir da graduação, mostram uma **assimetria à direita** (cauda longa para salários altos), indicando que em todos os níveis há profissionais que conseguem remunerações significativamente acima da média do seu grupo[1].
*   A **variabilidade salarial** (largura do violino e comprimento das caudas) também é considerável em todos os níveis, especialmente para aqueles com formação superior completa em diante[1].

## Grafico Interação entre Escolaridade, Experiência e Salário
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/99901a7169839052f5473ff6f4b57242/raw/6c71c7167850cb50f4e98432a646db7c69f2ffa1/grafico_3d_interativo.html)

![newplot](https://github.com/user-attachments/assets/5bb94b6a-aa5d-416d-be48-9bac9d9d01c0)
## Explicação do Gráfico 3D Interativo: Interação entre Escolaridade, Experiência e Salário

O gráfico apresentado é uma visualização 3D interativa que tem como objetivo investigar a interação entre o nível de escolaridade, o tempo de experiência e o salário dos profissionais de dados no Brasil[2]. Gráficos de superfície ou dispersão 3D são úteis para investigar como uma variável de resposta (neste caso, o salário) se relaciona com duas variáveis preditoras (escolaridade e experiência)[7].

**Eixos do Gráfico:**
*   **Eixo X (Horizontal, profundidade):** "Tempo de Experiência (anos)" – Representa os anos de experiência profissional na área de dados. A escala parece variar de 0 a aproximadamente 10 anos[2].
*   **Eixo Y (Horizontal, largura):** "Nível de Escolaridade (numérico)" – Representa o nível de escolaridade, que foi convertido para uma escala numérica para permitir a plotagem. A legenda indica a correspondência:
    *   0: Doutorado ou PhD
    *   1: Estudante de Graduação
    *   2: Graduação/Bacharelado
    *   3: Mestrado
    *   4: Pós-graduação[2]
*   **Eixo Z (Vertical):** "Salário (R$)" – Representa a remuneração mensal em Reais. A escala vai de R$0 até valores superiores a R$35.000[2].

**Interpretação dos Dados e Visualização:**
*   **Pontos de Dados (Scatter Plot 3D):** Cada ponto no gráfico representa um profissional de dados, posicionado de acordo com seu tempo de experiência, nível de escolaridade (numérico) e salário[2].
*   **Cores por Nível de Escolaridade:** Os pontos são coloridos de acordo com o nível de escolaridade, facilitando a distinção e a análise de como cada grupo educacional se distribui em relação à experiência e ao salário[2].
    *   **Doutorado ou PhD (Azul Escuro/Roxo):** Pontos para este grupo.
    *   **Estudante de Graduação (Azul Claro/Ciano):** Pontos para este grupo.
    *   **Graduação/Bacharelado (Verde):** Pontos para este grupo.
    *   **Mestrado (Laranja/Amarelo):** Pontos para este grupo.
    *   **Pós-graduação (Vermelho):** Pontos para este grupo.
*   **Interatividade:** A natureza interativa do gráfico permite ao usuário girar a visualização, alterar o ângulo de visão e dar zoom. Isso é crucial para explorar as relações complexas em um espaço tridimensional, identificando padrões, concentrações de pontos e outliers que poderiam não ser evidentes em gráficos 2D[2][15].

**Observações Gerais e Tendências (Inferidas pela Exploração Visual):**
*   **Impacto da Experiência:** Geralmente, observa-se que, para todos os níveis de escolaridade, um aumento no tempo de experiência (movimento ao longo do eixo X) tende a estar associado a salários mais altos (pontos mais elevados no eixo Z)[2].
*   **Impacto da Escolaridade:**
    *   **Estudantes de Graduação (cor Azul Claro/Ciano):** Tendem a se concentrar na parte inferior da escala salarial e com menor tempo de experiência[2].
    *   **Graduação/Bacharelado (cor Verde) e Pós-graduação (cor Vermelho):** Mostram uma dispersão maior, com salários aumentando com a experiência. Muitos pontos se situam em faixas salariais intermediárias, mas com potencial de alcançar salários mais altos com mais experiência[2].
    *   **Mestrado (cor Laranja/Amarelo) e Doutorado/PhD (cor Azul Escuro/Roxo):** Estes grupos tendem a ter pontos que alcançam os níveis salariais mais altos, especialmente quando combinados com maior tempo de experiência. Pode-se observar se há uma "elevação" geral dos pontos dessas cores no eixo Z[2].
*   **Interação entre Escolaridade e Experiência:** O objetivo principal deste gráfico é visualizar como a combinação específica de um nível de escolaridade e anos de experiência influencia o salário. Por exemplo, pode-se tentar observar se o "retorno" (aumento salarial) por ano adicional de experiência é diferente para quem tem um Mestrado em comparação com quem tem apenas Graduação. A densidade de pontos em certas regiões do gráfico (por exemplo, alta experiência e alto nível de escolaridade resultando em altos salários) pode indicar essas interações[2]. Picos e vales na distribuição dos pontos podem corresponder a combinações que produzem valores máximos ou mínimos de salário[7].

**Como Explorar o Gráfico Interativo:**
*   **Girar:** Clique e arraste para mudar o ponto de vista e observar a nuvem de pontos de diferentes ângulos. Isso ajuda a entender a profundidade e a sobreposição dos dados[2].
*   **Zoom:** Use o scroll do mouse para aproximar ou afastar, permitindo focar em áreas específicas de interesse (por exemplo, a distribuição salarial para um nível de escolaridade específico com muitos anos de experiência)[2].
*   **Observar Agrupamentos:** Procure por concentrações de pontos de uma mesma cor em determinadas regiões do espaço 3D.

Este tipo de gráfico é uma ferramenta poderosa na análise exploratória de dados (EDA) para identificar relações multivariadas e gerar hipóteses sobre as interações entre diferentes fatores[4][5].

## Grafico Mapa de Calor de Correlações
![__results___0_5](https://github.com/user-attachments/assets/5cf1cb29-6d4c-46dc-bc80-b9b32d679b12)
## Explicação do Gráfico: Mapa de Calor de Correlações

O gráfico apresentado é um **Mapa de Calor de Correlações** (heatmap) que visualiza a força e a direção das relações lineares entre três variáveis numéricas: "Faixa\_salarial\_num", "Oportunidade de aprendizado" e "Reputação da empresa"[1].

**Como ler este Mapa de Calor:**
*   **Variáveis:** As variáveis analisadas estão listadas tanto nas linhas (eixo Y) quanto nas colunas (eixo X) da matriz[1].
*   **Células Coloridas:** Cada célula na interseção de duas variáveis mostra o coeficiente de correlação entre elas. A cor da célula representa visualmente esse coeficiente[1].
*   **Barra de Cores (Escala):** Localizada à direita do gráfico, a barra de cores indica como os valores de correlação mapeiam para as cores. Nesta visualização:
    *   Cores quentes (como vermelho intenso) indicam correlações positivas fortes, aproximando-se de +1.0[1].
    *   Cores frias (como azul intenso/roxo) indicam correlações negativas fortes (aproximando-se de -1.0) ou, como neste caso, correlações muito fracas ou próximas de zero[1].
    *   Cores neutras ou claras no meio da escala (se presentes) indicariam correlações próximas de 0. A escala no gráfico vai de 0.0 (azul escuro) a 1.0 (vermelho escuro)[1].
*   **Valores Numéricos:** Dentro de cada célula, o valor numérico exato do coeficiente de correlação é exibido. Estes coeficientes variam de -1 (correlação negativa perfeita) a +1 (correlação positiva perfeita), com 0 indicando ausência de correlação linear[1].

**Interpretação das Correlações Exibidas:**

1.  **Diagonal Principal (de cima para baixo, da esquerda para a direita):**
    *   As células na diagonal principal mostram a correlação de cada variável consigo mesma. Esses valores são sempre **1.00** (vermelho intenso), indicando uma correlação positiva perfeita, o que é esperado[1].
        *   Faixa\_salarial\_num com Faixa\_salarial\_num: 1.00
        *   Oportunidade de aprendizado com Oportunidade de aprendizado: 1.00
        *   Reputação da empresa com Reputação da empresa: 1.00

2.  **Correlações entre Variáveis Distintas:**
    *   **Faixa\_salarial\_num e Oportunidade de aprendizado:**
        *   Coeficiente: **-0.04**[1].
        *   Cor: Azul escuro[1].
        *   Interpretação: Existe uma correlação linear negativa muito fraca, praticamente inexistente, entre a faixa salarial e a oportunidade de aprendizado. Um valor tão próximo de zero sugere que não há uma tendência clara de aumento ou diminuição salarial associada diretamente a maiores ou menores oportunidades de aprendizado, conforme os dados analisados[1].

    *   **Faixa\_salarial\_num e Reputação da empresa:**
        *   Coeficiente: **0.00**[1].
        *   Cor: Azul escuro[1].
        *   Interpretação: Não há correlação linear entre a faixa salarial e a reputação da empresa. Isso indica que, neste conjunto de dados, a reputação da empresa não está linearmente associada a salários mais altos ou mais baixos[1].

    *   **Oportunidade de aprendizado e Reputação da empresa:**
        *   Coeficiente: **-0.05**[1].
        *   Cor: Azul escuro[1].
        *   Interpretação: Há uma correlação linear negativa muito fraca, quase nula, entre a oportunidade de aprendizado e a reputação da empresa. Isso sugere que não há uma relação linear significativa onde empresas com melhor reputação ofereçam consistentemente mais (ou menos) oportunidades de aprendizado, ou vice-versa, de acordo com os dados[1].

**Conclusão Geral do Mapa de Calor:**
Este mapa de calor indica que as três variáveis analisadas ("Faixa\_salarial\_num", "Oportunidade de aprendizado" e "Reputação da empresa") não possuem correlações lineares fortes entre si no contexto dos dados utilizados para esta análise. Todos os coeficientes de correlação entre pares de variáveis distintas são muito próximos de zero, sugerindo que essas variáveis são, em grande medida, linearmente independentes umas das outras[1]. É importante notar que a correlação mede apenas relações lineares; podem existir relações não lineares que não seriam capturadas por este tipo de análise.

## Grafico Distribuição por Gênero e Raça/Etnia
![__results___0_6](https://github.com/user-attachments/assets/46d749b3-6293-46b5-bca7-021d3843a544)
## Explicação dos Gráficos: Distribuição por Gênero e Raça/Etnia

A imagem anexa exibe dois gráficos de barras que ilustram a distribuição demográfica dos profissionais no conjunto de dados analisado, um por gênero e outro por raça/etnia[1].

### Gráfico 1: Distribuição por Gênero

*   **Título:** "Distribuição por Gênero"[1]
*   **Tipo de Gráfico:** Gráfico de barras verticais.
*   **Eixo Y (Vertical):** "count" (Contagem) – Indica o número de profissionais. A escala vai de 0 a 2500[1].
*   **Eixo X (Horizontal):** "Gênero do profissional" – Apresenta as categorias de gênero[1].
*   **Observações:**
    *   **Masculino:** É a categoria predominante, com uma contagem de aproximadamente 2500 profissionais. Esta é a barra mais alta no gráfico[1].
    *   **Feminino:** A segunda maior categoria, com uma contagem significativamente menor, em torno de 800 profissionais[1].
    *   **Outro:** Representa uma contagem muito pequena, quase insignificante visualmente no gráfico[1].
    *   **Prefiro não informar:** Também representa uma contagem muito pequena, similar à categoria "Outro"[1].
*   **Conclusão:** O gráfico demonstra uma expressiva maioria de profissionais do gênero masculino no conjunto de dados analisado[1].

### Gráfico 2: Distribuição por Raça/Etnia

*   **Título:** "Distribuição por Raça/Etnia"[1]
*   **Tipo de Gráfico:** Gráfico de barras verticais.
*   **Eixo Y (Vertical):** "count" (Contagem) – Indica o número de profissionais. A escala vai de 0 a mais de 2000[1].
*   **Eixo X (Horizontal):** "Cor/Raça/Etnia" – Apresenta as categorias de raça ou etnia[1].
*   **Observações:**
    *   **Branca:** É a categoria com a maior contagem, superando 2000 profissionais. Esta é a barra mais alta[1].
    *   **Parda:** A segunda categoria mais representada, com uma contagem de aproximadamente 800 profissionais[1].
    *   **Preta:** Apresenta uma contagem de cerca de 250 profissionais[1].
    *   **Amarela:** Possui uma contagem menor, em torno de 100 profissionais[1].
    *   **Prefiro não informar:** Representa uma contagem muito pequena, inferior a 50 profissionais[1].
    *   **Outra:** Contagem visualmente insignificante[1].
    *   **Indígena:** Contagem visualmente insignificante[1].
*   **Conclusão:** O gráfico indica que a maioria dos profissionais no conjunto de dados se identifica como Branca, seguida pela categoria Parda. Outras categorias raciais/étnicas têm representação consideravelmente menor[1].

**Resumo Geral:**
Ambos os gráficos mostram desequilíbrios significativos nas distribuições. Há uma predominância de profissionais do gênero masculino e de profissionais que se identificam como da cor/raça Branca no dataset utilizado para a análise exploratória de dados[1].

## Grafico Distribuição Geográfica dos Profissionais
![__results___0_8](https://github.com/user-attachments/assets/b1f41cbe-9705-44ac-8b50-9407b5b07dd2)
## Explicação do Gráfico: Distribuição Geográfica dos Profissionais

O gráfico de barras verticais intitulado "Distribuição Geográfica dos Profissionais" ilustra a contagem de profissionais de dados distribuídos pelos diferentes estados (Unidades Federativas - UF) do Brasil, conforme o conjunto de dados analisado[1].

**Eixos do Gráfico:**
*   **Eixo Y (Vertical):** "Contagem" – Representa o número de profissionais em cada estado. A escala varia de 0 a mais de 1200[1].
*   **Eixo X (Horizontal):** "Estado (UF)" – Apresenta as siglas dos estados brasileiros[1].

**Interpretação da Distribuição Geográfica:**

*   **Concentração em São Paulo (SP):** O estado de São Paulo (SP) destaca-se com a maior concentração de profissionais, com uma contagem que ultrapassa 1200. Esta é, de longe, a barra mais alta no gráfico, indicando que uma parcela muito significativa dos profissionais no dataset está localizada em SP[1].
*   **Estados com Representação Significativa:** Após São Paulo, alguns outros estados apresentam contagens notáveis, embora consideravelmente menores:
    *   **Minas Gerais (MG):** É o segundo estado com maior número de profissionais, com uma contagem próxima de 400 (especificamente, cerca de 380)[1].
    *   **Paraná (PR):** Apresenta uma contagem um pouco acima de 300 profissionais[1].
    *   **Rio de Janeiro (RJ):** Também com uma contagem em torno de 300 profissionais[1].
    *   **Rio Grande do Sul (RS):** Possui cerca de 200 profissionais[1].
    *   **Santa Catarina (SC):** Apresenta uma contagem um pouco abaixo de 200, em torno de 180 profissionais[1].
*   **Demais Estados:**
    *   **Distrito Federal (DF), Bahia (BA), Ceará (CE), Pernambuco (PE), Espírito Santo (ES), Goiás (GO), Paraíba (PB):** Estes estados formam um grupo com contagens menores, variando aproximadamente entre 50 e 100 profissionais cada[1].
    *   **Outros Estados (MT, RN, AM, PA, SE, AL, MS, MA, PI, RO, AP, TO):** A grande maioria dos demais estados brasileiros apresenta contagens muito baixas, com barras quase insignificantes em comparação com os estados mais populosos em termos de profissionais de dados. Muitos desses estados têm menos de 50 profissionais representados no dataset[1].

**Conclusão Geral do Gráfico:**
O gráfico evidencia uma forte concentração geográfica dos profissionais de dados no Brasil, com o estado de São Paulo dominando expressivamente. A região Sudeste (com SP, MG, RJ, ES) e a região Sul (com PR, RS, SC) concentram a maior parte desses profissionais. As demais regiões e estados possuem uma representação significativamente menor no conjunto de dados analisado[1].

## Grafico Salário por Nível de Senioridade
![__results___0_9](https://github.com/user-attachments/assets/4cb778a5-1f36-40a9-b815-b0e97c02d2c8)
## Explicação do Gráfico: Salário por Nível de Senioridade

O gráfico de boxplot intitulado "Salário por Nível de Senioridade" ilustra a distribuição da faixa salarial numérica ("Faixa\_salarial\_num") entre diferentes níveis de senioridade profissional: Júnior, Pleno e Sênior[1].

**Como ler este gráfico de Boxplot:**
*   **Caixa (Box):** Representa o intervalo interquartil (IQR), onde se concentram 50% dos salários. A linha inferior da caixa é o primeiro quartil (Q1 - 25º percentil), e a linha superior é o terceiro quartil (Q3 - 75º percentil)[1].
*   **Linha dentro da Caixa:** Indica a mediana (Q2 - 50º percentil), que é o valor salarial central para cada nível de senioridade[1].
*   **Hastess/"Bigodes" (Whiskers):** As linhas que se estendem a partir da caixa mostram o alcance dos dados, geralmente até 1,5 vezes o IQR. Pontos além dessas hastes são considerados outliers[1].
*   **Outliers:** São pontos individuais (representados por losangos no gráfico) que indicam salários atípicos, significativamente mais altos ou mais baixos do que a maioria dos salários para aquele nível de senioridade[1].
*   **Eixo Y (Vertical):** "Faixa\_salarial\_num" representa os salários em Reais (R$), com a escala variando de R$0 a R$40.000[1].
*   **Eixo X (Horizontal):** "Nível de senioridade" categoriza os profissionais em "Júnior", "Pleno" e "Sênior"[1].

**Interpretação das Distribuições Salariais por Nível de Senioridade:**

*   **Júnior (Caixa Verde):**
    *   **Mediana Salarial:** É a mais baixa entre os três níveis, situando-se em torno de R$3.500 - R$4.000[1].
    *   **Intervalo Interquartil (IQR):** A maioria dos salários (50% centrais) está concentrada entre aproximadamente R$2.500 e R$5.000[1].
    *   **Dispersão e Outliers:** A faixa salarial típica (incluindo os "bigodes") vai de perto de R$0 até cerca de R$7.000. Observam-se alguns outliers com salários mais altos, chegando até aproximadamente R$18.000[1].

*   **Pleno (Caixa Laranja):**
    *   **Mediana Salarial:** Apresenta um aumento significativo em relação ao nível Júnior, localizando-se em torno de R$7.000[1].
    *   **Intervalo Interquartil (IQR):** Os 50% centrais dos salários estão entre aproximadamente R$5.000 e R$10.000[1].
    *   **Dispersão e Outliers:** A faixa salarial típica se estende de cerca de R$1.000 até aproximadamente R$14.000. Este nível possui vários outliers com salários mais elevados, incluindo valores próximos a R$18.000, R$22.500 e até um ponto próximo a R$40.000[1].

*   **Sênior (Caixa Azul):**
    *   **Mediana Salarial:** É a mais alta dos três níveis, posicionando-se em torno de R$11.500 - R$12.000[1].
    *   **Intervalo Interquartil (IQR):** A maior parte dos salários (50% centrais) varia entre R$10.000 e R$14.000[1].
    *   **Dispersão e Outliers:** A faixa salarial típica vai de aproximadamente R$5.000 até cerca de R$18.500. Assim como o nível Pleno, o nível Sênior também apresenta outliers com salários significativamente altos, com pontos próximos a R$22.500 e um próximo a R$40.000. Existem também alguns outliers inferiores, indicando salários mais baixos que o usual para esta senioridade[1].

**Conclusões Gerais do Gráfico:**
*   **Progressão Salarial Clara:** O gráfico demonstra uma clara progressão salarial à medida que o nível de senioridade aumenta. Profissionais Sênior têm a maior mediana salarial, seguidos por Pleno e depois Júnior[1].
*   **Aumento da Dispersão:** A variabilidade salarial (altura da caixa e extensão dos "bigodes") tende a aumentar com a senioridade, indicando uma gama mais ampla de salários pagos nos níveis Pleno e Sênior em comparação com o Júnior[1].
*   **Potencial de Altos Salários:** Embora os outliers existam em todos os níveis, eles atingem valores mais altos e são mais frequentes nos níveis Pleno e Sênior, sugerindo que profissionais com maior senioridade têm maior potencial para alcançar remunerações excepcionalmente elevadas[1].

Em resumo, o nível de senioridade é um fator importante na determinação da faixa salarial, com um aumento consistente na remuneração e na variabilidade salarial à medida que os profissionais progridem de Júnior para Pleno e Sênior[1].

## Grafico Análise Multivariada das Relações entre Variáveis Selecionadas (Pair Plot)
![__results___0_11](https://github.com/user-attachments/assets/f8a270d1-8bb7-4612-9c54-0c083f46936a)
## Explicação do Gráfico: Análise Multivariada das Relações entre Variáveis Selecionadas (Pair Plot)

O gráfico apresentado é uma **matriz de gráficos de dispersão (pair plot)**, intitulada "Análise Multivariada das Relações entre Variáveis Selecionadas". Este tipo de visualização é utilizado para mostrar as relações entre pares de múltiplas variáveis simultaneamente, bem como a distribuição individual de cada variável[1].

As variáveis analisadas são:
*   "Faixa\_salarial\_num" (Salário)
*   "Oportunidade de aprendizado"
*   "Reputação da empresa"

**Estrutura do Gráfico:**

*   **Diagonal Principal:** Os gráficos ao longo da diagonal (do canto superior esquerdo ao canto inferior direito) mostram a **distribuição de cada variável individualmente**, geralmente através de um histograma ou, como neste caso, uma estimativa de densidade do kernel (KDE)[1].
*   **Fora da Diagonal:** Os gráficos fora da diagonal são **gráficos de dispersão (scatter plots)** que mostram a relação entre duas variáveis diferentes. Cada gráfico de dispersão (i,j) mostra a variável do eixo i contra a variável do eixo j[1].

**Interpretação dos Gráficos Individuais:**

1.  **Distribuições Individuais (Diagonal):**
    *   **Faixa\_salarial\_num (Topo Esquerdo):** A distribuição dos salários é multimodal (apresenta múltiplos picos) e assimétrica à direita. Há uma concentração maior em salários mais baixos (em torno de R$5.000-R$10.000), com picos menores em salários mais altos e uma cauda que se estende até R$40.000[1].
    *   **Oportunidade de aprendizado (Meio):** Esta variável parece ser binária ou categórica, com a grande maioria dos dados concentrada em dois valores principais (provavelmente 0 e 1, representando, por exemplo, baixa/alta oportunidade ou sim/não). Há um pico maior em um dos valores e um pico menor no outro[1].
    *   **Reputação da empresa (Inferior Direito):** Similar à "Oportunidade de aprendizado", esta variável também parece ser binária ou categórica, com a maioria dos dados concentrados em dois valores principais. Um dos valores tem uma densidade muito maior que o outro[1].

2.  **Relações entre Pares de Variáveis (Fora da Diagonal):**

    *   **Oportunidade de aprendizado vs. Faixa\_salarial\_num (Linha 1, Coluna 2 e Linha 2, Coluna 1):**
        *   Os pontos estão concentrados em duas faixas horizontais (ou verticais, dependendo da orientação do par), correspondentes aos dois principais valores da variável "Oportunidade de aprendizado"[1].
        *   Visualmente, não há uma tendência clara (ascendente ou descendente) que sugira uma forte correlação linear entre salário e oportunidade de aprendizado. Os salários parecem variar amplamente para ambos os níveis de oportunidade de aprendizado[1].

    *   **Reputação da empresa vs. Faixa\_salarial\_num (Linha 1, Coluna 3 e Linha 3, Coluna 1):**
        *   Similar ao par anterior, os pontos se agrupam em duas faixas horizontais (ou verticais) correspondentes aos valores da "Reputação da empresa"[1].
        *   Não se observa uma relação linear forte. Os salários variam amplamente independentemente do nível de reputação da empresa exibido[1].

    *   **Reputação da empresa vs. Oportunidade de aprendizado (Linha 2, Coluna 3 e Linha 3, Coluna 2):**
        *   Este gráfico mostra como os dois valores de "Oportunidade de aprendizado" se distribuem em relação aos dois valores de "Reputação da empresa". Os pontos se agrupam nos quatro cantos possíveis (0,0; 0,1; 1,0; 1,1), se as variáveis forem binárias 0/1. A densidade de pontos em cada um desses "cantos" indicaria a frequência dessas combinações[1].
        *   Visualmente, parece não haver um padrão forte de associação. Por exemplo, não parece que empresas com alta reputação consistentemente oferecem alta oportunidade de aprendizado, ou vice-versa[1].

**Conclusão Geral do Gráfico:**
O pair plot reforça visualmente a ausência de correlações lineares fortes entre "Faixa\_salarial\_num", "Oportunidade de aprendizado" e "Reputação da empresa", o que já havia sido sugerido pelo mapa de calor de correlações anteriormente. As variáveis "Oportunidade de aprendizado" e "Reputação da empresa" apresentam distribuições que sugerem natureza binária ou categórica com poucos níveis. As relações entre os pares de variáveis não exibem padrões lineares claros, indicando que esses fatores, isoladamente ou em pares diretos, não explicam de forma linear e significativa a variação salarial ou uns aos outros neste conjunto de dados[1].

## Grafico Sunburst da Distribuição de Profissionais de Dados
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/11ec6c319fd644ad08f61cff87cc702c/raw/392be6308934280602be52c7a1ec9cab21e1ad03/sunburst_chart.html)
![newplot (1)](https://github.com/user-attachments/assets/fc4076b1-1a10-48d1-89b2-3f76a107321b)

## Explicação do Gráfico Interativo: Sunburst da Distribuição de Profissionais de Dados

O gráfico apresentado é um **gráfico de explosão solar (sunburst chart)** interativo. Este tipo de visualização é ideal para exibir dados hierárquicos, mostrando como um grupo principal se divide em subgrupos e assim por diante, em uma série de anéis concêntricos[1][3][5][7].

**Como Ler Este Gráfico Sunburst:**

*   **Círculos Concêntricos (Anéis):** Cada anel representa um nível na hierarquia dos dados[3][4][8].
    *   **Centro do Gráfico:** O círculo mais interno representa o topo da hierarquia, neste caso, o total de "Profissionais de Dados" no dataset analisado[1].
    *   **Anéis Subsequentes:** Cada anel externo subdivide as categorias do anel interno adjacente[3][7].
*   **Segmentos (Fatias):** Cada anel é dividido em segmentos. O tamanho (ângulo ou área) de cada segmento é proporcional à sua participação ou contagem dentro da categoria pai no anel interno[4][5].
*   **Cores:** Cores diferentes são usadas para distinguir as categorias em cada nível, ajudando na visualização das proporções e relações[8].
*   **Interatividade:**
    *   **Hover (Passar o Mouse):** Ao passar o mouse sobre um segmento, ele é destacado, e geralmente uma dica de ferramenta (tooltip) exibe informações detalhadas, como o caminho hierárquico completo e o valor (contagem de profissionais) para aquele segmento específico[1].
    *   **Clique:** Clicar em um segmento geralmente "foca" ou "dá zoom" naquela categoria, tornando-a o novo centro do gráfico e exibindo suas subdivisões com mais detalhes[1]. Clicar no centro do gráfico retorna ao nível hierárquico anterior.

**Hierarquia e Interpretação dos Dados Neste Gráfico Específico:**

Observando o gráfico interativo[1]:

1.  **Nível Central (Raiz):**
    *   Representa o total de "Profissionais de Dados" considerados na análise.

2.  **Primeiro Anel (Nível de Escolaridade):**
    *   Subdivide os profissionais de dados pelo "Nível de Escolaridade".
    *   As categorias visíveis são: "Graduação/Bacharelado", "Pós-graduação", "Mestrado", "Estudante de Graduação" e "Doutorado ou PhD"[1].
    *   O tamanho de cada segmento neste anel indica a proporção de profissionais com aquele nível de escolaridade. Por exemplo, "Graduação/Bacharelado" parece ser a maior fatia, indicando o nível de escolaridade mais comum[1].

3.  **Segundo Anel (Tempo de Experiência):**
    *   Subdivide cada categoria de "Nível de Escolaridade" pelo "Tempo de experiência na área de dados".
    *   As faixas de experiência incluem: "de 1 a 2 anos", "de 3 a 4 anos", "Menos de 1 ano", "de 4 a 6 anos", "de 7 a 10 anos" e "de 5 a 6 anos"[1].
    *   O tamanho de um segmento neste anel mostra, por exemplo, quantos profissionais com "Graduação/Bacharelado" têm "de 1 a 2 anos" de experiência.

4.  **Terceiro Anel (Faixa Salarial Média):**
    *   Subdivide cada combinação de "Nível de Escolaridade" e "Tempo de Experiência" pela "Faixa Salarial Média (R$)".
    *   As faixas salariais incluem: "0-5000", "5001-10000", "10001-15000", "15001-20000", etc[1].
    *   O tamanho de um segmento neste anel mais externo indica, por exemplo, quantos profissionais com "Graduação/Bacharelado" e "de 1 a 2 anos" de experiência se enquadram na faixa salarial de "5001-10000". Os números dentro dos segmentos representam a contagem de profissionais[1].

**Como Extrair Insights:**

*   **Proporções Dominantes:** Identifique rapidamente os níveis de escolaridade mais comuns, as faixas de experiência predominantes dentro de cada nível de escolaridade e as faixas salariais mais frequentes para cada combinação de escolaridade e experiência.
*   **Relações Hierárquicas:** Entenda como os grupos se subdividem. Por exemplo, pode-se explorar se profissionais com "Mestrado" e "de 7 a 10 anos" de experiência tendem a se concentrar em faixas salariais mais altas em comparação com aqueles com "Graduação/Bacharelado" e a mesma experiência.
*   **Exploração Interativa:** Use o clique para focar em segmentos de interesse. Por exemplo, clicando em "Mestrado", o gráfico se reorganizará para mostrar apenas as subdivisões de experiência e salário para mestres, permitindo uma análise mais detalhada desse subgrupo específico.

Este gráfico sunburst oferece uma visão rica e interativa da composição da força de trabalho de profissionais de dados no Brasil, de acordo com o dataset, permitindo a exploração de como a escolaridade, a experiência e os salários se inter-relacionam em diferentes níveis[1][6].

---

## Analise exploratoria de dados base de dados Microdados

---

## Grafico Distribuição Nacional de Níveis de Formação dos Docentes
![01_distribuicao_formacao_nacional](https://github.com/user-attachments/assets/0052b7ec-4124-4e90-a500-8abd26d0ccc8)
## Explicação do Gráfico: Distribuição Nacional de Níveis de Formação dos Docentes

O gráfico de pizza ilustra a proporção dos docentes em nível nacional, classificados de acordo com seu nível de formação acadêmica[2]. Os dados são provenientes do arquivo `microdados_agrupados_por_uf.csv`[1].

**Principais observações do gráfico:**

*   **Docentes com Doutorado:** Este grupo constitui a maior fatia, representando **52,3%** do total de docentes analisados[2]. Isso indica que mais da metade dos docentes possui o título acadêmico mais elevado.
*   **Docentes com Mestrado:** Correspondem a **33,3%** do corpo docente[2]. Somados aos doutores, os docentes com pós-graduação *stricto sensu* (mestrado ou doutorado) são a grande maioria.
*   **Docentes com Especialização:** Representam **13,9%** dos docentes[2]. Este grupo possui pós-graduação *lato sensu*.
*   **Docentes com Graduação:** Apenas **0,6%** dos docentes possuem somente a graduação como nível de formação mais alto[2]. Este é o menor grupo, sugerindo que a progressão para níveis de pós-graduação é comum na carreira docente.

**Contextualização para a Análise Exploratória de Dados:**

Este gráfico de pizza fornece uma visão geral do perfil educacional dos docentes no Brasil, com base nos dados disponíveis[1][2]. Ele demonstra uma alta qualificação acadêmica, com a maioria possuindo títulos de mestre ou doutor[2].

Para a pergunta de pesquisa original sobre "como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil", este gráfico oferece um panorama da variável "formação acadêmica" para o grupo de "docentes". No entanto, conforme discutido anteriormente, para analisar a disparidade salarial, seriam necessários dados de remuneração e uma clara identificação de "profissionais de dados", que não estão presentes no dataset atual[1].

A predominância de altos níveis de escolaridade é um fator importante, mas sua interação com a experiência profissional e o impacto na disparidade salarial demandariam um conjunto de dados mais completo[1].


## Grafico Top 10 Estados por Nível de Formação de Docentes
![02_top10_estados_formacao](https://github.com/user-attachments/assets/4513d6de-20bd-4e5b-9b93-1cd10b819ad5)
## Explicação do Gráfico: Top 10 Estados por Nível de Formação de Docentes

O gráfico de barras empilhadas ilustra o número total de docentes nos 10 estados com maior contingente, detalhando a distribuição desses profissionais conforme seu nível de formação acadêmica[1]. O eixo vertical ("Número de Docentes") quantifica o total de docentes, enquanto o eixo horizontal ("Estado") lista as siglas dos respectivos estados. Cada barra é segmentada por cores que representam os diferentes níveis de formação[1]:

*   **Rosa:** Docentes com Graduação
*   **Dourado/Marrom:** Docentes com Especialização
*   **Verde:** Docentes com Mestrado
*   **Azul-petróleo (Teal):** Docentes com Doutorado

**Principais observações do gráfico:**

*   **Liderança de São Paulo (SP):** O estado de São Paulo (SP) destaca-se com o maior número absoluto de docentes, ultrapassando 70.000 profissionais. Dentro deste total, a maior parcela é composta por docentes com doutorado, seguida por mestrado e especialização[1].
*   **Minas Gerais (MG) e Rio de Janeiro (RJ):** Minas Gerais (MG) ocupa a segunda posição, com aproximadamente 40.000 docentes, seguido pelo Rio de Janeiro (RJ), com pouco mais de 30.000. Ambos os estados também apresentam uma predominância de docentes com doutorado e mestrado[1].
*   **Demais Estados no Top 10:** Os estados do Paraná (PR), Rio Grande do Sul (RS), Bahia (BA), Santa Catarina (SC), Pernambuco (PE), Ceará (CE) e Goiás (GO) completam o ranking dos 10 estados com mais docentes. Em todos eles, a tendência de maior concentração nos níveis de doutorado e mestrado se mantém, embora em menor escala absoluta comparado a SP, MG e RJ[1].
*   **Proporção dos Níveis de Formação:** Em todos os estados visualizados, a formação de doutorado (azul-petróleo) representa a maior ou uma das maiores parcelas do total de docentes. Em seguida, geralmente aparecem os docentes com mestrado (verde). Docentes com apenas especialização (dourado/marrom) formam um grupo menor, e aqueles com apenas graduação (rosa) são a menor fração, quase imperceptível em alguns estados, indicando um alto nível de qualificação formal do corpo docente nesses estados[1].

**Contextualização para a Análise Exploratória de Dados:**

Este gráfico permite uma comparação visual da quantidade e do perfil de formação dos docentes entre os principais estados brasileiros. Ele reforça a observação de que o corpo docente, especialmente nos estados com maior número de profissionais, possui elevada qualificação acadêmica, com forte presença de doutores e mestres[1].

Para a pergunta de pesquisa sobre a influência da formação acadêmica e experiência profissional na disparidade salarial entre profissionais de dados, este gráfico detalha a variável "formação acadêmica" em um nível geográfico (estadual) para "docentes". A análise da disparidade salarial, contudo, ainda dependeria da inclusão de dados de remuneração e da identificação específica de "profissionais de dados" dentro desse universo de docentes ou em um dataset complementar[1]. Observar onde se concentram os docentes mais qualificados pode ser um ponto de partida para investigar se há correlação com polos de desenvolvimento em ciência de dados, mas a relação direta com salários não pode ser inferida apenas com este gráfico.

## Grafico Distribuição Etária Nacional dos Docentes
![03_distribuicao_etaria_nacional](https://github.com/user-attachments/assets/38b315e0-7eb6-4c40-820f-3b0281b1b1d8)
## Explicação do Gráfico: Distribuição Etária Nacional dos Docentes

O gráfico de barras verticais, intitulado "Distribuição Etária Nacional dos Docentes", exibe a quantidade de docentes em nível nacional, agrupados por diferentes faixas etárias[1]. O eixo vertical ("Quantidade") indica o número de docentes, enquanto o eixo horizontal ("Faixa Etária") categoriza os docentes em grupos de idade[1].

**Principais observações do gráfico:**

*   **Pico na Faixa de 40-44 anos:** A faixa etária com o maior número de docentes é a de "Docentes\_Idade\_40\_44", com quase 70.000 profissionais[1]. Isso sugere que o maior contingente de docentes se encontra nessa fase da carreira.
*   **Concentração entre 35 e 49 anos:** As faixas etárias "Docentes\_Idade\_35\_39" (pouco mais de 60.000 docentes) e "Docentes\_Idade\_45\_49" (pouco menos de 60.000 docentes) também apresentam um número elevado de profissionais, indicando que uma parcela significativa do corpo docente nacional está entre 35 e 49 anos[1].
*   **Presença Significativa em Faixas Mais Elevadas:** A faixa "Docentes\_Idade\_60\_mais" também mostra um número considerável de docentes, com mais de 45.000 profissionais. Isso indica uma retenção de docentes mais experientes no sistema ou um envelhecimento da força de trabalho docente[1].
*   **Menor Quantidade nas Faixas Mais Jovens e Intermediárias Superiores:** As faixas "Docentes\_Idade\_30\_34" (pouco menos de 40.000), "Docentes\_Idade\_50\_54" (aproximadamente 45.000) e "Docentes\_Idade\_55\_59" (pouco menos de 40.000) apresentam quantidades menores em comparação com o pico, mas ainda representam um número substancial de docentes[1]. A distribuição geral se assemelha a uma curva que atinge seu pico na faixa dos 40-44 anos e depois declina gradualmente, com uma leve recuperação na faixa de 60 anos ou mais.

**Contextualização para a Análise Exploratória de Dados:**

Este gráfico fornece um panorama da distribuição etária dos docentes no Brasil[1]. No contexto da pergunta de pesquisa sobre "como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil", a idade pode ser utilizada como um *proxy* (uma aproximação) para a experiência profissional. Geralmente, espera-se que profissionais mais velhos tenham acumulado mais anos de experiência.

A concentração de docentes em faixas etárias mais maduras (40-49 anos) e a presença significativa de docentes com 60 anos ou mais podem indicar um corpo docente experiente[1]. Para analisar a disparidade salarial, seria necessário cruzar esses dados etários (como proxy de experiência) com informações sobre a formação acadêmica (analisada em gráficos anteriores) e, crucialmente, com dados de remuneração específicos para "profissionais de dados", os quais não estão presentes no dataset atual. Este gráfico ajuda a caracterizar uma dimensão da "experiência profissional" de forma agregada para o grupo de docentes.


## Grafico Matriz de Correlação entre Formação e Faixa Etária
![04_heatmap_correlacao](https://github.com/user-attachments/assets/18c3148a-1e19-49af-bc4e-bbc1b61910bf)
## Explicação do Gráfico: Matriz de Correlação entre Formação e Faixa Etária

O gráfico apresentado é uma **matriz de correlação**, visualizada como um *heatmap* (mapa de calor)[1]. Ele exibe a força e a direção da relação linear entre diferentes níveis de formação acadêmica dos docentes e suas faixas etárias, com base nos dados agregados por Unidade da Federação (UF).

**Como interpretar o gráfico:**

*   **Eixos:** Tanto o eixo horizontal quanto o vertical listam as mesmas variáveis: os diferentes níveis de formação (`Docentes_Graduacao`, `Docentes_Especializacao`, `Docentes_Mestrado`, `Docentes_Doutorado`) e as diferentes faixas etárias (`Docentes_Idade_30_34`, ..., `Docentes_Idade_60_mais`)[1].
*   **Células e Valores:** Cada célula na interseção de duas variáveis mostra o coeficiente de correlação de Pearson entre elas. Este coeficiente varia de -1 a +1:
    *   **+1:** Correlação positiva perfeita (quando uma variável aumenta, a outra também aumenta proporcionalmente).
    *   **0:** Nenhuma correlação linear.
    *   **-1:** Correlação negativa perfeita (quando uma variável aumenta, a outra diminui proporcionalmente).
*   **Cores:** A barra de cores à direita indica a intensidade da correlação:
    *   **Cores quentes (vermelho intenso):** Correlação positiva forte (próxima de +1).
    *   **Cores frias (azul intenso):** Correlação negativa forte (próxima de -1).
    *   **Cores neutras (próximo ao branco/cinza claro):** Correlação fraca (próxima de 0).
*   **Diagonal Principal:** A diagonal de cima para baixo, da esquerda para a direita, sempre mostra o valor 1.00 (vermelho intenso), pois representa a correlação de cada variável consigo mesma, que é sempre perfeita[1].

**Principais observações e correlações:**

1.  **Alta Correlação entre Níveis de Pós-Graduação:**
    *   Há correlações muito fortes e positivas entre os diferentes níveis de pós-graduação. Por exemplo, `Docentes_Mestrado` e `Docentes_Doutorado` têm uma correlação de 0.98. Similarmente, `Docentes_Especializacao` e `Docentes_Mestrado` também apresentam 0.98[1].
    *   Isso sugere que as UFs que possuem um alto número de docentes com um tipo de pós-graduação (ex: mestrado) tendem a ter também um alto número de docentes com outros tipos de pós-graduação (ex: doutorado, especialização).

2.  **Alta Correlação entre Faixas Etárias Adjacentes e Próximas:**
    *   As faixas etárias demonstram correlações positivas muito altas entre si, especialmente as adjacentes. Por exemplo, `Docentes_Idade_35_39` e `Docentes_Idade_40_44` têm correlação de 0.99[1].
    *   Isso indica que UFs com muitos docentes em uma faixa etária específica tendem a ter também muitos docentes nas faixas etárias vizinhas.

3.  **Forte Correlação entre Níveis de Pós-Graduação e a Maioria das Faixas Etárias:**
    *   Os níveis de pós-graduação (`Docentes_Especializacao`, `Docentes_Mestrado`, `Docentes_Doutorado`) mostram correlações positivas consistentemente altas (geralmente acima de 0.90) com a maioria das faixas etárias, especialmente as intermediárias e mais velhas (a partir de `Docentes_Idade_35_39` até `Docentes_Idade_55_59`)[1].
    *   Por exemplo, `Docentes_Mestrado` tem correlação de 1.00 com `Docentes_Idade_45_49`, e `Docentes_Doutorado` tem 0.99 com `Docentes_Idade_40_44` e `Docentes_Idade_45_49`[1].
    *   Isso sugere que UFs com um grande número de docentes pós-graduados tendem a ter um grande número de docentes distribuídos por diversas faixas etárias, refletindo um corpo docente qualificado e maduro.

4.  **Correlações Mais Baixas com `Docentes_Graduacao`:**
    *   A variável `Docentes_Graduacao` (que representa docentes apenas com graduação) apresenta correlações consideravelmente mais baixas com todos os outros níveis de formação e com todas as faixas etárias (valores variando de 0.26 a 0.40)[1].
    *   Por exemplo, a correlação entre `Docentes_Graduacao` e `Docentes_Doutorado` é de 0.38, e entre `Docentes_Graduacao` e `Docentes_Idade_35_39` é de 0.40[1].
    *   Isso pode indicar que a distribuição de docentes apenas com graduação pelas UFs não segue o mesmo padrão da distribuição de docentes pós-graduados ou das diferentes faixas etárias de forma tão intensa.

5.  **Correlações Ligeiramente Menores nas Faixas Etárias Extremas com Formação:**
    *   Para a faixa etária mais jovem (`Docentes_Idade_30_34`), as correlações com os níveis mais altos de formação (Mestrado e Doutorado) são um pouco menores (0.95 e 0.94, respectivamente) em comparação com faixas etárias intermediárias. Isso é esperado, pois leva tempo para obter esses títulos[1].
    *   Da mesma forma, para a faixa `Docentes_Idade_60_mais`, as correlações com os níveis de pós-graduação também são um pouco menores, embora ainda altas (ex: 0.96 com Doutorado, 0.89 com `Docentes_Idade_35_39`)[1].

**Contextualização para a Análise Exploratória de Dados:**

Esta matriz de correlação revela que, em nível estadual, a presença de docentes com alta qualificação (mestrado, doutorado) está fortemente associada à presença de docentes em diversas faixas etárias, especialmente as mais experientes. Indica também que estados com um forte contingente em um nível de pós-graduação tendem a ser fortes nos outros.

Para a pergunta de pesquisa sobre como formação e experiência (proxy pela idade) interagem para influenciar a disparidade salarial, esta análise mostra que, nos estados, há uma coocorrência significativa de alta formação e diversas faixas etárias. No entanto, a matriz não inclui dados salariais. Se dados salariais fossem adicionados, poderíamos investigar se UFs com alta correlação entre formação e idade (experiência) apresentam padrões específicos de disparidade salarial para "profissionais de dados". A ausência de uma forte correlação da variável `Docentes_Graduacao` com as demais sugere que este grupo pode ter características distintas que precisariam ser exploradas separadamente.


## Grafico Mapa Interativo de Bolhas - Distribuição de Docentes por Nível de Formação e UF
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/9d708a6e00717a471ed00ab3e3742a40/raw/c1f0d385f7c9ad6f156de6d78dfcc9d245c68c99/06_mapa_bolhas_interativo.html)
![06_mapa_bolhas](https://github.com/user-attachments/assets/8a39d31d-a20f-4e3a-a51a-010005ad43b1)
## Explicação do Gráfico: Mapa Interativo de Bolhas - Distribuição de Docentes por Nível de Formação e UF

O gráfico apresentado é um **mapa de bolhas interativo** que visualiza a distribuição do número de docentes em cada Unidade da Federação (UF) do Brasil, segmentado por nível de formação acadêmica[1]. Este tipo de gráfico utiliza círculos (bolhas) de tamanhos variados sobre um mapa para representar a magnitude de uma variável em diferentes regiões geográficas[7][4].

**Como interpretar o gráfico:**

*   **Base Geográfica:** O mapa do Brasil serve como plano de fundo, com as bolhas posicionadas sobre os respectivos estados[1].
*   **Bolhas:** Cada bolha no mapa representa um nível de formação específico dentro de um estado[1].
    *   **Cor da Bolha:** A cor da bolha indica o nível de formação acadêmica, conforme a legenda fornecida no gráfico[1]:
        *   **Azul:** Docentes com Doutorado
        *   **Verde:** Docentes com Mestrado
        *   **Laranja/Amarelo:** Docentes com Especialização
        *   **Vermelho:** Docentes com Graduação
    *   **Tamanho da Bolha:** O tamanho da bolha é diretamente proporcional ao **número de docentes** com aquele nível de formação específico naquela UF. Bolhas maiores indicam um número maior de docentes[1][4].
    *   **Interatividade:** Ao passar o cursor do mouse sobre uma bolha, uma caixa de informações (tooltip) aparece, exibindo detalhes como a sigla da UF, o nível de formação representado pela bolha e o número exato de docentes correspondente[1].

**Principais observações do gráfico:**

*   **Concentração Regional de Alta Qualificação:** Observa-se visualmente que estados como São Paulo (SP), Minas Gerais (MG), Rio de Janeiro (RJ), Paraná (PR) e Rio Grande do Sul (RS) tendem a apresentar bolhas azuis (Doutorado) e verdes (Mestrado) proeminentes, indicando uma concentração significativa de docentes com alta qualificação nessas regiões[1].
*   **Predominância de Doutorado e Mestrado:** Em muitos estados, as bolhas azuis (Doutorado) e verdes (Mestrado) são as de maior tamanho, reforçando a constatação de gráficos anteriores sobre a alta qualificação (pós-graduação *stricto sensu*) do corpo docente na maioria das UFs[1].
*   **Variações Estaduais:** O mapa permite uma rápida comparação entre os estados. Alguns estados, especialmente nas regiões Norte e Nordeste, podem apresentar um volume total de docentes menor (bolhas geralmente menores) ou uma distribuição proporcional diferente entre os níveis de formação quando comparados aos estados do Sul e Sudeste[1].
*   **Baixa Representatividade da Graduação:** As bolhas vermelhas (Graduação), que representam docentes com apenas graduação, são consistentemente as menores em todos os estados, muitas vezes quase imperceptíveis, confirmando o baixo número de docentes que não possuem pós-graduação[1].

**Contextualização para a Análise Exploratória de Dados:**

Este mapa de bolhas interativo oferece uma dimensão geográfica à análise da formação acadêmica dos docentes[1][7]. Ele permite identificar visualmente "hotspots" ou áreas de maior concentração de docentes por nível de formação[7].

No contexto da pergunta de pesquisa sobre "como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil", este gráfico contribui ao:
*   Mapear a distribuição da **formação acadêmica** dos docentes (o grupo disponível no dataset) pelo território nacional[1].
*   Permitir a identificação de estados com maior ou menor concentração de docentes altamente qualificados[1].

Para avançar na resposta à pergunta de pesquisa, seria necessário cruzar essas informações geográficas de formação com dados de experiência profissional (que poderiam ser agregados por UF) e, fundamentalmente, com dados salariais específicos para "profissionais de dados" em cada estado. O mapa atual é uma ferramenta exploratória valiosa para entender a distribuição da qualificação docente, mas não contém, por si só, informações sobre salários ou experiência para analisar diretamente a disparidade salarial de profissionais de dados[1][6].


## Grafico Gráfico de Dispersão 3D Interativo - Mestrado, Doutorado e Média de Idade dos Docentes por UF
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/5edbfdc4c69d324455e65eef06c591b6/raw/d304db3742f4839c7bf4360c2ed75a06bce75bbe/07_3d_interativo.html)
![07_3d_interativo](https://github.com/user-attachments/assets/7b396546-3b72-4dc2-9897-0f6af9600cc7)
## Explicação do Gráfico: Gráfico de Dispersão 3D Interativo - Mestrado, Doutorado e Média de Idade dos Docentes por UF

O gráfico apresentado é um **gráfico de dispersão 3D interativo**[1][2][8]. Ele visualiza a relação entre três variáveis para cada Unidade da Federação (UF) do Brasil: o número de docentes com mestrado, o número de docentes com doutorado e a média de idade dos docentes.

**Como interpretar o gráfico:**

*   **Eixos:** O gráfico possui três eixos, cada um representando uma variável quantitativa[1][2][8]:
    *   **Eixo X (horizontal, profundidade):** `Docentes_Mestrado` - Número de docentes com título de Mestre na UF.
    *   **Eixo Y (horizontal, largura):** `Docentes_Doutorado` - Número de docentes com título de Doutor na UF.
    *   **Eixo Z (vertical, altura):** `Media_Idade_Docentes` - Média de idade dos docentes na UF.
*   **Pontos:** Cada ponto (esfera) no espaço 3D representa uma Unidade da Federação (UF)[1][2]. A posição do ponto é determinada pelos valores das três variáveis para aquela UF.
*   **Cores dos Pontos:** No gráfico visualizado, os pontos parecem ter uma cor azulada uniforme. A legenda ou interatividade poderiam revelar se a cor representa alguma outra variável, mas com base na imagem estática, ela parece ser apenas para visualização dos pontos.
*   **Interatividade:** Por ser um gráfico interativo (geralmente criado com bibliotecas como Plotly)[1][2][7][8]:
    *   **Rotação:** É possível girar o gráfico para visualizar a dispersão dos pontos de diferentes ângulos, ajudando a perceber padrões e relações espaciais[7].
    *   **Zoom:** Pode-se aproximar ou afastar para focar em regiões específicas do gráfico.
    *   **Hover (Passar o mouse):** Ao passar o cursor sobre um ponto, informações adicionais sobre aquela UF (como o nome da UF e os valores exatos das três variáveis) são tipicamente exibidas.

**Principais observações (baseadas na estrutura visual):**

*   **Relação entre Mestrado e Doutorado:** Observa-se uma tendência geral de que UFs com um alto número de docentes com mestrado (valores mais altos no eixo X) também tendem a ter um alto número de docentes com doutorado (valores mais altos no eixo Y). Isso é indicado pela dispersão dos pontos que tende a se estender diagonalmente no plano XY[1][2].
*   **Variação na Média de Idade:** Os pontos se distribuem em diferentes alturas ao longo do eixo Z, indicando variação na média de idade dos docentes entre as UFs[1][2].
*   **Identificação de Clusters e Outliers:**
    *   Pode haver agrupamentos (clusters) de UFs com características semelhantes (por exemplo, UFs com muitos mestres, muitos doutores e alta média de idade).
    *   Alguns pontos podem estar mais isolados (outliers), representando UFs com combinações menos comuns dessas três variáveis. Por exemplo, um ponto no canto superior direito do plano XY e alto no eixo Z representaria uma UF com muitos mestres, muitos doutores e uma alta média de idade dos docentes.
*   **Concentração de UFs:** A maioria dos pontos parece se concentrar em uma região onde os números de docentes com mestrado e doutorado não são os máximos observados, e a média de idade varia. Estados com grandes contingentes de docentes (como São Paulo, visualizado em gráficos anteriores) provavelmente se destacariam nas extremidades superiores dos eixos X e Y[1][2].

**Contextualização para a Análise Exploratória de Dados:**

Este gráfico 3D permite uma análise simultânea da **formação acadêmica** (níveis de mestrado e doutorado) e de um proxy para a **experiência profissional** (média de idade dos docentes) em nível estadual[8].

Para a pergunta de pesquisa ("Como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?"):
*   Este gráfico visualiza diretamente a coocorrência de altos níveis de formação (mestrado e doutorado) e diferentes médias de idade (experiência) nas UFs.
*   Ele ajuda a identificar se UFs com um perfil específico de formação e idade (ex: alta formação e alta média de idade) se agrupam.

Contudo, assim como os gráficos anteriores, este não inclui dados salariais. Para analisar a disparidade salarial, seria necessário integrar informações de remuneração a essa análise tridimensional, possivelmente usando a cor ou o tamanho dos pontos para representar uma variável salarial, ou realizando análises estatísticas subsequentes com dados mais completos. Este gráfico é uma ferramenta exploratória poderosa para entender a inter-relação das variáveis de formação e idade dos docentes entre os estados[7][8].


---

## Analise exploratoria de dados bases integradas

---

## Grafico 1
![bar_line_salario_medio_total_docentes_uf](https://github.com/user-attachments/assets/6060f457-2f9f-4c68-9839-82f9f4ac9312)

## Grafico 2
![boxplot_salario_por_area_formacao_top5](https://github.com/user-attachments/assets/521f1e12-e4bb-445e-982d-733d52142401)

## Grafico 3

## Grafico 4
![boxplot_salario_por_experiencia_seaborn](https://github.com/user-attachments/assets/1ae56e9f-614e-490c-9cea-c70402bd333c)

## Grafico 5

## Grafico 6
![boxplot_salario_por_nivel_ensino_seaborn](https://github.com/user-attachments/assets/320b22fc-43fb-40af-be93-e02572699fec)

## Grafico 7
![catplot_salario_exp_facet_nivel_ensino](https://github.com/user-attachments/assets/71164ccd-585b-4354-8473-631eac8a4f02)

## Grafico 8
![distribuicao_area_formacao](https://github.com/user-attachments/assets/fd0d4cb9-5e30-4f52-8a7e-9cd074ee04c5)

## Grafico 9
![distribuicao_faixa_salarial](https://github.com/user-attachments/assets/29688dff-55fd-492f-a897-ad9a4e89a657)

## Grafico 10
![distribuicao_nivel_ensino](https://github.com/user-attachments/assets/044e5446-b6bd-474d-86d4-3c8a94ca44c7)

## Grafico 11
![distribuicao_salario_estimado](https://github.com/user-attachments/assets/cb8d3675-ed41-4fcb-bf09-7f1c8b69cda4)

## Grafico 12
![distribuicao_tempo_experiencia](https://github.com/user-attachments/assets/986f2138-2838-4ff8-ae15-8495f36f0728)

## Grafico 13
![distribuicao_top10_uf](https://github.com/user-attachments/assets/1cf90782-fb39-475d-b70e-ac4b18bb3f7d)

## Grafico 14
![heatmap_correlacao_salario_exp_ensino](https://github.com/user-attachments/assets/2cd9887a-0a1d-4c89-b513-3a852d07b35c)

## Grafico 15
![lineplot_salario_exp_por_nivel_ensino](https://github.com/user-attachments/assets/8e847b68-732a-4df6-ac5f-3abde32e4245)

## Grafico 16

## Grafico 17
![scatterplot_salario_vs_prop_doc_doutorado_uf](https://github.com/user-attachments/assets/004cf9f3-3691-4536-aa8a-ae2a9ec938e9)


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

----------------------------------------------------------------------------------------------------------------------------------------------

## Indução de modelos

### Modelo 1 gbm (gradient boosting machines) modelo baseado em árvore de decisão
### 1º Pergunta orientada a dados
### *Justificativa*
- GBMs constroem árvores de decisão sequencialmente, onde cada nova árvore corrige os erros da anterior. Essa estrutura permite capturar interações complexas e não lineares entre as variáveis preditoras de forma natural, o que é central para responder à pergunta do projeto. Por exemplo, o modelo pode aprender que o impacto de saber Python no salário é diferente para um profissional Júnior com Graduação versus um Sênior com Doutorado.
- Algoritmos como LightGBM e CatBoost possuem mecanismos eficientes e nativos para lidar com variáveis categóricas (P1l, P1m, P2g, P4e, etc.) sem a necessidade de one-hot encoding extensivo, o que simplifica o pré-processamento e evita o problema da alta dimensionalidade, comum em datasets com muitas categorias.
- Embora mais complexos que modelos lineares, GBMs oferecem ferramentas robustas para interpretação:

	Feature Importance: Indica quais fatores (formação, anos de experiência, habilidades específicas como SQL P4d1 ou Python P4d3) têm maior impacto geral nas previsões salariais.

SHAP (SHapley Additive exPlanations): Permite entender a contribuição de cada fator para cada previsão individual e visualizar como as interações influenciam o resultado. Isso ajuda a detalhar como os fatores interagem.

- GBMs podem ser configurados tanto para tarefas de regressão (prevendo o ponto médio do salário) quanto para classificação (prevendo a faixa salarial), adaptando-se à forma como a variável alvo for tratada.

### *Processo de Amostragem de Dados (Particionamento e Cross-Validation)*

- No desenvolvimento do modelo LightGBM para previsão salarial, o processo de amostragem de dados foi realizado em duas etapas principais: particionamento (train/test split) e, opcionalmente, validação cruzada (cross-validation).

	- *Particionamento dos Dados (Train/Test Split)*
		Objetivo: Garantir que o modelo seja treinado em uma parte dos dados e testado em outra, permitindo avaliar sua capacidade de generalização para dados nunca vistos.

		Procedimento Utilizado:

		O dataset completo foi dividido em duas partes:

		Treinamento: 75% dos dados (3.559 registros).

		Teste: 25% dos dados (1.187 registros).

		O particionamento foi realizado com a função train_test_split do Scikit-Learn, utilizando um valor fixo de random_state para garantir reprodutibilidade.

		Exemplo de código:

			from sklearn.model_selection import train_test_split
			X_train, X_test, y_train, y_test = train_test_split(
			    X, y, test_size=0.25, random_state=42
			)
		Justificativa:

		O particionamento 75/25 é padrão em problemas de regressão e garante que o modelo não seja avaliado nos mesmos dados em que foi treinado, prevenindo overfitting e permitindo uma estimativa realista de desempenho.

	- *Validação Durante o Treinamento (Early Stopping)*
		Objetivo: Evitar overfitting durante o treinamento do LightGBM, monitorando o desempenho em dados de validação.

		Procedimento:

		O conjunto de teste foi também utilizado como conjunto de validação durante o ajuste do modelo.

		O parâmetro early_stopping_rounds=50 foi usado para interromper o treinamento caso o erro não melhorasse por 50 iterações consecutivas.

		Exemplo de código:

			lgbm.fit(
			    X_train, y_train,
			    eval_set=[(X_test, y_test)],
			    eval_metric='mae',
			    callbacks=[lgb.early_stopping(stopping_rounds=50, verbose=1)]
			)
Resultado:

O modelo parou na iteração 291, quando atingiu o menor erro MAE no conjunto de validação.

### *Parâmetros do Modelo e Processo de Raciocínio (Árvore Individual LightGBM)*
- O modelo apresentado na imagem é um LightGBM Regressor treinado para prever o salário de profissionais de dados. Os principais parâmetros e configurações utilizados foram:

  - **Objetivo:** Regressão (regression_l1), minimizando o erro absoluto médio (MAE)

  - **Particionamento dos dados:** 75% treino, 25% teste (train_test_split)

  - **Early Stopping:** Parada automática após 50 iterações sem melhora no MAE do conjunto de validação

  - **Número de árvores (estimators):** O treinamento parou na árvore de índice 291 (early stopping)

  - **Features categóricas:** Informadas explicitamente para o LightGBM (P1mreadeFormao, P4eEntreaslinguagenslistadasabaixoqualaquevocmaisutilizanotrabalho)

  - **Features numéricas:** Incluem variáveis ordinais (nível de ensino, experiência, senioridade) e binárias (uso de linguagens)

  - **Random State:** 42 (para reprodutibilidade)

- **Processo de Raciocínio da Árvore (Regras de Decisão)**
  - A árvore individual exibida representa uma das centenas que compõem o ensemble do LightGBM. Cada árvore é composta por nós de decisão (splits) e folhas (previsões). O processo de raciocínio segue o fluxo:

  - **Exemplo de Caminho de Decisão**
	  - Raiz:
		P2iQuantotempodeexperincianareadedadosvoctem <= 1.5

		Se o tempo de experiência na área de dados é até 1-2 anos (valor ordinal), segue à esquerda; caso contrário, à direita.

	  - Segundo Split (esquerda):

		P1lNiveldeEnsino <= 1.5

		Se o nível de ensino é até graduação, segue à esquerda; senão, à direita.

	  - Terceiro Split (direita da raiz):

		P4eEntreaslinguagenslistadasabaixoqualaquevocmaisutilizanotrabalho == "Python"

		Se a linguagem mais usada é Python, segue à esquerda; senão, à direita.

	 - Splits subsequentes:

		A árvore pode dividir ainda por senioridade (P2gNivel), uso de linguagens específicas (P4d3Python, P4d1SQL), área de formação, etc.

	- Folhas:

	 - Cada folha (elipse) mostra o valor previsto de salário para aquele grupo de profissionais, por exemplo:

	 - leaf 0: 9350.500 (previsão: R$ 9.350,50)

	 - leaf 13: 13500.000 (previsão: R$ 13.500,00)


- **Exemplo de Regra Completa**
		- Se o profissional tem experiência ≤ 1.5 e nível de ensino ≤ 1.5, então o salário previsto é R$ 9.350,50.
		- Se experiência > 1.5 e linguagem mais usada é Python e senioridade ≤ 1.5, então o salário previsto é R$ 13.500,00.


- **Feature Importances e Tomada de Decisão**
		- O modelo LightGBM atribui maior importância às features que aparecem nos primeiros splits das árvores, pois elas segmentam grandes grupos de dados. No contexto deste projeto, as principais variáveis de decisão (segundo a feature importance e os splits das árvores) foram:

	- Tempo de experiência na área de dados (P2iQuantotempodeexperincianareadedadosvoctem)
		
	- Nível de ensino (P1lNiveldeEnsino)
		
	- Senioridade (P2gNivel)
		
	- Linguagem mais usada no trabalho (P4eEntreaslinguagenslistadasabaixoqualaquevocmaisutilizanotrabalho)
		
	- Uso de Python (P4d3Python)
		
	- Área de formação acadêmica (P1mreadeFormao)
		
	- Estas variáveis são utilizadas repetidamente para dividir os dados em grupos mais homogêneos, refletindo o raciocínio do modelo para prever salários.

- **Medidas de Importância das Features**
		- Importância por ganho (gain): Mede o quanto cada feature contribuiu para a redução do erro em todas as árvores do modelo.

- No modelo treinado, experiência, senioridade e uso de Python aparecem entre as mais importantes, alinhando-se com os splits iniciais das árvores individuais.

- **Resumo Visual do Processo**
	- Cada caminho da raiz até uma folha representa uma regra de decisão baseada em múltiplas variáveis.

	- Os splits mais próximos da raiz indicam as variáveis mais relevantes para a previsão salarial.

	- O modelo utiliza essas regras para segmentar os profissionais em grupos e prever o salário médio de cada grupo.
 
 ### *Explicação do Código: Notebook de Modelo GBM com Árvore e Interpretação*

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

---


### Modelo 2: Algoritmo

Repita os passos anteriores para o segundo modelo.


---


## Resultados

### Resultados obtidos com o modelo 1.
![grafico_1](https://github.com/user-attachments/assets/32900aa7-400c-438b-99f4-16fc90d90bb3)

Este gráfico de barras horizontais exibe a **importância relativa de cada feature (variável)** utilizada pelo modelo LightGBM para prever o ponto médio da faixa salarial. A importância é medida pelo critério de **"Gain" (Ganho)**.

-   **Eixo Y (Features):** Lista as variáveis de entrada do modelo, ordenadas da mais importante (topo) para a menos importante (base). Os nomes correspondem aos códigos das perguntas na pesquisa ou aos nomes gerados após a limpeza (ex: `P2_i_...` representa o tempo de experiência).
-   **Eixo X (Feature importance):** Mostra o valor numérico do "Gain" total acumulado por cada feature.
-   **Barras:** O comprimento de cada barra é proporcional ao valor do "Gain" da feature correspondente. Barras mais longas indicam maior importância.
-   **Métrica "Gain":** Representa a contribuição total de cada feature para a redução do erro (ou impureza) do modelo em todas as árvores e em todos os splits onde essa feature foi utilizada. Features que resultam em divisões que separam melhor os dados em grupos com salários mais homogêneos terão um "Gain" maior.

## Como Interpretar os Resultados?

O gráfico classifica as features com base em quão úteis elas foram *durante o treinamento* do modelo LightGBM para fazer previsões precisas.

### Principais Achados (Features Mais Importantes):

1.  **`P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem` (Gain ≈ 8391):** De longe, a feature **mais importante**. Isso indica que o tempo de experiência na área de dados é o fator que mais contribuiu para a capacidade do modelo de prever salários. As divisões baseadas na experiência foram as que mais ajudaram a reduzir o erro de previsão.
2.  **`P2_g_Nivel` (Gain ≈ 6540):** A **segunda feature mais importante**. Representa o nível de senioridade (Júnior, Pleno, Sênior). Confirma que a senioridade formal é um fator crucial e altamente preditivo para o salário.
3.  **`P4_e_Entre_as_linguagens_listadas_abaixo_qual_é_a_que_você_mais_utiliza_no_trabalho` (Gain ≈ 2204):** A linguagem de programação *principal* utilizada no trabalho é o terceiro fator mais relevante. Isso sugere que a especialização ou o foco em uma determinada linguagem principal tem um impacto considerável no salário.
4.  **`P1_l_Nivel_de_Ensino` (Gain ≈ 1865):** O nível de educação formal (Graduação, Mestrado, Doutorado) aparece como o quarto fator mais importante, mostrando que a formação acadêmica ainda tem um peso significativo.
5.  **`P4_d_3_Python` (Gain ≈ 709):** O uso específico de Python é a quinta feature mais importante. Embora a linguagem *principal* (`P4_e_...`) seja mais relevante, saber Python especificamente também contribui significativamente para o modelo.

### Outras Features Relevantes (Impacto Moderado):

-   **`P1_m_Área_de_Formação` (Gain ≈ 626):** A área de estudo original (ex: Computação, Economia) tem um impacto moderado.
-   **`P4_d_1_SQL` (Gain ≈ 591):** O conhecimento de SQL também é relevante.
-   **`P4_d_9_Visual_BasicVBA` (Gain ≈ 355):** Surpreendentemente, VBA aparece com alguma relevância, talvez indicando nichos específicos de mercado ou tarefas de automação valorizadas.
-   **`P4_d_10_Scala` (Gain ≈ 172)** e **`P4_d_2_R` (Gain ≈ 124):** Linguagens comuns em dados, mas com impacto menor que Python ou SQL neste modelo.

### Features Menos Importantes:

-   Linguagens como **Java (`P4_d_6`), JavaScript (`P4_d_14`), SAS/Stata (`P4_d_8`), C/C++/C# (`P4_d_4`)** aparecem com importância relativamente baixa.
-   Linguagens como **PHP (`P4_d_13`), .NET (`P4_d_5`)** e **Matlab (`P4_d_11`)** tiveram um impacto **muito baixo** (Gain < 10) na performance geral do modelo durante o treinamento, sugerindo que são pouco preditivas para a faixa salarial geral neste dataset.

![grafico_2](https://github.com/user-attachments/assets/7da5b306-03cf-4257-9e4b-4a1c96960c36)

Este gráfico visualiza **uma única árvore de decisão** (especificamente, a de índice 0) que faz parte do *ensemble* (conjunto de árvores) do modelo LightGBM treinado. O LightGBM combina as previsões de muitas dessas árvores para chegar ao resultado final. Visualizar uma árvore individual nos ajuda a entender a **lógica de decisão hierárquica** que o modelo aprendeu a partir dos dados para prever o `salary_midpoint`.

## Como Interpretar os Elementos do Gráfico?

1.  **Nós Retangulares (Nós de Decisão ou Splits):**
    *   Cada retângulo representa um ponto onde a árvore toma uma decisão baseada em uma **feature** (variável).
    *   **Linha Superior:** Mostra a **feature** e a **condição de divisão**. Exemplo: `P2_i_Quanto_tempo_de_experiência... <= 1.500`. Isso significa "A feature 'Tempo de Experiência' (codificada numericamente) é menor ou igual a 1.5?".
        *   _Nota:_ Valores como `1.500` referem-se aos valores numéricos *após* o `OrdinalEncoder`. É preciso consultar o mapeamento para saber qual categoria original corresponde (ex: 0='Menos de 1 ano', 1='de 1 a 2 anos', portanto 1.5 fica entre essas categorias).
    *   **`gain`:** Indica o quanto essa divisão contribuiu para melhorar a métrica do modelo (neste caso, reduzir o erro MAE). Splits com maior `gain` são considerados mais importantes *por esta árvore*.
    *   **`value`:** O valor de saída (previsão de salário) que seria dado *neste ponto* se a árvore parasse aqui. Em nós internos, representa a média dos valores dos dados que chegam até ele.
    *   **`count`:** O número de amostras (profissionais) do conjunto de *treinamento* que chegaram a este nó.

2.  **Setas/Ramos:**
    *   Conectam os nós e indicam o caminho a seguir com base na condição do nó pai.
    *   **Convenção Comum (LightGBM/Sklearn):**
        *   O ramo da **esquerda** é geralmente seguido se a condição for **verdadeira** (`feature <= valor`). A seta pode ter um "yes" implícito ou uma condição repetida.
        *   O ramo da **direita** é geralmente seguido se a condição for **falsa** (`feature > valor`). A seta pode ter um "no" implícito.

3.  **Nós Ovais/Elípticos (Folhas ou Nós Terminais):**
    *   Representam o **fim de um caminho** na árvore. Não há mais divisões a partir daqui.
    *   **`leaf X`:** Identificador único da folha (ex: `leaf 0`, `leaf 13`).
    *   **`value`:** O **valor final previsto** pela *esta árvore específica* para todas as amostras que chegam a esta folha. Ex: `leaf 0: 9350.500` significa que a previsão desta árvore para quem cai na folha 0 é de R$ 9.350,50.
    *   **`count`:** O número de amostras do conjunto de *treinamento* que terminaram nesta folha.

## Análise Detalhada dos Splits Visíveis na Imagem:

*(Analisando a estrutura geral, focando nos nós superiores)*

1.  **Split Raiz (Nó superior):**
    *   **Feature:** `P2_i_Quanto_tempo_de_experiência...`
    *   **Condição:** `<= 1.500`
    *   **Gain:** `831.237` (alto, indicando grande importância inicial)
    *   **Value:** `10000.500` (Salário médio de todos no treino)
    *   **Count:** `3559` (Todas as amostras do treino começam aqui)
    *   **Interpretação:** A primeira e mais importante decisão desta árvore é separar os profissionais com *pouca experiência* (<= 1.5, ex: até 1-2 anos) dos profissionais com *mais experiência* (> 1.5).

2.  **Split (Ramo Esquerdo - Pouca Experiência):**
    *   **Feature:** `P1_l_Nivel_de_Ensino`
    *   **Condição:** `<= 1.500`
    *   **Gain:** `12.964`
    *   **Interpretação:** Para quem tem pouca experiência, a próxima decisão importante é separar por *nível de ensino* (baixo <= 1.5 vs. alto > 1.5).

3.  **Split (Ramo Direito - Mais Experiência):**
    *   **Feature:** `P4_e_Entre_as_linguagens...` (Linguagem Principal)
    *   **Condição:** Provavelmente uma comparação com uma linguagem específica (ex: `== "Python"`, embora o valor exato esteja cortado na imagem).
    *   **Gain:** `80.142`
    *   **Interpretação:** Para quem tem mais experiência, a *linguagem principal utilizada* se torna um fator decisivo importante.

4.  **Splits Subsequentes:** A árvore continua a dividir os dados usando outras features como `P2_g_Nivel` (Senioridade), `P4_d_3_Python`, `P4_d_1_SQL`, `P4_d_9_Visual_BasicVBA`, refinando os grupos com base em combinações dessas características até chegar às folhas com as previsões finais.

## Exemplo de Caminho Completo (Visual):

*Siga as setas a partir da raiz:*

1.  **Experiência > 1.5?** Sim -> Seguir ramo **direito**.
2.  **Linguagem Principal == "Python"?** (Suposição) Sim -> Seguir ramo **esquerdo** do nó `P4_e...`.
3.  **`P2_g_Nivel <= 1.5?`** Sim (Ex: Pleno ou Júnior) -> Seguir ramo **esquerdo** do nó `P2_g_Nivel`.
4.  ... continuar seguindo as condições até chegar a uma **folha** (ex: `leaf 13: 13500.000`).

*Interpretação dessa regra:* "Um profissional com mais de 1-2 anos de experiência, cuja linguagem principal é Python e cujo nível é Pleno ou Júnior, tem um salário previsto por esta árvore de R$ 13.500,00."

## O Que Esta Árvore Individual Revela?

-   **Hierarquia de Decisão:** Mostra quais features são consideradas mais importantes nos estágios iniciais da segmentação (experiência, seguida por educação ou linguagem principal).
-   **Regras Explícitas (Parciais):** Cada caminho da raiz a uma folha representa uma regra de decisão explícita baseada nas features.
-   **Como o Modelo Combina Fatores:** Ilustra visualmente como o modelo usa condições sequenciais para chegar a uma previsão.

## Limitações Importantes:

-   **Representação Parcial:** Esta é **apenas 1 árvore** de um total de 291 árvores treinadas pelo LightGBM. A previsão final do modelo é uma **combinação (ensemble)** das previsões de todas as árvores, não apenas desta.
-   **Complexidade do Ensemble:** O comportamento completo do modelo LightGBM é mais complexo e robusto do que o de uma única árvore.
-   **Valores Codificados:** As condições usam valores numéricos que resultaram do encoding (especialmente para variáveis ordinais). É necessário referenciar o mapeamento do encoder para entender o significado exato de limiares como `1.500`.

![grafico_3](https://github.com/user-attachments/assets/afa8c32a-4650-4e52-b9bc-d8805b2e2f44)

## O que o Gráfico Mostra?

Este gráfico, conhecido como **SHAP Summary Plot** do tipo "dot" (pontos), é uma ferramenta poderosa para visualizar o impacto das diferentes **features** (variáveis de entrada, como experiência, nível de ensino, etc.) nas previsões individuais do modelo LightGBM para o ponto médio da faixa salarial. Ele resume duas informações cruciais para cada feature em relação a cada profissional no conjunto de teste:

1.  **Magnitude do Impacto:** Quão fortemente aquela feature influenciou a previsão de salário.
2.  **Direção do Impacto:** Se a feature aumentou ou diminuiu a previsão de salário.

## Como Interpretar os Elementos do Gráfico?

-   **Eixo Y (Vertical): Features**
    -   Lista as variáveis de entrada do modelo, **ordenadas pela sua importância média global** (calculada como a média do valor absoluto do SHAP para aquela feature). As features no topo são as que tiveram, em média, o maior impacto nas previsões.
    -   Exemplo: `P2_i_Quanto_tempo_de_experiência...` está no topo, indicando ser a mais influente.

-   **Eixo X (Horizontal): Valor SHAP (Impacto no Resultado do Modelo)**
    -   Mostra o valor SHAP calculado para uma feature específica em uma previsão específica.
    -   **Valores Positivos (> 0):** Indicam que o valor daquela feature para aquele profissional *aumentou* a previsão de salário em relação à média base do modelo.
    -   **Valores Negativos (< 0):** Indicam que o valor daquela feature *diminuiu* a previsão de salário.
    -   **Valor Zero (0.0):** Indica que a feature não teve impacto naquela previsão específica. A linha vertical central marca este ponto de impacto zero.

-   **Pontos Coloridos:**
    -   Cada ponto no gráfico representa **um profissional** no conjunto de teste.
    -   A **posição horizontal** do ponto mostra o valor SHAP (impacto) da feature correspondente (no eixo Y) para *aquele* profissional.
    *   A **cor** do ponto representa o **valor original da feature** para aquele profissional, conforme a barra de cores à direita:
        -   **Vermelho (High):** Indica um valor *alto* da feature (ex: muitos anos de experiência, nível de ensino alto como Doutorado, usa Python=1).
        -   **Azul (Low):** Indica um valor *baixo* da feature (ex: pouca experiência, nível de ensino baixo como Graduação, não usa Python=0).
        -   **Cores Intermediárias (Roxo/Cinza):** Indicam valores medianos ou categorias intermediárias/não mapeadas pela cor padrão.

## Análise Detalhada dos Achados Visuais no Gráfico:

1.  **`P2_i_Quanto_tempo_de_experiência...` (Experiência):**
    -   **Padrão:** Claramente a feature mais importante (topo da lista). Há uma forte separação horizontal baseada na cor: pontos vermelhos (muita experiência) estão concentrados à direita, com altos valores SHAP positivos (até +6000). Pontos azuis (pouca experiência) estão concentrados à esquerda, com valores SHAP negativos (até -4000).
    -   **Conclusão:** A experiência tem um impacto **muito forte e consistentemente positivo** no salário previsto. Quanto maior a experiência, maior o aumento na previsão salarial.

2.  **`P2_g_Nivel` (Senioridade):**
    -   **Padrão:** Segunda mais importante. O padrão é similar à experiência: pontos vermelhos (presumivelmente Sênior) estão à direita (SHAP positivo, ~+3000 a +5000), pontos azuis (Júnior) estão à esquerda (SHAP negativo, ~-2000 a -4000). Pontos roxos (Pleno) ficam mais ao centro.
    -   **Conclusão:** A senioridade tem um impacto **forte e positivo**. Ser Sênior aumenta significativamente a previsão, enquanto ser Júnior a diminui.

3.  **`P4_e_Entre_as_linguagens...` (Linguagem Principal):**
    -   **Padrão:** Terceira mais importante. Os pontos aparecem majoritariamente em cinza, indicando que é uma feature categórica com muitas opções ou que a codificação de cor padrão não foi aplicada. No entanto, a **dispersão horizontal** dos pontos é significativa (de ~-2000 a ~+2000), mostrando que a escolha da linguagem principal influencia consideravelmente o salário previsto.
    -   **Conclusão:** A principal linguagem utilizada é um fator **importante**, mas o gráfico não permite identificar *quais* linguagens específicas têm impacto positivo ou negativo sem informação adicional sobre a codificação de cor/valor.

4.  **`P1_l_Nivel_de_Ensino` (Educação):**
    -   **Padrão:** Quarta mais importante. Há uma tendência visível, embora menos forte que experiência/senioridade: pontos vermelhos/roxos (níveis mais altos) tendem a ter valores SHAP mais altos (mais à direita, ~+1000 a +2000) do que os pontos azuis (níveis mais baixos, SHAP negativo ou próximo de zero).
    -   **Conclusão:** Níveis mais altos de educação formal têm um impacto **geralmente positivo**, mas menos intenso que experiência ou senioridade.

5.  **`P1_m_Área_de_Formação`:**
    -   **Padrão:** Quinta mais importante. Similar à Linguagem Principal, os pontos são cinzas, mas a dispersão horizontal (de ~-1000 a ~+1000) indica que a área de formação tem um impacto moderado no salário previsto.
    -   **Conclusão:** A área de formação influencia o salário, mas com menor intensidade e sem clareza sobre quais áreas são mais vantajosas a partir deste gráfico isolado.

6.  **`P4_d_3_Python` (Uso de Python):**
    -   **Padrão:** Sexta mais importante. Apresenta duas faixas de cor bem definidas. Os pontos vermelhos (Usa Python = 1) estão claramente deslocados para a direita (valores SHAP positivos, ~+500 a +1500) em comparação com os pontos azuis (Não usa Python = 0, SHAP próximo de zero ou ligeiramente negativo).
    -   **Conclusão:** Saber/usar Python tem um impacto **consistentemente positivo** no salário previsto pelo modelo.

7.  **`P4_d_1_SQL` (Uso de SQL):**
    -   **Padrão:** Sétima mais importante. Similar ao Python, mas com um impacto positivo talvez um pouco menor e mais concentrado perto de zero. Pontos vermelhos (Usa SQL = 1) tendem a ter SHAP ligeiramente positivo, enquanto azuis (Não usa = 0) estão mais à esquerda ou em zero.
    -   **Conclusão:** Saber/usar SQL tem um impacto **geralmente positivo**, mas menos pronunciado que Python neste modelo.

8.  **Outras Features (Scala, VBA, Java, JS, R, SAS, etc.):**
    -   Aparecem mais abaixo na lista, indicando **menor importância média global**.
    -   A dispersão horizontal dos pontos é bem menor, concentrada próxima do eixo zero (SHAP value ≈ 0).
    -   Isso significa que, *em média*, essas habilidades tiveram um impacto pequeno ou inconsistente nas previsões salariais feitas por este modelo específico, embora possam ter impacto em casos individuais (pontos isolados mais à direita ou esquerda).

![grafico_4](https://github.com/user-attachments/assets/9d1cc74d-4905-40ed-8d16-2da041d64a81)

## O que o Gráfico Mostra?

Este gráfico é o **SHAP Summary Plot** do tipo "bar" (barras). Sua função principal é **ranquear as features (variáveis)** de acordo com a **magnitude média do seu impacto** nas previsões do modelo LightGBM. Diferente do gráfico de pontos (dot plot), este gráfico foca apenas na **importância geral** de cada feature, sem mostrar a direção (positiva ou negativa) ou a distribuição dos impactos individuais.

## Como Interpretar os Elementos do Gráfico?

-   **Eixo Y (Vertical): Features**
    -   Lista as variáveis de entrada do modelo, **ordenadas pela sua importância média global**, da mais importante (topo) para a menos importante (base).
    -   Exemplo: `P2_i_Quanto_tempo_de_experiência...` está no topo, confirmando ser a mais impactante em média.

-   **Eixo X (Horizontal): `mean(|SHAP value|) (average impact on model output magnitude)`**
    -   Mostra o **valor médio absoluto do SHAP** para cada feature. Isso representa, em média, o quanto o valor daquela feature (seja ele alto ou baixo) desloca a previsão do modelo da média base, independentemente da direção.
    -   Valores maiores no eixo X indicam que a feature, em média, tem um impacto maior (seja positivo ou negativo) nas previsões salariais.

-   **Barras Azuis:**
    -   O **comprimento de cada barra** é diretamente proporcional ao valor médio absoluto do SHAP para a feature correspondente.
    -   **Barras mais longas indicam maior importância média global** da feature para o modelo.

## Análise Detalhada do Ranking de Importância:

O gráfico confirma a ordem de importância observada no SHAP Summary Plot (dot), destacando quantitativamente a magnitude média do impacto:

1.  **`P2_i_Quanto_tempo_de_experiência...` (Experiência):** **A feature mais importante**, com a barra mais longa, indicando que, em média, a experiência tem o maior impacto absoluto nas previsões salariais. `mean(|SHAP value|)` ≈ 2000.
2.  **`P2_g_Nivel` (Senioridade):** A **segunda feature mais importante**, com um impacto médio absoluto significativo, mas menor que a experiência. `mean(|SHAP value|)` ≈ 1600.
3.  **`P4_e_Entre_as_linguagens...` (Linguagem Principal):** A **terceira mais importante**, mostrando que a escolha da linguagem principal tem um impacto médio considerável. `mean(|SHAP value|)` ≈ 1300.
4.  **`P1_l_Nivel_de_Ensino` (Educação):** **Quarta mais importante**, com impacto médio relevante. `mean(|SHAP value|)` ≈ 550.
5.  **`P1_m_Área_de_Formação`:** **Quinta mais importante**, com impacto médio um pouco menor que o nível de ensino. `mean(|SHAP value|)` ≈ 400.
6.  **`P4_d_3_Python` (Uso de Python):** **Sexta mais importante**, confirmando seu papel relevante, embora com menor magnitude média que as anteriores. `mean(|SHAP value|)` ≈ 300.
7.  **`P4_d_1_SQL` (Uso de SQL):** **Sétima mais importante**, com impacto médio ligeiramente menor que Python. `mean(|SHAP value|)` ≈ 250.
8.  **`P4_d_10_Scala`, `P4_d_9_Visual_BasicVBA`, `P4_d_6_Java`, `P4_d_14_JavaScript`, `P4_d_2_R`, `P4_d_8_SASStata`, etc.:** As demais features aparecem em seguida, com barras progressivamente menores, indicando um **impacto médio absoluto decrescente** nas previsões do modelo. Features na base do gráfico tiveram pouca influência média geral.

![grafico_5](https://github.com/user-attachments/assets/9689533a-309c-4c23-a6e1-91a5b1c11f2f)

## O que o Gráfico Mostra?

Este gráfico é um **SHAP Dependence Plot** e é uma das visualizações mais importantes para entender as **interações** entre as features no modelo LightGBM. Especificamente, este gráfico mostra:

1.  **O impacto da feature principal (`P2_i_Quanto_tempo_de_experiência...`) no salário previsto:** Como diferentes níveis de experiência influenciam o valor SHAP (a contribuição da experiência para a previsão final do salário).
2.  **A interação com uma segunda feature (`P1_l_Nivel_de_Ensino`):** Como o nível de ensino do profissional modifica o impacto da experiência no salário.

## Como Interpretar os Elementos do Gráfico?

-   **Eixo X (Horizontal): `P2_i_Quanto_tempo_de_experiência...`**
    -   Representa o valor da feature principal: **Tempo de Experiência na área de dados**.
    -   **Importante:** Os valores no eixo (0, 1, 2, ..., 7) são os **valores numéricos resultantes do `OrdinalEncoder`**. Eles correspondem às categorias ordenadas de tempo de experiência. É necessário consultar o mapeamento do encoder para saber o significado exato:
        -   `0`: Não tenho experiência na área de dados
        -   `1`: Menos de 1 ano
        -   `2`: de 1 a 2 anos
        -   `3`: de 3 a 4 anos
        -   `4`: de 4 a 6 anos
        -   `5`: de 5 a 6 anos (ou a próxima categoria se '4 a 6' não estava nos dados)
        -   `6`: de 7 a 10 anos
        -   `7`: Mais de 10 anos
    -   _O `UserWarning` no log confirma que os nomes das categorias não puderam ser exibidos diretamente no eixo._

-   **Eixo Y (Vertical): `SHAP value for Quanto_tempo_de_experiência...`**
    -   Mostra o **valor SHAP** associado à feature "Tempo de Experiência" para cada profissional.
    -   Representa o **impacto (em Reais)** que o nível de experiência daquele profissional teve na previsão final do seu `salary_midpoint`.
    -   **Valores Positivos (> 0):** A experiência daquele profissional *aumentou* a previsão salarial.
    -   **Valores Negativos (< 0):** A experiência daquele profissional *diminuiu* a previsão salarial (comparado à média base).

-   **Pontos Coloridos:**
    -   Cada ponto representa **um profissional** no conjunto de teste.
    -   Sua posição horizontal é seu nível de experiência (codificado).
    -   Sua posição vertical é o impacto SHAP dessa experiência no seu salário previsto.
    *   A **cor** do ponto representa o valor da **feature de interação**: `P1_l_Nivel_de_Ensino` (Nível de Ensino), também **codificado numericamente** conforme a escala da barra de cores à direita.
        -   **Azul (Low ≈ 0.0):** Níveis de ensino mais baixos (ex: Não tenho graduação, Estudante).
        -   **Roxo/Magenta (Mid ≈ 3.0 - 4.0):** Níveis intermediários (ex: Pós-graduação, Mestrado).
        -   **Vermelho (High ≈ 6.0):** Níveis de ensino mais altos (ex: Doutorado, ou a categoria extra 'Prefiro não informar' que foi codificada por último).

## Análise Detalhada dos Padrões e Interações Visíveis:

1.  **Tendência Principal (Impacto da Experiência):**
    -   Há uma **forte tendência positiva** clara: quanto maior o valor no eixo X (mais experiência), maior o valor SHAP no eixo Y (maior o impacto positivo no salário previsto).
    -   Profissionais com baixa experiência (X=0, 1) têm valores SHAP fortemente negativos (entre -2000 e -4000), indicando que sua falta de experiência *reduz* significativamente a previsão salarial.
    -   Profissionais com alta experiência (X=6, 7) têm valores SHAP fortemente positivos (entre +2000 e +6000), indicando que sua vasta experiência *aumenta* muito a previsão salarial.

2.  **Dispersão Vertical (Variabilidade do Impacto):**
    -   Para um mesmo nível de experiência (mesmo valor X), existe uma **dispersão vertical** nos valores SHAP. Isso significa que, mesmo entre pessoas com a mesma experiência, o *impacto* dessa experiência no salário previsto varia.
    -   **Importante:** Essa dispersão vertical **aumenta** consideravelmente conforme a experiência (eixo X) aumenta. Para X=1, a dispersão é pequena; para X=7, a dispersão é muito grande (de +2000 a +6000).

3.  **Interação com Nível de Ensino (Cor dos Pontos):**
    -   A **cor** dos pontos explica grande parte da dispersão vertical, revelando a interação:
    -   **Baixa Experiência (X=0, 1, 2):** Os pontos azuis, roxos e vermelhos estão relativamente misturados e com impacto negativo ou próximo de zero. O nível de ensino tem pouco efeito sobre o impacto (já negativo) da baixa experiência.
    -   **Média Experiência (X=3, 4):** Começa a haver uma separação. Para um mesmo nível de experiência, os pontos mais roxos/vermelhos (ensino superior/pós) tendem a ficar *acima* dos pontos azuis (ensino inferior).
    -   **Alta Experiência (X=6, 7):** A separação é **muito clara**. Dentro da faixa vertical de alto impacto positivo, os pontos **vermelhos** (nível de ensino mais alto, ex: Doutorado) estão consistentemente no **topo** (SHAP mais alto, ex: +5000 a +6000), enquanto os pontos **azuis** (nível de ensino mais baixo) estão na **base** da nuvem de pontos (SHAP positivo, mas menor, ex: +2000 a +3000).
    -   **Conclusão da Interação:** O nível de ensino **potencializa** o retorno da experiência. Ter um alto nível de educação (Mestrado/Doutorado) tem um impacto positivo muito maior no salário previsto para aqueles que *já possuem alta experiência*, em comparação com aqueles com alta experiência mas menor nível educacional.


![grafico_6](https://github.com/user-attachments/assets/e8e63594-14d0-438a-b517-c24fea5ed25e)

## O que o Gráfico Mostra?

Este gráfico é um **SHAP Dependence Plot**, focado em visualizar:

1.  **O impacto da feature principal (`P4_d_3_Python` - Uso de Python) no salário previsto:** Como saber/usar Python (valor 0 ou 1) influencia o valor SHAP (a contribuição dessa habilidade para a previsão final do salário).
2.  **A interação com uma segunda feature (`P2_i_Quanto_tempo_de_experiência...`):** Como o tempo de experiência do profissional modifica o impacto do uso de Python no salário.

## Como Interpretar os Elementos do Gráfico?

-   **Eixo X (Horizontal): `P4_d_3_Python`**
    -   Representa o valor da feature principal: **Uso de Python**.
    -   Os pontos estão concentrados em dois valores:
        -   **`0.0`:** O profissional *não* usa Python (conforme registrado nos dados).
        -   **`1.0`:** O profissional *usa* Python.

-   **Eixo Y (Vertical): `SHAP value for P4_d_3_Python`**
    -   Mostra o **valor SHAP** associado à feature "Uso de Python" para cada profissional.
    -   Representa o **impacto (em Reais)** que saber/usar Python teve na previsão final do `salary_midpoint` daquele profissional.
    -   **Valores Positivos (> 0):** Usar Python *aumentou* a previsão salarial.
    -   **Valores Negativos (< 0):** Usar Python *diminuiu* (ou não usar aumentou) a previsão salarial.
    -   **Valor Zero (0.0):** A feature não teve impacto naquela previsão específica.

-   **Pontos Coloridos:**
    -   Cada ponto representa **um profissional** no conjunto de teste.
    -   Sua posição horizontal indica se ele usa (1.0) ou não (0.0) Python.
    -   Sua posição vertical é o impacto SHAP dessa informação no seu salário previsto.
    *   A **cor** do ponto representa o valor da **feature de interação**: `P2_i_Quanto_tempo_de_experiência...` (Tempo de Experiência), **codificado numericamente** conforme a escala da barra de cores à direita.
        -   **Azul (Low ≈ 0.0):** Pouca ou nenhuma experiência.
        -   **Roxo/Magenta (Mid ≈ 3.0 - 5.0):** Experiência intermediária.
        -   **Vermelho (High ≈ 7.0):** Muita experiência (10+ anos).
        -   _Lembrete:_ Os valores são codificados ordinalmente.

## Análise Detalhada dos Padrões e Interações Visíveis:

1.  **Impacto Principal do Uso de Python (Comparação Horizontal):**
    -   Observe a posição vertical média dos pontos em `X=0.0` vs `X=1.0`.
    -   Os pontos em `X=1.0` (Usa Python) estão, em geral, **verticalmente mais altos** (valores SHAP mais positivos) do que os pontos em `X=0.0` (Não usa Python).
    -   Em média, os pontos em X=0 se concentram em torno de SHAP = -200 a 0, enquanto os pontos em X=1 se concentram em torno de SHAP = 0 a +300 (ignorando alguns outliers).
    -   **Conclusão Principal:** Saber/usar Python tem um **impacto positivo** geral na previsão salarial feita pelo modelo. A diferença média no impacto SHAP entre usar e não usar Python parece ser de algumas centenas de Reais.

2.  **Interação com Tempo de Experiência (Análise Vertical e por Cor):**
    -   **Dentro do grupo `X=0.0` (Não usa Python):** Os pontos azuis, roxos e vermelhos estão bastante misturados verticalmente, principalmente entre SHAP -400 e +200. Isso sugere que, para quem *não usa* Python, a experiência tem pouco efeito sobre o (já pequeno ou negativo) impacto SHAP desta feature.
    -   **Dentro do grupo `X=1.0` (Usa Python):** Aqui a interação é mais clara:
        -   Os pontos com **maior valor SHAP positivo** (topo da nuvem, entre +200 e +500) são predominantemente **vermelhos e roxos escuros**, indicando **alta experiência**.
        -   Os pontos com **valor SHAP próximo de zero ou negativo** (parte inferior da nuvem, incluindo alguns outliers perto de -1500) tendem a ser mais **azuis e roxos claros**, indicando **baixa ou média experiência**.
    -   **Conclusão da Interação:** O **benefício salarial previsto por saber/usar Python é significativamente maior para profissionais com mais experiência**. Embora Python traga algum benefício (ou menos penalidade) mesmo para iniciantes, seu impacto positivo é maximizado quando combinado com um histórico de carreira mais longo na área de dados.

3.  **Outliers:**
    -   Existem alguns pontos em `X=1.0` com valores SHAP muito negativos (~-1500). Estes podem representar casos específicos onde, apesar de usar Python, outras características (não visíveis neste gráfico) levaram a uma previsão salarial muito baixa, ou podem ser artefatos do modelo. No entanto, a tendência geral é clara.

![grafico_7](https://github.com/user-attachments/assets/4b159a22-98c1-4cda-aaad-2e19e12ad876)

## O que o Gráfico Mostra?

Este gráfico é um **SHAP Dependence Plot**, projetado para visualizar duas coisas principais sobre o modelo LightGBM:

1.  **O impacto da feature principal (`P1_l_Nivel_de_Ensino`) no salário previsto:** Como diferentes níveis de educação formal influenciam o valor SHAP (a contribuição da educação para a previsão final do salário).
2.  **A interação com uma segunda feature (`P2_i_Quanto_tempo_de_experiência...`):** Como o tempo de experiência do profissional modifica o impacto do nível de ensino no salário.

## Como Interpretar os Elementos do Gráfico?

-   **Eixo X (Horizontal): `P1_l_Nivel_de_Ensino`**
    -   Representa o valor da feature principal: **Nível de Ensino**.
    -   **Importante:** Os valores no eixo (0, 1, 2, ..., 6) são os **valores numéricos resultantes do `OrdinalEncoder`**. Eles correspondem às categorias ordenadas de nível de ensino. É necessário consultar o mapeamento do encoder para saber o significado exato:
        -   `0`: 'Não tenho graduação formal'
        -   `1`: 'Estudante de Graduação'
        -   `2`: 'Graduação/Bacharelado'
        -   `3`: 'Pós-graduação'
        -   `4`: 'Mestrado'
        -   `5`: 'Doutorado ou Phd'
        -   `6`: Provavelmente a categoria extra 'Prefiro não informar' (adicionada durante o encoding).
    -   _O `UserWarning` nos logs anteriores confirma que os nomes das categorias não puderam ser exibidos diretamente no eixo._

-   **Eixo Y (Vertical): `SHAP value for P1_l_Nivel_de_Ensino`**
    -   Mostra o **valor SHAP** associado à feature "Nível de Ensino" para cada profissional.
    -   Representa o **impacto (em Reais)** que o nível de ensino daquele profissional teve na previsão final do seu `salary_midpoint`.
    -   **Valores Positivos (> 0):** O nível de ensino daquele profissional *aumentou* a previsão salarial.
    -   **Valores Negativos (< 0):** O nível de ensino daquele profissional *diminuiu* a previsão salarial (comparado à média base).

-   **Pontos Coloridos:**
    -   Cada ponto representa **um profissional** no conjunto de teste.
    -   Sua posição horizontal é seu nível de ensino (codificado).
    -   Sua posição vertical é o impacto SHAP desse nível de ensino no seu salário previsto.
    *   A **cor** do ponto representa o valor da **feature de interação**: `P2_i_Quanto_tempo_de_experiência...` (Tempo de Experiência), também **codificado numericamente** conforme a escala da barra de cores à direita.
        -   **Azul (Low ≈ 0.0):** Pouca ou nenhuma experiência.
        -   **Roxo/Magenta (Mid ≈ 3.0 - 5.0):** Experiência intermediária.
        -   **Vermelho (High ≈ 7.0):** Muita experiência (10+ anos).

## Análise Detalhada dos Padrões e Interações Visíveis:

1.  **Tendência Principal (Impacto do Nível de Ensino):**
    -   Há uma **clara tendência positiva** geral: quanto maior o valor no eixo X (maior o nível de ensino, até Doutorado em X=5), maior o valor SHAP médio no eixo Y (maior o impacto positivo no salário previsto).
    -   **Níveis Baixos (X=0, 1):** O impacto SHAP é consistentemente negativo (~ -1000), indicando que não ter graduação ou ser estudante *diminui* a previsão salarial.
    -   **Graduação (X=2):** O impacto SHAP médio está próximo de zero, mas com alguma dispersão.
    -   **Pós-graduação (X=3):** O impacto médio torna-se positivo (~ +500).
    -   **Mestrado (X=4):** O impacto médio aumenta significativamente (~ +1500).
    -   **Doutorado (X=5):** O impacto médio é o mais alto (~ +2200).
    -   **X=6 ('Prefiro não informar'?):** O impacto médio parece ser positivo (~ +1000), mas menor que Mestrado/Doutorado, e com menos pontos.

2.  **Dispersão Vertical (Variabilidade do Impacto):**
    -   Para cada nível de ensino (valor X), existe uma **dispersão vertical** nos valores SHAP. Isso significa que o impacto do *mesmo* nível de ensino varia entre diferentes profissionais.
    -   Essa dispersão vertical **aumenta notavelmente** para níveis de ensino mais altos (Mestrado X=4 e Doutorado X=5).

3.  **Interação com Tempo de Experiência (Cor dos Pontos):**
    -   A **cor** dos pontos explica grande parte da dispersão vertical, especialmente nos níveis de ensino mais altos:
    -   **Níveis Baixos/Médios (X=0 a 3):** Os pontos azuis, roxos e vermelhos estão relativamente misturados verticalmente. A experiência parece ter pouco efeito sobre o impacto (já definido) do nível de ensino nessas faixas.
    -   **Mestrado (X=4):** A separação por cor começa a ficar evidente. Dentro do cluster vertical (SHAP ~ +500 a +2200), os pontos **vermelhos** (alta experiência) estão predominantemente na **parte superior** do cluster (maior impacto positivo), enquanto os pontos **azuis** (baixa experiência) estão na **parte inferior**.
    -   **Doutorado (X=5):** A interação é **muito clara**. A dispersão vertical é grande (SHAP ~ +1500 a +2800). Os pontos **vermelhos** (alta experiência) estão quase exclusivamente no **topo absoluto** do cluster, indicando o máximo impacto positivo do Doutorado. Os pontos **azuis** (baixa experiência), embora ainda tenham SHAP positivo por terem Doutorado, estão na **base** desse cluster.
    -   **Conclusão da Interação:** O **tempo de experiência amplifica significativamente o benefício salarial de ter um nível de ensino mais alto (Mestrado e Doutorado)**. Um Doutorado tem um impacto muito maior na previsão salarial de alguém com 10+ anos de experiência do que na de alguém com pouca experiência. Para níveis de ensino inferiores (até Pós-graduação), a experiência parece ter menos influência sobre o impacto *do próprio nível de ensino*.

![grafico_8](https://github.com/user-attachments/assets/707722ce-d185-40c2-a08a-e42ab320daf1)

## O que o Gráfico Mostra?

Este gráfico é um **SHAP Dependence Plot**, focado em visualizar como a **senioridade** influencia a previsão salarial e como essa influência é modificada pelo **tempo de experiência** do profissional. Especificamente, ele mostra:

1.  **O impacto da feature principal (`P2_g_Nivel` - Senioridade) no salário previsto:** Como ser Júnior, Pleno ou Sênior influencia o valor SHAP (a contribuição da senioridade para a previsão final do salário).
2.  **A interação com uma segunda feature (`P2_i_Quanto_tempo_de_experiência...`):** Como o tempo de experiência do profissional modifica o impacto da senioridade no salário.

## Como Interpretar os Elementos do Gráfico?

-   **Eixo X (Horizontal): `P2_g_Nivel`**
    -   Representa o valor da feature principal: **Nível de Senioridade**.
    -   **Importante:** Os valores no eixo (0.0, 1.0, 2.0) são os **valores numéricos resultantes do `OrdinalEncoder`**. Eles correspondem às categorias ordenadas de senioridade. É necessário consultar o mapeamento do encoder:
        -   `0.0`: 'Júnior'
        -   `1.0`: 'Pleno'
        -   `2.0`: 'Sênior'
        -   *(Valores > 2.0, se existissem, poderiam representar 'Gestor' ou outras categorias adicionadas)*.
    -   _O `UserWarning` nos logs anteriores confirma que os nomes das categorias ('Júnior', 'Pleno', 'Sênior') não puderam ser exibidos diretamente no eixo._

-   **Eixo Y (Vertical): `SHAP value for P2_g_Nivel`**
    -   Mostra o **valor SHAP** associado à feature "Nível de Senioridade" para cada profissional.
    -   Representa o **impacto (em Reais)** que o nível de senioridade daquele profissional teve na previsão final do seu `salary_midpoint`.
    -   **Valores Positivos (> 0):** A senioridade daquele profissional *aumentou* a previsão salarial.
    -   **Valores Negativos (< 0):** A senioridade daquele profissional *diminuiu* a previsão salarial (comparado à média base).

-   **Pontos Coloridos:**
    -   Cada ponto representa **um profissional** no conjunto de teste.
    -   Sua posição horizontal é seu nível de senioridade (codificado).
    -   Sua posição vertical é o impacto SHAP dessa senioridade no seu salário previsto.
    *   A **cor** do ponto representa o valor da **feature de interação**: `P2_i_Quanto_tempo_de_experiência...` (Tempo de Experiência), também **codificado numericamente** conforme a escala da barra de cores à direita.
        -   **Azul (Low ≈ 0.0):** Pouca ou nenhuma experiência.
        -   **Roxo/Magenta (Mid ≈ 3.0 - 5.0):** Experiência intermediária.
        -   **Vermelho (High ≈ 7.0):** Muita experiência (10+ anos).

## Análise Detalhada dos Padrões e Interações Visíveis:

1.  **Tendência Principal (Impacto da Senioridade):**
    -   Há um **claro "salto" positivo** no valor SHAP médio ao passar de um nível de senioridade para o próximo.
    -   **Júnior (X=0.0):** O impacto SHAP é fortemente negativo (concentrado entre -2000 e -4000), indicando que ser Júnior *reduz* substancialmente a previsão salarial.
    -   **Pleno (X=1.0):** O impacto SHAP médio fica próximo de zero (ligeiramente negativo, entre -1000 e +1000), sugerindo que o nível Pleno serve como uma base intermediária.
    -   **Sênior (X=2.0):** O impacto SHAP médio torna-se fortemente positivo (entre +1000 e +3500), indicando que ser Sênior *aumenta* significativamente a previsão salarial.

2.  **Dispersão Vertical (Variabilidade do Impacto):**
    -   Dentro de cada nível de senioridade (valor X), existe uma **dispersão vertical** notável nos valores SHAP. O impacto de ser Júnior, Pleno ou Sênior não é o mesmo para todos.
    -   A dispersão parece **maior** para os níveis **Júnior (X=0.0)** e **Sênior (X=2.0)** do que para o nível Pleno (X=1.0).

3.  **Interação com Tempo de Experiência (Cor dos Pontos):**
    -   A **cor** dos pontos ajuda a explicar a dispersão vertical, revelando uma interação interessante:
    -   **Júnior (X=0.0):** Os pontos com **SHAP menos negativo** (mais próximos de -2000) tendem a ser mais **roxos/vermelhos**, indicando que Júniores com *alguma* experiência (1-4 anos talvez) são menos "penalizados" do que aqueles com baixíssima experiência (azuis, com SHAP até -4000).
    -   **Pleno (X=1.0):** A mistura de cores é grande, mas parece haver uma leve tendência de pontos vermelhos (mais experientes) ficarem um pouco acima dos azuis (menos experientes) dentro desta faixa de senioridade. A interação é menos pronunciada aqui.
    -   **Sênior (X=2.0):** A interação é **muito clara**. A dispersão vertical é grande (SHAP de +1000 a +3500).
        -   Os pontos **vermelhos** (alta experiência) estão consistentemente no **topo** da nuvem, recebendo o maior impulso positivo (SHAP > +2500) por serem Sêniores.
        -   Os pontos **azuis e roxos claros** (menor experiência, talvez recém-promovidos a Sênior ou com menos tempo total de carreira) estão na **base** da nuvem, ainda com SHAP positivo, mas significativamente menor (SHAP ≈ +1000 a +2000).
    -   **Conclusão da Interação:** O **tempo de experiência modula o impacto da senioridade**. Embora ser Sênior sempre aumente a previsão salarial em relação a ser Pleno ou Júnior, o *tamanho* desse aumento é muito maior para profissionais que já possuem uma bagagem considerável de experiência. Ser Sênior com pouca experiência total de carreira tem um impacto positivo menor. Da mesma forma, ser Júnior com alguma experiência é menos desvantajoso do que ser Júnior sem nenhuma experiência.

# Medidas de Performance do Modelo LightGBM

A performance do modelo LightGBM Regressor, treinado para prever o ponto médio da faixa salarial (`salary_midpoint`) dos profissionais de dados, foi avaliada no conjunto de teste (dados não vistos durante o treino). As principais métricas obtidas foram:

---

### 1. MAE (Mean Absolute Error - Erro Absoluto Médio)

-   **Valor Obtido:** `R$ 3.534,09`
-   **O que é:** A média da diferença absoluta (ignorando o sinal positivo ou negativo) entre o valor real do `salary_midpoint` e o valor previsto pelo modelo para cada profissional no conjunto de teste.
-   **Interpretação:** Em média, as previsões de salário geradas pelo modelo desviam aproximadamente **R$ 3.534,09** do valor real (ponto médio da faixa). Esta métrica indica o erro típico de previsão na unidade monetária original (Reais).

---

### 2. RMSE (Root Mean Squared Error - Raiz do Erro Quadrático Médio)

-   **Valor Obtido:** `R$ 5.618,81`
-   **O que é:** Calcula a raiz quadrada da média dos erros de previsão elevados ao quadrado. Isso penaliza erros maiores de forma mais significativa do que o MAE. O resultado também está em Reais.
-   **Interpretação:** O valor do RMSE ser consideravelmente maior que o MAE (R$ 5.618 vs R$ 3.534) sugere que, embora o erro médio seja de ~R$3.5k, o modelo comete alguns erros de previsão substancialmente maiores para certos perfis de profissionais. Isso pode ocorrer em faixas salariais extremas ou para combinações de características menos comuns nos dados de treino.

---

### 3. R² (R-squared - Coeficiente de Determinação)

-   **Valor Obtido:** `0.5004` (ou 50,04%)
-   **O que é:** Representa a proporção da variância total na variável alvo (ponto médio do salário) que é explicada pelas variáveis preditoras (features) incluídas no modelo. Varia entre 0 e 1 (ou 0% e 100%).
-   **Interpretação:** O modelo consegue explicar aproximadamente **50,04%** da variação observada nos salários do conjunto de teste. Isso indica uma capacidade preditiva **moderada**. As features selecionadas (experiência, formação, senioridade, habilidades, etc.) são relevantes e capturam metade da dinâmica salarial, mas a outra metade da variação é atribuível a fatores não incluídos no modelo, interações não capturadas, ou aleatoriedade nos dados.

---

## Resumo da Performance

O modelo LightGBM demonstrou uma capacidade moderada de prever o ponto médio da faixa salarial dos profissionais de dados. Ele explica cerca de metade da variabilidade salarial com um erro médio de previsão na casa dos R$ 3.500. A presença de erros maiores (indicada pelo RMSE) sugere que a precisão pode variar para diferentes subgrupos de profissionais. As métricas, em conjunto com a análise SHAP, indicam que o modelo aprendeu padrões relevantes, mas ainda há espaço para melhorias, possivelmente explorando mais features, técnicas de engenharia de features, ou modelos alternativos.

---

## Explicação Detalhada do Modelo LightGBM para Previsão de Faixa Salarial para a 3º pergunta orientada a dados

# Relatório do Modelo LightGBM para Previsão de Experiência Profissional Prejudicada por Cor/Raça/Etnia

## Resumo do Modelo

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
 

### Interpretação do modelo 1

Apresente os parâmetros do modelo obtido. Tentre mostrar as regras que são utilizadas no
processo de 'raciocínio' (*reasoning*) do sistema inteligente. Utilize medidas como 
o *feature importances* para tentar entender quais atributos o modelo se baseia no
processo de tomada de decisão.


### Resultados obtidos com o modelo 2.

Repita o passo anterior com os resultados do modelo 2.

### Interpretação do modelo 2

Repita o passo anterior com os parâmetros do modelo 2.


## Análise comparativa dos modelos

Discuta sobre as forças e fragilidades de cada modelo. Exemplifique casos em que um
modelo se sairia melhor que o outro. Nesta seção é possível utilizar a sua imaginação
e extrapolar um pouco o que os dados sugerem.


### Distribuição do modelo (opcional)

Tende criar um pacote de distribuição para o modelo construído, para ser aplicado 
em um sistema inteligente.


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




