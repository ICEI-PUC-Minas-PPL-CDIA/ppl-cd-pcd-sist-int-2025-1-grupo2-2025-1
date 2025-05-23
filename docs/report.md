# Disparidade Salarial dos Profissionais de Dados no Brasil


**Pedro Dias Soares, [pdsoares@sga.pucminas.br]** 

**Gabriel Chaves Nascimento, [gabriel.nascimento.1483087@sga.pucminas.br]**

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
*   [Indução de modelos](#indução-de-modelos)
    *   [Modelo 1:](#modelo-1-análise-de-disparidade-salarial-de-profissionais-de-dados-no-brasil-utilizando-o-modelo-random-forest)
    *   [Modelo 2:](#modelo-2-algoritmo)
    *   [Modelo 3](#modelo-3)
*   [Resultados](#resultados)
    *   [Resultados obtidos com o modelo 1.](#resultados-obtidos-com-o-modelo-1)
    *   [Resultados obtidos com o modelo 2.](#resultados-obtidos-com-o-modelo-2)
    *   [Resultados obtidos com o modelo 3.](#resultados-obtidos-com-o-modelo-3)
*   [Interpretação do modelo](#interpretação-dos-modelos)
    *   [Interpretação do modelo 1](#interpretação-do-modelo-1)
    *   [Interpretação do modelo 2](#interpretação-do-modelo-2)
    *   [Interpretação do modelo 3](#interpretação-do-modelo-3)
*   [Análise comparativa dos modelos](#analise-comparativa-dos-modelos)
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
Nome: `salary_midpoint`, `dtype: object`  

**Salários Médio por Etnia:**  
etnia  
Asiático          R$ 10.000,00  
Negro              R$ 7.000,00  
Indígena           R$ 5.000,00  
Pardo              R$ 7.000,00  
Não Informado      R$ 7.000,00  
Branco            R$ 10.000,00  
Nome: `salary_midpoint`, `dtype: object`  

**Salários Médio por Nível de Educação:**  
nível_educacional  
Graduação                  R$ 7.000,00  
Mestrado                  R$ 10.000,00  
Sem Educação Formal        R$ 5.000,00  
Doutorado                 R$ 14.000,00  
Pós-graduação             R$ 10.000,00  
Estudante de Graduação     R$ 3.500,00  
Nome: `salary_midpoint`, `dtype: object`  

**Salários Médio por Senioridade:**  
senioridade  
Júnior         R$ 3.500,00  
Pleno          R$ 7.000,00  
Sênior        R$ 10.000,00  
Nome: `salary_midpoint`, `dtype: object`  

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
Nome: `salary_midpoint`, `dtype: object`  

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
Nome: `salary_midpoint`, `dtype: object`  

**Salários Médio por Região:**  
região  
Centro-oeste    R$ 10.000,00  
Sudeste         R$ 10.000,00  
Nordeste         R$ 7.000,00  
Norte            R$ 7.000,00  
Sul              R$ 7.000,00  
Nome: `salary_midpoint`, `dtype: object`  

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
**Pergunta orientada a dados::** *Como fatores como  formalidade no emprego , características demográficas e regionais se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?*

| Atributo                                           | Código de Referência | Tipo         | Subtipo                             | Descrição                                                                                     | Relevância  |
|----------------------------------------------------|-----------------------|--------------|-------------------------------------|-----------------------------------------------------------------------------------------------|------------|
| Faixa etária                                       | P1a1                  | Qualitativo  | Ordinal                             | Faixa etária do respondente                                                                   | Alta       |
| Gênero                                             | P1b                   | Qualitativo  | Nominal (Multivalorado)             | Identidade de gênero do respondente                                                           | Alta       |
| Nivel de ensino alcançado                          | P1l                   | Qualitativo  | Ordinal                             | Nível de ensino do respondente (graduação, mestrado, etc.)                                    | Alta       |
| Faixa salarial mensal                              | P2h                   | Qualitativo  | Ordinal                             | Faixa salarial mensal do respondente                                                          | Alta       |
| Tempo de experiência na área de dados              | P2i                   | Quantitativo | Discreto                            | Tempo de experiência do respondente na área de dados (em anos)                                | Alta       |
| UF onde mora                                       | P1i1                  | Qualitativo  | Nominal (Multivalorado)             | Unidade Federativa onde o respondente reside                                                  | Alta       |
| Cargo atual                                        | P2f                   | Qualitativo  | Nominal (Multivalorado)             | Cargo atual ocupado pelo respondente                                                          | Alta       |
| Nível de senioridade                               | P2g                   | Qualitativo  | Ordinal                             | Nível de senioridade do respondente (Júnior, Pleno, Sênior)                                   | Alta       |


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


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Analises exploratorias de dados

*   [1º Pergunta orientada a dados ](#1º-pergunta-orientada-a-dados)
  
	*   [Analise exploratoria de dados base de dados State of Data 2023](#analise-exploratoria-de-dados-base-de-dados-state-of-data-2023) 
		   *    [Grafico Distribuição de Salários Mensais](#grafico-distribuição-de-salários-mensais) 
		   *   	[Grafico Relação entre Salário e Tempo de Experiência](#grafico-relação-entre-salário-e-tempo-de-experiência) 
		   *   	[Grafico Distribuição Salarial por Nível de Ensino](#grafico-distribuição-salarial-por-nível-de-ensino) 
		   *   	[Grafico Interação entre Escolaridade, Experiência e Salário](#grafico-interação-entre-escolaridade-experiência-e-salário) 
		   *   	[Grafico Mapa de Calor de Correlações](#grafico-mapa-de-calor-de-correlações) 
		   *   	[Grafico Distribuição por Gênero e Raça-Etnia](#grafico-distribuição-por-gênero-e-raça-etnia) 
		   *   	[Grafico Distribuição Geográfica dos Profissionais](#grafico-distribuição-geográfica-dos-profissionais) 
		   *   	[Grafico Salário por Nível de Senioridade](#grafico-salário-por-nível-de-senioridade) 
		   *   	[Grafico Análise Multivariada das Relações entre Variáveis Selecionadas](#grafico-análise-multivariada-das-relações-entre-variáveis-selecionadas) 
		   *   	[Grafico Sunburst da Distribuição de Profissionais de Dados](#grafico-sunburst-da-distribuição-de-profissionais-de-dados) 


	*   [Analise exploratoria de dados base de dados Microdados](#analise-exploratoria-de-dados-base-de-dados-microdados) 
		   *   	[Grafico Distribuição Nacional de Níveis de Formação dos Docentes](#grafico-distribuição-nacional-de-níveis-de-formação-dos-docentes) 
		   *   	[Grafico Top 10 Estados por Nível de Formação de Docentes](#grafico-top-10-estados-por-nível-de-formação-de-docentes) 
		   *   	[Grafico Distribuição Etária Nacional dos Docentes](#grafico-distribuição-etária-nacional-dos-docentes) 
		   *   	[Grafico Matriz de Correlação entre Formação e Faixa Etária](#grafico-matriz-de-correlação-entre-formação-e-faixa-etária) 
		   *   	[Grafico Mapa Interativo de Bolhas - Distribuição de Docentes por Nível de Formação e UF](#grafico-mapa-interativo-de-bolhas---distribuição-de-docentes-por-nível-de-formação-e-uf) 
		   *   	[Gráfico de Dispersão 3D Interativo - Mestrado, Doutorado e Média de Idade dos Docentes por UF](#grafico-gráfico-de-dispersão-3d-interativo---mestrado-doutorado-e-média-de-idade-dos-docentes-por-uf) 


	*   [Analise exploratoria de dados bases integradas](#analise-exploratoria-de-dados-bases-integradas) 
		   *   	[Grafico Salário Médio Estimado e Total de Docentes por UF](#grafico-salário-médio-estimado-e-total-de-docentes-por-uf) 
		   *   	[Grafico Salário Estimado por Área de Formação - Top 5](#grafico-salário-estimado-por-área-de-formação---top-5) 
		   *   	[Grafico Salário Estimado por Tempo de Experiência](#grafico-salário-estimado-por-tempo-de-experiência) 
		   *   	[Grafico Salário Estimado por Tempo de Experiência em Dados](#grafico-salário-estimado-por-tempo-de-experiência-em-dados)
		   *   	[Grafico Salário Estimado por Nível de Ensino](#grafico-salário-estimado-por-nível-de-ensino) 
		   *   	[Grafico Salário Estimado por Experiência, Agrupado por Nível de Ensino](#grafico-salário-estimado-por-experiência-agrupado-por-nível-de-ensino) 
		   *   	[Grafico Distribuição de Profissionais por Área de Formação Acadêmica](#grafico-distribuição-de-profissionais-por-área-de-formação-acadêmica) 
		   *   	[Grafico Distribuição de Profissionais por Faixa Salarial Mensal](#grafico-distribuição-de-profissionais-por-faixa-salarial-mensal) 
		   *   	[Grafico Distribuição de Profissionais por Nível de Ensino](#grafico-distribuição-de-profissionais-por-nível-de-ensino) 
		   *   	[Grafico Distribuição do Salário Estimado](#grafico-distribuição-do-salário-estimado) 
		   *   	[Grafico Distribuição de Profissionais por Tempo de Experiência em Dados](#grafico-distribuição-de-profissionais-por-tempo-de-experiência-em-dados)
		   *   	[Grafico Top 10 UF de Residência dos Profissionais de Dados](#grafico-top-10-uf-de-residência-dos-profissionais-de-dados)
		   *   	[Grafico Heatmap de Correlação entre Salário, Experiência e Nível de Ensino](#grafico-heatmap-de-correlação-entre-salário-experiência-e-nível-de-ensino)
		   *   	[Grafico Salário Médio Estimado vs. Anos de Experiência por Nível de Ensino](#grafico-salário-médio-estimado-vs-anos-de-experiência-por-nível-de-ensino)
		   *   	[Grafico Relação 3D entre Salário, Experiência e Nível de Ensino](#grafico-relação-3d-entre-salário-experiência-e-nível-de-ensino)
		   *   	[Grafico Salário Estimado vs. Proporção de Docentes com Doutorado na UF de Residência](#grafico-salário-estimado-vs-proporção-de-docentes-com-doutorado-na-uf-de-residência)
		   *   	[Gráfico Relação 3D entre Salário, Experiência e Nível de Ensino](#gráfico-relação-3d-entre-salário-experiência-e-nível-de-ensino)

*   [2º Pergunta orientada a dados ](#2º-pergunta-orientada-a-dados)
  
*   [3º Pergunta orientada a dados ](#3º-pergunta-orientada-a-dados)


# 1º Pergunta orientada a dados 
**Pergunta Orientada a Dados:** *Como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?*

## Analise exploratoria de dados base de dados State of Data 2023

---

### Grafico Distribuição de Salários Mensais
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

## Grafico Distribuição por Gênero e Raça-Etnia
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

## Grafico Análise Multivariada das Relações entre Variáveis Selecionadas
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

## Grafico Salário Estimado por Área de Formação - Top 5
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


## Grafico Distribuição do Salário Estimado
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


## Grafico Heatmap de Correlação entre Salário, Experiência e Nível de Ensino
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


## Gráfico Relação 3D entre Salário, Experiência e Nível de Ensino
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
**Pergunta Orientada a Dados:**
*Qual é a relação entre o tempo de experiência na área de dados, o nível de senioridade e a faixa salarial dos profissionais no Brasil?*

## Objetivo

Investigar as relações entre os principais fatores da carreira de profissionais de dados no Brasil e suas faixas salariais, utilizando dados da base survey_cleaned.csv. Esta análise busca entender como variáveis como experiência, senioridade, formação acadêmica, estado (UF) e habilidades técnicas (ex: Python, SQL) influenciam a remuneração.

## Dicionário de Dados

*Análise Numérica da coluna `salary_numeric_lower_bound`*

O script exibe estatísticas descritivas para a coluna `salary_numeric_lower_bound`. Esta coluna representa o limite inferior da faixa salarial convertida para um valor numérico.

| Estatística     | Valor     | Descrição                                       |
|-----------------|-----------|-------------------------------------------------|
| count           | 4753      | Número de observações não nulas na coluna       |
| mean            | 8935.37   | Média do limite inferior do salário (R$ 8.935,37)|
| std             | 7308.44   | Desvio padrão, indicando grande dispersão dos salários |
| min             | 0         | Valor mínimo (pode indicar salários \"menos de X\") |
| 25% (1º Quartil)| 4001      | 25% dos respondentes ganham até R$ 4.001        |
| 50% (Mediana)   | 8001      | Mediana do limite inferior do salário           |
| 75% (3º Quartil)| 12001     | 75% dos respondentes ganham até R$ 12.001       |
| max             | 40001     | Valor máximo registrado                         |

**Comentários:**  
Esta saída é típica do método `.describe()` do Pandas aplicado a séries numéricas, fornecendo um resumo estatístico essencial.


## Comandos e Visualizações Utilizadas

1. Importação e preparo dos dados

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configuração de estilo
plt.style.use('seaborn')
sns.set_palette("viridis")

# Leitura da base de dados
df = pd.read_csv("survey_cleaned.csv")

# Função para converter faixas salariais em valores médios
def convert_salary_range(salary_range):
    conversions = {
        'de R$ 4.001/mês a R$ 6.000/mês': 5000.50,
        'de R$ 6.001/mês a R$ 8.000/mês': 7000.50,
        'de R$ 8.001/mês a R$ 12.000/mês': 10000.50,
        'de R$ 12.001/mês a R$ 16.000/mês': 14000.50,
        'de R$ 16.001/mês a R$ 20.000/mês': 18000.50,
        'de R$ 20.001/mês a R$ 25.000/mês': 22500.50,
        'Acima de R$ 25.001/mês': 27500.50
    }
    return conversions.get(salary_range, np.nan)

# Aplicação da função e criação da coluna 'Salario_Medio'
df['Salario_Medio'] = df['Faixa_Salarial'].apply(convert_salary_range)

# Criação da coluna 'Habilidades' (soma de conhecimento em SQL e Python)
df['Habilidades'] = df['SQL'] + df['Python']
```

## Resultados e Gráficos

**Faixa Salarial por Grau de Escolaridade**

**O gráfico abaixo apresenta a distribuição das faixas salariais por grau de escolaridade dos profissionais de dados no Brasil, utilizando boxplots para visualizar medianas, dispersão e outliers. De forma geral, observa-se que níveis mais altos de escolaridade, como mestrado e doutorado, tendem a estar associados a faixas salariais superiores, embora haja sobreposição entre categorias e variações dentro de cada grupo.**

![Faixa Salarial por Grau de Escolaridade](docs/imagens/graficos_analise_exploratoria_2_pergunta_orientada_a_dados/Faixa_Salarial_Por_Grau_Escolaridade.png)

```python
# Importando bibliotecas necessárias
import matplotlib.pyplot as plt
import seaborn as sns

# Ordem desejada para o eixo x (níveis de ensino)
order = ['Estudante de Graduação', 'Graduação/Bacharelado', 'Pós-graduação', 'Mestrado', 'Doutorado ou Phd']

# Configuração da figura com tamanho personalizado
plt.figure(figsize=(14, 7))

# Criando o boxplot para faixa salarial por grau de escolaridade
sns.boxplot(
    x='Nivel_Ensino',
    y='Salario_Medio',
    data=df,
    order=order
)

# Adicionando título e ajustes visuais
plt.title('Faixa Salarial por Grau de Escolaridade')
plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para melhor leitura
plt.tight_layout()       # Ajusta o layout para evitar cortes

# Exibindo o gráfico
plt.show()
```

*Insight: Profissionais com médias salariais mais altas tendem a possuir formação em pós-graduação, mestrado ou doutorado. Contudo, a dispersão salarial é ampla em todos os níveis, indicando variação mesmo entre indivíduos com mesma formação.*

## Distribuição Salarial por Estado (UF)

**O gráfico abaixo apresenta uma matriz de calor com a distribuição das faixas salariais por estado no Brasil. Observa-se uma forte concentração de salários mais altos nos estados de São Paulo, Rio de Janeiro e Minas Gerais, indicando que esses centros urbanos oferecem mais oportunidades ou melhor remuneração para profissionais de dados. A visualização também evidencia disparidades regionais significativas, com muitos estados apresentando predominância de faixas salariais mais baixas.**

![Distribuica_Faixa_salarial_por_Estado](docs/imagens/graficos_analise_exploratoria_2_pergunta_orientada_a_dados/Distribuica_Faixa_salarial_por_Estado.png)

```python
uf_stats = df.groupby('UF')['Salario_Medio'].agg(['median', 'count']).reset_index()
uf_stats = uf_stats[uf_stats['count'] >= 10].sort_values('median', ascending=False)
sns.barplot(x='UF', y='median', data=uf_stats)
```

*Insight: Estados como SP, RJ e MG concentram os maiores salários. Há disparidade relevante entre estados do Norte/Nordeste e Sul/Sudeste, refletindo desigualdade estrutural no setor de tecnologia.*

## Linguagens de Programação Mais Utilizadas

**O gráfico abaixo mostra as 10 linguagens de programação mais utilizadas no trabalho entre profissionais de dados no Brasil. Destacam-se SQL e Python como as mais utilizadas, refletindo seu papel essencial em tarefas de manipulação de dados, análise e machine learning. Linguagens como R, Visual Basic/VBA e JavaScript aparecem com menor frequência, indicando uso mais específico ou nichado. O domínio de SQL e Python se confirma como requisito central na área.**

![10_linguagens_mais_utilizadas](docs/imagens/graficos_analise_exploratoria_2_pergunta_orientada_a_dados/10_linguagens_mais_utilizadas.png)

```python
tech_counts = df[['SQL', 'Python']].sum().sort_values(ascending=False)
tech_counts.plot(kind='barh')
```

*Insight: As linguagens SQL e Python dominam a atuação dos profissionais de dados. São amplamente mais utilizadas que outras tecnologias, sugerindo que o conhecimento nelas é quase obrigatório no setor.*

##Conclusões

#Escolaridade influencia positivamente a remuneração, embora haja grande variabilidade dentro de cada grupo.

#Região geográfica (UF) é um dos maiores fatores de desigualdade salarial. SP lidera com folga, seguido de RJ, MG e SC.

#Proeficiência técnica, principalmente em SQL e Python, está presente nos perfis com maiores salários.

#A experiência e senioridade contribuem diretamente para a progressão salarial — o que está de acordo com o esperado.



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3º Pergunta orientada a dados
**Pergunta Orientada a Dados:**
*Como fatores como formalidade no emprego , características demográficas e regionais se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?*

## 1. Importação de Bibliotecas
O script inicia com a importação de diversas bibliotecas Python, cada uma com uma finalidade específica no processo de manipulação e análise de dados.

* Snippet de código
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re
import plotly.express as px
# from ydata_profiling import ProfileReport
import statsmodels.api as sm
```
---
## 2. Funções de Pré-processamento

O script define um conjunto de funções customizadas para realizar tarefas específicas de limpeza e transformação de dados.

### 2.1. clean_col_name(col_name)

Esta função é projetada para limpar e padronizar os nomes das colunas.

```python
# --- Funções de pré-processamento (Mantidas) ---
def clean_col_name(col_name):
    original_input = col_name
    if isinstance(col_name, tuple):
        col_name = "_".join(str(item).strip() for item in col_name)
    elif not isinstance(col_name, str):
        col_name = str(col_name)
    col_name = re.sub(r'[^\w\s-]', '', col_name).strip()
    col_name = re.sub(r'[-\s]+', '_', col_name)
    col_name = re.sub(r"_+", "_", col_name)
    col_name = col_name.strip("_")
    if not col_name: return f"col_limpa_vazia_{hash(original_input)}"
    if col_name and col_name[0].isdigit(): col_name = "_" + col_name
    return col_name
```

Explicação da Função clean_col_name:  
- Converte nomes de colunas que são tuplas em uma string única, unindo os elementos com underscores.  
- Converte nomes de colunas que não são strings para o tipo string.  
- Remove caracteres especiais (exceto alfanuméricos, espaços e hífens) e remove espaços em branco das extremidades.  
- Substitui sequências de hífens e/ou espaços por um único underscore.  
- Substitui múltiplos underscores consecutivos por um único underscore.  
- Remove underscores no início ou fim do nome da coluna.  
- Se, após a limpeza, o nome da coluna se tornar uma string vazia, um nome único é gerado usando um hash do nome original para evitar conflitos.  
- Se o nome da coluna limpo começar com um dígito, um underscore é prefixado para garantir que seja um identificador válido em muitos contextos de programação e análise.

### 2.2. extract_salary_lower_bound(salary_range_str)

Esta função extrai o limite inferior numérico de uma string que representa uma faixa salarial.

```python
def extract_salary_lower_bound(salary_range_str):
    if pd.isna(salary_range_str): return np.nan
    s = str(salary_range_str).lower().replace('r$', '').replace('.', '').replace('/mês', '').strip()
    match_de_a = re.search(r'de\s*(\d+)\s*a\s*(\d+)', s)
    if match_de_a: return float(match_de_a.group(1))
    match_acima_de = re.search(r'acima de\s*(\d+)', s)
    if match_acima_de: return float(match_acima_de.group(1))
    match_menos_de = re.search(r'menos de\s*(\d+)', s)
    if match_menos_de: return 0
    match_so_numeros = re.findall(r'\d+', s)
    if match_so_numeros: return float(match_so_numeros[0])
    return np.nan
```

Explicação da Função extract_salary_lower_bound:  
- Retorna np.nan se a entrada for nula (ausente).  
- Padroniza a string de entrada: converte para minúsculas, remove "R$", ".", "/mês", além de espaços em branco nas extremidades.  
- Utiliza expressões regulares para identificar e extrair o valor numérico correspondente ao limite inferior da faixa salarial, considerando os seguintes padrões:  
  - de X a Y: Retorna X.  
  - acima de X: Retorna X.  
  - menos de X: Retorna 0 (assumindo que o limite inferior é zero ou um valor mínimo).  
- Se nenhum dos padrões acima for encontrado, extrai o primeiro conjunto de dígitos da string.  
- Retorna np.nan se nenhum valor numérico puder ser extraído.  

### 2.3. map_uf_to_region(uf_series: pd.Series) -> pd.Series

Esta função mapeia uma série de siglas de Unidades Federativas (UF) do Brasil para suas respectivas regiões geográficas.

```python
def map_uf_to_region(uf_series: pd.Series) -> pd.Series:
    mapa_regioes = {
        'AC': 'Norte', 'AL': 'Nordeste', 'AP': 'Norte', 'AM': 'Norte', 'BA': 'Nordeste',
        'CE': 'Nordeste', 'DF': 'Centro-Oeste', 'ES': 'Sudeste', 'GO': 'Centro-Oeste',
        'MA': 'Nordeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste', 'MG': 'Sudeste',
        'PA': 'Norte', 'PB': 'Nordeste', 'PR': 'Sul', 'PE': 'Nordeste', 'PI': 'Nordeste',
        'RJ': 'Sudeste', 'RN': 'Nordeste', 'RS': 'Sul', 'RO': 'Norte', 'RR': 'Norte',
        'SC': 'Sul', 'SP': 'Sudeste', 'SE': 'Nordeste', 'TO': 'Norte'
    }
    uf_series_normalized = uf_series.astype(str).str.upper().str.strip()
    siglas_uf = list(mapa_regioes.keys())
    def extract_sigla(val):
        if val in siglas_uf: return val
        for sigla in siglas_uf:
            if f"({sigla})" in val or f" {sigla} " in val or val.endswith(f" {sigla}"): return sigla
        if "DISTRITO FEDERAL" in val: return "DF"
        if "SAO PAULO" in val: return "SP"
        if "RIO DE JANEIRO" in val: return "RJ"
        if "MINAS GERAIS" in val: return "MG"
        if "ESPIRITO SANTO" in val: return "ES"
        if "RIO GRANDE DO SUL" in val: return "RS"
        if "SANTA CATARINA" in val: return "SC"
        if "PARANA" in val: return "PR"
        return val
    uf_series_normalized = uf_series_normalized.apply(extract_sigla)
    mapped_series = uf_series_normalized.map(mapa_regioes)
    return mapped_series.fillna('Desconhecida')
```

Explicação da Função map_uf_to_region:  
- Define um dicionário `mapa_regioes` que associa cada sigla de UF à sua região correspondente.  
- Normaliza a série de UFs de entrada, convertendo para string, maiúsculas e removendo espaços.  
- Define uma subfunção `extract_sigla` que tenta identificar a sigla da UF dentro de uma string que pode conter informações adicionais (ex: "Nome da Cidade (SP)"). Esta subfunção também lida com nomes completos de alguns estados.  
- Aplica `extract_sigla` para obter as UFs padronizadas.  
- Utiliza o método `.map()` com `mapa_regioes` para traduzir as siglas das UFs para os nomes das regiões.  
- Valores que não puderam ser mapeados são preenchidos com `'Desconhecida'`.  

### 2.4. clean_experience_to_numeric(exp_val)

Esta função converte descrições textuais de tempo de experiência em valores numéricos (em anos).

```python
def clean_experience_to_numeric(exp_val):
    if pd.isna(exp_val):
        return np.nan
    s = str(exp_val).lower().strip()
    if 'menos de 1 ano' in s or 'menos de um ano' in s or '< 1 ano' in s:
        return 0.5
    if 'não tenho experiência' in s or 'sem experiência' in s:
        return 0
    numbers = re.findall(r'\d+\.?\d*', s)
    if numbers:
        return float(numbers[0])
    return np.nan
```

Explicação da Função clean_experience_to_numeric:  
- Retorna `np.nan` se o valor de entrada for nulo.  
- Padroniza a string de entrada (minúsculas, remoção de espaços).  
- Converte expressões específicas para valores numéricos:  
  - "menos de 1 ano" (ou variações) para 0.5 anos.  
  - "não tenho experiência" (ou variações) para 0 anos.  
- Se nenhum dos padrões acima for encontrado, utiliza expressões regulares para extrair o primeiro número (inteiro ou decimal) da string, que é assumido como o tempo de experiência em anos.  
- Retorna `np.nan` se nenhum valor numérico puder ser extraído.  

---

## 3. Configurações da Análise Exploratória de Dados (EDA)
Esta seção define configurações globais para o processo de EDA.

```python
eda_output_dir_script = 'visualizacoes_eda_script_univariada_final'
os.makedirs(eda_output_dir_script, exist_ok=True)
sns.set_style("whitegrid")
```

Explicação das Configurações:  
- `eda_output_dir_script`: Define uma string com o nome do diretório ('visualizacoes_eda_script_univariada_final') onde as visualizações ou outros artefatos gerados durante a EDA podem ser salvos.  
- `os.makedirs(eda_output_dir_script, exist_ok=True)`: Cria o diretório especificado. O parâmetro `exist_ok=True` impede que um erro seja levantado caso o diretório já exista.  
- `sns.set_style("whitegrid")`: Define o estilo padrão para os gráficos gerados pela biblioteca Seaborn como "whitegrid". Este estilo adiciona uma grade clara ao fundo dos gráficos, o que pode melhorar a legibilidade.  

---

## 4. Pipeline de Processamento de Dados  
O script segue um pipeline estruturado para carregar, limpar, selecionar e transformar os dados.

### 4.1. Carregar Dados  
A primeira etapa do pipeline é o carregamento do conjunto de dados a partir de um arquivo Excel.

```python
# --- 1. Carregar Dados ---
print("--- 1. Carregando Dados ---")
file_path = "Main_database (2).xlsx"
if not os.path.exists(file_path):
    print(f"ERRO: Arquivo de dados '{file_path}' não encontrado.")
    exit()
df_original = pd.read_excel(file_path)
print(f"Base de dados original carregada: {df_original.shape[0]} linhas, {df_original.shape[1]} colunas.")
```

Explicação do Carregamento de Dados:  
- O caminho para o arquivo de dados é definido na variável `file_path`.  
- O script verifica se o arquivo existe no caminho especificado. Se não existir, uma mensagem de erro é exibida e o script é encerrado.  
- Os dados do arquivo Excel são lidos para um DataFrame do Pandas chamado `df_original`.  
- As dimensões (número de linhas e colunas) do DataFrame carregado são impressas para confirmação.  

### 4.2. Limpeza Inicial de Nomes de Colunas  
Após o carregamento, os nomes das colunas do DataFrame são limpos e padronizados.

```python
# --- 2. Limpeza Inicial de Nomes de Colunas ---
print("\n--- 2. Limpando Nomes de Colunas ---")
df_cleaned_names = df_original.copy()
df_cleaned_names.columns = [clean_col_name(col) for col in df_original.columns]
print("Nomes de colunas limpos.")
```

Explicação da Limpeza de Nomes de Colunas:  
- Uma cópia do DataFrame original (`df_original`) é criada como `df_cleaned_names` para preservar os dados brutos.  
- A função `clean_col_name` (definida anteriormente) é aplicada a cada nome de coluna do `df_cleaned_names`.  
- Uma mensagem confirma a conclusão da limpeza dos nomes das colunas.  

### 4.3. Seleção dos Atributos para EDA  
Nesta etapa, colunas específicas são selecionadas do DataFrame para serem incluídas na Análise Exploratória de Dados.

```python
# --- 3. Selecionando Atributos para EDA ---
print("\n--- 3. Selecionando Atributos para EDA ---")
col_identifiers = {
    'P1_a_1': 'P1_a_1', 'P1_b': 'P1_b', 'P1_l': 'P1_l',
    'P2_h': 'P2_h', 'P2_i': 'P2_i', 'P1_i_1': 'P1_i_1_uf_onde_mora',
    'P2_f': 'P2_f_Cargo_Atual', 'P2_g': 'P2_g_Nivel'
}
df_eda = pd.DataFrame()
for original_key, pattern in col_identifiers.items():
    found_col_name = next((cn for cn in df_cleaned_names.columns if pattern.lower() in cn.lower()), None)
    if found_col_name:
        df_eda[original_key] = df_cleaned_names[found_col_name]
        print(f"Coluna '{original_key}' (mapeada de '{found_col_name}') selecionada.")
    else:
        print(f"Aviso: Padrão '{pattern}' para '{original_key}' não encontrado.")
if df_eda.empty or 'P2_h' not in df_eda.columns:
    print("ERRO: Colunas essenciais para EDA não encontradas ou 'P2_h' ausente.")
    exit()
print(f"Shape do DataFrame de EDA inicial: {df_eda.shape}")
```

Explicação da Seleção de Atributos:  
- Um dicionário `col_identifiers` é definido para mapear nomes de chaves internas (que se tornarão os nomes das colunas no `df_eda`) para padrões de texto. Estes padrões são usados para encontrar as colunas correspondentes no `df_cleaned_names` (após a limpeza dos nomes).  
- Um novo DataFrame vazio, `df_eda`, é inicializado.  
- O script itera sobre `col_identifiers`, procurando por colunas no `df_cleaned_names` cujos nomes (em minúsculas) contenham o padrão especificado (também em minúsculas).  
- Se uma coluna correspondente é encontrada, ela é adicionada ao `df_eda` com o nome da chave interna.  
- Avisos são emitidos se padrões não forem encontrados.  
- Uma verificação crítica é realizada para garantir que o `df_eda` não esteja vazio e que a coluna `'P2_h'` (presumivelmente uma coluna essencial, como salário) esteja presente. Se estas condições não forem atendidas, o script é encerrado.  
- As dimensões do `df_eda` inicial são impressas.  

### 4.4. Limpeza e Transformação dos Atributos Selecionados

Esta é a etapa final do pré-processamento, onde as colunas selecionadas no `df_eda` passam por transformações e limpezas mais detalhadas.

```python
# --- 4. Limpando e Transformando Atributos ---
print("\n--- 4. Limpando e Transformando Atributos ---")
# Processamento de Salário (P2_h)
if 'P2_h' in df_eda.columns:
    df_eda['salary_numeric_lower_bound'] = df_eda['P2_h'].apply(extract_salary_lower_bound)
    df_eda.dropna(subset=['salary_numeric_lower_bound'], inplace=True) # Remove linhas onde o salário não pôde ser convertido
    if not df_eda.empty:
        min_salary_eda = df_eda['salary_numeric_lower_bound'].min()
        max_salary_eda = df_eda['salary_numeric_lower_bound'].max()
        point_of_cut_eda = 7500.0
        print(f"Usando ponto de corte para EDA: {point_of_cut_eda}")
        eda_salary_labels = ["Salário Baixo", "Salário Alto"]

        if min_salary_eda == max_salary_eda: # Caso especial: todos os salários são iguais
            df_eda['faixa_salarial_eda_2cat'] = eda_salary_labels[0] if point_of_cut_eda >= min_salary_eda else eda_salary_labels[1]
        else:
            # Define bins e labels para pd.cut
            bins_eda, labels_eda_cut = ([min_salary_eda, max_salary_eda], [eda_salary_labels[1]]) if point_of_cut_eda <= min_salary_eda else \
                                  ([min_salary_eda, max_salary_eda], [eda_salary_labels[0]]) if point_of_cut_eda >= max_salary_eda else \
                                  ([min_salary_eda, point_of_cut_eda, max_salary_eda], eda_salary_labels)

            unique_bins_eda = sorted(list(set(bins_eda)))
            if len(unique_bins_eda) < 2: unique_bins_eda = [min_salary_eda, max_salary_eda]

            actual_labels = labels_eda_cut # Inicia com os labels determinados pela lógica de bins
            # Ajusta 'actual_labels' se a combinação de 'unique_bins_eda' e 'labels_eda_cut' indicar um único intervalo efetivo
            if len(unique_bins_eda) == 2: # Indica um único intervalo [bin_start, bin_end]
                if len(labels_eda_cut) == 2: # Se havia dois labels possíveis para este intervalo
                    # Cenário 1: O intervalo é [min_salary, point_of_cut] -> Salário Baixo
                    if unique_bins_eda[0] == min_salary_eda and unique_bins_eda[1] == point_of_cut_eda:
                         actual_labels = [labels_eda_cut[0]]
                    # Cenário 2: O intervalo é [point_of_cut, max_salary] -> Salário Alto
                    elif unique_bins_eda[0] == point_of_cut_eda and unique_bins_eda[1] == max_salary_eda:
                         actual_labels = [labels_eda_cut[1]]
                    # Cenário 3: O intervalo é [min_salary, max_salary] (point_of_cut fora da faixa ou na borda)
                    elif unique_bins_eda[0] == min_salary_eda and unique_bins_eda[1] == max_salary_eda:
                        # Aqui, labels_eda_cut já deve ser um único label determinado pela condição inicial
                        # Esta re-verificação garante consistência se a lógica anterior de 1 label foi acionada.
                        if point_of_cut_eda <= min_salary_eda : actual_labels = [eda_salary_labels[1]] # Todos são 'Salário Alto'
                        elif point_of_cut_eda >= max_salary_eda : actual_labels = [eda_salary_labels[0]] # Todos são 'Salário Baixo'
                # Se len(labels_eda_cut) == 1, 'actual_labels' já está correto.
            
            df_eda['faixa_salarial_eda_2cat'] = pd.cut(
                df_eda['salary_numeric_lower_bound'], bins=unique_bins_eda,
                labels=actual_labels, include_lowest=True, duplicates='drop'
            )
        df_eda.dropna(subset=['faixa_salarial_eda_2cat'], inplace=True) # Remove linhas onde a faixa não pôde ser definida
        print(f"'faixa_salarial_eda_2cat' criada. Contas:\n{df_eda['faixa_salarial_eda_2cat'].value_counts(dropna=False)}")
    else: print("DataFrame vazio após processar 'salary_numeric_lower_bound'.")
else: print("ERRO: Coluna 'P2_h' não encontrada."); exit()
```

* Processamento de Experiência (P2_i):
```python
if 'P2_i' in df_eda.columns:
    df_eda['experiencia_anos'] = df_eda['P2_i'].apply(clean_experience_to_numeric)
    median_exp = df_eda['experiencia_anos'].median() # Calcula a mediana ANTES de preencher NaNs
    df_eda['experiencia_anos'].fillna(median_exp, inplace=True)
    print(f"'experiencia_anos' criada. Nulos preenchidos com mediana ({median_exp:.1f}).")

* Processamento de UF para Região (P1_i_1)
# Ajuste para usar o nome da coluna mapeado no passo 3, se existir, ou o nome base.
uf_column_name_in_eda = 'P1_i_1' # Nome da chave como usado em col_identifiers
if uf_column_name_in_eda in df_eda.columns:
    df_eda['Regiao_Mapeada'] = map_uf_to_region(df_eda[uf_column_name_in_eda])
    print(f"'Regiao_Mapeada' criada. Contas:\n{df_eda['Regiao_Mapeada'].value_counts(dropna=False)}")
```
* Processamento de Colunas Categóricas:
```python
categorical_cols_original_keys = ['P1_a_1', 'P1_b', 'P1_l', 'P2_f', 'P2_g']
for key in categorical_cols_original_keys:
    if key in df_eda.columns:
        df_eda[key] = df_eda[key].astype(str).fillna("Não Informado").str.strip()
        if df_eda[key].nunique() > 20: # Limita a cardinalidade
            top_categories = df_eda[key].value_counts().nlargest(19).index
            df_eda[key] = df_eda[key].apply(lambda x: x if x in top_categories else 'Outros')
        print(f"Coluna categórica '{key}' processada. Valores únicos: {df_eda[key].nunique()}")

print(f"Shape do DataFrame de EDA final: {df_eda.shape}")
if df_eda.empty or 'faixa_salarial_eda_2cat' not in df_eda.columns:
    print("ERRO: DataFrame de EDA vazio ou sem coluna alvo ('faixa_salarial_eda_2cat')."); exit()
```
### Explicação da Limpeza e Transformação de Atributos:  
#### Processamento de Salário (coluna `P2_h`):

- Aplica a função `extract_salary_lower_bound` para converter os valores de salário em formato numérico, criando a coluna `salary_numeric_lower_bound`.
- Remove linhas onde a conversão do salário falhou (resultando em `NaN`).
- Se o DataFrame não estiver vazio, categoriza os salários numéricos em **"Salário Baixo"** ou **"Salário Alto"** usando a função `pd.cut`.
- Um ponto de corte (`point_of_cut_eda = 7500.0`) é utilizado.
- A lógica para definir os **bins** (intervalos) e **labels** (rótulos) para `pd.cut` tenta adaptar-se à distribuição dos salários em relação ao ponto de corte.  
  Casos especiais são tratados, como quando todos os salários são iguais ou estão todos de um lado do ponto de corte.  
  A lógica de `actual_labels` foi refinada para garantir que o número correto de rótulos seja usado com base nos bins efetivos.
- A nova coluna categórica é chamada `faixa_salarial_eda_2cat`. Linhas onde esta categorização falha são removidas.
- A contagem de cada categoria de faixa salarial é impressa para validação.

---

### Processamento de Experiência (coluna `P2_i`):

- Aplica a função `clean_experience_to_numeric` para converter as descrições de experiência em anos numéricos, criando a coluna `experiencia_anos`.
- Calcula a mediana dos anos de experiência antes de preencher os valores ausentes, para evitar que o preenchimento influencie a mediana.
- Valores ausentes (`NaN`) na coluna `experiencia_anos` são preenchidos com esta mediana.

### Processamento de UF para Região (coluna referenciada por `P1_i_1`):

- Aplica a função `map_uf_to_region` à coluna de UF (cujo nome no `df_eda` é `P1_i_1`, conforme definido em `col_identifiers`) para criar a coluna `Regiao_Mapeada`.
- A contagem de cada região mapeada é impressa.

### Processamento de Outras Colunas Categóricas:

- Uma lista `categorical_cols_original_keys` define as colunas a serem tratadas.
- Para cada uma dessas colunas:
  - Converte os valores para string.
  - Preenche valores `NaN` com `"Não Informado"`.
  - Remove espaços em branco das extremidades.
  - Se a coluna tiver mais de 20 categorias únicas (alta cardinalidade), as categorias menos frequentes são agrupadas em uma única categoria `"Outros"`, mantendo as 19 mais frequentes.  
    Isso ajuda a simplificar a análise e a modelagem.
- O número de valores únicos após o processamento é impresso.

### Verificações Finais:

- As dimensões do `df_eda` final são impressas.
- Uma verificação final assegura que o `df_eda` não esteja vazio e que a coluna alvo `faixa_salarial_eda_2cat` exista.
- Caso contrário, um erro é impresso e o script é encerrado.

---

# 5 Visualizacao dos dados (Análise Univariada)
Esta seção do script inicializa a análise exploratória de dados univariada, onde cada variável é analisada individualmente. O foco aqui é entender a distribuição e as características de cada atributo.

---

**Mensagem do Script:**


---

**Análise Numérica da coluna `salary_numeric_lower_bound`:**

O script exibe estatísticas descritivas para a coluna `salary_numeric_lower_bound`. Esta coluna representa o limite inferior da faixa salarial convertida para um valor numérico.

| Estatística       | Valor         | Descrição                                                      |
|-------------------|---------------|----------------------------------------------------------------|
| count             | 4753          | Número de observações não nulas na coluna                      |
| mean              | 8935.37       | Média do limite inferior do salário (R$ 8.935,37)              |
| std               | 7308.44       | Desvio padrão, indicando grande dispersão dos salários         |
| min               | 0             | Valor mínimo (pode indicar salários "menos de X")              |
| 25% (1º Quartil)   | 4001          | 25% dos respondentes ganham até R$ 4.001                        |
| 50% (Mediana)     | 8001          | Mediana do limite inferior do salário (metade ganha até isso)  |
| 75% (3º Quartil)   | 12001         | 75% dos respondentes ganham até R$ 12.001                       |
| max               | 40001         | Valor máximo registrado                                        |
| Name & dtype      | salary_numeric_lower_bound (float64) | Nome e tipo de dado da coluna              |

---

**Comentários:**  
Esta saída é típica do método `.describe()` do Pandas aplicado a séries numéricas, fornecendo um resumo estatístico essencial para entender a distribuição central, a dispersão e a amplitude dos dados salariais.

---

### Análise do histograma e KDE dos salarios numericos 

O gráfico apresentado é uma combinação de um histograma e uma estimativa de densidade do kernel (KDE) para a variável `salary_numeric_lower_bound`, que representa o limite inferior da faixa salarial dos profissionais de dados no Brasil. Este tipo de visualização é fundamental para entendermos a distribuição dos salários e, consequentemente, as disparidades existentes.


![Histogrma e KDE de salary_numeric_lower_bound](https://github.com/user-attachments/assets/62391c2d-14eb-4784-90a3-fc1062bda7ba)

---

#### Como Interpretar o Gráfico

- **Eixo X (`salary_numeric_lower_bound`)**:  
  Representa os valores do limite inferior da faixa salarial. No gráfico, varia de valores próximos a zero até acima de R$ 40.000.

- **Eixo Y Esquerdo (Contagem - Histograma)**:  
  Associado às barras azuis (histograma). Cada barra representa um intervalo de salários (bin), e a altura indica o número de profissionais de dados cujo limite inferior da faixa salarial se encontra naquele intervalo.

- **Eixo Y Direito (Densidade - Linha KDE)**:  
  Associado à linha azul escura (linha KDE estimada). A curva KDE é uma versão suavizada do histograma, mostrando a forma da distribuição salarial de forma contínua. A área sob a curva em um intervalo representa a proporção de profissionais naquela faixa salarial. Picos indicam concentrações maiores.

- **Título**:  
  "Histograma e KDE de salary_numeric_lower_bound" – indica claramente o conteúdo do gráfico.

---

#### Informações Extraídas do Gráfico

- **Concentração Salarial**:  
  Há uma concentração significativa de profissionais na faixa salarial mais baixa. O pico principal do histograma e da curva KDE está em torno de R$ 5.000 a R$ 10.000, indicando que a maioria dos profissionais de dados está nessa faixa de remuneração inicial.

- **Assimetria Positiva (Skewness)**:  
  A distribuição é assimétrica à direita, com a maioria dos salários em valores mais baixos, mas com uma cauda longa para valores altos. Alguns profissionais recebem salários muito superiores, elevando a média geral.

- **Multimodalidade Sugerida**:  
  A curva KDE mostra múltiplos picos (modas). Além do pico dominante na faixa baixa, há picos menores em faixas salariais superiores (ex.: em torno de R$ 15.000, R$ 20.000 e outros menos pronunciados), sugerindo diferentes grupos salariais.

---

#### Possíveis Insights e Conexão com a Pergunta Orientada a Dados

**Pergunta central:**  
*"Como fatores como formalidade no emprego, características demográficas e regionais se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?"*

- O gráfico evidencia que existem disparidades salariais significativas.
- A longa cauda à direita e os múltiplos picos na distribuição mostram visualmente essa variação salarial.
- Este ponto de partida visual ajuda a direcionar análises mais detalhadas sobre como os fatores demográficos, regionais e de proficiência técnica afetam essas disparidades.

> Em resumo, o gráfico de Histograma e KDE do salary_numeric_lower_bound visualiza as disparidades salariais existentes entre profissionais de dados no Brasil. A forma da distribuição, com sua assimetria e múltiplos picos, sugere que diversos fatores, incluindo formalidade no emprego, características demográficas, regionais e, crucialmente, a proficiência técnica, estão interagindo de maneiras complexas para criar esses diferentes patamares salariais. O gráfico é a evidência do "o quê" (as disparidades), e a análise mais aprofundada dos fatores mencionados permitirá entender o "porquê" e o "como".

---

### Análise histograma e estimativa de densidade do kernel (KDE) de salarios:

O gráfico apresentado é uma combinação de um histograma e uma estimativa de densidade do kernel (KDE) para a variável `salary_numeric_lower_bound`, que representa o limite inferior da faixa salarial dos profissionais de dados no Brasil. Este tipo de visualização é fundamental para entendermos a distribuição dos salários e, consequentemente, as disparidades existentes.

![box plot salary_numeric_lower](https://github.com/user-attachments/assets/a9d63676-9522-4665-b1d4-66b716fcc70c)


---

#### Como Interpretar o Gráfico

- **Eixo X (`salary_numeric_lower_bound`)**  
  Representa os valores do limite inferior da faixa salarial. No gráfico, varia de valores próximos a zero até acima de R$ 40.000.

- **Eixo Y Esquerdo (Contagem - Histograma)**  
  Associado às barras azuis (histograma). Cada barra representa um intervalo de salários (bin), e a altura indica o número de profissionais de dados cujo limite inferior da faixa salarial se encontra naquele intervalo.

- **Eixo Y Direito (Densidade - Linha KDE)**  
  Associado à linha azul escura (linha KDE estimada). A curva KDE é uma versão suavizada do histograma, mostrando a forma da distribuição salarial de forma contínua. A área sob a curva em um intervalo representa a proporção de profissionais naquela faixa salarial. Picos indicam concentrações maiores.

- **Título**  
  "Histograma e KDE de salary_numeric_lower_bound" – indica claramente o conteúdo do gráfico.

---

#### Informações Extraídas do Gráfico

- **Concentração Salarial**  
  Observa-se uma concentração significativa de profissionais na faixa salarial mais baixa. O pico mais alto do histograma e da curva KDE está em torno de R$ 5.000 a R$ 10.000, indicando que a maioria dos profissionais de dados se encontra nessa faixa de remuneração inicial.

- **Assimetria Positiva (Skewness)**  
  A distribuição é assimétrica à direita (ou positiva). Isso significa que, embora a maioria dos salários esteja concentrada em valores mais baixos, existem alguns profissionais com salários consideravelmente mais altos, o que "puxa" a cauda da distribuição para a direita. Esses salários mais altos são menos frequentes, mas elevam a média geral.

- **Multimodalidade Sugerida**  
  A curva KDE apresenta múltiplos picos (modas), embora um seja dominante. Há um pico principal na faixa mais baixa já mencionada, e picos secundários menores em faixas salariais mais altas (por exemplo, em torno de R$ 15.000, R$ 20.000 e possivelmente outros menos pronunciados). Isso sugere a existência de diferentes grupos de profissionais de dados com níveis salariais distintos.

---

#### Possíveis Insights e Conexão com a Pergunta Orientada a Dados

**Pergunta central:**  
*"Como fatores como formalidade no emprego, características demográficas e regionais se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?"*

O gráfico, ao mostrar a distribuição e as disparidades salariais, serve como ponto de partida para investigar essa questão. Os insights abaixo conectam o gráfico à pergunta:

- **Existência de Disparidades**  
  O gráfico demonstra claramente que existem disparidades salariais significativas. A longa cauda à direita e os múltiplos picos são evidências visuais dessa variação.

>Em resumo, o gráfico de Histograma e KDE do salary_numeric_lower_bound visualiza as disparidades salariais existentes entre profissionais de dados no Brasil. A forma da distribuição, com sua assimetria e múltiplos picos, sugere que diversos fatores, incluindo formalidade no emprego, características demográficas, regionais e, crucialmente, a proficiência técnica, estão interagindo de maneiras complexas para criar esses diferentes patamares salariais. O gráfico é a evidência do "o quê" (as disparidades), e a análise mais aprofundada dos fatores mencionados permitirá entender o "porquê" e o "como".

---

---

### Análise do Gráfico ECDF de salarios 

![ECDF de salary_numeric_lower](https://github.com/user-attachments/assets/45ac6402-0f8b-494a-ab58-71bef586ac65)

**O que o Gráfico ECDF Mostra:**

- **Eixo X (salary_numeric_lower_bound):**  
  Representa os valores do limite inferior da faixa salarial, ordenados do menor para o maior.

- **Eixo Y (Proporção Cumulativa):**  
  Varia de 0 a 1 (ou 0% a 100%). Para qualquer valor de salário no eixo X, o valor correspondente no eixo Y indica a proporção (ou porcentagem) de profissionais de dados que ganham até aquele valor salarial.

- **Forma da Curva:**  
  A curva sobe em "degraus". Cada degrau representa um ou mais profissionais com aquele valor salarial específico. A altura de cada salto vertical corresponde à proporção de observações naquele ponto. Onde a curva é mais íngreme, há uma maior concentração de dados.

**Informações Extraídas Diretamente:**

- **Percentis Salariais:**  
  É fácil ler percentis diretamente no gráfico.

- **Mediana (P50):**  
  Encontrando 0.5 no eixo Y e seguindo horizontalmente até a curva e depois verticalmente até o eixo X, observa-se que a mediana está próxima de R$ 7.500 - R$ 8.000.

- **Outros Percentis:**  
  Aproximadamente 20% (0.2 no eixo Y) dos profissionais ganham até cerca de R$ 4.000. Cerca de 80% (0.8 no eixo Y) ganham até aproximadamente R$ 12.000 - R$ 13.000. Quase 90% (0.9 no eixo Y) ganham até R$ 20.000.

- **Concentração de Salários:**  
  Degraus mais longos horizontalmente indicam faixas salariais com poucos profissionais, enquanto saltos verticais altos indicam concentrações salariais específicas. A subida rápida da curva até R$10.000-R$15.000 mostra a maioria concentrada nessa faixa.

- **Dispersão e Cauda Superior:**  
  A curva continua subindo até atingir 1.0 próximo a R$ 40.000, indicando a presença de salários elevados, embora menos frequentes.

**Conexão com a Pergunta Orientada a Dados:**

- A ECDF oferece uma visão quantitativa das disparidades salariais e da distribuição dos profissionais ao longo da faixa salarial.

- Permite quantificar desigualdades, por exemplo: "X% dos profissionais de dados no Brasil têm um limite inferior de salário até Y reais".  
  Exemplo: Se 90% ganham até R$ 20.000, os 10% restantes estão distribuídos em uma faixa salarial mais ampla, evidenciando disparidade entre os mais bem pagos.

>Em resumo, a ECDF do salary_numeric_lower_bound oferece uma maneira clara de visualizar a proporção acumulada de profissionais em cada nível salarial. Ela quantifica as disparidades mostrando quantos profissionais estão abaixo de certos tetos salariais e destaca as faixas de concentração. Para responder à pergunta sobre a influência e interação dos fatores, seria necessário comparar ECDFs de diferentes segmentos da população de profissionais de dados, usando este gráfico como uma linha de base da distribuição geral.
---

![QQ-plot salary_numeric_lower](https://github.com/user-attachments/assets/6d31facb-2e17-410c-a524-4c3d772644d9)

### Análise do Gráfico QQ-Plot de salarios 

**O que o Gráfico QQ-Plot Mostra:**

- **Eixo X (Quantis Teóricos - Distribuição Normal Padrão):**  
  Valores que seriam esperados se os dados seguissem perfeitamente uma distribuição normal.

- **Eixo Y (Quantis da Amostra - Ordenados):**  
  Os valores reais do `salary_numeric_lower_bound`, ordenados do menor para o maior.

- **Linha de Referência (Normal Teórica):**  
  Linha diagonal que representa a distribuição normal perfeita. Se os pontos estivessem alinhados a esta linha, indicaria que os dados seguem uma distribuição normal.

- **Pontos Azuis:**  
  Quantis dos salários observados plotados contra os quantis teóricos de uma distribuição normal.

---

**Informações Extraídas do Gráfico:**

- **Não Normalidade dos Dados Salariais:**  
  Os pontos azuis não seguem a linha de referência consistentemente, indicando que a distribuição dos salários não é normal.

- **Desvios da Linha:**  
  - *Cauda Inferior (Valores Baixos de Salário):*  
    Na extremidade esquerda, pontos estão ligeiramente abaixo da linha ou apresentam comportamento em "degraus", sugerindo concentração em salários baixos, inclusive valores zero ou próximos a zero, que não seguem uma distribuição normal.  
  - *Corpo Central da Distribuição:*  
    Os pontos se aproximam da linha, mas ainda com alguma curvatura.  
  - *Cauda Superior (Valores Altos de Salário):*  
    Na extremidade direita, os pontos desviam-se acima da linha, caracterizando uma cauda direita pesada (longa). Isso indica que os salários mais altos são mais elevados e frequentes do que o esperado numa normal.

- **Assimetria Positiva:**  
  O desvio acentuado na cauda superior reforça a presença de assimetria positiva — maioria dos salários baixos, com uma minoria recebendo salários substancialmente mais altos.

---

**Conexão com a Pergunta Orientada a Dados:**

- O QQ-Plot ajuda a caracterizar a natureza da distribuição salarial e as disparidades associadas.

- **Caracterização da Disparidade Salarial:**  
  A não normalidade, especialmente a cauda direita pesada, evidencia visualmente a disparidade salarial. Os salários não estão distribuídos simetricamente; há uma minoria que ganha significativamente mais, impactando a média e a desigualdade no setor.

>Em resumo, o QQ-Plot contra uma distribuição normal demonstra que os salários dos profissionais de dados no Brasil não seguem esse padrão teórico, exibindo notavelmente uma cauda direita mais pesada. Isso significa que os salários mais altos são consideravelmente maiores do que o esperado em uma distribuição normal. Essa característica da distribuição é uma manifestação das disparidades salariais, onde fatores como alta proficiência técnica, combinados com aspectos regionais, demográficos e de formalidade, provavelmente impulsionam os ganhos de uma minoria para níveis significativamente elevados em comparação com o restante dos profissionais.
---

![Histogrma e KDE de experiencia_anos](https://github.com/user-attachments/assets/ac711cb0-d98a-4bf8-8a0a-830b6800c5ca)

---

### Análise do Gráfico (Histograma e KDE de `experiencia_anos`)

**O que o Gráfico Mostra:**

Este gráfico exibe a distribuição dos **anos de experiência** dos profissionais de dados na amostra.

- **Eixo X (`experiencia_anos`)**:  
  Representa o número de anos de experiência.

- **Eixo Y Esquerdo (Contagem - Histograma)**:  
  Altura das barras indica o número de profissionais em cada faixa de experiência.

- **Eixo Y Direito (Densidade - Linha KDE Estimada)**:  
  Curva suavizada que mostra a forma contínua da distribuição.

---

**Informações Extraídas do Gráfico:**

- **Picos de Concentração:**  
  - Pico mais alto em torno de **1 ano de experiência** — grande concentração de profissionais iniciantes ou em transição.
  - Outro pico relevante em torno de **3-4 anos**.
  - Concentrações menores aparecem em torno de **0 anos**, **5-6 anos**, **7-8 anos** e **cerca de 10 anos**.

- **Multimodalidade:**  
  A presença de múltiplos picos sugere diferentes grupos de profissionais com perfis distintos de experiência no mercado de dados.

- **Assimetria:**  
  Leve assimetria à direita — mais profissionais com pouca experiência, mas uma cauda indicando presença significativa de profissionais experientes.

- **Amplitude da Experiência:**  
  A distribuição abrange desde iniciantes (0 anos) até profissionais com mais de 10 anos de atuação.

---

**Conexão com a Pergunta Orientada a Dados (Disparidades Salariais):**

- A variável `experiencia_anos` é um **proxy essencial para proficiência técnica**, um dos pilares da sua pergunta de pesquisa.

#### 🧠 **Fundamento para Disparidades Salariais:**

- **Variabilidade na Experiência → Variabilidade Salarial**  
  Espera-se que profissionais com mais anos de experiência possuam maior proficiência, responsabilidades e, consequentemente, salários mais elevados.

- **Relacionamento com a Distribuição Salarial:**  
  - O grupo com ~1 ano de experiência provavelmente compõe boa parte da base da distribuição salarial (faixas júnior/iniciais).  
  - Picos em 3-4 e 5-6 anos sugerem profissionais plenos e seniores.  
  - Picos em 10+ anos podem indicar especialistas, gestores ou profissionais altamente experientes — esses contribuem para a cauda direita da distribuição de salários.

---

**Interação da Experiência (Proficiência) com Outros Fatores:**

- **Formalidade no Emprego:**  
  Profissionais experientes tendem a ter mais barganha por contratos formais (ex: CLT sênior, PJ com altos valores), ou ocupam posições de liderança com estruturas salariais diferenciadas.

- **Características Regionais:**  
  O retorno financeiro por ano de experiência varia por região. Mercados maiores ou com maior demanda podem valorizar mais a senioridade.

- **Características Demográficas:**  
  Idade se correlaciona com experiência, e outros fatores como gênero e raça podem influenciar progressões salariais mesmo entre profissionais com o mesmo tempo de atuação.

---

**Base para Análises Segmentadas:**

A distribuição de `experiencia_anos` permite formar **grupos de análise comparativa**:

- Disparidade salarial entre iniciantes (0-2 anos) vs. seniores (8-10+ anos).  
- Como **formalidade** e **região** afetam o salário em cada faixa de experiência?  
- A experiência amplifica ou atenua desigualdades causadas por outras variáveis?

  
>Em resumo: O gráfico da distribuição de `experiencia_anos` revela a estrutura da força de trabalho em dados no Brasil em termos de tempo de atuação, um dos principais indicadores de proficiência técnica. Os múltiplos picos e ampla variação são peças-chave para entender as disparidades salariais. A experiência interage com formalidade, região e características demográficas, moldando de maneira complexa a estrutura salarial observada no setor.

---

![boxplot de experiencia_anos](https://github.com/user-attachments/assets/6554d62f-4069-4111-8870-6862f26c1eae)

---

### Análise do Gráfico (Boxplot de `experiencia_anos`)

**O que o Gráfico Mostra:**

Este boxplot resume visualmente a distribuição dos **anos de experiência** dos profissionais de dados na amostra.

- **Caixa (Intervalo Interquartil - IQR):**  
  Contém os 50% centrais dos dados — de Q1 a Q3.

- **Linha Central (Mediana - Q2):**  
  Divide a distribuição em duas metades. Está posicionada em **aproximadamente 3 anos**.

- **Bordas da Caixa:**  
  - **Q1 (25%)**: Cerca de **1 ano** de experiência.  
  - **Q3 (75%)**: Cerca de **5 anos** de experiência.

- **Hastes (Whiskers):**  
  - **Inferior**: Vai até **0 anos**, indicando presença de iniciantes.  
  - **Superior**: Vai até cerca de **10 anos**, representando os mais experientes da amostra.

- **Outliers:**  
  O gráfico não exibe explicitamente pontos além das hastes como outliers, sugerindo que valores até 10 anos são considerados dentro da faixa aceitável pela definição padrão de 1.5×IQR.

---

**Informações Extraídas do Gráfico:**

- **Experiência Mediana:**  
  Metade dos profissionais tem até **3 anos** de experiência.

- **Concentração da Experiência:**  
  50% da amostra está concentrada entre **1 e 5 anos** (IQR), indicando um mercado composto majoritariamente por profissionais júnior a pleno.

- **Amplitude da Experiência Comum:**  
  A maior parte da distribuição está entre **0 e 10 anos**, cobrindo a maior parte das fases da carreira técnica.

- **Assimetria Positiva:**  
  A mediana (3 anos) está mais próxima de Q1 (1 ano) do que de Q3 (5 anos), e a haste superior é mais longa — características típicas de uma assimetria à direita.  
  Isso sugere maior concentração em níveis iniciais, com alguns profissionais se estendendo para níveis mais altos de senioridade.

---

**Conexão com a Pergunta Orientada a Dados (Disparidades Salariais):**

O boxplot de `experiencia_anos` fornece um resumo conciso de um dos fatores centrais de sua análise: **proficiência técnica** como motor das **disparidades salariais**.

#### 🧠 **Perfil de Senioridade e Disparidade Salarial:**

- A mediana de 3 anos mostra que boa parte do mercado é composta por profissionais em início ou meio de carreira.
- A variação dentro do IQR (1–5 anos) já representa um potencial de diferenciação salarial significativa, pois o acúmulo de experiência geralmente implica maior conhecimento e responsabilidades.
- A faixa de 5 a 10 anos (acima de Q3) abrange profissionais mais seniores, que provavelmente ocupam cargos com salários mais elevados.

---

**Interação da Experiência com Outros Fatores:**

- **Formalidade no Emprego:**  
  Profissionais mais experientes (Q3 em diante) tendem a acessar formatos de trabalho mais estruturados (CLT sênior, PJ consultivo) com salários mais altos. Iniciantes, por outro lado, podem estar em estágios ou vínculos mais precários.

- **Impacto Regional:**  
  A valorização da experiência pode variar regionalmente. Polos tecnológicos ou regiões com alta demanda podem oferecer salários mais altos mesmo para profissionais com experiência mediana.

- **Conexão com Demografia:**  
  A experiência está fortemente relacionada à idade. Outras variáveis, como gênero, raça ou formação, podem influenciar como a experiência se converte em retorno financeiro.

---

**Ponto de Partida para Análises Salariais Segmentadas:**

O boxplot permite a definição de **faixas de experiência** para investigar disparidades salariais:

- **Q1 e abaixo (0–1 ano)**: Profissionais em início de carreira.  
- **IQR (1–5 anos)**: Base representativa do mercado pleno.  
- **Q3 em diante (5–10 anos)**: Profissionais seniores ou especialistas.

🔍 *Exemplo de pergunta de análise:*  
Como variam os salários de profissionais com 4 anos de experiência trabalhando como CLT em São Paulo, em comparação com profissionais com mesma experiência atuando como PJ no Nordeste?
  
>Em resumo: O boxplot de `experiencia_anos` mostra uma mediana de cerca de **3 anos** e uma concentração de 50% dos profissionais entre **1 e 5 anos**, indicando um mercado majoritariamente jovem, com distribuição assimétrica à direita. A variação da experiência é um componente central da proficiência técnica e um dos **principais impulsionadores das disparidades salariais**. A interação entre experiência, formalidade, localização geográfica e perfil demográfico delineia os padrões salariais observados no setor de dados no Brasil.

---

![Distribuicao de nivel ](https://github.com/user-attachments/assets/b15039bb-1771-4c20-a06b-a0ba54aa7cae)

### Análise do Gráfico (Distribuição de `P2_g` – Nível de Senioridade)

---

#### **O que o Gráfico Mostra:**

Este gráfico de barras horizontais exibe a **frequência de profissionais de dados** em diferentes categorias de senioridade (`P2_g`):

- **Eixo Y (P2_g):** Categorias de nível de senioridade: `Júnior`, `Pleno`, `Sênior` e `nan` (não informado).
- **Eixo X (Contagem):** Número de profissionais em cada categoria.

#### **Distribuição Observada:**

- **Sênior:** Categoria mais numerosa, com mais de **1.400 profissionais**.
- **Pleno:** Segunda mais frequente, próxima de **1.350**.
- **Júnior:** Menor grupo entre os níveis definidos, com **pouco mais de 1.000**.
- **`nan`:** Categoria ausente ou indefinida, com cerca de **900 profissionais**, representando uma **proporção significativa** da amostra.

---

### Conexão com a Pergunta Orientadora (Disparidades Salariais)

> *Como fatores como formalidade no emprego, características demográficas e regionais interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?*

#### **1. Senioridade como Determinante Salarial:**

- A hierarquia Júnior → Pleno → Sênior está geralmente associada a uma **progressão salarial crescente**.
- Profissionais Sênior tendem a ter **maior remuneração**, dado seu nível de responsabilidade, autonomia e experiência técnica.

#### **2. Correlação com Proficiência Técnica e Experiência:**

- O nível de `P2_g` reflete, em muitos casos, os **anos de experiência** e o grau de **proficiência técnica**.
- A distribuição observada (predominância de Plenos e Sêniors) é consistente com a **mediana de 3 anos** de experiência já identificada anteriormente.

#### **3. Segmentação Necessária para Análise Salarial:**

- Avaliar as **faixas salariais dentro de cada nível de senioridade** é essencial.
  - Ex: Como variam os salários entre Júnior x Pleno x Sênior?
- **`nan`** deve ser analisado separadamente:
  - São profissionais com perfil atípico? Freelancers? Gestores? Ou apenas dados faltantes?
  - Comparar sua remuneração com os demais pode revelar **subgrupos ocultos** no mercado.

#### **4. Interações com Outros Fatores:**

- **Formalidade no emprego:**
  - Níveis mais altos de senioridade costumam vir acompanhados de **contratos mais formais** (ex: PJ de alto valor, CLT com benefícios).
- **Região:**
  - O mesmo cargo (ex: Pleno) pode ter **valores salariais distintos** entre São Paulo, Nordeste ou interior.
- **Demografia:**
  - Características como **gênero, raça, idade, escolaridade** podem impactar tanto a **progressão entre níveis** quanto a **remuneração dentro de cada nível**.

#### **5. Reflexões sobre o Grupo `nan`:**

- Pode conter perfis como:
  - Autônomos/freelancers sem classificação tradicional;
  - Profissionais em transição ou multifuncionais;
  - Dados ausentes por falha ou omissão.
- Deve ser avaliado com atenção para **evitar viés** ou perda de insights valiosos.

>Em resumo: O gráfico de `P2_g` revela uma **estrutura de senioridade equilibrada**, com leve predominância de níveis mais experientes. Essa variável é **fundamental para entender a segmentação salarial** no setor de dados. Ao combiná-la com variáveis como **experiência, formalidade contratual, região e demografia**, é possível **compreender as múltiplas dimensões das disparidades salariais** entre os profissionais da área no Brasil.

---

![Distribuicao_regiao](https://github.com/user-attachments/assets/61c205ef-3dea-4c72-93f1-9435efcfa160)

---

### Análise do Gráfico (Distribuição de `Regiao_Mapeada`)

---

#### O que o Gráfico Mostra

Este gráfico de barras horizontais exibe a **contagem de profissionais de dados** distribuídos pelas diferentes regiões mapeadas do Brasil, além de uma categoria "Desconhecida".

- **Eixo Y (`Regiao_Mapeada`)**: Categorias regionais – Sudeste, Sul, Nordeste, Centro-Oeste, Norte e Desconhecida.  
- **Eixo X (Contagem)**: Número de profissionais em cada uma dessas regiões.

---

#### Informações Extraídas do Gráfico

**Concentração Regional:**

- **Sudeste**: É a região com a maior concentração de profissionais, com uma contagem próxima de **3.000**.
- **Sul**: Segunda maior representatividade, com cerca de **900 a 1.000** profissionais.
- **Nordeste**: Terceira maior, com aproximadamente **500** profissionais.
- **Centro-Oeste**: Cerca de **250 a 300**.
- **Norte**: A menor contagem, abaixo de **100** profissionais.
- **Desconhecida**: Aproximadamente **100 a 150**, com região não identificada.

**Perfil Geográfico da Amostra:**  
A maior parte dos profissionais de dados está concentrada no Sudeste, seguido pela região Sul. As demais regiões apresentam participação significativamente menor.

---

#### Conexão com a Pergunta Orientadora

**Como fatores como formalidade no emprego, características demográficas e regionais se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?**

---

#### Impactos da Região nas Disparidades Salariais

**Mercados Regionais Diferenciados:**  
Cada região do Brasil possui níveis distintos de desenvolvimento econômico, maturidade do mercado de trabalho, custo de vida e demanda por profissionais de dados, afetando diretamente as faixas salariais.

**Polos Econômicos e Tecnológicos:**  
O Sudeste e o Sul concentram os principais centros urbanos e tecnológicos, com maior volume de vagas e salários mais competitivos.

**Interações com Outros Fatores:**

- **Proficiência Técnica:** O retorno salarial da qualificação técnica varia conforme a região; o mesmo nível de competência pode ter maior valorização no Sudeste do que no Norte, por exemplo.
- **Formalidade no Emprego:** A predominância de modelos como CLT ou PJ pode variar entre regiões, afetando a renda líquida e benefícios.
- **Demografia Regional:** A distribuição de perfis demográficos (gênero, raça, escolaridade) também não é uniforme, o que impacta oportunidades salariais.
- **Custo de Vida:** Salários nominais maiores no Sudeste podem ser compensados por custos de vida igualmente altos.

---

#### Considerações Analíticas

- **Disparidades Intra e Inter-Regionais:**  
  - Dentro da mesma região (ex: Sudeste), diferentes níveis de proficiência ou tipos de contrato podem gerar variações salariais relevantes.
  - Entre regiões, a mediana salarial para a mesma senioridade pode variar substancialmente.

- **Categoria “Desconhecida”:**  
  Pode valer a pena investigar se seus salários se assemelham aos de alguma região específica ou se compõem um grupo com características distintas.

>Em resumo: A forte concentração de profissionais no Sudeste pode influenciar de maneira significativa as médias salariais nacionais. Portanto, análises regionais segmentadas são fundamentais para entender as **disparidades salariais reais** no setor de dados no Brasil, considerando a **interação entre localização, qualificação técnica, tipo de contrato e perfil demográfico**.

---

# 6 Visualizacao dos dados (Análise Bivariada)

---

### Análise do Gráfico (Violin Plot)

![Histograma_sobreposto_salario](https://github.com/user-attachments/assets/7e26cf54-1306-4748-a3c1-7bcd87a12005)

---

#### O que o Gráfico Mostra

Este gráfico de violino compara a distribuição da variável `salary_numeric_lower_bound` (limite inferior da faixa salarial) entre duas categorias definidas em `faixa_salarial_eda_2cat`: **"Salário Baixo"** e **"Salário Alto"**.

- **Eixo Y (`salary_numeric_lower_bound`)**: Representa os valores do limite inferior da faixa salarial.  
- **Eixo X (`faixa_salarial_eda_2cat`)**: Mostra as duas categorias de agrupamento salarial.  
- **Forma do Violino**: Cada violino representa uma curva de densidade espelhada (KDE), indicando a distribuição de salários. A largura em um ponto indica a densidade de profissionais com aquele salário.

> **Observação**: Os violin plots geralmente contêm elementos internos como box plots com linha de mediana e quartis.

---

#### Informações Extraídas do Gráfico

**Distribuições Salariais Distintas**  
Como esperado, as categorias "Salário Baixo" e "Salário Alto" apresentam distribuições distintas:

- **Salário Baixo**:
  - Maior concentração de salários abaixo de R$ 10.000.
  - Violino mais largo em faixas salariais inferiores.
  - Mediana baixa.
  - Distribuição possivelmente multimodal com inchaços em faixas salariais específicas.

- **Salário Alto**:
  - Distribuição ampla, alcançando salários acima de R$ 40.000.
  - Mediana significativamente mais elevada.
  - Cauda longa com outliers.
  - Distribuição também multimodal, indicando subgrupos com diferentes níveis de alta remuneração.

**Disparidade Visualizada**  
O gráfico deixa clara a disparidade salarial entre os dois grupos definidos.

---

#### Conexão com a Pergunta Orientadora

**Como fatores como formalidade no emprego, características demográficas e regionais se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?**

---

#### Caracterizando os Grupos "Salário Baixo" e "Salário Alto"

1. **Proficiência Técnica**  
   - Espera-se maior proficiência (experiência, senioridade, habilidades avançadas) no grupo "Salário Alto".
   - Grupo "Salário Baixo" pode representar perfis iniciantes ou em transição de carreira.

2. **Formalidade no Emprego**  
   - Diferenças em tipo de contrato (CLT, PJ), setor e porte da empresa podem explicar parte da diferença entre os grupos.

3. **Características Regionais**  
   - Profissionais com "Salário Alto" tendem a se concentrar em regiões com mercados mais aquecidos (ex: Sudeste).
   - Pode haver variações regionais dentro de cada violino.

4. **Características Demográficas**  
   - Escolaridade, idade e outros fatores demográficos podem variar entre os grupos.  
   - Grupo com salários mais altos pode ter maior proporção de profissionais com pós-graduação.

---

#### Interação dos Fatores Dentro de Cada Categoria

Mesmo dentro de cada categoria ("Salário Alto" ou "Salário Baixo"), há variabilidade:

- **No grupo "Salário Alto"**:
  - Quem está na base do violino pode ter perfis diferentes de quem está no topo.
  - Diferenças regionais ou contratuais (ex: PJ no Norte vs. CLT no Sudeste).

- **No grupo "Salário Baixo"**:
  - Pode haver diferenças entre iniciantes e profissionais com perfil mais técnico porém com barreiras regionais ou contratuais.

---

#### Considerações Adicionais

- **Definição das Categorias**  
  Importante entender o critério para definir "Salário Baixo" e "Salário Alto" — isso impacta a análise.

- **Potencial para Modelagem**  
  Essas categorias podem ser usadas como variável-alvo em um modelo preditivo para entender quais fatores são determinantes para pertencer a cada grupo.

>Em resumo: O gráfico de violino evidencia de forma visual a segmentação dos profissionais entre duas grandes faixas salariais, servindo como ponto de partida para entender a disparidade salarial. O próximo passo da análise deve ser a decomposição desses grupos segundo:

- Proficiência técnica  
- Formalidade no emprego  
- Características regionais  
- Fatores demográficos  
---
### Análise do Gráfico (Gráfico de Barras Empilhadas)

![proporcao de faixa salarial](https://github.com/user-attachments/assets/b83c3e0c-6bcd-4409-b363-82aabd4607cf)

---

#### O que o Gráfico Mostra

Este gráfico de barras empilhadas 100% apresenta a **proporção de profissionais** nas categorias **"Salário Baixo"** e **"Salário Alto"** (definidas pela variável `faixa_salarial_eda_2cat`) em diferentes **faixas etárias** (`P1_a_1`).

- **Eixo Y (`P1_a_1`)**: Faixas etárias dos profissionais (ex: 25-29, 30-34, ..., 55+).
- **Eixo X (Porcentagem)**: Representa de 0% a 100% dos profissionais em cada faixa etária.
- **Legenda (`faixa_salarial_eda_2cat`)**:
  - **Amarelo (cor clara)**: Salário Baixo  
  - **Azul Marinho (cor escura)**: Salário Alto

Cada barra horizontal representa uma faixa etária, e a proporção de cada cor indica o percentual de profissionais naquela faixa que pertencem a cada grupo salarial.

---

#### Informações Extraídas do Gráfico

**Tendência Geral com a Idade**  
Há uma tendência clara: **quanto maior a faixa etária, maior a proporção de profissionais na categoria "Salário Alto"**.

- **Faixas Jovens (17-21, 22-24)**:
  - Predominância quase total de "Salário Baixo".
  - A faixa 22-24 possui um pequeno percentual em "Salário Alto", mas ainda muito reduzido.

- **Faixas Intermediárias (25-29, 30-34, 35-39)**:
  - Proporção de "Salário Alto" aumenta gradualmente.
  - Faixa 25-29: Cerca de 25% já em "Salário Alto".
  - Faixa 35-39: "Salário Alto" se aproxima (ou ultrapassa) 50%.

- **Faixas Maduras (40-44, 45-49, 50-54, 55+)**:
  - "Salário Alto" torna-se predominante.
  - Para "55+", mais de 60% já estão na categoria de alta remuneração.

- **Ponto de Virada**: A faixa de 35-44 anos parece marcar a transição para quando "Salário Alto" começa a superar "Salário Baixo".

---

#### Conexão com a Pergunta Orientadora

**Como fatores como idade, experiência, formalidade e características técnicas/demográficas influenciam as disparidades salariais entre profissionais de dados no Brasil?**

Este gráfico reforça o papel da **idade** (como **proxy de experiência/proficiência**) na explicação da **disparidade salarial**.

---

#### Idade como Indicador de Experiência e Impacto Salarial

- A forte correlação entre idade e "Salário Alto" confirma que:
  - Profissionais mais velhos → Mais experiência acumulada → Maior proficiência técnica → Maior probabilidade de estarem em faixas salariais elevadas.
  - Jovens → Menos tempo de carreira → Salários iniciais, frequentemente associados a cargos Júnior/Pleno.

---

#### Interação da Idade/Experiência com Outros Fatores

- **Formalidade no Emprego**:
  - Profissionais mais velhos podem ocupar cargos de gestão ou atuar como PJs altamente remunerados.

- **Características Regionais**:
  - A valorização da experiência pode variar conforme a região.
  - Mercados mais aquecidos (como Sudeste) podem oferecer melhores oportunidades salariais para profissionais experientes.

- **Educação**:
  - Profissionais mais maduros também podem ter investido mais em formação (pós-graduação, certificações), o que amplia as chances de alcançar salários altos.

---

#### Ciclo de Carreira e Remuneração

Este gráfico representa, visualmente, a progressão natural de carreira:

> Início com salários baixos → Crescimento com a experiência → Consolidação salarial em estágios mais avançados.

---

#### Disparidades Dentro da Mesma Faixa Etária

Mesmo dentro de faixas mais maduras (ex: 35-39), há divisão entre "Salário Baixo" e "Salário Alto", o que sugere que **idade/experiência não explicam tudo**.

Para entender as disparidades dentro da mesma faixa etária, é preciso investigar:

- **Proficiência Técnica Específica** (ex: habilidades em demanda, especializações).
- **Tipo de Contrato e Setor** (CLT vs. PJ, privado vs. público).
- **Região de Atuação**.
- **Educação e Certificações**.

>Em resumo: O gráfico **"Proporção de faixa_salarial_eda_2cat por P1_a_1 (Top 9)"** revela uma forte associação entre avanço da idade e maior probabilidade de estar na categoria "Salário Alto". Isso reforça a hipótese de que **experiência e proficiência acumulada** são fatores centrais nas disparidades salariais.
---
### Análise do Gráfico (Gráfico de Barras Agrupadas por Gênero)
![Contagem_faixa_salarial](https://github.com/user-attachments/assets/2518b56c-80b8-45fa-b1b6-6964c63b67f3)

---

#### O que o Gráfico Mostra

Este gráfico de barras apresenta a **contagem absoluta** de profissionais em cada faixa da variável `faixa_salarial_eda_2cat` ("Salário Baixo" e "Salário Alto") por **categoria de gênero** (`P1_b`).

- **Eixo Y (`P1_b`)**: Categorias de gênero ("Masculino", "Feminino", "Prefiro não informar", "Outro").
- **Eixo X (Contagem)**: Número de respondentes em cada combinação de gênero e faixa salarial.
- **Legenda (`faixa_salarial_eda_2cat`)**:
  - **Vermelho**: Salário Baixo  
  - **Azul/Cinza**: Salário Alto

Cada categoria de gênero possui duas barras (agrupadas ou sobrepostas), representando a quantidade de pessoas daquele gênero em cada faixa salarial.

---

#### Informações Extraídas do Gráfico

**Distribuição por Gênero e Faixa Salarial:**

- **Masculino**:
  - Maior número absoluto de respondentes.
  - Cerca de 2.400 homens estão na faixa de **Salário Baixo** e 1.200 em **Salário Alto**.
  - Proporcionalmente: ~1/3 dos homens estão em "Salário Alto".

- **Feminino**:
  - Número total significativamente menor que o masculino.
  - Cerca de 850 mulheres estão em **Salário Baixo** e 250 em **Salário Alto**.
  - Proporcionalmente: A fração de mulheres na faixa "Salário Alto" é **menor que a dos homens**, indicando possível desigualdade.

- **"Prefiro não informar" e "Outro"**:
  - Contagens muito pequenas (praticamente invisíveis no gráfico).
  - A maioria aparenta estar em "Salário Baixo".

---

#### Disparidade de Gênero Sugerida

O gráfico indica duas dimensões de possível desigualdade:

1. **Representatividade**:
   - Homens são maioria na amostra.
   - Mulheres e outras identidades de gênero aparecem em número muito inferior.

2. **Distribuição Salarial**:
   - Apesar de a maioria dos profissionais (de ambos os gêneros) estar em "Salário Baixo", **homens têm uma proporção maior em "Salário Alto"** do que mulheres.
   - Isso pode indicar **disparidade salarial de gênero** no setor de dados.

---

#### Conexão com a Pergunta Orientadora

> Como fatores como características demográficas (como gênero), formalidade no emprego e proficiência técnica influenciam as disparidades salariais entre profissionais de dados no Brasil?

Este gráfico contribui diretamente para essa investigação, ao evidenciar uma **diferença na distribuição de salários entre gêneros** — um ponto-chave para compreender disparidades estruturais.

---

#### Gênero como Fator nas Disparidades Salariais

- A **menor proporção de mulheres** em "Salário Alto" pode refletir uma combinação de fatores, como:
  - Menor tempo de mercado ou acesso limitado a oportunidades de progressão.
  - Diferenças na formalidade do emprego.
  - Barreiras estruturais e vieses de gênero no setor de tecnologia/dados.

---

#### Interações Possíveis a Serem Investigadas

1. **Proficiência Técnica e Experiência**:
   - As mulheres da amostra possuem, em média, menos anos de experiência?
   - Estão em cargos mais júnior?
   - Mesmo nível de proficiência técnica leva à mesma remuneração entre homens e mulheres?

2. **Formalidade no Emprego**:
   - Há diferenças significativas nos tipos de contrato (CLT vs PJ) entre gêneros?

3. **Características Regionais**:
   - A diferença de salários por gênero se mantém constante entre regiões?  
     Ou em algumas regiões a desigualdade é mais acentuada?

4. **Educação e Idade**:
   - Mulheres com o mesmo nível de formação e idade que os homens estão sendo remuneradas de forma equivalente?

---

#### Necessidade de Análise Proporcional e Controle de Variáveis

- Este gráfico mostra **contagens absolutas**, mas para compreender as **disparidades reais**, é necessário:
  - Calcular proporções dentro de cada gênero.
  - Utilizar **análises multivariadas** que controlem fatores como:
    - Experiência
    - Escolaridade
    - Região
    - Formalidade
    - Carga horária

Isso permitirá isolar o **efeito do gênero** sobre o salário.

---

#### Representatividade e Grupos Minoritários

- As categorias **"Prefiro não informar"** e **"Outro"** têm amostras muito pequenas, limitando a análise.
- A baixa resposta desses grupos pode refletir:
  - Falta de segurança para se identificar.
  - Invisibilidade estatística.
- Reforça a importância de promover **ambientes mais inclusivos** e **coletas mais sensíveis** a essas realidades.

>Em resumo: O gráfico **"Contagem de faixa_salarial_eda_2cat por P1_b (Top 4)"** sugere que:

- Existe uma **desigualdade de gênero** na **representação** e **distribuição de salários** entre profissionais de dados no Brasil.
- Mulheres são minoria e, dentro do grupo, **menos propensas a alcançar a faixa de "Salário Alto"**.
- Para compreender essa desigualdade, é necessário investigar:
  - Experiência e proficiência técnica
  - Tipo de contrato e setor
  - Região
  - Educação
- A **interação entre esses fatores** será essencial para entender por que, mesmo com idade ou experiência similares, homens e mulheres têm salários distintos.
---
### Análise do Gráfico (Gráfico de Barras Agrupadas: Senioridade por Escolaridade)

![Distribuicao de Senioridade](https://github.com/user-attachments/assets/b6cd4f6c-91cf-479f-a153-fd04f3ecb6d9)
---

#### O que o Gráfico Mostra

Este gráfico exibe a **contagem absoluta** de profissionais para diferentes níveis de senioridade (`P2_g`) dentro de cada categoria de nível de escolaridade (`P1_l`).

- **Eixo Y (`P1_l`)**: Níveis de escolaridade (ex.: Pós-graduação, Graduação/Bacharelado, Mestrado, Estudante de Graduação, Doutorado/PhD, Não tenho graduação formal, Prefiro não informar).
- **Eixo X (Contagem)**: Número de profissionais em cada combinação escolaridade × senioridade.
- **Legenda (`P2_g`)**: Cores indicando níveis de senioridade:
  - Azul Escuro: Sênior  
  - Azul Claro: Pleno  
  - Laranja Escuro: Júnior  
  - Laranja Claro: nan (não especificado/ausente)

Cada nível de escolaridade possui barras que indicam a distribuição dos profissionais pelos níveis de senioridade.

---

#### Informações Extraídas do Gráfico

- **Pós-graduação e Graduação/Bacharelado** são os níveis mais comuns, concentrando a maior parte dos profissionais em todos os níveis de senioridade.
- **Distribuição de Senioridade por Escolaridade**:
  - **Pós-graduação**: forte concentração nos níveis Sênior e Pleno, mas também presença considerável em Júnior e nan.
  - **Graduação/Bacharelado**: ampla distribuição em Sênior, Pleno e Júnior, com representação similar ou maior em nan comparada à Pós-graduação.
  - **Mestrado**: predominância em Sênior, Pleno e nan, menos em Júnior.
  - **Estudante de Graduação**: maioria em Júnior e nan, pouca ou nenhuma presença em Sênior.
  - **Doutorado ou PhD**: embora menos numerosos, proporcionalmente muitos estão em Sênior e Pleno; nan também relevante.
  - **Não tenho graduação formal / Prefiro não informar**: pequenas contagens, maior concentração em Júnior e nan.

- **Categoria "nan" (Senioridade)** aparece em todos os níveis, especialmente em Pós-graduação, Graduação/Bacharelado e Mestrado, indicando necessidade de investigar quem são esses profissionais (ex: consultores, autônomos, gestores).

---

#### Conexão com a Pergunta Orientadora (Disparidades Salariais)

- O gráfico relaciona escolaridade (característica demográfica) com senioridade (proxy para proficiência técnica/experiência), ambos fatores chave que impactam salário.
- Níveis educacionais mais elevados (Pós, Mestrado, Doutorado) tendem a se associar a níveis mais altos de senioridade (Sênior e Pleno), sugerindo que educação avançada pode facilitar posições de maior responsabilidade e remuneração.
- Contudo, profissionais com apenas graduação também alcançam senioridade elevada, indicando que experiência e outros fatores são relevantes.

---

#### Interações e Implicações para Disparidades Salariais

- **Proficiência Técnica Específica**: Salários podem variar dentro de mesmo nível educacional e senioridade, dependendo da especialização e habilidades.
- **Formalidade no Emprego**: Tipo de contrato e setor podem influenciar salários mesmo para profissionais similares em escolaridade/senioridade.
- **Características Regionais**: O valor salarial da escolaridade e senioridade pode variar por região do Brasil.
- **Idade e Experiência**: Escolaridade interage com tempo de experiência — um Doutorado com pouca experiência pode ter remuneração diferente de um graduado experiente.

---

#### Considerações Importantes

- O prêmio salarial da educação formal avançada deve ser analisado controlando senioridade e experiência.
- A presença expressiva da categoria "nan" em senioridade, principalmente em níveis altos de escolaridade, sugere perfis diversos que merecem análise detalhada (ex: autônomos, gestores).
- Análises posteriores devem comparar salários para combinações específicas (ex: Sênior com graduação vs. Sênior com pós-graduação) para quantificar impacto real.

>Em resumo: O gráfico **"Distribuição de senioridade (P2_g) por escolaridade (P1_l)"** mostra que:

- Senioridade ocorre em todos os níveis educacionais, mas níveis mais altos de escolaridade concentram profissionais em níveis superiores (Sênior e Pleno).
- Esta interação entre educação e senioridade é fundamental para compreender as disparidades salariais no setor de dados.
- A análise salarial deve aprofundar-se nas diferenças dentro desses grupos para entender o impacto isolado da escolaridade e da senioridade.

---

# 7 Visualizacao dos dados (Análise multivariada)

### Análise do Gráfico de Dispersão: Experiência vs. Limite Inferior do Salário por Nível de Senioridade

![Experiencia vs Salario por nivel de senioridade](https://github.com/user-attachments/assets/cf0500fa-2de4-44c6-8e5d-f6d040b2fed1)

---

#### O que o Gráfico Mostra

- **Variáveis representadas:**
  - Eixo X: Anos de Experiência
  - Eixo Y: Limite Inferior do Salário
- **Cores indicam o Nível de Senioridade (`P2_g`):**
  - Verde Claro: Sênior
  - Verde Azulado/Turquesa: Pleno
  - Azul Escuro/Roxo: Júnior
  - Cinza/Azul muito escuro: nan (não especificado/ausente)
- Cada ponto representa um profissional, mostrando sua experiência, salário mínimo estimado e senioridade.

---

#### Informações Extraídas do Gráfico

- **Tendência geral positiva:**  
  Salários tendem a aumentar com o crescimento da experiência.
  
- **Dispersão salarial ampla:**  
  Para um mesmo número de anos de experiência, salários podem variar bastante, indicando que experiência sozinha não explica tudo.

- **Distribuição por senioridade:**
  - **Júnior:** Concentrados em experiências baixas (0-4 anos) e salários baixos (muitos abaixo de R$5.000, quase todos abaixo de R$10.000).
  - **Pleno:** Abrangem faixa intermediária de experiência (0-10 anos, concentração em 1-7 anos) e salários (até cerca de R$15.000–R$20.000). Sobreposição significativa com Júnior em experiência baixa e com Sênior em experiência alta.
  - **Sênior:** Geralmente mais experientes (a partir de 2-3 anos), dominando os salários mais altos (acima de R$10.000, chegando a R$40.000). Presentes em quase toda faixa de experiência, exceto zero absoluto.
  - **nan:** Dispersos em vários níveis, frequentemente sobrepostos a Júnior e Pleno em salários baixos e médios, indicando grupo heterogêneo.

- **Salários máximos:**
  - Faixa alta (R$30.000–R$40.000) quase exclusivamente de Sêniores, com experiência variando bastante (3-4 anos a mais de 10 anos).

- **Casos notáveis:**
  - Alguns profissionais com pouca experiência (0-2 anos) alcançam salários altos, especialmente se Pleno ou Sênior, sugerindo rápida progressão, habilidades muito demandadas ou critérios internos de senioridade flexíveis.

---

#### Conexão com a Pergunta Orientadora (Disparidades Salariais)

- **Experiência e senioridade como fatores principais:**  
  Ambos são fortes determinantes dos salários, com combinação mais alta em experiência e senioridade resultando em maiores remunerações.

- **Variabilidade dentro de mesma experiência:**  
  A dispersão vertical mostra que experiência isolada não explica disparidades; senioridade adiciona uma camada explicativa importante.

- **Interação experiência-senioridade:**  
  Relação não perfeita — há Júniores com vários anos e Sêniores com relativamente poucos anos, indicando que critérios de senioridade são influenciados por outros fatores além do tempo.

---

#### Influência de Outros Fatores (implícitos)

- **Formalidade no emprego:**  
  Regimes PJ, CLT, empresas grandes e pequenas afetam salários mesmo para profissionais similares.

- **Região geográfica:**  
  Mercados regionais podem valorizar experiência e senioridade de forma diferente.

- **Características demográficas e educacionais:**  
  Escolaridade, gênero, idade influenciam salários além de experiência e senioridade.

- **Especialização técnica:**  
  Habilidades específicas (ex.: IA, Big Data, linguagens) impactam fortemente remuneração.

---

#### Pontos para Investigar

- **Sêniores com pouca experiência e alto salário:**  
  O que explica essa combinação? Educação, setor, empresa, região?

- **Júniores/Plenos com experiência e salário baixos:**  
  Barreiras regionais, setoriais ou formais que limitam progressão?

- **Perfil e impacto dos "nan":**  
  Grupo heterogêneo que pode incluir autônomos, consultores ou iniciantes sem classificação definida.

>Em resumo: O gráfico evidencia a complexa interação entre:

- **Anos de experiência (proxy para proficiência técnica)**
- **Nível de senioridade (proxy para proficiência e posição)**
- **Salário**

Essa tríade é central para compreender disparidades salariais, mas as variações dentro de níveis semelhantes indicam a necessidade de considerar fatores adicionais para explicar plenamente os diferentes padrões salariais observados.

---

### Análise do Gráfico de Dispersão: Experiência vs. Limite Inferior do Salário  

![Experiencia vs Salario por nivel de ensino e faixa salarial](https://github.com/user-attachments/assets/f474a8f4-8245-4b02-9f80-f4650fbc7eb4)

---

#### O que o Gráfico Mostra

- **Eixo X:** Anos de Experiência  
- **Eixo Y:** Limite Inferior do Salário  
- **Cores:**  
  - Vermelho = Faixa Salarial Alta ("Salário Alto")  
  - Azul = Faixa Salarial Baixa ("Salário Baixo")  
- **Formas (Marcadores):** Diferenciam o Nível de Ensino (P1_l)  
  - Pós-graduação, Graduação/Bacharelado, Mestrado, Estudante de Graduação  
- **Legenda:** Explica as cores e as formas usadas.

---

#### Informações Extraídas

- **Separação clara por faixa salarial:**  
  Pontos vermelhos concentram-se na parte superior (salários altos), azuis na inferior (salários baixos).

- **Tendência geral:**  
  Salários maiores tendem a se associar a mais anos de experiência, mas há grande variabilidade.

- **Distribuição do nível de ensino dentro das faixas salariais:**

  - **Faixa Salário Baixo (Azul):**  
    - Presentes em toda faixa de experiência.  
    - Todos os níveis de ensino aparecem, incluindo pós-graduação e mestrado, especialmente em níveis iniciais de experiência.  
    - Estudantes de graduação quase exclusivos dessa faixa e com pouca experiência (0-3 anos).  
    - Pós-graduação e mestrado aparecem aqui, mostrando que a educação avançada isolada não garante salários altos, principalmente no começo da carreira.

  - **Faixa Salário Alto (Vermelho):**  
    - Geralmente profissionais com mais experiência, mas há pontos com 0-2 anos.  
    - Graduação/Bacharelado já pode levar a faixa alta em vários níveis de experiência.  
    - Pós-graduação e mestrado fortemente representados em toda a faixa de experiência, especialmente entre os salários mais altos.  
    - Estudantes de graduação praticamente ausentes nesta faixa.

- **Educação e teto salarial:**  
  Profissionais com pós-graduação e mestrado aparecem em maior proporção nas faixas salariais mais elevadas (ex: R$30.000 - R$40.000), embora graduados também alcancem esses patamares.

- **Salários altos com pouca experiência:**  
  Indivíduos com graduação, pós-graduação ou mestrado e poucos anos de experiência que já recebem salários altos indicam aceleração possível por educação, demanda de mercado ou outras vantagens.

---

#### Conexão com a Pergunta Orientadora (Disparidades Salariais)

- **Educação como potencializadora:**  
  Para mesma experiência, níveis educacionais mais altos aumentam a probabilidade de estar na faixa de salário alto.

- **Experiência ainda essencial:**  
  Salários muito altos tendem a requerer também alguns anos de experiência.

- **Presença de pós-graduados e mestres em faixa salarial baixa:**  
  Educação avançada não garante salário alto imediato — fatores adicionais entram em jogo.

---

#### Fatores Adicionais (não visíveis no gráfico, mas sugeridos pela dispersão)

- **Proficiência técnica e qualidade da experiência:** Relevância e especialização das habilidades.  
- **Formalidade no emprego:** Tipo de contrato, porte e setor da empresa.  
- **Características regionais:** Diferenças salariais regionais significativas.  
- **Demografia:** Gênero, idade e senioridade interagem com experiência e educação.

---

#### Implicações para Disparidades Salariais

- Disparidades são resultado da interação complexa entre experiência, nível de ensino e outros fatores.  
- Educação avançada pode acelerar a entrada em faixas salariais altas, mas não é suficiente isoladamente.  
- Profissionais com formação sólida podem permanecer em faixas baixas por motivos ligados a local de trabalho, contrato, região, entre outros.  
- Profissionais com pouca experiência e salário alto provavelmente atuam em nichos muito demandados ou têm diferenciais específicos.

>Em resumo: O gráfico revela como **experiência e nível de ensino** interagem para moldar a faixa salarial dos profissionais de dados no Brasil.  
Apesar da experiência ser um fator crucial, níveis mais elevados de escolaridade (pós-graduação, mestrado) facilitam o acesso a salários mais altos, especialmente quando combinados com experiência.  
No entanto, a ampla dispersão e a presença de todas as formações em ambas as faixas salariais indicam que variáveis adicionais, como proficiência técnica específica, formalidade no emprego, região e outras características demográficas, são fundamentais para compreender plenamente as disparidades salariais observadas.

---
### Análise do Gráfico de Boxplots: Limite Inferior do Salário por Nível de Ensino e Faixa Salarial (Alvo)

![Salario por nivel de ensino e faixa salarial](https://github.com/user-attachments/assets/03c2160b-f21f-442b-ab0d-d5b31d3292da)

---

#### O que o Gráfico Mostra

- **Eixo X:** Nível de Ensino (P1_l)  
- **Eixo Y:** Limite Inferior do Salário  
- Para cada nível de ensino, há dois boxplots lado a lado, correspondendo a:  
  - **Vermelho:** Faixa "Salário Baixo"  
  - **Azul:** Faixa "Salário Alto"  
- Cada boxplot exibe mediana, quartis (Q1, Q3), hastes (whiskers) e outliers da distribuição salarial naquela combinação.

---

#### Informações Extraídas

- **Separação clara por faixa salarial:**  
  Boxplots vermelhos ("Salário Baixo") apresentam níveis salariais significativamente mais baixos que os azuis ("Salário Alto") em todos os níveis de ensino, validando a variável "Faixa Salarial (Alvo)".

- **Distribuição para "Salário Baixo":**  
  - Medianas geralmente próximas de R$ 5.000 para Pós-graduação, Graduação, Mestrado, Doutorado.  
  - Estudantes de Graduação possuem a mediana mais baixa, refletindo salários de entrada ou estágio.  
  - Indivíduos sem graduação formal ou que preferem não informar mostram medianas baixas, com alguma variabilidade.

- **Distribuição para "Salário Alto":**  
  - Medianas tipicamente entre R$ 15.000 e R$ 20.000 para os níveis mais comuns (Pós-graduação, Graduação, Mestrado, Doutorado).  
  - Mestrado e Doutorado apresentam medianas ligeiramente superiores, com maior dispersão indicando maior variabilidade salarial.  
  - Estudantes de Graduação têm boxplot azul achatado com poucos dados, indicando que poucos alcançam essa faixa alta — provavelmente dados pouco representativos.  
  - Pessoas sem graduação formal ou que preferem não informar mostram medianas elevadas e grande dispersão, mas o baixo número de casos pode influenciar.

- **Outliers:**  
  Presentes especialmente nos boxplots de "Salário Alto" para níveis mais comuns, sugerindo profissionais que atingem salários excepcionalmente altos.

---

#### Conexão com a Pergunta Orientadora (Disparidades Salariais)

- **Educação e remuneração:**  
  Níveis de ensino mais elevados estão associados a medianas salariais maiores dentro da faixa "Salário Alto", indicando que educação formal facilita acesso a salários mais altos.

- **Pouca variação entre níveis na faixa "Salário Baixo":**  
  Isso sugere que, para salários menores, o nível de escolaridade formal é menos determinante, e outros fatores podem ter papel mais relevante.

- **Dispersão maior na faixa "Salário Alto":**  
  Indica que, ao alcançar patamares salariais altos, a educação pode definir um piso salarial, mas outras variáveis (experiência, senioridade, setor, localização) são fundamentais para a variação salarial dentro desse grupo.

---

#### Considerações sobre Casos Atípicos

- "Salário Alto" para estudantes ou sem graduação formal podem ser casos reais de profissionais com alta proficiência técnica, habilidades diferenciadas, ou empreendedorismo, mas o baixo número desses casos torna as inferências cautelosas.

---

#### Interação entre Educação e Proficiência Técnica

- A educação formal atua como base para o desenvolvimento profissional, mas o avanço salarial até níveis elevados depende também de proficiência técnica adquirida via experiência e aprendizado contínuo.

>Em resumo: O gráfico confirma que a educação formal é um fator importante para o alcance da faixa de "Salário Alto" e está associada a medianas salariais maiores.  
Porém, a significativa variabilidade salarial dentro de cada nível de ensino — mesmo segmentada pela faixa salarial — indica que fatores como experiência, senioridade, formalidade no emprego e características regionais são essenciais para explicar as disparidades salariais entre profissionais de dados no Brasil.  
A educação pode garantir um “piso” mais alto para salários, mas não determina sozinha o teto salarial.

---
### Análise do Gráfico de Violin Plots Divididos: Experiência (anos) por Nível de Senioridade e Faixa Salarial (Alvo)

![Experiencia por seneridade e faixa salarial (Alvo)](https://github.com/user-attachments/assets/7cb4de01-50f5-439c-9baa-42b91cdb7a58)

---

#### O que o Gráfico Mostra

- **Eixo X:** Nível de Senioridade (P2_g) — Sênior, Pleno, Júnior, nan (não especificado).  
- **Eixo Y:** Experiência (anos).  
- Cada violino está dividido verticalmente em duas metades:  
  - **Vermelho (esquerda):** Distribuição da experiência para profissionais na faixa "Salário Baixo".  
  - **Azul (direita):** Distribuição da experiência para profissionais na faixa "Salário Alto".  
- A largura do violino em determinado ponto indica a densidade de profissionais com aquela experiência.

---

#### Informações Extraídas

- **Júnior:**  
  - Salário Baixo: Maioria concentrada entre 0 e 2-3 anos de experiência, com alta densidade em níveis muito baixos.  
  - Salário Alto: Poucos Júniores, com experiência ligeiramente maior (2-4 anos), porém baixa densidade, indicando raridade desse caso.

- **Pleno:**  
  - Salário Baixo: Distribuição ampla até 5-6 anos, com picos entre 1-3 anos.  
  - Salário Alto: Distribuição deslocada para mais experiência (3-7 anos), mostrando que mais experiência é necessária para atingir salário alto nesta senioridade.

- **Sênior:**  
  - Salário Baixo: Grupo menor, concentrado entre 2-6 anos de experiência.  
  - Salário Alto: Distribuição ampla, de 3-4 até 10+ anos, com densidade maior em experiências elevadas.

- **nan (senioridade não informada):**  
  - Ambos os grupos apresentam ampla variação em anos de experiência, com tendência de maior experiência para o grupo de salário alto, mas heterogeneidade alta.

---

#### Tendências e Interpretações

- Para cada nível de senioridade, a distribuição azul ("Salário Alto") tende a deslocar-se para mais anos de experiência e maior densidade em faixas elevadas, em comparação com a distribuição vermelha ("Salário Baixo").  
- Isso reforça que, mesmo com o mesmo título de senioridade, mais experiência costuma estar associada a salários mais altos.  
- A progressão natural da carreira reflete-se: Júniores com pouca experiência geralmente ganham salários baixos; para Plenos e Seniores, experiência crescente é correlacionada com faixas salariais elevadas.

---

#### Conexão com a Pergunta Orientadora (Disparidades Salariais)

- **Experiência como diferencial dentro da senioridade:**  
  O gráfico destaca que o título de senioridade por si só não explica as diferenças salariais. A profundidade da experiência (anos no campo) é fundamental para compreender a faixa salarial dentro de cada nível.

- **Interação Proficiência Técnica e Salário:**  
  Anos de experiência e reconhecimento formal (senioridade) juntos explicam grande parte das disparidades salariais observadas.

- **Fatores adicionais para variações restantes:**  
  - **Formalidade no emprego:** Contrato CLT, PJ, setor e tamanho da empresa impactam salários.  
  - **Características regionais:** Mercado local, custo de vida e demanda influenciam remuneração.  
  - **Demografia e formação:** Gênero, raça, nível de educação e suas interações com o mercado.  
  - **Qualidade da experiência:** Tecnologias, responsabilidades e escopo de atuação, que não são capturados só por anos ou título.

- **Grupo nan:**  
  Alta heterogeneidade sugere perfis diversos, possivelmente freelancers ou profissionais fora das classificações tradicionais.

>Em resumo: O gráfico "Experiência por Senioridade e Faixa Salarial" evidencia que, dentro de cada título profissional, mais anos de experiência tendem a associar-se a salários mais altos, reforçando a importância da proficiência técnica aprofundada.  
As diferenças que permanecem após controlar senioridade e experiência apontam para a necessidade de incluir análise de formalidade no emprego, fatores regionais e demográficos para compreender plenamente as disparidades salariais no setor de dados brasileiro.

---

# Análise do Gráfico "Nível de Ensino por Região e Faixa Salarial (Alvo)"
![Nivel de ensino por regiao e faixa salarial (alvo)](https://github.com/user-attachments/assets/65516cef-91cd-4308-a150-582c26d0bb50)

---

## O que o Gráfico Mostra:

Este gráfico consiste em múltiplos subplots, cada um representando uma região do Brasil (Sudeste, Sul, Nordeste, Centro-Oeste).  
A região Norte e "Desconhecida" não aparecem nestes subplots, provavelmente devido a um menor número de respondentes ou por decisão de focar nas regiões com mais dados.  
Dentro de cada subplot regional, são exibidas barras horizontais que mostram a contagem de profissionais para diferentes Níveis de Ensino (P1_l).  
Cada barra de nível de ensino é dividida (ou acompanhada) por cores que representam a faixa_salarial_eda_2cat ("Salário Baixo" em vermelho e "Salário Alto" em azul).  
Eixo Y (Comum aos subplots, implícito dentro de cada um): Nível de Ensino (P1_l) (Pós-graduação, Graduação/Bacharelado, Mestrado, Estudante de Graduação, Doutorado ou Phd).  
Eixo X (Dentro de cada subplot): Contagem de profissionais.  
Legenda (Comum ao gráfico geral):  
- Vermelho: "Salário Baixo"  
- Azul: "Salário Alto"  

## Interpretação:

Para cada região, pode-se observar quantos profissionais de cada nível de ensino se enquadram na faixa de "Salário Baixo" versus "Salário Alto".

## Informações Extraídas do Gráfico (Comparando as Regiões):

- **Predominância da Região Sudeste:**  
O eixo X da contagem para o Sudeste vai até valores muito mais altos (ex: 1000) em comparação com as outras regiões (Sul até ~400, Nordeste e Centro-Oeste até ~200 ou menos), refletindo a maior concentração de profissionais nesta região, como visto em gráficos anteriores.

- **Padrão Geral (Salário Baixo vs. Salário Alto por Escolaridade):**  
Em todas as regiões, para a maioria dos níveis de ensino, a contagem de profissionais em "Salário Baixo" (vermelho) é geralmente maior ou comparável à de "Salário Alto" (azul).  
Estudantes de Graduação: Consistentemente, em todas as regiões, estão quase que exclusivamente na faixa de "Salário Baixo". A barra azul para "Salário Alto" é inexistente ou minúscula.  
Graduação/Bacharelado e Pós-graduação: São os níveis de ensino com maior número de profissionais em todas as regiões. Em ambos, há representação tanto em "Salário Baixo" quanto em "Salário Alto".

- **Diferenças Regionais na Proporção Salário Alto/Baixo (Análise Visual Aproximada):**  
Sudeste: Para Pós-graduação e Graduação/Bacharelado, embora a contagem absoluta em "Salário Baixo" seja alta, a contagem em "Salário Alto" (azul) também é muito significativa. A proporção de profissionais com Pós-graduação em "Salário Alto" parece ser relativamente boa. Para Mestrado e Doutorado, a barra azul ("Salário Alto") é proeminente, muitas vezes superando ou igualando a vermelha, apesar das contagens absolutas serem menores.  
Sul: O padrão é similar ao Sudeste, mas com contagens menores. Para Pós-graduação e Graduação, há uma boa representação em "Salário Alto". Mestrado e Doutorado também mostram uma tendência a "Salário Alto", proporcionalmente.  
Nordeste: As barras azuis ("Salário Alto") são visivelmente menores em comparação com as vermelhas ("Salário Baixo") para a maioria dos níveis de ensino, mesmo para Pós-graduação e Graduação. Proporcionalmente, parece haver uma menor chance de estar na faixa de "Salário Alto" nesta região em comparação com Sudeste e Sul para um mesmo nível de escolaridade.  
Centro-Oeste: Similar ao Nordeste, as contagens em "Salário Alto" são mais modestas. Para Pós-graduação e Graduação, a barra vermelha é dominantemente maior que a azul.

- **Impacto do Mestrado e Doutorado:**  
Em regiões como Sudeste e Sul, ter Mestrado ou Doutorado parece estar mais consistentemente associado à faixa de "Salário Alto" (barras azuis proporcionalmente grandes ou maiores que as vermelhas).  
Nas regiões Nordeste e Centro-Oeste, o número absoluto de profissionais com Mestrado/Doutorado é menor, mas aqueles que existem também tendem a estar em "Salário Alto", embora a oportunidade geral pareça mais restrita.

## Conexão com a Pergunta Orientada a Dados (Disparidades Salariais):

- **Região como Moduladora do Retorno da Educação:**  
Fica claro que o "retorno" salarial (chance de estar em "Salário Alto") para um determinado nível de ensino não é o mesmo em todas as regiões. Profissionais com Pós-graduação no Sudeste ou Sul parecem ter uma probabilidade maior de alcançar salários altos do que seus pares com a mesma formação no Nordeste ou Centro-Oeste.  
Isso sugere que o mercado de trabalho regional (demanda por qualificações, tipos de indústrias presentes, custo de vida e capacidade de pagamento das empresas) influencia significativamente o valor atribuído à educação formal.

- **Interação com Proficiência Técnica (Implícita):**  
Embora a proficiência técnica (experiência, senioridade, habilidades específicas) não esteja explicitada neste gráfico, ela interage com a educação e a região. Por exemplo, a disponibilidade de vagas que exigem alta proficiência (e pagam mais) pode ser maior no Sudeste, beneficiando aqueles com alta escolaridade e experiência relevante naquela região.  
Pode ser que, para atingir "Salário Alto" no Nordeste ou Centro-Oeste com um diploma de Graduação, seja necessário um nível de proficiência técnica/experiência ainda maior do que no Sudeste, ou que as oportunidades simplesmente sejam mais escassas.

- **Formalidade no Emprego (Implícita):**  
A natureza das vagas (CLT, PJ, tamanho da empresa, setor) também varia regionalmente e pode interagir com a escolaridade. Regiões com mais empresas de grande porte ou setores tecnológicos podem oferecer mais vagas formais com salários mais altos para profissionais qualificados.

- **Disparidades Salariais Explicadas pela Interação:**  
Um profissional com Pós-graduação (demografia/educação) trabalhando no Sudeste (região) tem um perfil de chance salarial diferente de um com a mesma Pós-graduação no Nordeste.  
Para entender completamente a disparidade, precisaríamos adicionar a camada de proficiência técnica (quantos anos de experiência tem o pós-graduado no Sudeste vs. Nordeste para estar em "Salário Alto"?) e a formalidade do emprego.

- **Concentração de Oportunidades:**  
A maior contagem de profissionais em "Salário Alto" (barras azuis) no Sudeste e Sul, em diversos níveis de escolaridade, sugere uma maior concentração de oportunidades de alta remuneração nessas regiões.

>Em resumo: O gráfico "Nível de Ensino por Região e Faixa Salarial (Alvo)" é fundamental para ilustrar que a região é um fator crucial que interage com o nível de ensino para influenciar a probabilidade de um profissional de dados alcançar uma faixa salarial mais alta.  
As disparidades salariais no Brasil para profissionais de dados não podem ser entendidas sem considerar o contexto regional, que modula o valor da educação e, provavelmente, da proficiência técnica.  
Para uma análise mais completa, seria ideal cruzar esses dados também com a experiência/senioridade e a formalidade do emprego dentro de cada combinação de região e nível de ensino.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Indução de modelos

*   [1º Pergunta orientada a dados ](#modelo-1-análise-de-disparidade-salarial-de-profissionais-de-dados-no-brasil-utilizando-o-modelo-random-forest)
  
	*   [Modelo 1 Análise de Disparidade Salarial de Profissionais de Dados no Brasil Utilizando o Modelo Random Forest](#modelo-1-análise-de-disparidade-salarial-de-profissionais-de-dados-no-brasil-utilizando-o-modelo-random-forest)
  
		*   [Justificativa1.1](#justificativa1-1)
		*   [Processo de Amostragem de Dados (Particionamento e Cross-Validation1.1)](#processo-de-amostragem-de-dados1-1)
		*   [Parâmetros utilizados1.1](#parâmetros-utilizados1-1)
		*   [Explicação do Código1.1](#explicação-do-código1-1)

	*   [Modelo 1 Análise de Disparidade Salarial de Profissionais de Dados no Brasil Utilizando o Arvore de decisão por classificação](#modelo-1-análise-de-disparidade-salarial-de-profissionais-de-dados-no-brasil-utilizando-o-arvore-de-decisão-por-classificação)
  
		*   [Justificativa1.2](#justificativa1-2)
		*   [Processo de Amostragem de Dados (Particionamento e Cross-Validation1.2)](#processo-de-amostragem-de-dados1-2)
		*   [Parâmetros utilizados1.2](#parâmetros-utilizados1-2)
		*   [Explicação do Código1.2](#explicação-do-código1-2)

 
*   [2º Pergunta orientada a dados ](#modelo-2)

*   [3º Pergunta orientada a dados ](#modelo-3)


## 1º Pergunta orientada a dados
### Modelo 1 Análise de Disparidade Salarial de Profissionais de Dados no Brasil Utilizando o Modelo Random Forest
### *Justificativa1-1*

### - Capacidade de Capturar Interações Complexas:

### - Fornecimento de Importância das Features:

### - Robustez e Generalização:

### - Bom Desempenho em Problemas de Classificação:

### - Manejo de Features Categóricas e Numéricas:

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



### *Processo de Amostragem de Dados1-1*


### *Parâmetros utilizados1-1*


 ### *Explicação do Código1-1*


**Etapa 0: Configuração Inicial**
   
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, roc_curve, auc, balanced_accuracy_score, f1_score, precision_recall_curve
from sklearn.calibration import CalibratedClassifierCV
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import seaborn as sns
import os



**Importações das bibliotecas essenciais:**

- pandas e numpy: Manipulação e processamento de dados

- sklearn: Ferramentas de machine learning, incluindo divisão de dados, algoritmos, métricas e calibração

- matplotlib e seaborn: Visualização de dados e gráficos

- os: Operações do sistema operacional para criação de diretórios

# Criar diretório para salvar os gráficos, se não existir

    output_dir = '/kaggle/working/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

**Configuração do diretório de saída para salvar os gráficos gerados. O código verifica se o diretório existe e o cria caso necessário.**


# Configurar o estilo dos gráficos para melhor visualização
    
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['axes.labelsize'] = 14

**Configuração global dos gráficos estabelecendo um estilo consistente com:**

- Estilo seaborn: Grade branca para melhor visualização

- Tamanho padrão: 12x8 polegadas

- Fontes: Tamanhos diferenciados para títulos (16), labels (14) e texto geral (12)

# Etapa 1: Carregamento e Pré-processamento dos Dados

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
            exit()

**Sistema de carregamento robusto que tenta múltiplos caminhos:**

- Primeiro: Caminho do Kaggle para execução na plataforma

- Segundo: Caminho local para desenvolvimento

- Tratamento de erro: Mensagem informativa e encerramento seguro se o arquivo não for encontrado

        colunas_features = [
            'Nível de ensino alcançado', 
            'Tempo de experiência na área de dados',
            'Área de formação acadêmica',
            'Nível de senioridade',
            'UF onde mora',
            'Setor de atuação da empresa'
        ]
        coluna_target = 'Faixa salarial mensal'
        colunas_necessarias = colunas_features + [coluna_target]


**Definição das variáveis do modelo expandindo significativamente o conjunto de features em relação a versões anteriores:**

- Features ordinais: Nível de ensino, experiência e senioridade

- Features categóricas: Área de formação, localização geográfica e setor empresarial

- Target: Faixa salarial mensal para classificação binária

        df_limpo = df[colunas_necessarias].copy()
        df_limpo.dropna(subset=colunas_necessarias, inplace=True)

**Limpeza inicial dos dados removendo registros com valores ausentes nas colunas cruciais para garantir qualidade dos dados de entrada.**

# Etapa 2: Engenharia de Features e Criação da Variável Alvo

    nivel_ensino_map = {
        'Estudante de Graduação': 0,
        'Graduação/Bacharelado': 1,
        'Pós-graduação': 2,
        'Mestrado': 3,
        'Doutorado ou Phd': 4
    }
    df_limpo['formacao_academica_encoded'] = df_limpo['Nível de ensino alcançado'].map(nivel_ensino_map)

Mapeamento ordinal para nível educacional criando uma escala numérica que preserva a hierarquia natural dos níveis de formação acadêmica, onde valores maiores representam maior qualificação.
    
    experiencia_map = {
        'Menos de 1 ano': 0,
        'de 1 a 2 anos': 1,
        'de 3 a 4 anos': 2,
        'de 4 a 6 anos': 3,
        'de 5 a 6 anos': 3, 
        'de 7 a 10 anos': 4,
        'Mais de 10 anos': 5
    }
    df_limpo['experiencia_profissional_encoded'] = df_limpo['Tempo de experiência na área de dados'].map(experiencia_map)

Codificação ordinal da experiência profissional com tratamento especial para sobreposições nas faixas (como "de 4 a 6 anos" e "de 5 a 6 anos" recebendo o mesmo valor 3).

    senioridade_map = {
        'Júnior': 0,
        'Pleno': 1,
        'Sênior': 2
    }
    df_limpo['senioridade_encoded'] = df_limpo['Nível de senioridade'].map(senioridade_map)

Mapeamento do nível de senioridade seguindo a progressão natural da carreira em tecnologia.

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

Codificação ordinal detalhada das faixas salariais criando uma escala numérica de 0 a 12 que preserva a ordem crescente dos valores monetários.

    df_limpo['salario_alto'] = df_limpo['faixa_salarial_encoded'].apply(lambda x: 1 if x > 5 else 0)

**Criação da variável alvo binária definindo o ponto de corte em R$ 8.000 (valor 5 na escala ordinal):**

- 0: Salários até R$ 8.000 (baixo/médio)

- 1: Salários acima de R$ 8.000 (alto)

        df_encoded = pd.get_dummies(df_limpo, columns=['Área de formação acadêmica', 'UF onde mora', 'Setor de atuação da empresa'])

Codificação one-hot para variáveis categóricas transformando variáveis categóricas nominais em múltiplas variáveis binárias, permitindo que o modelo capture diferentes padrões para cada categoria.

    X_columns = ['formacao_academica_encoded', 'experiencia_profissional_encoded', 'senioridade_encoded'] + \
                [col for col in df_encoded.columns if col.startswith(('Área de formação acadêmica_', 
                                                                     'UF onde mora_', 
                                                                     'Setor de atuação da empresa_'))]
    X = df_encoded[X_columns]
    y = df_encoded['salario_alto']

Seleção final das features combinando variáveis ordinais codificadas com variáveis dummy criadas pelo one-hot encoding.

# Etapa 3: Validação e Balanceamento dos Dados
    
    if X.shape[0] < 10 or len(y.unique()) < 2:
        print("Não há dados suficientes ou classes suficientes após o pré-processamento para treinar o modelo.")
        print(f"Tamanho de X: {X.shape}, Classes em y: {y.unique()}")
        exit()

Verificação de viabilidade do modelo garantindo que existem dados suficientes e ambas as classes estão representadas.

    class_counts = y.value_counts()
    print("\nDistribuição das classes:")
    print(f"Salário Baixo/Médio (0): {class_counts[0]} ({class_counts[0]/len(y)*100:.2f}%)")
    print(f"Salário Alto (1): {class_counts[1]} ({class_counts[1]/len(y)*100:.2f}%)")

Análise do balanceamento das classes exibindo a distribuição para identificar possível desbalanceamento que pode afetar o desempenho do modelo.


    class_weights = {0: 1.0, 1: class_counts[0] / class_counts[1]}
    sample_weights = np.array([class_weights[cls] for cls in y])

Cálculo de pesos para balanceamento criando pesos inversamente proporcionais à frequência das classes para compensar desbalanceamento sem usar técnicas de reamostragem como SMOTE.

    X_train, X_test, y_train, y_test, sample_weights_train, _ = train_test_split(
        X, y, sample_weights, test_size=0.3, random_state=42, stratify=y
    )

Divisão estratificada dos dados mantendo a proporção das classes nos conjuntos de treino e teste, incluindo os pesos calculados.

# Etapa 4: Desenvolvimento do Modelo com Otimização de Hiperparâmetros

    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20],
        'min_samples_split': [5, 10, 15],
        'min_samples_leaf': [3, 5, 7],
        'class_weight': ['balanced', 'balanced_subsample']
    }

**Grade de hiperparâmetros para otimização definindo múltiplas combinações para:**

- n_estimators: Número de árvores na floresta

- max_depth: Profundidade máxima das árvores (None permite crescimento completo)

- min_samples_split: Mínimo de amostras para dividir um nó

- min_samples_leaf: Mínimo de amostras em folhas

- class_weight: Estratégias de balanceamento automático

      rf_base = RandomForestClassifier(random_state=42, n_jobs=-1)
      balanced_acc_scorer = 'balanced_accuracy'
      grid_search = GridSearchCV(estimator=rf_base, param_grid=param_grid,
                                cv=5, n_jobs=-1, verbose=1, scoring=balanced_acc_scorer)

**Configuração do GridSearchCV utilizando:**

- Validação cruzada: 5 folds para avaliação robusta

- Métrica balanceada: balanced_accuracy para lidar com desbalanceamento

- Paralelização: n_jobs=-1 para usar todos os cores disponíveis
      
      grid_search.fit(X_train, y_train, sample_weight=sample_weights_train)
      best_rf_model = grid_search.best_estimator_

Treinamento e seleção do melhor modelo aplicando os pesos de amostra durante o treinamento para reforçar o balanceamento.

# Etapa 5: Calibração de Probabilidades

      calibrated_model = CalibratedClassifierCV(
          base_estimator=best_rf_model,
          method='isotonic',
          cv=5
      )
      calibrated_model.fit(X_train, y_train, sample_weight=sample_weights_train)

**Calibração isotônica das probabilidades melhorando a confiabilidade das estimativas de probabilidade do modelo através de:**

- Método isotônico: Mais flexível que calibração sigmoid

- Validação cruzada: 5 folds para calibração robusta

# Etapa 6: Otimização de Limiar de Classificação

      y_pred_proba_test = calibrated_model.predict_proba(X_test)[:, 1]
      thresholds = [0.3, 0.4, 0.5, 0.6, 0.7]
      results = []

Teste de múltiplos limiares avaliando diferentes pontos de corte para otimizar o desempenho em métricas específicas.
Pesos de amostra: Mantendo o balanceamento durante calibração

      for threshold in thresholds:
          y_pred_custom = (y_pred_proba_test >= threshold).astype(int)
    
    acc = accuracy_score(y_test, y_pred_custom)
    bal_acc = balanced_accuracy_score(y_test, y_pred_custom)
    f1 = f1_score(y_test, y_pred_custom)
    
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred_custom).ravel()

**Avaliação abrangente para cada limiar calculando múltiplas métricas:**

- Acurácia simples e balanceada

- F1-score

- Componentes da matriz de confusão

- Precisão e recall por classe


      best_threshold_idx = max(range(len(results)), key=lambda i: results[i]['balanced_accuracy'])
      best_threshold = results[best_threshold_idx]['threshold']
      y_pred_final = (y_pred_proba_test >= best_threshold).astype(int)

Seleção do limiar ótimo baseado na acurácia balanceada, que é mais apropriada para datasets desbalanceados.

# Etapa 7: Avaliação Final e Relatórios
      print("\nRelatório de Classificação Final (com limiar otimizado):")
      print(classification_report(y_test, y_pred_final, target_names=['Salário Baixo/Médio', 'Salário Alto']))

Relatório detalhado de classificação apresentando precisão, recall, F1-score e suporte para cada classe com o limiar otimizado.

# Etapa 8: Geração de Visualizações Avançadas

**8.1 Matriz de Confusão Otimizada**
      
      cm = confusion_matrix(y_test, y_pred_final)
      plt.figure(figsize=(10, 8))
      sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                  xticklabels=['Salário Baixo/Médio', 'Salário Alto'],
                  yticklabels=['Salário Baixo/Médio', 'Salário Alto'],
                  annot_kws={"size": 14})

Visualização da matriz de confusão com formatação profissional usando heatmap do seaborn, incluindo rótulos descritivos e anotações em tamanho legível.

**8.2 Curva ROC com Limiar Otimizado**

      fpr, tpr, _ = roc_curve(y_test, y_pred_proba_test)
      roc_auc = auc(fpr, tpr)
      plt.plot(fpr, tpr, color='darkorange', lw=3, label=f'Curva ROC (AUC = {roc_auc:.2f})')
      plt.axvline(x=fpr[np.argmin(np.abs(tpr - best_threshold))], color='green', linestyle='--', 
                  label=f'Limiar Ótimo = {best_threshold}')

**Curva ROC aprimorada incluindo:**

- Área sob a curva (AUC) como métrica de desempenho

- Linha vertical indicando o limiar otimizado

- Formatação profissional com cores contrastantes e legendas

**8.3 Análise de Importância das Features**

      importances = best_rf_model.feature_importances_
      feature_names = X.columns
      indices = np.argsort(importances)[::-1]
      n_features_to_show = min(20, len(indices))
      top_indices = indices[:n_features_to_show]
Ranking de importância das features limitado às 20 mais relevantes para melhor visualização e interpretabilidade.

      # Agrupar features por prefixo para melhor organização
      prefixes = {}
      for i in indices:
          feature = feature_names[i]
          prefix = feature.split('_')[0] if '_' in feature else feature
          if prefix not in prefixes:
              prefixes[prefix] = []
          prefixes[prefix].append((i, importances[i]))
Agrupamento inteligente por categorias organizando features por prefixos (formação, localização, setor) para análise estruturada da importância por domínio.

**8.4 Agrupamento por Categorias**

      prefixes = {}
      for i in indices:
          feature = feature_names[i]
          prefix = feature.split('_')[0] if '_' in feature else feature
          if prefix not in prefixes:
              prefixes[prefix] = []
          prefixes[prefix].append((i, importances[i]))

Agrupamento inteligente por categorias organizando features por prefixos (formação, localização, setor) para análise estruturada da importância por domínio.

**8.5 Distribuição das Probabilidades Preditas**

      plt.figure(figsize=(12, 8))
      sns.histplot(y_pred_proba_test, bins=50, kde=True)
      plt.axvline(x=best_threshold, color='red', linestyle='--', linewidth=2,
                 label=f'Limiar Ótimo = {best_threshold}')

Análise da distribuição das probabilidades geradas pelo modelo calibrado com marcação do limiar ótimo, permitindo visualizar quantas amostras ficam de cada lado do ponto de corte.

**8.6 Visualização de Árvores de Decisão**
      
      plt.figure(figsize=(24, 18))
      plot_tree(best_rf_model.estimators_[0], 
                feature_names=X.columns, 
                class_names=['Salário Baixo/Médio', 'Salário Alto'],
                filled=True, 
                rounded=True, 
                fontsize=12,
                max_depth=4)

- Visualização detalhada de árvore individual do Random Forest com:

- Tamanho expandido: 24x18 polegadas para máxima legibilidade

- Profundidade controlada: max_depth=4 para mostrar detalhes sem complexidade excessiva

- Formatação aprimorada: Nós preenchidos, bordas arredondadas e fonte de tamanho 12

**8.7 Análise de Interação entre Formação e Experiência**

      pivot_table = pd.crosstab(
          index=df_limpo['formacao_academica_encoded'], 
          columns=df_limpo['experiencia_profissional_encoded'],
          values=df_limpo['salario_alto'],
          aggfunc=np.mean
      )

Tabela cruzada avançada utilizando pd.crosstab para calcular a probabilidade média de salário alto para cada combinação de formação acadêmica e experiência profissional.

      formacao_labels = {v: k for k, v in nivel_ensino_map.items()}
      experiencia_labels = {v: k for k, v in experiencia_map.items()}
      
      pivot_table.index = [formacao_labels.get(i, i) for i in pivot_table.index]
      pivot_table.columns = [experiencia_labels.get(i, i) for i in pivot_table.columns]

Mapeamento reverso dos rótulos convertendo os valores numéricos codificados de volta para suas descrições originais, tornando o heatmap mais interpretável.

**8.8 Visualização das Top 3 Features**

      top3_indices = indices[:3]
      top3_features = [feature_names[i] for i in top3_indices]
      top3_importances = importances[top3_indices]
      
      plt.figure(figsize=(10, 6))
      bars = plt.barh(range(3), top3_importances, align='center', color=['#1f77b4', '#ff7f0e', '#2ca02c'])

Gráfico especializado para as 3 features mais importantes com cores diferenciadas e valores anotados nas barras para facilitar a interpretação.

**8.9 Gráfico de Dispersão das Features Principais**
      
      if len(indices) >= 2:
          top2_indices = indices[:2]
          feature1 = feature_names[top2_indices[0]]
          feature2 = feature_names[top2_indices[1]]
          
          scatter = plt.scatter(X_test[feature1], X_test[feature2], 
                               c=y_pred_proba_test, cmap='coolwarm', 
                               alpha=0.7, s=100, edgecolors='k')

Visualização da relação entre as duas features mais importantes colorido pelas probabilidades preditas, revelando padrões espaciais na classificação e permitindo identificar regiões de alta e baixa probabilidade de salário alto.

**8.10 Finalização e Salvamento**
print(f"\nTodos os gráficos foram salvos no diretório: {output_dir}")




-------------------------------------------

### Modelo 1 Análise de Disparidade Salarial de Profissionais de Dados no Brasil Utilizando o Arvore de decisão por classificação
### *Justificativa1-2*
### *Processo de Amostragem de Dados (Particionamento e Cross-Validation)1-2*
### *Parâmetros utilizados1-2*
### *Explicação do Código:1-2*



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

# Modelo 3  
## 3º Pergunta orientada a dados
*  Como fatores como formalidade no emprego , características demográficas e regionais se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?
## 1. Justificativa e Objetivo

O objetivo deste modelo é classificar a faixa salarial de indivíduos em duas categorias: "Salário Baixo" e "Salário Alto". A transição de uma classificação multiclasse (3 faixas) para uma binária visa simplificar o problema e potencialmente melhorar a distinção entre os grupos salariais, buscando um equilíbrio na distribuição das amostras entre as classes definidas por um ponto de corte específico. A última execução utilizou um ponto de corte fixo (presumivelmente R$7.500,00 com base nos resultados) para a variável `salary_numeric_lower_bound` para realizar essa divisão.

## 2. Processo de Amostragem de Dados (Particionamento e Cross-Validation)

O processo de amostragem e validação do modelo é crucial para garantir sua generalização e evitar overfitting. As seguintes etapas são empregadas no código:

### 2.1. Particionamento Inicial (Treino e Teste Principal)

* **Método**: `train_test_split` da biblioteca `sklearn.model_selection`.
* **Divisão**: O conjunto de dados processado (`X_initial`, `y_full`) é dividido em:
    * Conjunto de Treinamento para Optuna e RFECV (`X_train_optuna`, `y_train_optuna`): 75% dos dados.
    * Conjunto de Teste Final (`X_test`, `y_test`): 25% dos dados.
* **Parâmetros Utilizados**:
    * `test_size=0.25`: Reserva 25% dos dados para o conjunto de teste final, que não é utilizado durante o treinamento ou otimização de hiperparâmetros.
    * `random_state=42`: Garante a reprodutibilidade da divisão. O mesmo estado aleatório resultará sempre na mesma divisão dos dados.
    * `stratify=y_full`: Realiza uma divisão estratificada. Isso significa que a proporção das classes da variável alvo (`y_full`, que contém "Salário Baixo" e "Salário Alto" codificados) é mantida tanto no conjunto de treino quanto no de teste. Isso é especialmente importante para dados desbalanceados ou quando se quer garantir que ambas as classes estejam representadas adequadamente em ambas as partições.

### 2.2. Validação Cruzada Estratificada para RFECV (Recursive Feature Elimination with Cross-Validation)

* **Método**: `StratifiedKFold` da `sklearn.model_selection`, utilizado dentro do `RFECV`.
* **Objetivo**: Selecionar o subconjunto ótimo de features de forma robusta, avaliando o desempenho do modelo com diferentes combinações de features em múltiplas dobras (folds) do conjunto de treinamento.
* **Parâmetros Utilizados no `StratifiedKFold` para `RFECV`**:
    * `n_splits=rfecv_folds` (padrão `3` no código): O conjunto de treinamento (`X_train_optuna_for_rfecv`, `y_train_optuna`) é dividido em 3 folds.
    * `shuffle=True`: Embaralha os dados antes de dividir em folds.
    * `random_state=42`: Garante a reprodutibilidade do embaralhamento e da divisão em folds.
* **Funcionamento do `RFECV`**: Treina o estimador (`lgb.LGBMClassifier`) recursivamente, removendo features e avaliando o desempenho (definido por `rfecv_scoring`, padrão `'accuracy'`) através da validação cruzada estratificada. Isso ajuda a encontrar o número de features que maximiza a métrica de scoring.

### 2.3. Validação Cruzada Estratificada para Otimização de Hiperparâmetros com Optuna

* **Método**: `StratifiedKFold` utilizado dentro da função `objective_optuna_cv`.
* **Objetivo**: Avaliar o desempenho de diferentes combinações de hiperparâmetros do `lgb.LGBMClassifier` de forma robusta, treinando e validando em múltiplas dobras do conjunto de treinamento selecionado pelo RFECV (`X_train_optuna_selected`, `y_train_optuna`).
* **Parâmetros Utilizados no `StratifiedKFold` para `Optuna`**:
    * `n_splits=n_cv_folds_optuna`: O número de folds é determinado dinamicamente, sendo o mínimo entre 5 e a contagem da classe minoritária no conjunto `y_train_optuna` (desde que essa contagem seja >= 2). Se a contagem da classe minoritária for muito pequena, é usado um fallback para validação simples (holdout). Na sua última execução com classes mais equilibradas, provavelmente usou 5 folds.
    * `shuffle=True`: Embaralha os dados.
    * `random_state=trial.number`: O estado aleatório é vinculado ao número do "trial" do Optuna, promovendo diversidade nas divisões entre diferentes trials.
* **Funcionamento**: Para cada "trial" do Optuna (combinação de hiperparâmetros), o modelo é treinado e avaliado `n_cv_folds_optuna` vezes. A métrica de desempenho (acurácia média dos folds) é retornada ao Optuna, que busca maximizá-la.

### 2.4. Partição Interna para Early Stopping no Treinamento Final

* **Método**: `train_test_split` para criar um conjunto de validação interna.
* **Divisão**: O conjunto `X_train_optuna_selected` (que é 75% do total) é novamente dividido:
    * Conjunto de Treinamento Final (`X_train_final`, `y_train_final`): 80% de `X_train_optuna_selected`.
    * Conjunto de Validação Interna (`X_val_internal`, `y_val_internal`): 20% de `X_train_optuna_selected`.
* **Objetivo**: Este conjunto de validação interna é usado para o mecanismo de `early_stopping` do LightGBM durante o treinamento do modelo final com os melhores hiperparâmetros encontrados pelo Optuna. O `early_stopping` monitora a métrica (`binary_logloss` para o caso binário) no conjunto de validação interna e para o treinamento quando essa métrica não melhora por um número definido de rodadas (`early_stopping_rounds=25`), ajudando a evitar overfitting no conjunto de treinamento final.
* **Parâmetros Utilizados**:
    * `test_size=0.20`
    * `random_state=42`
    * `stratify=y_train_optuna`

### Justificativa das Escolhas de Amostragem:

* **Divisão Treino/Teste Principal**: Essencial para avaliar o desempenho final do modelo em dados não vistos. A proporção 75/25 é comum.
* **Estratificação**: Crucial para problemas de classificação, especialmente com classes desbalanceadas (embora o objetivo seja reduzir o desbalanceamento), para garantir que as proporções das classes sejam mantidas nas divisões, levando a estimativas de desempenho mais confiáveis.
* **Validação Cruzada (RFECV e Optuna)**: Reduz a variância da estimativa de desempenho e torna a seleção de features e hiperparâmetros mais robusta, diminuindo a chance de escolhas baseadas em uma divisão particular dos dados. `StratifiedKFold` é usado para manter a proporção das classes em cada fold.
* **Conjunto de Validação Interna para Early Stopping**: Permite que o modelo pare de treinar no momento ótimo, evitando o overfitting aos dados de `X_train_final`, usando `X_val_internal` como um proxy para dados não vistos durante essa fase.

## 3. Parâmetros Utilizados (Principais)

### 3.1.1 Criação da Variável Alvo (`target_col_agrupada_name`)

* **`salary_group_labels = ["Salário Baixo", "Salário Alto"]`**: Define os nomes das duas categorias da variável alvo.
* **`point_of_cut_fixed`**: Um valor monetário específico (ex: `7500.0` na última execução que produziu o suporte 622/567) usado para dividir `salary_numeric_lower_bound`. Salários `<= point_of_cut_fixed` são "Salário Baixo/Médios", e `> point_of_cut_fixed` são "Salário Alto". **Este é o parâmetro chave que você tem ajustado para controlar a distribuição das classes.**
* O gráfico abaixo mostra a distruibuicao da faixa salarial, onde é notável que uma divisao de `<= point_of_cut_fixed` (Salários Baixos/Medios) e `> point_of_cut_fixed` (salários Altos), produziram um suporte 622/567 .
  ![Image](https://github.com/user-attachments/assets/cc8fdd29-49bd-4b07-82a3-803c81bcb2a7)
* **`pd.cut(..., include_lowest=True, duplicates='drop')`**: Usado para realizar a divisão com base no `point_of_cut_fixed`.

## 3.1.2 Utilizacao das variáveis preditivas 

| Atributo                                           | Código de Referência | Tipo         | Subtipo                             | Descrição                                                                                     | Relevância  |
|----------------------------------------------------|-----------------------|--------------|-------------------------------------|-----------------------------------------------------------------------------------------------|------------|
| Faixa etária                                       | P1a1                  | Qualitativo  | Ordinal                             | Faixa etária do respondente                                                                   | Alta       |
| Gênero                                             | P1b                   | Qualitativo  | Nominal (Multivalorado)             | Identidade de gênero do respondente                                                           | Alta       |
| Nivel de ensino alcançado                          | P1l                   | Qualitativo  | Ordinal                             | Nível de ensino do respondente (graduação, mestrado, etc.)                                    | Alta       |
| Faixa salarial mensal                              | P2h                   | Qualitativo  | Ordinal                             | Faixa salarial mensal do respondente                                                          | Alta       |
| Tempo de experiência na área de dados              | P2i                   | Quantitativo | Discreto                            | Tempo de experiência do respondente na área de dados (em anos)                                | Alta       |
| UF onde mora                                       | P1i1                  | Qualitativo  | Nominal (Multivalorado)             | Unidade Federativa onde o respondente reside                                                  | Alta       |
| Cargo atual                                        | P2f                   | Qualitativo  | Nominal (Multivalorado)             | Cargo atual ocupado pelo respondente                                                          | Alta       |
| Nível de senioridade                               | P2g                   | Qualitativo  | Ordinal                             | Nível de senioridade do respondente (Júnior, Pleno, Sênior)                                   | Alta       |

### 3.2. `RFECV`

* `estimator=lgb.LGBMClassifier(random_state=42, n_jobs=-1, verbose=-1)`: Modelo base para a seleção de features.
* `step=rfecv_step` (padrão `1`): Número de features a serem removidas em cada iteração.
* `cv=StratifiedKFold(n_splits=rfecv_folds, ...)` (padrão `rfecv_folds=3`): Estratégia de validação cruzada.
* `scoring=rfecv_scoring` (padrão `'accuracy'`): Métrica para avaliar o subconjunto de features.
* `min_features_to_select=1`: Número mínimo de features a serem selecionadas.

### 3.3. `Optuna` (Otimização de Hiperparâmetros para `lgb.LGBMClassifier`)

* `n_trials=n_optuna_trials` (padrão `100`): Número de combinações de hiperparâmetros a serem testadas.
* `timeout=optuna_timeout` (padrão `1800` segundos): Tempo máximo para a otimização.
* `direction='maximize'`: O Optuna tenta maximizar a métrica retornada por `objective_optuna_cv` (que é a acurácia).
* **Espaço de Busca dos Hiperparâmetros (exemplos da sua última execução bem-sucedida):**
    * `n_estimators`: 1100 (valor encontrado)
    * `learning_rate`: 0.06509... (valor encontrado)
    * `num_leaves`: 80 (valor encontrado)
    * `max_depth`: 12 (valor encontrado)
    * `min_child_samples`: 25 (valor encontrado)
    * `subsample`: 0.5 (valor encontrado)
    * `colsample_bytree`: 0.6 (valor encontrado)
    * `reg_alpha`: 1.567... (valor encontrado)
    * `reg_lambda`: 14.655... (valor encontrado)
    * `min_split_gain`: 0.385... (valor encontrado)
    * `min_child_weight`: 0.139... (valor encontrado)
* **Adaptação para Classificação Binária em Optuna e Modelo Final**:
    * `objective`: Definido como `'binary'` (pois `is_binary_classification` é `True`).
    * `metric`: Definido como `'binary_logloss'` para avaliação interna e early stopping.
    * `num_class`: Omitido para classificação binária no LightGBM (ou definido como 1 implicitamente).

### 3.4. Treinamento do Modelo Final (`best_lgbm`)

* Usa os `best_params_optuna` encontrados.
* `early_stopping(callbacks=[lgb.early_stopping(25, verbose=False)])`: Para o treinamento se a métrica no conjunto de validação interna (`X_val_internal`) não melhorar por 25 rodadas. O número de árvores final foi 105 na sua última execução.

## 4. Explicação do Código (Fluxo Principal)

### Pergunta orientada a dados : **Como fatores como formalidade no emprego , características demográficas e regionais se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?**
  * O fluxo de execução do código principal pode ser resumido nas seguintes etapas:

1.  **Carregamento e Preparação Inicial dos Dados**:
    * Leitura do arquivo Excel (`Main_database (2).xlsx`).
    * Limpeza dos nomes das colunas para remover caracteres especiais e espaços (função `clean_col_name`).
    * Mapeamento heurístico de colunas importantes (faixa salarial original, experiência, senioridade, etc.) para nomes padronizados internos (armazenados em `col_mapping`).
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split, KFold, StratifiedKFold
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, f1_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.feature_selection import RFECV
import lightgbm as lgb
import optuna
import warnings
import re
import pickle
import time
import traceback

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=optuna.exceptions.ExperimentalWarning)

# Certifique-se de que a pasta para salvar visualizações existe
os.makedirs('visualizacoes_classificacao_salario_v7_rfecv', exist_ok=True)
```

2.  **Engenharia da Variável Alvo (`target_col_agrupada_name`)**:
    * A coluna da faixa salarial original (ex: `P2_h`) é processada para extrair um valor numérico (`salary_numeric_lower_bound`) usando `extract_salary_lower_bound`.
    * **Divisão em Duas Categorias**: Um **ponto de corte fixo** (`point_of_cut_fixed`, que você estava ajustando, por exemplo, para R$7.500,00 na última execução) é usado para dividir `salary_numeric_lower_bound` em "Salário Baixo" e "Salário Alto" usando `pd.cut`. Esta etapa inclui lógica para lidar com casos onde o ponto de corte é extremo (menor/igual ao mínimo ou maior/igual ao máximo) e um fallback para `pd.qcut` (divisão pela mediana) se o `pd.cut` falhar.
    * A distribuição de `salary_numeric_lower_bound` é plotada para auxiliar na escolha/ajuste do `point_of_cut_fixed`.
    * Amostras com valor nulo na nova variável alvo são removidas.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)

        # ... (Após mapeamento de colunas e limpeza da coluna de experiência) ...

        original_salary_col_name = col_mapping["target_original_salary_range"]
        df_main_processed = df_main.dropna(subset=[original_salary_col_name]).copy()
        if df_main_processed.empty: print(f"Erro: DataFrame vazio após NaNs na faixa salarial original."); return None

        # Extrai o limite inferior numérico da faixa salarial
        df_main_processed['salary_numeric_lower_bound'] = df_main_processed[original_salary_col_name].apply(extract_salary_lower_bound)
        df_main_processed.dropna(subset=['salary_numeric_lower_bound'], inplace=True)

        if df_main_processed.empty:
            print(f"Erro: DataFrame vazio após remover NaNs de 'salary_numeric_lower_bound'."); return None

        # --- CRIAÇÃO DA VARIÁVEL ALVO COM 2 CATEGORIAS E PONTO DE CORTE FIXO ---
        salary_group_labels = ["Salário Baixo", "Salário Alto"]
        target_col_agrupada_name = col_mapping["target"] # Definido anteriormente no mapeamento

        if df_main_processed.shape[0] < 2:
            print(f"Erro: Dados insuficientes ({df_main_processed.shape[0]}) para criar faixas."); return None

        min_salary = df_main_processed['salary_numeric_lower_bound'].min()
        max_salary = df_main_processed['salary_numeric_lower_bound'].max()

        if min_salary == max_salary:
            print(f"Aviso: Todos os valores de 'salary_numeric_lower_bound' são iguais ({min_salary}). Apenas uma categoria ('{salary_group_labels[0]}') será criada.")
            df_main_processed[target_col_agrupada_name] = salary_group_labels[0]
        else:
            # AJUSTE ESTE VALOR PARA CONTROLAR A DISTRIBUIÇÃO DAS CLASSES
            # Se "Salário Baixo" tiver muitas amostras, DIMINUA este valor.
            # Se "Salário Baixo" tiver poucas amostras, AUMENTE este valor.
            # Exemplos baseados no seu histograma: 7500, 8000, 9000.
            point_of_cut_fixed = 7500.0  # <-- PONTO DE CORTE AJUSTÁVEL

            print(f"Info: Usando ponto de corte fixo para salários: {point_of_cut_fixed:.2f}")
            print(f"       Salários <= {point_of_cut_fixed:.2f} serão '{salary_group_labels[0]}' (Salário Baixo)")
            print(f"       Salários >  {point_of_cut_fixed:.2f} serão '{salary_group_labels[1]}' (Salário Alto)")

            final_bins = []
            final_labels = []

            if point_of_cut_fixed <= min_salary:
                print(f"Aviso: Ponto de corte fixo ({point_of_cut_fixed:.2f}) é <= ao mínimo ({min_salary:.2f}). Todos os dados cairão em '{salary_group_labels[1]}'.")
                final_bins = [min_salary, max_salary]
                final_labels = [salary_group_labels[1]]
            elif point_of_cut_fixed >= max_salary:
                print(f"Aviso: Ponto de corte fixo ({point_of_cut_fixed:.2f}) é >= ao máximo ({max_salary:.2f}). Todos os dados cairão em '{salary_group_labels[0]}'.")
                final_bins = [min_salary, max_salary]
                final_labels = [salary_group_labels[0]]
            else:
                final_bins = [min_salary, point_of_cut_fixed, max_salary]
                final_labels = salary_group_labels

            unique_sorted_bins = sorted(list(set(final_bins)))

            if len(unique_sorted_bins) < 2:
                print(f"Erro crítico: Não foi possível definir pelo menos 2 bins únicos ({unique_sorted_bins}) com o ponto de corte fixo."); return None

            # Ajuste para o caso de unique_sorted_bins ter apenas 2 elementos e final_labels ter 2 labels
            # Isso pode acontecer se o ponto de corte for igual ao min ou max, ou muito próximo.
            if len(unique_sorted_bins) == 2 and len(final_labels) == 2:
                print(f"Aviso: Ponto de corte fixo resultou em apenas 2 bins efetivos ({unique_sorted_bins}). Será criada apenas 1 categoria.")
                # Decide qual label usar baseado na posição do ponto de corte
                if point_of_cut_fixed <= min_salary + 1e-9: # Se o corte é no mínimo ou abaixo, todos são "Alto"
                    final_labels = [salary_group_labels[1]]
                elif point_of_cut_fixed >= max_salary - 1e-9: # Se o corte é no máximo ou acima, todos são "Baixo"
                    final_labels = [salary_group_labels[0]]
                else: # Se o corte está entre min e max mas resultou em 1 categoria (devido a 'duplicates=drop' ou bins muito próximos)
                      # Tenta inferir a categoria predominante ou a que faz mais sentido.
                      # Aqui, uma heurística simples: se o ponto de corte está mais perto do mínimo,
                      # significa que a maior parte dos dados está acima, então seriam "Salário Alto".
                      # Se está mais perto do máximo, a maioria é "Salário Baixo".
                      # Isso é uma simplificação e pode precisar de ajuste mais fino dependendo do caso de uso.
                    if (point_of_cut_fixed - min_salary) < (max_salary - point_of_cut_fixed):
                        # Ponto de corte mais próximo do mínimo -> maioria é Alto
                        final_labels = [salary_group_labels[1]]
                    else:
                        # Ponto de corte mais próximo do máximo -> maioria é Baixo
                        final_labels = [salary_group_labels[0]]


            bins_to_use = unique_sorted_bins
            labels_to_use = final_labels

            try:
                df_main_processed[target_col_agrupada_name] = pd.cut(
                    df_main_processed['salary_numeric_lower_bound'],
                    bins=bins_to_use,
                    labels=labels_to_use,
                    include_lowest=True, # Garante que o valor mínimo seja incluído no primeiro bin
                    duplicates='drop'    # Remove bins duplicados se existirem
                )
            except Exception as e:
                print(f"Erro durante pd.cut com ponto de corte fixo: {e}")
                print(f"  Bins usados: {bins_to_use}, Labels usados: {labels_to_use}")
                print("  Tentando fallback para divisão pela mediana (pd.qcut)...")
                try:
                    df_main_processed[target_col_agrupada_name] = pd.qcut(
                        df_main_processed['salary_numeric_lower_bound'],
                        q=2, labels=salary_group_labels, duplicates='drop'
                    )
                    num_qcut_cats = len(df_main_processed[target_col_agrupada_name].cat.categories)
                    if num_qcut_cats < 2: # Se qcut também falhar em criar 2 categorias
                        print("Fallback com qcut também resultou em menos de 2 categorias. Agrupando em uma única categoria.")
                        df_main_processed[target_col_agrupada_name] = salary_group_labels[0] # Ou a categoria mais apropriada
                except Exception as e_qcut_fallback:
                     print(f"Erro no fallback com pd.qcut: {e_qcut_fallback}. Não foi possível criar a variável alvo."); return None

        print(f"Nova coluna alvo '{target_col_agrupada_name}' criada. Contagens no DataFrame processado completo:\\n{df_main_processed[target_col_agrupada_name].value_counts(dropna=False).sort_index()}")

        print("\nDiagnóstico da distribuição de 'salary_numeric_lower_bound':")
        print(df_main_processed['salary_numeric_lower_bound'].describe())
        plt.figure(figsize=(10,4))
        sns.histplot(df_main_processed['salary_numeric_lower_bound'], kde=True, bins=50)
        plt.title("Distribuição de 'salary_numeric_lower_bound'")
        plt.savefig('visualizacoes_classificacao_salario_v7_rfecv/distribuicao_salario_numerico.png')
        # plt.show() # Removido ou comentado para execução em lote/sem interface gráfica
        plt.close()

        df_main_processed.dropna(subset=[target_col_agrupada_name], inplace=True)
        if df_main_processed.empty:
            print("Erro: DataFrame vazio após remover NaNs na coluna alvo agrupada. Verifique a criação das categorias."); return None
        print(f"Linhas após remover NaN na coluna alvo AGRUPADA: {df_main_processed.shape[0]}")
        # --- FIM DAS MODIFICAÇÕES NA VARIÁVEL ALVO ---
```
3.  **Preparação das Features (`X_initial`) e Codificação do Alvo (`y_full`)**:
    * As features relevantes (idade, gênero, UF, ensino, cargo, senioridade, experiência) são selecionadas.
    * A coluna 'UF' é transformada na feature 'Regiao\_Mapeada'.
    * A variável alvo (`target_col_agrupada_name`) é codificada numericamente (0 e 1) usando `LabelEncoder`, e é determinado se o problema é de classificação binária.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após a engenharia da variável alvo e remoção de NaNs na coluna alvo agrupada) ...

        # Seleciona as colunas de features iniciais com base no mapeamento
        # required_cols_internal_for_features foi definido anteriormente como:
        # ["faixa_etaria", "genero", "nivel_ensino", "tempo_experiencia_P2i", 
        #  "nivel_senioridade_P2g", "uf_mora_P1i1", "cargo_atual_P2f"]
        feature_cols_to_use_initial = [
            col_mapping[col_internal] for col_internal in required_cols_internal_for_features 
            if col_internal in col_mapping and col_mapping[col_internal] in df_main_processed.columns
        ]
        X_initial = df_main_processed[feature_cols_to_use_initial].copy()

        # Mapeia UF para Região e remove a coluna original de UF
        uf_col_original_name_mapped = col_mapping.get("uf_mora_P1i1")
        if uf_col_original_name_mapped and uf_col_original_name_mapped in X_initial.columns:
            X_initial['Regiao_Mapeada'] = map_uf_to_region(X_initial[uf_col_original_name_mapped])
            X_initial.drop(columns=[uf_col_original_name_mapped], inplace=True)

        # Codifica a variável alvo
        # 'le' e 'is_binary_classification' são declaradas como globais para serem acessadas
        # pela função objective_optuna_cv que é definida no escopo global do script,
        # mas chamada dentro desta função principal.
        global le, is_binary_classification 
        le = LabelEncoder()
        y_full = pd.Series(le.fit_transform(df_main_processed[target_col_agrupada_name]), index=df_main_processed.index)
        
        print(f"Alvo AGRUPADA '{target_col_agrupada_name}' codificada. Classes: {list(le.classes_)} -> {list(le.transform(le.classes_))}")

        if len(le.classes_) < 2:
            print(f"ERRO CRÍTICO: A variável alvo final tem menos de 2 classes ({len(le.classes_)}: {list(le.classes_)}). Não é possível treinar o modelo de classificação."); return None
        
        is_binary_classification = len(le.classes_) == 2

        if is_binary_classification:
            print("Classificação Binária Detectada.")
        else:
            print(f"Classificação Multiclasse Detectada ({len(le.classes_)} classes).")

        initial_feature_columns_after_region = X_initial.columns.tolist()
        print(f"Features para processamento inicial (antes RFECV): {initial_feature_columns_after_region}")
```
4.  **Pré-processamento das Features**:
    * **Valores Ausentes**:
        * Features numéricas (como tempo de experiência): imputados com a mediana.
        * Features categóricas: imputados com a string "Missing\_Val\_Cat".
    * **Outliers**: Para features numéricas, outliers são identificados usando o critério de 1.5\*IQR e as linhas contendo outliers são removidas.
    * **Codificação de Categóricas**: Features categóricas são convertidas para o tipo `category` do pandas.
    * **Escalonamento**: Features numéricas são padronizadas usando `StandardScaler`.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após a preparação de X_initial e y_full) ...

        # Identifica features numéricas e categóricas em X_initial
        # initial_feature_columns_after_region já contém os nomes das colunas em X_initial
        numerical_features_initial = X_initial.select_dtypes(include=np.number).columns.tolist()
        categorical_features_initial = X_initial.select_dtypes(exclude=np.number).columns.tolist()

        print(f"Features numéricas identificadas: {numerical_features_initial}")
        print(f"Features categóricas identificadas: {categorical_features_initial}")

        # Tratamento de Ausentes (Features Numéricas)
        for col in numerical_features_initial:
            if X_initial[col].isnull().sum() > 0:
                print(f"Imputando NaNs na feature numérica '{col}' com a mediana.")
                X_initial.loc[:, col] = X_initial[col].fillna(X_initial[col].median())

        # Tratamento de Outliers (Features Numéricas)
        outliers_indices = pd.Series(False, index=X_initial.index)
        if numerical_features_initial:
            print("Processando outliers para features numéricas...")
            for col in numerical_features_initial:
                Q1 = X_initial[col].quantile(0.25); Q3 = X_initial[col].quantile(0.75); IQR = Q3 - Q1
                lim_inf = Q1 - 1.5 * IQR; lim_sup = Q3 + 1.5 * IQR
                col_outliers = (X_initial[col] < lim_inf) | (X_initial[col] > lim_sup)
                if col_outliers.sum() > 0: print(f"  Feature '{col}': {col_outliers.sum()} outliers detectados.")
                outliers_indices = outliers_indices | col_outliers # Acumula os índices de outliers de todas as colunas numéricas
            
            if outliers_indices.sum() > 0:
                print(f"Total de amostras com outliers: {outliers_indices.sum()}")
                # Remove as linhas (amostras) que contêm outliers
                X_initial = X_initial[~outliers_indices]; 
                y_full = y_full[~outliers_indices] # Mantém y_full sincronizado com X_initial
                print(f"Shape de X_initial e y_full após remover outliers: {X_initial.shape}, {y_full.shape}")
                if X_initial.empty: print("ERRO: Todos os dados removidos como outliers."); return None
            else: print("Nenhum outlier encontrado em features numéricas.")
        else: print("Nenhuma feature numérica para checar outliers.")

        # Tratamento de Ausentes (Features Categóricas) e conversão para tipo 'category'
        for col_name in categorical_features_initial:
            if col_name not in X_initial.columns: continue # Caso a coluna tenha sido removida (pouco provável aqui)
            
            # Converte para string para facilitar a busca por valores ausentes textuais
            processed_series = X_initial[col_name].astype(str) 
            missing_vals = ['nan', 'none', '<na>', '', 'missing', 'missing_category_value', 'missing_val_cat', 'null']
            temp_lower_stripped = processed_series.str.lower().str.strip()
            
            # Identifica tanto NaNs originais quanto strings que representam ausência
            is_missing = temp_lower_stripped.isin(missing_vals) | X_initial[col_name].isnull() 
            
            if is_missing.any():
                # Usa .loc para evitar SettingWithCopyWarning e garantir a modificação no DataFrame original
                X_initial.loc[is_missing, col_name] = "Missing_Val_Cat" 
            
            # Converte a coluna para o tipo 'category' do pandas
            X_initial[col_name] = X_initial[col_name].astype("category")

        # Escalonamento (Features Numéricas)
        # O scaler é inicializado como scaler_rfecv, mas ele é ajustado aqui nos dados X_initial (que ainda não foram divididos)
        # e será usado posteriormente.
        scaler_rfecv = StandardScaler()
        # Re-identifica as features numéricas caso alguma tenha sido removida ou alterada
        numerical_features_present_after_outliers = [col for col in numerical_features_initial if col in X_initial.columns]
        
        if numerical_features_present_after_outliers:
             # Usa .loc para garantir a atribuição correta e evitar warnings
             X_initial.loc[:, numerical_features_present_after_outliers] = scaler_rfecv.fit_transform(X_initial[numerical_features_present_after_outliers])
             print(f"Features numéricas ({numerical_features_present_after_outliers}) em X_initial escalonadas.")
        else:
            print("Nenhuma feature numérica presente em X_initial para escalonar.")

        # Verifica novamente se y_full tem classes suficientes após a remoção de outliers
        if y_full.nunique() < 2:
            print(f"ERRO CRÍTICO: A variável alvo final tem menos de 2 classes únicas ({y_full.nunique()}: {y_full.unique()}) após processamento. Não é possível treinar o modelo."); return None
```
5.  **Divisão Treino-Teste Principal**:
    * Os dados processados (`X_initial`, `y_full`) são divididos em 75% para treino/otimização (`X_train_optuna`, `y_train_optuna`) e 25% para teste final (`X_test`, `y_test`), de forma estratificada.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após o pré-processamento completo de X_initial e y_full) ...

        # Verifica se y_full ainda tem classes suficientes para estratificação após todos os processamentos anteriores
        if y_full.nunique() < 2:
            print(f"ERRO CRÍTICO: A variável alvo final tem menos de 2 classes únicas ({y_full.nunique()}: {y_full.unique()}) "
                  "antes da divisão treino-teste. Não é possível treinar o modelo.")
            return None

        # Divisão dos dados em conjuntos de treino para Optuna/RFECV e conjunto de teste
        # test_size=0.25 significa 75% para treino e 25% para teste.
        # random_state=42 garante a reprodutibilidade da divisão.
        # stratify=y_full garante que a proporção das classes da variável alvo seja mantida
        # tanto no conjunto de treino quanto no de teste.
        X_train_optuna, X_test, y_train_optuna, y_test = train_test_split(
            X_initial, y_full, 
            test_size=0.25, 
            random_state=42, 
            stratify=y_full
        )
        
        print(f"Dados divididos em treino ({X_train_optuna.shape[0]}) e teste ({X_test.shape[0]})")
```
6.  **Seleção de Features com RFECV**:
    * As features categóricas no conjunto de treino do RFECV são convertidas para códigos numéricos.
    * `RFECV` é aplicado usando `lgb.LGBMClassifier` e `StratifiedKFold` (3 folds) para encontrar o subconjunto ótimo de features baseado na acurácia.
    * `X_train_optuna` e `X_test` são atualizados para conter apenas as features selecionadas.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após a divisão treino-teste principal) ...

        print("\nIniciando Seleção de Features com RFECV...")
        start_time_rfecv = time.time()
        
        # Cria uma cópia de X_train_optuna para o RFECV para não modificar o original ainda
        X_train_optuna_for_rfecv = X_train_optuna.copy()
        
        # Identifica colunas categóricas que precisam ser codificadas para o RFECV
        categorical_cols_for_rfecv_encoding = X_train_optuna_for_rfecv.select_dtypes(include='category').columns
        print(f"Colunas categóricas para codificação numérica no RFECV: {list(categorical_cols_for_rfecv_encoding)}")
        
        # Codifica as features categóricas para o RFECV usando .cat.codes
        # Isso transforma as categorias em inteiros (0, 1, 2, ...)
        for col in categorical_cols_for_rfecv_encoding:
            X_train_optuna_for_rfecv[col] = X_train_optuna_for_rfecv[col].cat.codes

        # Define o estimador para o RFECV
        estimator_rfecv = lgb.LGBMClassifier(random_state=42, n_jobs=-1, verbose=-1)
        
        # Define a estratégia de validação cruzada para o RFECV
        # rfecv_folds é um parâmetro da função, por padrão 3
        cv_rfecv = StratifiedKFold(n_splits=rfecv_folds, shuffle=True, random_state=42)
        
        # Inicializa o RFECV
        # step=rfecv_step (padrão 1) indica quantas features remover a cada iteração.
        # scoring=rfecv_scoring (padrão 'accuracy') é a métrica para avaliar o subconjunto de features.
        # min_features_to_select=1 garante que pelo menos uma feature seja selecionada.
        # verbose=1 mostra o progresso.
        rfecv_selector = RFECV(
            estimator=estimator_rfecv, 
            step=rfecv_step, 
            cv=cv_rfecv,
            scoring=rfecv_scoring, 
            min_features_to_select=1, 
            n_jobs=-1, # Usa todos os processadores disponíveis
            verbose=1
        )

        # Ajusta o RFECV aos dados de treino (com features categóricas codificadas)
        rfecv_selector.fit(X_train_optuna_for_rfecv, y_train_optuna)

        end_time_rfecv = time.time()
        print(f"RFECV concluído em {(end_time_rfecv - start_time_rfecv):.2f} segundos.")
        print(f"Número ótimo de features selecionadas: {rfecv_selector.n_features_}")

        # Obtém os nomes das features selecionadas pelo RFECV
        # rfecv_selector.support_ é uma máscara booleana das features selecionadas
        selected_features_names = X_train_optuna.columns[rfecv_selector.support_].tolist()
        print(f"Features selecionadas: {selected_features_names}")

        if not selected_features_names:
            print("ERRO CRÍTICO: Nenhuma feature selecionada pelo RFECV."); return None

        # Atualiza X_train_optuna e X_test para conter apenas as features selecionadas
        # Mantém os dtypes originais de X_train_optuna (com 'category' para categóricas)
        X_train_optuna_selected = X_train_optuna[selected_features_names].copy()
        X_test_selected = X_test[selected_features_names].copy() # Aplica a mesma seleção ao conjunto de teste

        print(f"Features finais (selecionadas) para modelagem: {X_train_optuna_selected.columns.tolist()}")
        print(f"Dtypes de X_train_optuna_selected:\\n{X_train_optuna_selected.dtypes}")
```
7.  **Otimização de Hiperparâmetros com Optuna**:
    * A função `objective_optuna_cv` é definida para avaliar cada conjunto de hiperparâmetros sugeridos pelo Optuna.
    * Esta função utiliza `StratifiedKFold` (padrão de 5 folds, se possível) para treinar e validar o `lgb.LGBMClassifier`.
    * O Optuna executa `n_optuna_trials` (padrão 100) para encontrar os hiperparâmetros que maximizam a acurácia média da validação cruzada.
    * Os parâmetros `objective` e `metric` do LightGBM são ajustados para `'binary'` e `'binary_logloss'` respectivamente, pois a classificação é binária.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após a seleção de features com RFECV e criação de X_train_optuna_selected, X_test_selected) ...

        # Determina o número de folds para a validação cruzada interna do Optuna
        # Limita o número de folds pela contagem da classe minoritária em y_train_optuna
        min_class_count_cv = y_train_optuna.value_counts().min()
        n_cv_folds_optuna = min(5, min_class_count_cv) if min_class_count_cv >= 2 else 1
        
        if n_cv_folds_optuna < 2 and X_train_optuna_selected.shape[0] > 10:
             print(f"Aviso: Classe minoritária ({min_class_count_cv}) impede CV com mais de 1 fold. Optuna rodará sem CV interno robusto.")
             n_cv_folds_optuna = 1 # Garante que seja pelo menos 1 para o lambda
        elif X_train_optuna_selected.shape[0] <=10: # Muito poucos dados para treinar
             print("ERRO CRÍTICO: Dados de treino insuficientes após seleções/processamento."); return None
        if n_cv_folds_optuna == 0: n_cv_folds_optuna = 1 # Prevenção caso min_class_count_cv seja 0 ou 1

        # A função objective_optuna_cv foi definida anteriormente no script.
        # Ela usa as variáveis globais 'is_binary_classification' e 'le' que foram
        # definidas após a codificação da variável alvo y_full.

        study_name = f'LGBM_Salary_Clf_Optuna_CV_v7_final_rfecv_trials{n_optuna_trials}'
        study = optuna.create_study(direction='maximize', study_name=study_name)
        
        if n_cv_folds_optuna >=2:
            print(f"\nIniciando otimização com Optuna ({n_optuna_trials} trials) e {n_cv_folds_optuna}-Fold CV...")
        else:
            print(f"\nIniciando otimização com Optuna ({n_optuna_trials} trials) e validação simples (holdout)...")

        # Executa a otimização
        # A função lambda passa os dados e o número de folds para objective_optuna_cv
        study.optimize(
            lambda trial: objective_optuna_cv(
                trial, 
                X_train_optuna_selected, # Usa as features selecionadas pelo RFECV
                y_train_optuna, 
                n_cv_splits_internal=n_cv_folds_optuna
            ),
            n_trials=n_optuna_trials, 
            timeout=optuna_timeout
        )

        print("\nOtimização com Optuna concluída!")
        best_optuna_score = study.best_trial.value if study.best_trial else -1.0
        print(f"Melhor Acurácia Média no CV/Val do Optuna: {best_optuna_score:.4f}")
        best_params_optuna = study.best_trial.params if study.best_trial else {}
        print(f"Melhores hiperparâmetros (Optuna): {best_params_optuna}")
```
8.  **Treinamento do Modelo Final**:
    * O conjunto `X_train_optuna_selected` é dividido em um conjunto de treino final (80%) e um conjunto de validação interna (20%).
    * O modelo `lgb.LGBMClassifier` é treinado nesses dados usando os melhores hiperparâmetros encontrados pelo Optuna e `early_stopping` (25 rodadas de paciência) para evitar overfitting, usando o conjunto de validação interna.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após a otimização com Optuna e obtenção de best_params_optuna) ...

        # Divide X_train_optuna_selected e y_train_optuna em conjuntos finais de treino e validação interna
        # Esta validação interna é para o early stopping do modelo final.
        X_train_final, X_val_internal, y_train_final, y_val_internal = train_test_split(
            X_train_optuna_selected, y_train_optuna, 
            test_size=0.20, # 20% para validação interna, 80% para treino final
            random_state=42, 
            stratify=y_train_optuna # Mantém a proporção das classes
        )

        # Define o objetivo e a métrica para o modelo final, baseado se é binário ou multiclasse
        lgbm_final_objective = 'binary' if is_binary_classification else 'multiclass'
        lgbm_final_metric = 'binary_logloss' if is_binary_classification else 'multi_logloss'

        # Cria a instância final do LGBMClassifier com os melhores parâmetros do Optuna
        best_lgbm = lgb.LGBMClassifier(
            objective=lgbm_final_objective, 
            metric=lgbm_final_metric,
            random_state=42, 
            n_jobs=-1, 
            verbose=-1, # Suprime a maioria dos logs do LightGBM durante o fit
            **best_params_optuna # Desempacota os melhores hiperparâmetros encontrados
        )
        
        # Se for multiclasse, define o número de classes explicitamente
        if not is_binary_classification:
            best_lgbm.set_params(num_class=len(le.classes_)) # le.classes_ vem do LabelEncoder

        print("Treinando o modelo final com early stopping...")
        # Treina o modelo final
        # eval_set é usado para early stopping
        # callbacks=[lgb.early_stopping(25, verbose=False)] para o treinamento se a métrica em
        # X_val_internal não melhorar por 25 rodadas. verbose=False para não imprimir logs do early stopping.
        best_lgbm.fit(
            X_train_final, y_train_final, 
            eval_set=[(X_val_internal, y_val_internal)],
            eval_metric=lgbm_final_metric, 
            callbacks=[lgb.early_stopping(25, verbose=False)] 
        )

        # Obtém o número de árvores efetivamente usado pelo modelo final (devido ao early stopping)
        final_model_iter = best_lgbm.best_iteration_ if hasattr(best_lgbm, 'best_iteration_') and best_lgbm.best_iteration_ is not None else best_params_optuna.get('n_estimators')
        print(f"Modelo final treinado. Número de árvores: {final_model_iter}")

        # Avalia a acurácia do modelo final no seu próprio conjunto de treinamento (para referência)
        y_pred_train_final = best_lgbm.predict(X_train_final)
        accuracy_train_final = accuracy_score(y_train_final, y_pred_train_final)
        print(f"Acurácia do Modelo Final no seu Conjunto de Treinamento (X_train_final): {accuracy_train_final:.4f}")
```
9.  **Avaliação do Modelo Final**:
    * O modelo treinado é usado para fazer previsões no conjunto de teste (`X_test_selected`).
    * São calculadas e exibidas diversas métricas: acurácia, relatório de classificação (precisão, recall, F1-score por classe), matriz de confusão e ROC AUC.
    * A matriz de confusão normalizada e um gráfico de importância das features do modelo final são plotados e salvos.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após o treinamento do modelo final, best_lgbm) ...

        print("\nAvaliação do modelo final no conjunto de teste (com features selecionadas)...")
        
        # Faz previsões no conjunto de teste
        y_pred_test = best_lgbm.predict(X_test_selected)
        
        # Faz previsões de probabilidade para todas as classes (necessário para ROC AUC)
        y_pred_proba_all_classes_test = best_lgbm.predict_proba(X_test_selected)

        # Calcula as métricas
        accuracy_test = accuracy_score(y_test, y_pred_test)
        f1_test = f1_score(y_test, y_pred_test, average='weighted') # Ponderado para levar em conta desbalanceamento

        # Gera o relatório de classificação como dicionário e string
        report_dict_test = classification_report(y_test, y_pred_test, target_names=le.classes_, zero_division=0, output_dict=True)
        report_str_test = classification_report(y_test, y_pred_test, target_names=le.classes_, zero_division=0)

        conf_matrix_test = confusion_matrix(y_test, y_pred_test)
        
        roc_auc_test = 0.0
        if len(le.classes_) >= 2: # ROC AUC só faz sentido com pelo menos 2 classes
            if is_binary_classification:
                # Para binário, usa a probabilidade da classe positiva (geralmente a classe 1)
                roc_auc_test = roc_auc_score(y_test, y_pred_proba_all_classes_test[:, 1]) if y_pred_proba_all_classes_test.shape[1] == 2 else 0.0
            else:
                # Para multiclasse, usa 'ovr' (One-vs-Rest) e média ponderada
                 roc_auc_test = roc_auc_score(y_test, y_pred_proba_all_classes_test, multi_class='ovr', average='weighted')

        # Extrai precisões do relatório para resumo
        macro_avg_precision_test = report_dict_test.get('macro avg', {}).get('precision', 0.0)
        weighted_avg_precision_test = report_dict_test.get('weighted avg', {}).get('precision', 0.0)

        print(f"\n--- Resultados da Avaliação no CONJUNTO DE TESTE (v7 - Final - {'Binário' if is_binary_classification else 'Multiclasse'}) ---")
        print(f"Acurácia no Teste: {accuracy_test:.4f}")
        print(f"Precisão Média (Macro Avg) no Teste: {macro_avg_precision_test:.4f}")
        print(f"Precisão Média (Weighted Avg) no Teste: {weighted_avg_precision_test:.4f}")
        print(f"F1-Score (Ponderado) no Teste: {f1_test:.4f}")
        print(f"ROC AUC ({'Binário' if is_binary_classification else 'Ponderado OVR'}) no Teste: {roc_auc_test:.4f}")
        print("\nRelatório de Classificação (Teste):\n", report_str_test)

        # Plotagem e salvamento da Matriz de Confusão Normalizada
        conf_matrix_normalized_test = None
        # Verifica se a normalização é possível (evita divisão por zero se uma classe não tiver amostras verdadeiras)
        if len(le.classes_) > 1 and conf_matrix_test.sum(axis=1, keepdims=True).all() > 0 :
            conf_matrix_normalized_test = conf_matrix_test.astype('float') / conf_matrix_test.sum(axis=1, keepdims=True)
            plt.figure(figsize=(max(8, len(le.classes_)*1.5), max(6, len(le.classes_)*1.2)))
            sns.heatmap(conf_matrix_normalized_test, annot=True, fmt=".2%", cmap="Blues", xticklabels=le.classes_, yticklabels=le.classes_)
            plt.title(f'Matriz de Confusão Normalizada (Teste - v7 Final - {"Binário" if is_binary_classification else "Multiclasse"})')
            plt.ylabel('Classe Verdadeira'); plt.xlabel('Classe Prevista')
            plt.savefig('visualizacoes_classificacao_salario_v7_rfecv/matriz_confusao_norm_v7_final_teste.png')
            plt.show() # No notebook, isso exibe o gráfico
            plt.close()
        elif len(le.classes_) > 1:
            print("Aviso: Não foi possível normalizar a matriz de confusão (alguma classe pode não ter amostras verdadeiras no conjunto de teste).")

        # Plotagem e salvamento da Importância das Features
        feature_importance_df = None
        if hasattr(best_lgbm, 'feature_importances_') and X_train_final.shape[1] > 0: # X_train_final tem as features selecionadas
            feature_importance_df = pd.DataFrame({
                'feature': X_train_final.columns, # Nomes das features usadas no modelo final
                'importance': best_lgbm.feature_importances_
            }).sort_values(by='importance', ascending=False)
            
            print("\nImportância das Features (após RFECV, modelo Optuna com ES):\n", feature_importance_df.head(min(15, len(X_train_final.columns))))
            
            plt.figure(figsize=(10, max(6, len(feature_importance_df.head(min(15, len(X_train_final.columns)))) * 0.5)))
            sns.barplot(x='importance', y='feature', data=feature_importance_df.head(min(15, len(X_train_final.columns))))
            plt.title(f'Top {min(15, len(X_train_final.columns))} Features (v7 Final - {"Binário" if is_binary_classification else "Multiclasse"})')
            plt.tight_layout()
            plt.savefig('visualizacoes_classificacao_salario_v7_rfecv/feature_importance_v7_final.png')
            plt.show() # No notebook, isso exibe o gráfico
            plt.close()
```
10. **Salvamento de Resultados e Modelo**:
    * Um arquivo de texto com os resultados detalhados e os parâmetros é salvo.
    * O modelo treinado, o `LabelEncoder`, as features selecionadas e o `StandardScaler` são salvos em um arquivo `.pkl` usando `pickle` para uso futuro (ex: previsões em novos dados ou análises adicionais).

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após a avaliação do modelo final) ...

        results_filename_txt = "modelo_classificacao_faixa_salarial_v7_final_rfecv_resultados.txt"
        model_filename_pkl = 'modelo_lgbm_classificacao_faixa_salarial_v7_final_rfecv.pkl'
        
        with open(results_filename_txt, "w", encoding="utf-8") as f:
            f.write(f"Modelo: LightGBM (Optuna, RFECV, ES) para classificação de Faixa Salarial (v7 Final - {'Binário' if is_binary_classification else f'Multiclasse ({len(le.classes_)} classes)'})\\n")
            f.write(f"Coluna Alvo Agrupada: {target_col_agrupada_name} com classes: {list(le.classes_)}\\n")
            # initial_feature_columns_after_region contém as features antes do RFECV, após mapeamento de UF
            f.write(f"Features Iniciais para processamento ({len(initial_feature_columns_after_region)}): {initial_feature_columns_after_region}\\n")
            f.write(f"Features Selecionadas pelo RFECV ({rfecv_selector.n_features_}): {selected_features_names}\\n\\n")
            
            f.write(f"Melhores parâmetros (Optuna): {best_params_optuna}\\n")
            f.write(f"Número de árvores usadas pelo modelo final: {final_model_iter}\\n\\n")
            
            f.write(f"Acurácia Média CV/Val (Optuna): {best_optuna_score:.4f}\\n")
            f.write(f"Acurácia do Modelo Final no seu Conjunto de Treinamento (X_train_final): {accuracy_train_final:.4f}\\n\\n")
            
            f.write(f"RESULTADOS NO CONJUNTO DE TESTE:\\n")
            f.write(f"  Acurácia no Teste: {accuracy_test:.4f}\\n")
            f.write(f"  Precisão Média (Macro Avg) no Teste: {macro_avg_precision_test:.4f}\\n")
            f.write(f"  Precisão Média (Weighted Avg) no Teste: {weighted_avg_precision_test:.4f}\\n")
            f.write(f"  F1-Score (Ponderado) no Teste: {f1_test:.4f}\\n")
            f.write(f"  ROC AUC ({'Binário' if is_binary_classification else 'Ponderado OVR'}) no Teste: {roc_auc_test:.4f}\\n\\n")
            
            f.write("Relatório de Classificação (Teste):\\n"); f.write(report_str_test)
            f.write("\\nMatriz de Confusão (Teste - Absoluta):\\n"); f.write(str(conf_matrix_test)) # Salva a matriz de confusão absoluta
            
            if feature_importance_df is not None:
                 f.write("\\n\\nImportância das Features:\\n"); f.write(feature_importance_df.to_string())

        # Salva o modelo e outros objetos necessários para inferência/análise futura
        with open(model_filename_pkl, 'wb') as f: 
            pickle.dump({
                'model': best_lgbm, 
                'label_encoder': le, 
                'selected_features': selected_features_names,
                'scaler_rfecv_fitted_on_initial_numerical': scaler_rfecv, # O scaler ajustado em X_initial
                'original_columns_for_scaler': numerical_features_present_after_outliers, # Colunas em que o scaler foi ajustado
                'is_binary_classification': is_binary_classification,
                'target_col_name': target_col_agrupada_name
            }, f)
        print(f"Modelo e metadados salvos em {model_filename_pkl}")

        # Retorna um dicionário com os principais resultados
        return {
            'accuracy_train_final': accuracy_train_final,
            'optuna_best_cv_score': best_optuna_score,
            'accuracy_test': accuracy_test,
            'macro_avg_precision_test': macro_avg_precision_test,
            'weighted_avg_precision_test': weighted_avg_precision_test,
            'f1_score_test': f1_test,
            'roc_auc_test': roc_auc_test,
            'selected_features_count': rfecv_selector.n_features_,
            'selected_features_names': selected_features_names,
            'best_params': best_params_optuna, 
            'model_object_path': model_filename_pkl,
            'final_model_best_iteration': final_model_iter,
            'classification_report_dict_test': report_dict_test,
            'is_binary_classification': is_binary_classification,
            'target_classes': list(le.classes_)
        }

    except Exception as e:
        print(f"Ocorreu um erro inesperado na função principal: {e}")
        traceback.print_exc(); return None
```
11. **Retorno de Resultados**:
    * A função retorna um dicionário contendo as principais métricas e informações da execução.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após o salvamento do modelo e dos resultados em arquivo) ...

        # Retorna um dicionário com os principais resultados e informações da execução
        return {
            'accuracy_train_final': accuracy_train_final,
            'optuna_best_cv_score': best_optuna_score,
            'accuracy_test': accuracy_test,
            'macro_avg_precision_test': macro_avg_precision_test,
            'weighted_avg_precision_test': weighted_avg_precision_test,
            'f1_score_test': f1_test,
            'roc_auc_test': roc_auc_test,
            'selected_features_count': rfecv_selector.n_features_,
            'selected_features_names': selected_features_names,
            'best_params': best_params_optuna, 
            'model_object_path': model_filename_pkl, # Caminho para o arquivo .pkl salvo
            'final_model_best_iteration': final_model_iter, # Número de árvores do modelo final
            'classification_report_dict_test': report_dict_test, # Relatório de classificação como dicionário
            'is_binary_classification': is_binary_classification, # Flag se é binário
            'target_classes': list(le.classes_) # Nomes das classes do alvo
        }

    # Bloco try-except principal da função
    except Exception as e:
        print(f"Ocorreu um erro inesperado na função principal: {e}")
        traceback.print_exc()
        return None # Retorna None em caso de erro para indicar falha na execução
```
Este processo estruturado visa garantir que o modelo seja treinado de forma eficiente, otimizado para o melhor desempenho possível nos dados disponíveis e avaliado de maneira justa em dados não vistos, fornecendo insights sobre a importância das features no problema de classificação da faixa salarial.

> Este fluxo demonstra uma abordagem robusta para modelagem, incluindo pré-processamento cuidadoso, seleção de features, otimização de hiperparâmetros e avaliação rigorosa usando múltiplas técnicas de particionamento de dados.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Indução de modelos

# Modelo 3.1(segundo modelo da 3° pergunta orientada a dados): Rede Neural com Embeddings e Otimização via Ray Tune (RNA v2)

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

>Este processo visa construir um modelo de rede neural otimizado e avaliado de forma robusta, fornecendo insights sobre os fatores que determinam as faixas salariais, focando na capacidade da RNA de aprender representações e interações complexas.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Resultados


*   [Resultados obtidos com o modelo 1.](#resultados-obtidos-com-o-modelo-1) 
	*   [top3_features](#top3_features)
	*   [precision_recall_curve](#precision_recall_curve)
 	*   [matriz_confusao_otimizada](#matriz_confusao_otimizada) 
	*   [interacao_formacao_experiencia](#interacao_formacao_experiencia)
	*   [importancia_features_top20](#importancia_features_top20)
	*   [importancia_features_grupo_UF onde mora](#importancia_features_grupo_uf-onde-mora)
	*   [importancia_features_grupo_Setor de atuação da empresa](#importancia_features_grupo_setor-de-atuação-da-empresa)
	*   [importancia_features_grupo_senioridade](#importancia_features_grupo_senioridade)
	*   [importancia_features_grupo_formacao](#importancia_features_grupo_formacao)
	*   [importancia_features_grupo_experiencia](#importancia_features_grupo_experiencia)
	*   [importancia_features_grupo_Área de formação acadêmica](#importancia_features_grupo_área-de-formação-acadêmica)
	*   [distribuicao_probabilidades](#distribuicao_probabilidades)
	*   [dispersao_top2_features](#dispersao_top2_features)
	*   [curva_roc_otimizada](#curva_roc_otimizada)
	*   [arvore_exemplo_simplificada](#arvore_exemplo_simplificada)
	*   [arvore_exemplo_melhorada](#arvore_exemplo_melhorada)


*   [Resultados obtidos com o modelo 2.](#resultados-obtidos-com-o-modelo-2)

*   [Resultados obtidos com o modelo 3.](#resultados-obtidos-com-o-modelo-3)




## Resultados obtidos com o modelo 1.


| Classe          | Precisão | Recall | F1-Score | Suporte |
|-----------------|----------|--------|----------|---------|
| Salário Baixo/Médio    | 0.84     | 0.84   | 0.84     | 568     |
| Salário Alto | 0.79     | 0.78   | 0.78     | 422     |
| accuracy |  |  | **0.82** | **990** |
| macro avg | **0.81** | **0.81** | **0.81** | **990** |
| weighted avg | **0.81** | **0.82** | **0.82** | **990** |

- Acurácia do Modelo: 0.82
- Acurácia do Modelo no Conjunto de Treinamento: -
- Acurácia do Modelo no Conjunto de Teste: -
- Diferença de Acurácia (Treino - Teste): -

**Parâmetros do Modelo Random Forest Utilizado:**

### top3_features
![top3_features](https://github.com/user-attachments/assets/02f25d1b-4639-4cd9-a357-7a89297bff03)

### precision_recall_curve
![precision_recall_curve (1)](https://github.com/user-attachments/assets/c74124a4-f6b4-4592-9011-bba7013e93f4)

### matriz_confusao_otimizada
![matriz_confusao_otimizada (1)](https://github.com/user-attachments/assets/44b373ea-b840-4d47-afd7-804967449a49)

### interacao_formacao_experiencia
![interacao_formacao_experiencia (1)](https://github.com/user-attachments/assets/c6c03e66-554e-42db-a435-e5e909bb9857)

### importancia_features_top20
![importancia_features_top20](https://github.com/user-attachments/assets/cbfc487f-4a48-45e1-8a0a-b5ccdf0b2bb5)

### importancia_features_grupo_UF onde mora
![importancia_features_grupo_UF onde mora](https://github.com/user-attachments/assets/45719ffa-d305-41f2-b595-4bb70ee884bc)

### importancia_features_grupo_Setor de atuação da empresa
![importancia_features_grupo_Setor de atuação da empresa](https://github.com/user-attachments/assets/af6a6298-28fc-4629-890e-c645aa54ca47)

### importancia_features_grupo_senioridade
![importancia_features_grupo_senioridade](https://github.com/user-attachments/assets/88a8e6a4-5bff-4e58-a613-523fe4915bed)

### importancia_features_grupo_formacao
![importancia_features_grupo_formacao](https://github.com/user-attachments/assets/e9180d58-b603-4e09-9f57-a94ecc4d824f)

### importancia_features_grupo_experiencia
![importancia_features_grupo_experiencia](https://github.com/user-attachments/assets/bffd0e4f-bc56-42d1-802c-ea1b22b872b7)

### importancia_features_grupo_Área de formação acadêmica
![importancia_features_grupo_Área de formação acadêmica](https://github.com/user-attachments/assets/17e5dd69-f141-4fc0-b0e5-fbb180912aeb)

### distribuicao_probabilidades
![distribuicao_probabilidades (1)](https://github.com/user-attachments/assets/f7ed3668-f41f-486f-87bd-dbac9fcd74f1)

### dispersao_top2_features
![dispersao_top2_features](https://github.com/user-attachments/assets/99eb2c9f-d3ef-47d7-b337-5431c00d0571)

### curva_roc_otimizada
![curva_roc_otimizada (1)](https://github.com/user-attachments/assets/2bd509b0-24c8-46ad-9bb0-b18203609795)

### arvore_exemplo_simplificada
![arvore_exemplo_simplificada](https://github.com/user-attachments/assets/a4d395fd-d40a-43e0-a655-1cc5eece761e)

### arvore_exemplo_melhorada
![arvore_exemplo_melhorada](https://github.com/user-attachments/assets/410ea2af-736a-4cbf-9541-d0edb1ac49d1)



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Resultados obtidos com o modelo 2.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Resultados obtidos com o modelo 3.


### Relatório de Resultados e Insights: Classificação Binária de Faixa Salarial (v7)

Este relatório detalha os resultados da última execução do modelo LightGBM para classificação binária da faixa salarial ("Salário Alto" vs. "Salário Baixo"). A análise inclui métricas de desempenho, a importância das features e uma interpretação dos gráficos gerados para extrair insights.

### 1. Resumo do Desempenho do Modelo

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

## 2. Configuração do Modelo

### 2.1. Features Selecionadas pelo RFECV
As 6 features selecionadas foram: `['P1_a_1', 'P1_l', 'P2_i', 'P2_g_Nivel', 'P2_f_Cargo_Atual', 'Regiao_Mapeada']`
*(Nota: A sua última saída do RFECV indicou 6 features, diferente de saídas anteriores que indicavam 7. Este relatório baseia-se na última informação de 6 features.)*

### 2.2. Melhores Hiperparâmetros (Optuna) para LightGBM
* `n_estimators`: 1100 (modelo final usou 105 árvores devido ao early stopping)
* `learning_rate`: 0.06509228494862056
* `num_leaves`: 80
* `max_depth`: 12
* `min_child_samples`: 25
* `subsample`: 0.5
* `colsample_bytree`: 0.6000000000000001
* `reg_alpha`: 1.5671157141467156
* `reg_lambda`: 14.655960291115573
* `min_split_gain`: 0.3854595582770911
* `min_child_weight`: 0.1393188921160219

## 3. Análise e Insights dos Gráficos Gerados

A seguir, uma interpretação dos gráficos que seu script gera. *Para incluir os gráficos diretamente neste relatório Markdown, você precisaria converter este texto para um formato que suporte a incorporação de imagens (como HTML ou PDF) e inserir os arquivos .png gerados.*

### 3.1. Matriz de Confusão Normalizada (Teste)


* **Nome do arquivo**: `matriz_confusao_norm_v7_final_teste.png`
* **O que ela informa**: A matriz de confusão mostra o desempenho do modelo em termos de classificações corretas e incorretas para cada classe. As porcentagens na diagonal principal representam as taxas de acerto (recall) para cada classe.
    * **Salário Alto (Verdadeiro) -> Salário Alto (Previsto)**: Aproximadamente 84.08% (diagonal superior esquerda na sua imagem `download (77).png`). O modelo acertou 84.08% dos casos que eram de fato "Salário Alto".
    * **Salário Baixo (Verdadeiro) -> Salário Baixo (Previsto)**: Aproximadamente 82.54% (diagonal inferior direita na sua imagem `download (77).png`). O modelo acertou 82.54% dos casos que eram de fato "Salário Baixo".
    * **Fora da diagonal**: Representam os erros.
        * ~15.92% dos "Salário Alto" foram incorretamente classificados como "Salário Baixo".
        * ~17.46% dos "Salário Baixo" foram incorretamente classificados como "Salário Alto".
* **Possíveis Insights**:
    * O modelo tem um desempenho similar e bom para ambas as classes, com recall em torno de 83-84%.
    * Há uma taxa de erro relativamente equilibrada entre confundir "Salário Alto" com "Baixo" e vice-versa.
    * O equilíbrio na distribuição de suporte (622 vs 567) ajuda a dar confiança de que o modelo não está excessivamente enviesado para uma classe.

![Image](https://github.com/user-attachments/assets/2e9d9ea5-2a0b-42ae-bd7e-5d4cc188a293)


## 3.2. Importância das Features

**Nome do arquivo:** `feature_importance_v7_final.png`

**O que ela informa:** Este gráfico de barras horizontais mostra quais features tiveram o maior impacto nas decisões do modelo LightGBM. A importância é geralmente calculada com base em quantas vezes uma feature foi usada para dividir os dados nas árvores do modelo e o quanto essa divisão melhorou a métrica (ganho).
Na sua última saída, as features mais importantes foram:
`P2_i` (Tempo de experiência)
`P2_f_Cargo_Atual` (Cargo atual)
`P2_g_Nivel` (Nível de senioridade)
`P1_l` (Nível de ensino)
`P1_a_1` (Faixa etária)
`Regiao_Mapeada` (Região onde mora)

**Possíveis Insights:**
* Experiência (`P2_i`) e Cargo (`P2_f_Cargo_Atual`) são os preditores mais fortes da faixa salarial, o que é intuitivo.
* Nível de senioridade (`P2_g_Nivel`), nível de ensino (`P1_l`) e faixa etária (`P1_a_1`) também têm contribuições significativas.
* A `Regiao_Mapeada` tem uma importância considerável, sugerindo disparidades regionais nos salários.
* Features como `P1_b` (Gênero), que foi eliminada pelo RFECV na última execução (6 features selecionadas), teriam menor impacto direto na predição deste modelo específico, embora possam interagir com outras features ou ter impacto em análises mais aprofundadas de equidade.

![Image](https://github.com/user-attachments/assets/48fd3daf-dc28-4a8f-bc89-9459b1945aee)
 
 ---
 
## 3.3. Distribuição de Faixa Salarial por Top 15 Cargos

**Nome do arquivo:** `insight_cargo_vs_faixa_salarial_2cat.png`
 
**O que ela informa:** É um gráfico de contagem (countplot) que mostra, para os 15 cargos mais frequentes, quantas pessoas se enquadram em "Salário Baixo" e "Salário Alto".
 
**Possíveis Insights:**
* **Cargos com Predominância de "Salário Alto":** Cientista de Dados, Engenheiro/Arquiteto de Dados, Analista de Negócios/Business Analyst (embora este também tenha muitos "Salário Baixo", a proporção de "Salário Alto" é notável).
* **Cargos com Predominância de "Salário Baixo":** Analista de Dados/Data Analyst, Analista de BI/BI Analyst, "Outra Opção", Desenvolvedor/Engenheiro de Software/Analista de Sistemas.
* **Insights Específicos:**
    * "Analista de Dados/Data Analyst" é um cargo muito comum, mas a grande maioria está na faixa "Salário Baixo".
    * "Cientista de Dados/Data Scientist" tem uma proporção significativamente maior de "Salário Alto" em comparação com "Analista de Dados".
    * Cargos como "Professor/Pesquisador" e "Estatístico" aparecem com poucas amostras no Top 15, mas os que aparecem tendem a "Salário Alto".
* Isso pode guiar investigações sobre quais cargos estão associados a melhores remunerações e onde há maior concentração de salários mais baixos.
 
![Image](https://github.com/user-attachments/assets/ba7c4d30-870f-48f7-951f-cc2263f9c65a)
 
 ---
 
## 3.4. Distribuição de Faixa Salarial por Nível de Senioridade
 
**Nome do arquivo:** `insight_nivel_vs_faixa_salarial_2cat.png`
 
**O que ela informa:** Um countplot mostrando a distribuição de "Salário Baixo" e "Salário Alto" para cada nível de senioridade (`P2_g_Nivel`).
 
**Possíveis Insights:**
* **Sênior:** Predominantemente "Salário Alto", com uma contagem quase igual de "Salário Baixo". Isso pode indicar que mesmo em níveis sênior, uma parcela considerável ainda se enquadra no que foi definido como "Salário Baixo" pelo ponto de corte.
* **Pleno:** Uma grande maioria na categoria "Salário Baixo", com uma pequena parcela em "Salário Alto". Este é o nível com maior número de respondentes.
* **Júnior:** Quase exclusivamente "Salário Baixo", com pouquíssimas ou nenhuma ocorrência em "Salário Alto".
* Este gráfico claramente demonstra a progressão salarial esperada com o aumento da senioridade. O caso "Sênior" com uma quantidade relevante de "Salário Baixo" pode merecer uma investigação mais aprofundada (talvez o ponto de corte para "Salário Alto" seja muito exigente, ou há seniors em áreas/empresas que pagam menos).

![Image](https://github.com/user-attachments/assets/3ee422da-3ebc-4ab5-92d0-208953caf231)
 
 ---
 
## 3.5. Boxplot e Violin Plot de Tempo de Experiência por Faixa Salarial
 
**Nomes dos arquivos:** `insight_experiencia_vs_faixa_salarial_2cat_boxplot.png` e `insight_experiencia_vs_faixa_salarial_2cat_violin.png`.
 
**O que eles informam:**
* **Boxplot:** Mostra a distribuição do tempo de experiência (em anos) para cada faixa salarial. Exibe a mediana (linha no meio da caixa), os quartis (bordas da caixa - IQR), e possíveis outliers (pontos).
* **Violin Plot:** Similar ao boxplot, mas também mostra a densidade da distribuição da experiência para cada faixa salarial (a "largura" do violino indica onde os dados estão mais concentrados).
 
**Possíveis Insights:**
* **Salário Baixo:**
     * A mediana da experiência é baixa (parece estar entre 1 e 2 anos no boxplot).
     * A maioria dos dados está concentrada em poucos anos de experiência (0-3 anos, aproximadamente, como visto pela largura do violino e a caixa do boxplot).
     * Há alguns outliers com mais experiência que ainda estão na faixa de "Salário Baixo".
* **Salário Alto:**
     * A mediana da experiência é significativamente mais alta (parece estar em torno de 5 anos no boxplot).
     * A distribuição da experiência é mais ampla e espalhada para cima, com uma concentração notável em torno de 2-3 anos e depois novamente em níveis mais altos de experiência. O violin plot mostra múltiplas "modas" ou concentrações.
     * O IQR (caixa do boxplot) é maior, indicando maior variabilidade na experiência para quem está em "Salário Alto".
* **Comparação:** Claramente, indivíduos com "Salário Alto" tendem a ter mais tempo de experiência. O violin plot para "Salário Alto" é interessante, pois sugere que há diferentes "grupos" de experiência que alcançam salários altos – talvez alguns com menos anos, mas em posições/empresas específicas, e um grupo maior com experiência mais consolidada. Os outliers de "Salário Baixo" com alta experiência podem ser casos de transição de carreira, atuação em setores/regiões com menor remuneração, ou outras particularidades.
 
![Image](https://github.com/user-attachments/assets/390ae2c5-36e8-4af9-9eda-ba46a1abaf7b)
![Image](https://github.com/user-attachments/assets/c8674650-d96c-4932-972b-c8d1a0ac64f9)
 
 ---
 
## 4. Considerações Finais
 
Os resultados indicam que o modelo LightGBM tem um bom potencial para classificar faixas salariais. 
A análise da importância das features e dos gráficos de distribuição fornece insights valiosos sobre os fatores que influenciam os salários e como eles se relacionam com as duas categorias definidas. 
A escolha do `point_of_cut_fixed` é crucial para a definição das classes e afeta diretamente a interpretação e o balanceamento do suporte. 
Ajustes iterativos nesse ponto de corte, com base na análise do histograma de salários e nos objetivos de balanceamento, são recomendados para refinar ainda mais o modelo e os insights.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Indução de modelos

# Modelo 4: Rede Neural com Embeddings e Otimização via Ray Tune (RNA v2)

## 1. Justificativa e Objetivo

O objetivo deste modelo é classificar a faixa salarial de indivíduos em duas categorias: "Salário Baixo" e "Salário Alto", utilizando uma abordagem de rede neural artificial (RNA). A intenção é explorar se uma arquitetura de RNA, com capacidade de aprender interações complexas e representações ricas para features categóricas (via embeddings), pode oferecer um desempenho comparável ou superior aos modelos baseados em árvores para a mesma pergunta orientada a dados.

A classificação binária ("Salário Baixo" vs. "Salário Alto") visa simplificar o problema e potencialmente melhorar a distinção entre os grupos salariais. Foi utilizado um ponto de corte fixo de R$ 7.500,00 para a variável `salary_numeric_lower_bound` para realizar essa divisão. Com base nos logs anteriores, isso resultou em aproximadamente 2268 amostras para "Salário Baixo" e 2485 para "Salário Alto" no dataset processado antes da divisão treino/teste.

## 2. Processo de Amostragem de Dados e Configuração do Modelo RNA v2

(Esta seção detalharia as etapas de particionamento de dados, pré-processamento específico para RNA como escalonamento e label encoding + embeddings, a arquitetura da rede neural Keras, e a otimização de hiperparâmetros com Ray Tune, conforme discutido e implementado no código da RNA v2).

### 2.1. Features Utilizadas (Entrada para a RNA v2)
As features utilizadas diretamente pela Rede Neural v2 foram (após mapeamento e tratamento inicial):
* Faixa etária (`P1_a_1`)
* Gênero (`P1_b`)
* Nível de ensino (`P1_l`)
* Tempo de experiência na área de dados (`P2_i`)
* Nível de senioridade (`P2_g_Nivel`)
* Cargo atual (`P2_f_Cargo_Atual`)
* Região Mapeada (derivada da UF)

### 2.2. Melhores Hiperparâmetros (Ray Tune) para RNA v2 (Exemplo da Última Execução Bem-Sucedida)
* `dense_units_1`: 64
* `dense_units_2`: 128 (mas `num_hidden_layers`: 1, então esta não foi usada)
* `dropout_1`: 0.45
* `dropout_2`: 0.30 (não usada se `num_hidden_layers`: 1)
* `learning_rate_nn`: 0.0002366...
* `batch_size`: 32
* `epochs`: 50 (controlado por EarlyStopping)
* `num_hidden_layers`: 1
* `early_stopping_patience`: 10
* `l2_strength_embedding`: 0.0046...
* `l2_strength_dense`: 4.19e-05
* `optimizer`: 'adam'
* `emb_dim_P1_a_1`: 8, `emb_dim_P1_b`: 4, `emb_dim_P1_l`: 4, `emb_dim_P2_g_Nivel`: 4, `emb_dim_P2_f_Cargo_Atual`: 9, `emb_dim_Regiao_Mapeada`: 4

## 3. Resultados da Avaliação da Rede Neural v2 (RNA v2)

Com base nos logs da última execução bem-sucedida:

| Métrica                          | Valor  |
| :------------------------------- | :----- |
| **Melhor Acurácia Validação HPO**| 0.8345 |
| **Acurácia no Teste** | 0.8377 |
| Precisão Média (Macro Avg) Teste | 0.8377 (calculado a partir do relatório) |
| F1-Score (Ponderado) Teste       | 0.8377 |
| **ROC AUC (Binário) Teste** | 0.9263 |

**Relatório de Classificação Detalhado (Teste - RNA v2):**

| Classe        | Precision | Recall | F1-score | Support |
| :------------ | :-------- | :----- | :------- | :------ |
| Salário Alto  | 0.85      | 0.84   | 0.84     | 622     |
| Salário Baixo | 0.83      | 0.84   | 0.83     | 567     |
|               |           |        |          |         |
| accuracy      |           |        | 0.84     | 1189    |
| macro avg     | 0.84      | 0.84   | 0.84     | 1189    |
| weighted avg  | 0.84      | 0.84   | 0.84     | 1189    |

*(Nota: Os valores de Precision, Recall, F1-score para macro e weighted avg no relatório acima são ligeiramente diferentes dos que constavam no log de resumo para Precisão Média (Macro Avg). Utilizei os valores do relatório de classificação mais detalhado do seu último log para esta tabela.)*

## 4. Análise e Insights dos Gráficos Gerados (Contexto RNA v2)

### 4.1. Matriz de Confusão Normalizada (Teste - RNA v2)

* **Nome do arquivo (gerado pelo script de plotagem adaptado)**: `matriz_confusao_norm_RNA.png` (substituindo a imagem `download.png` fornecida).
* **O que ela informa**: A matriz de confusão mostra o desempenho do modelo RNA v2 em termos de classificações corretas e incorretas para cada classe no conjunto de teste. As porcentagens na diagonal principal representam as taxas de acerto (recall) para cada classe.
    * **Salário Alto (Verdadeiro) -> Salário Alto (Previsto)**: Aproximadamente 83.60% (valor da imagem `download.png` que você forneceu). *Este valor deve ser consistente com o Recall de "Salário Alto" do relatório de classificação da RNA v2, que foi 0.84.*
    * **Salário Baixo (Verdadeiro) -> Salário Baixo (Previsto)**: Aproximadamente 83.95% (valor da imagem `download.png` que você forneceu). *Este valor deve ser consistente com o Recall de "Salário Baixo" do relatório de classificação da RNA v2, que foi 0.84.*
    * **Fora da diagonal**: Representam os erros.
        * ~16.40% dos "Salário Alto" foram incorretamente classificados como "Salário Baixo" (pela imagem `download.png`).
        * ~16.05% dos "Salário Baixo" foram incorretamente classificados como "Salário Alto" (pela imagem `download.png`).
* **Possíveis Insights**:
    * O modelo RNA v2 apresenta um bom equilíbrio no desempenho entre as classes, com recall em torno de 84% para ambas, conforme o relatório de classificação.
    * As taxas de erro entre confundir "Salário Alto" com "Baixo" e vice-versa são relativamente similares.

*(Placeholder para a imagem da matriz de confusão da RNA v2 - `download.png`)*
![Matriz de Confusão RNA v2](download.png)

### 4.2. Importância das Features (RNA v2)

* **O que ela informa**: Para redes neurais, a "importância das features" não é obtida diretamente como em modelos baseados em árvores. Técnicas como Permutation Importance ou SHAP values podem ser aplicadas para estimar a contribuição de cada feature.
* **Possíveis Insights (Geral, com base na expectativa e na seleção de features para a RNA v2)**:
    * Espera-se que features ligadas à **proficiência técnica** como `P2_i` (Tempo de experiência), `P2_f_Cargo_Atual` (Cargo atual) e `P2_g_Nivel` (Nível de senioridade) tenham um impacto significativo.
    * **Características demográficas** como `P1_l` (Nível de ensino), `P1_a_1` (Faixa etária) e `P1_b` (Gênero) também são consideradas pelo modelo e sua influência pode ser analisada com as técnicas mencionadas.
    * A `Regiao_Mapeada` também é um fator que o modelo considera.
    * A análise quantitativa exata da importância requereria a aplicação das técnicas mencionadas (Permutation Importance ou SHAP) no modelo RNA v2 treinado.

---

### 4.3. Distribuição de Faixa Salarial (Real) por Top 15 Cargos (Contexto RNA v2)

* **Nome do arquivo**: `dist_salario_top15_cargos_RNA_contexto.png`
* **O que ela informa**: Mostra, para os 15 cargos mais frequentes no dataset, a contagem de profissionais que se enquadram na categoria "Salário Baixo" versus "Salário Alto" (com base na variável alvo real). Isso fornece o contexto dos dados que a RNA tentou modelar.
* **Possíveis Insights**:
    * Permite identificar cargos onde há uma predominância de profissionais em faixas salariais mais altas ou mais baixas.
    * Por exemplo, cargos como "Cientista de Dados" e "Engenheiro de Dados" tendem a ter uma proporção maior de "Salário Alto", enquanto "Analista de Dados" pode ter uma maior concentração em "Salário Baixo".
    * A RNA tenta aprender esses padrões para realizar suas classificações.

*(Placeholder para a imagem `dist_salario_top15_cargos_RNA_contexto.png`)*
![Distribuição de Faixa Salarial por Top 15 Cargos](dist_salario_top15_cargos_RNA_contexto.png)

---

### 4.4. Distribuição de Faixa Salarial (Real) por Nível de Senioridade (Contexto RNA v2)

* **Nome do arquivo**: `dist_salario_senioridade_RNA_contexto.png`
* **O que ela informa**: Apresenta a distribuição de "Salário Baixo" e "Salário Alto" (variável alvo real) para cada nível de senioridade.
* **Possíveis Insights**:
    * Demonstra a progressão salarial esperada com o aumento da senioridade: Júniores majoritariamente em "Salário Baixo", Plenos com uma mistura, e Sêniores com uma proporção maior em "Salário Alto".
    * A RNA utiliza o nível de senioridade como uma feature importante para distinguir as faixas salariais.

*(Placeholder para a imagem `dist_salario_senioridade_RNA_contexto.png`)*
![Distribuição de Faixa Salarial por Nível de Senioridade](dist_salario_senioridade_RNA_contexto.png)

---

### 4.5. Boxplot e Violin Plot de Tempo de Experiência (Real) por Faixa Salarial (Contexto RNA v2)

* **Nome do arquivo**: `dist_experiencia_salario_RNA_contexto.png` (Esta imagem parece ser os dois plots combinados ou um deles. Assumirei que representa ambos os conceitos).
* **O que eles informam**:
    * Mostram a distribuição do tempo de experiência (em anos) para os profissionais classificados na variável alvo real como "Salário Baixo" versus "Salário Alto".
    * Exibem medianas, quartis e a densidade da distribuição da experiência.
* **Possíveis Insights**:
    * Indivíduos na faixa "Salário Alto" tendem a ter, em média e mediana, mais tempo de experiência.
    * A dispersão da experiência pode ser diferente entre as duas faixas salariais. O violin plot pode revelar se há concentrações específicas de anos de experiência que levam a salários mais altos.
    * A experiência é uma das features mais importantes para a RNA, e estes gráficos ilustram o porquê.

*(Placeholder para a imagem `dist_experiencia_salario_RNA_contexto.png`)*
![Boxplot e Violin Plot de Tempo de Experiência por Faixa Salarial](dist_experiencia_salario_RNA_contexto.png)

---

Este relatório adaptado foca nos resultados e no contexto da Rede Neural v2, utilizando a estrutura do seu `Explicacao_do_modelo.txt` como base e incorporando as imagens fornecidas.

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




