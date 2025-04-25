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
    *   [Modelo 1 gbm (gradient boosting machines) modelo baseado em árvore de decisão](#modelo-1-gbm-(gradient-boosting-machines)-modelo-baseado-em-árvore-de-decisão)
    *   [Modelo 2: Algoritmo](#modelo-2-algoritmo)
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

### Atributos relevantes para temática da base de dados principal
#### **State of Data Brazil** DATA HACKERS. State of Data Brazil 2023. Disponível em: https://www.kaggle.com/datasets/datahackers/state-of-data-brazil-2023. Acesso em: 4 Abr. 2025.


| Atributo                                           | Código de Referência | Tipo         | Subtipo                             | Descrição                                                                                     | Relevância |
|----------------------------------------------------|-----------------------|--------------|-------------------------------------|-----------------------------------------------------------------------------------------------|------------|
| Idade                                              | P1a                   | Quantitativo | Discreto                            | Idade do respondente                                                                          | Alta       |
| Faixa etária                                       | P1a1                  | Qualitativo  | Ordinal                             | Faixa etária do respondente                                                                   | Alta       |
| Gênero                                             | P1b                   | Qualitativo  | Nominal (Multivalorado)             | Identidade de gênero do respondente                                                           | Alta       |
| Cor/Raça/Etnia                                     | P1c                   | Qualitativo  | Nominal (Multivalorado)             | Cor, raça ou etnia do respondente                                                             | Alta       |
| Pessoa com Deficiência (PCD)                       | P1d                   | Qualitativo  | Nominal (Binário)                   | Indicação se o respondente é uma pessoa com deficiência                                       | Alta       |
| UF onde mora                                       | P1i1                  | Qualitativo  | Nominal (Multivalorado)             | Unidade Federativa onde o respondente reside                                                  | Média      |
| Experiência profissional prejudicada              | P1e                   | Qualitativo  | Nominal (Binário)                   | Indicação geral se o respondente acredita que sua experiência foi prejudicada por discriminação | Alta       |
| Não acredito que minha experiência profissional seja afetada     | P1e1                  | Qualitativo  | Nominal (Binário)                   | Resposta indicando que o respondente não acredita que sua experiência foi afetada             | Alta       |
| Experiência prejudicada devido à minha Cor/Raça/Etnia            | P1e2                  | Qualitativo  | Nominal (Binário)                   | Indicação de prejuízo na experiência profissional devido à cor, raça ou etnia                 | Alta       |
| Experiência prejudicada devido à minha identidade de gênero      | P1e3                  | Qualitativo  | Nominal (Binário)                   | Indicação de prejuízo na experiência profissional devido à identidade de gênero               | Alta       |
| Experiência prejudicada devido ao fato de ser PCD                | P1e4                  | Qualitativo  | Nominal (Binário)                   | Indicação de prejuízo na experiência profissional devido ao fato de ser uma pessoa com deficiência (PCD)  | Alta       |
| Quanto tempo de experiência na área de dados você tem?           | P2i                   | Quantitativo  | Discreto                            | Tempo de experiência do respondente na área de dados                                          | Alta       |
| Cargo atual                                        | P2f                   | Qualitativo  | Nominal (Multivalorado)             | Cargo atual ocupado pelo respondente                                                          | Alta       |
| Senioridade das vagas recebidas em relação à sua experiência     | P1f2                  | Qualitativo  | Ordinal                             | Nível de senioridade das vagas recebidas pelo respondente                                     | Média      |
| Nível                                              | P2g                   | Qualitativo  | Ordinal                             | Nível profissional do respondente                                                             | Alta       |
| Faixa salarial                                     | P2h                   | Qualitativo  | Ordinal                             | Faixa salarial do respondente                                                                 | Alta       |

---

### Atributos relevantes da base de dados principal para 1ºpergunta orientada
**Pergunta orientada a dados:** *Como fatores como formação acadêmica, habilidades técnicas e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?*


| Atributo                                         | Nome                                      | Tipo         | Subtipo                             | Descrição                                                                                     | Relevância |
|--------------------------------------------------|-------------------------------------------|--------------|-------------------------------------|-----------------------------------------------------------------------------------------------|------------|
| P1l                                              | Nível de ensino alcançado                 | Qualitativo  | Ordinal                             | Nível de ensino do respondente (graduação, mestrado, etc.)                                    | Alta       |
| P1m                                              | Área de formação acadêmica                | Qualitativo  | Nominal (Multivalorado)             | Área de formação acadêmica do respondente (TI, Economia, etc.)                                | Alta       |
| P2h                                              | Faixa salarial mensal                     | Qualitativo  | Ordinal                             | Faixa salarial mensal do respondente                                                          | Alta       |
| P2i                                              | Tempo de experiência na área de dados     | Quantitativo | Discreto                            | Tempo de experiência do respondente na área de dados (em anos)                                | Alta       |
| P2g                                              | Nível de senioridade                      | Qualitativo  | Ordinal                             | Nível de senioridade do respondente (Júnior, Pleno, Sênior)                                   | Alta       |
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
| P1b                                              | Gênero do profissional                    | Qualitativo  | Nominal (Multivalorado)             | Identidade de gênero do respondente                                                           | Alta       |
| P1c                                              | Cor/Raça/Etnia                            | Qualitativo  | Nominal (Multivalorado)             | Cor ou raça do respondente                                                                    | Alta       |
| P2b                                              | Setor de atuação da empresa               | Qualitativo  | Nominal (Multivalorado)             | Setor em que a empresa do respondente atua (Tecnologia, Finanças, etc.)                       | Média      |
| P1i1                                             | UF onde mora                              | Qualitativo  | Nominal (Multivalorado)             | Unidade Federativa onde o respondente reside                                                  | Média      |
| P2f                                              | Cargo atual                               | Qualitativo  | Nominal (Multivalorado)             | Cargo atual ocupado pelo respondente                                                          | Alta       |
| P4e                                              | Linguagem mais utilizada no trabalho      | Qualitativo  | Nominal (Multivalorado)             | Linguagem de programação mais usada no trabalho                                               | Alta       |
| P2o1                                             | Remuneração/Salário                       | Qualitativo  | Nominal (Multivalorado)             | Importância atribuída à remuneração na escolha de um emprego                                  | Alta       |
| P2o2                                             | Benefícios                                | Qualitativo  | Nominal (Multivalorado)             | Importância atribuída aos benefícios oferecidos pela empresa                                  | Alta       |
| P2o3                                             | Propósito do trabalho e da empresa        | Qualitativo  | Nominal (Multivalorado)             | Consideração sobre o propósito do trabalho e da empresa                                       | Média      |
| P2o4                                             | Flexibilidade de trabalho remoto          | Qualitativo  | Nominal (Multivalorado)             | Relevância da possibilidade de trabalhar remotamente                                          | Alta       |
| P2o5                                             | Ambiente e clima de trabalho              | Qualitativo  | Nominal (Multivalorado)             | Importância atribuída ao ambiente e clima organizacional                                      | Média      |
| P2o6                                             | Oportunidade de aprendizado               | Qualitativo  | Nominal (Multivalorado)             | Valorização das oportunidades de aprendizado e crescimento profissional                       | Alta       |
| P2o7                                             | Plano de carreira                         | Qualitativo  | Nominal (Multivalorado)             | Relevância atribuída ao plano de carreira e crescimento profissional                          | Alta       |
| P2o8                                             | Maturidade tecnológica                    | Qualitativo  | Nominal (Multivalorado)             | Consideração sobre a maturidade da empresa em termos de tecnologia e dados                    | Média      |
| P2o9                                             | Qualidade dos gestores                    | Qualitativo  | Nominal (Multivalorado)             | Importância atribuída à qualidade dos gestores e líderes                                      | Média      |
| P2o10                                            | Reputação da empresa                      |  Qualitativo | Nominal (Multivalorado)             | Valorização da reputação que a empresa tem no mercado                                         | Média      |

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
**Pergunta orientada a dados::** *Como fatores como localização geográfica, formalidade no emprego e características demográficas (gênero e raça) interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?*

| Atributo                                           | Código de Referência | Tipo         | Subtipo                             | Descrição                                                                                     | Relevância  |
|----------------------------------------------------|-----------------------|--------------|-------------------------------------|-----------------------------------------------------------------------------------------------|------------|
| Faixa etária                                       | P1a1                  | Qualitativo  | Ordinal                             | Faixa etária do respondente                                                                   | Alta       |
| Gênero                                             | P1b                   | Qualitativo  | Nominal (Multivalorado)             | Identidade de gênero do respondente                                                           | Alta       |
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
**Pergunta orientada a dados:** *Como fatores como formação acadêmica, habilidades técnicas e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?*
- Microdados do Censo da Educação Superior
- Link: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-da-educacao-superior
  
- [Base de dados](/assets/data/bases_principais/bases_auxiliar/1_pergunta_orientada_a_dados/MICRODADOS_ED_SUP_IES_2023.CSV)


### Base de dados auxiliar para 2º pergunta orientada a dados
**Pergunta orientada a dados:** *Qual é a relação entre o tempo de experiência na área de dados, o nível de senioridade e a faixa salarial dos profissionais no Brasil?*
- Relatórios de Transparência Salarial e Critérios Remuneratórios
- Link: [https://relatoriodetransparenciasalarial.trabalho.gov.br/](https://relatoriodetransparenciasalarial.trabalho.gov.br/)

### Base de dados auxiliar para a 3º pergunta orientada a dados
**Pergunta orientada a dados:** *Como fatores como localização geográfica, formalidade no emprego e características demográficas (gênero e raça) interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?*
- Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD-C)
- Link: https://basedosdados.org/dataset/9fa532fb-5681-4903-b99d-01dc45fd527a?table=a04fc85d-908a-4393-b51d-1bd517a40210

### Base de dados auxiliar para 4º pergunta orientada a dados
**Pergunta orientada a dados:** Como o domínio de diferentes linguagens de programação influencia a disparidade salarial entre os
profissionais de tecnologia?*

### Base de dados auxiliar para 5º pergunta orientada a dados
**Pergunta orientada a dados:** *De que forma a especialização em áreas de dados, como inteligência artificial ou engenharia de dados, considerando graduações e pós-graduaçōes, pode influenciar na desigualdade salarial entre os profissionais da área?*

---

## Analises exploratorias de dados 

### 1º Pergunta orientada a dados 
**Pergunta Orientada a Dados:** *Como fatores como formação acadêmica, habilidades técnicas e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?*

![image](https://github.com/user-attachments/assets/9037f75e-d52b-4163-9a8d-ac7d50f957ec)

![image](https://github.com/user-attachments/assets/65d01e5d-5973-4409-9be8-16b2bd66a0b7)

![image](https://github.com/user-attachments/assets/f281fe5e-39a0-4533-9be9-47891b818b45)

![image](https://github.com/user-attachments/assets/79a3d5cf-0589-4693-9439-f392cddf386f)

![image](https://github.com/user-attachments/assets/d22bddda-7971-47d6-b8ad-3ac3d0982534)

![image](https://github.com/user-attachments/assets/869942a1-5cf5-4865-8ed8-597724f8dd8b)

![grafico_1](https://github.com/user-attachments/assets/c5eb1bfb-6cd6-4147-a46f-3e33c6dd4141)

![grafico_2](https://github.com/user-attachments/assets/b1547005-3ccd-48e6-8c9f-d8c9ea9cc026)

![grafico_3](https://github.com/user-attachments/assets/cd8dd69f-72a1-4e53-935b-b3222e7de079)

![grafico_4](https://github.com/user-attachments/assets/2289435b-c407-47fd-9523-9943dec46c38)

![grafico_5](https://github.com/user-attachments/assets/61e9d463-96f7-48f0-b687-33e496f5b7de)

![grafico_6](https://github.com/user-attachments/assets/fe4559ed-833d-4856-9de2-ff14bf5c3c07)

![grafico_7](https://github.com/user-attachments/assets/16abed4c-eff1-4a79-9a11-b96d1aed5aca)

![grafico_8](https://github.com/user-attachments/assets/ecbc2903-3782-41e4-a666-1cb029dc58d5)

![grafico_9](https://github.com/user-attachments/assets/04d10ca3-c7eb-4fc8-bd06-2f2d81b98585)

![grafico_10](https://github.com/user-attachments/assets/2ac5f30a-65f2-47f4-972d-0a8757932ebe)

![grafico_11](https://github.com/user-attachments/assets/aa6a284f-9c3a-46c0-a180-c2f808b267a5)

![grafico_12](https://github.com/user-attachments/assets/a1d64f41-feba-4589-87fd-934396a95199)

![grafico_13](https://github.com/user-attachments/assets/50529659-0afa-45ec-ae72-f65fbcc83277)

![grafico_14](https://github.com/user-attachments/assets/3b239d62-a82b-43d1-aa10-26b5e957bcce)

![grafico_15](https://github.com/user-attachments/assets/3bf4cfdf-2032-4158-9012-7091f14121cb)

![grafico_16](https://github.com/user-attachments/assets/71c55ed0-cc29-4cd9-961a-aa2de7039049)

![grafico_17](https://github.com/user-attachments/assets/a1a4a041-92c9-4d03-bac8-0a711126095b)

![grafico_19](https://github.com/user-attachments/assets/aa5da302-2016-4c87-b30d-d8c7a61df5c5)

![grafico_30](https://github.com/user-attachments/assets/c7594562-2e4d-466b-b166-c7a698a4ccfd)

![grafico_28](https://github.com/user-attachments/assets/8e6609d8-de57-4b31-8419-227742953347)

![grafico_27](https://github.com/user-attachments/assets/a8b55cbd-c6af-49c3-9c10-4d8c1ac07603)

![grafico_22](https://github.com/user-attachments/assets/a2fe8ce1-c80a-4f64-b626-04f757474d3e)

![grafico_21](https://github.com/user-attachments/assets/774f76bc-3988-4e3d-ad0c-d763c51b68f7)


### 3º Pergunta orientada a dados
**Pergunta Orientada a Dados:**
*Como fatores como localização geográfica, formalidade no emprego e características demográficas (gênero e raça) interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?*

![cor_e_raça_ensino_heatmap](https://github.com/user-attachments/assets/f147fa83-1501-4669-b6ff-95165ed54894)

![distribuição_regional_barras](https://github.com/user-attachments/assets/24542e74-b49f-4edc-8ffc-0d17085c1e8f)

![genero_salario_heatmap](https://github.com/user-attachments/assets/1121692b-f59c-4a1e-b90f-00f3312f94e5)

![impacto_por_faixa_etaria](https://github.com/user-attachments/assets/4a65cd12-718b-4200-bce4-52f300fe9f0d)

![impacto_por_genero](https://github.com/user-attachments/assets/4bc43c53-b76d-4ce6-ba00-51797eb30d20)

![indice_representividade_interseccional](https://github.com/user-attachments/assets/b7a0f780-f2ba-416f-8fde-1832282e05cc)

![heatmap_calor_disparidae](https://github.com/user-attachments/assets/29521e78-6709-47a1-964e-fffb1d65ab09)

![matriz_correlação](https://github.com/user-attachments/assets/aa66357b-c3cc-4507-a780-843303b7131f)

![relação_salario_ensino_heatmap](https://github.com/user-attachments/assets/ad208ee3-80cc-43fc-bd74-541c1c9ff10d)

---

## Microdados
 State of Data Brazil DATA HACKERS



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

## Explicação Detalhada do Modelo GBM para Previsão de Faixa Salarial para a 3º pergunta orientada a dados

### Modelo: GBM (Gradient Boosting Machines) - Modelo Baseado em Árvore de Decisão

### Justificativa da Escolha do Modelo

Os modelos GBM (Gradient Boosting Machines) foram escolhidos para este projeto de previsão de faixa salarial devido às seguintes características:

1. **Capacidade de capturar interações complexas**: GBMs constroem árvores de decisão sequencialmente, onde cada nova árvore corrige os erros da anterior. Esta estrutura permite capturar interações não lineares entre variáveis demográficas (gênero, raça/cor, região) e educacionais (escolaridade), essenciais para prever faixas salariais com precisão.

2. **Tratamento eficiente de variáveis categóricas**: Algoritmos como XGBoost possuem mecanismos eficientes para lidar com variáveis categóricas sem necessidade de one-hot encoding extensivo, o que é ideal para nosso conjunto de dados com múltiplas categorias demográficas.

3. **Ferramentas robustas para interpretação**:
   - **Feature Importance**: Permite identificar quais fatores demográficos e educacionais têm maior impacto nas faixas salariais.
   - **SHAP (SHapley Additive exPlanations)**: Possibilita entender a contribuição de cada fator para previsões individuais e visualizar como as interações entre características demográficas influenciam o resultado.

4. **Flexibilidade de aplicação**: O modelo foi configurado para classificação multiclasse, prevendo a faixa salarial categorizada em cinco níveis (Muito Baixa, Baixa, Média, Alta, Muito Alta).

### Processo de Amostragem de Dados (Particionamento e Cross-Validation)

O processo de amostragem de dados foi realizado em duas etapas principais:

#### Particionamento dos Dados (Train/Test Split)
**Objetivo**: Garantir que o modelo seja avaliado em dados nunca vistos durante o treinamento.

**Procedimento Utilizado**:
- O dataset foi dividido em duas partes:
  - **Treinamento**: 80% dos dados
  - **Teste**: 20% dos dados
- O particionamento foi realizado com a função `train_test_split` do Scikit-Learn, utilizando `random_state=42` para garantir reprodutibilidade.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)
```

**Justificativa**:
- A estratificação (`stratify=y_encoded`) garante que a distribuição das faixas salariais seja mantida nos conjuntos de treino e teste.
- A proporção 80/20 é um equilíbrio entre ter dados suficientes para treinar o modelo e uma amostra representativa para testá-lo.

#### Validação Cruzada (Cross-Validation)
**Objetivo**: Otimizar hiperparâmetros e evitar overfitting.

**Procedimento**:
- Utilizamos `StratifiedKFold` com 5 divisões para manter a distribuição das classes em cada fold.
- O `GridSearchCV` foi configurado para buscar a melhor combinação de hiperparâmetros.

```python
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=cv,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)
```

**Resultado**:
- O modelo foi otimizado para maximizar a acurácia na classificação das faixas salariais.
- A validação cruzada estratificada garantiu que o modelo fosse avaliado em diferentes subconjuntos dos dados, aumentando a robustez da avaliação.

### Parâmetros do Modelo e Processo de Raciocínio

O modelo XGBoost foi configurado com os seguintes parâmetros principais:

- **objective**: 'multi:softprob' (classificação multiclasse com probabilidades)
- **num_class**: número de faixas salariais (5 categorias)
- **n_estimators**: número de árvores no ensemble (otimizado via GridSearch)
- **max_depth**: profundidade máxima das árvores (otimizado via GridSearch)
- **learning_rate**: taxa de aprendizado (otimizado via GridSearch)
- **subsample**: fração de amostras usadas para treinar cada árvore
- **colsample_bytree**: fração de features usadas para treinar cada árvore

#### Processo de Raciocínio da Árvore (Regras de Decisão)

Cada árvore no ensemble segue um processo de decisão hierárquico:

1. **Nó Raiz**: A primeira divisão geralmente ocorre na variável mais discriminativa, como nível de ensino ou região.
   
2. **Nós Intermediários**: Divisões subsequentes refinam a previsão com base em outras variáveis, como gênero e raça/cor.

3. **Nós Folha**: Cada caminho da raiz até uma folha representa uma regra de decisão que leva a uma probabilidade específica para cada faixa salarial.

**Exemplo de Caminho de Decisão**:
- Se nível de ensino = "Mestrado" E região = "Sudeste", segue para o nó à direita.
- Se gênero = "Masculino", segue para o nó à direita.
- Folha: Probabilidade alta para faixa salarial "Alta (R$ 8.001 a R$ 16.000)".

### Feature Importances e Tomada de Decisão

As variáveis mais importantes para a previsão de faixa salarial, conforme identificado pelo modelo, foram:

1. **Nível de Ensino**: Variável com maior impacto, demonstrando a forte correlação entre educação formal e faixa salarial.

2. **Região**: A segunda variável mais importante, refletindo as disparidades regionais significativas no Brasil.

3. **Gênero**: Contribui para a previsão, capturando possíveis disparidades salariais relacionadas ao gênero.

4. **Raça/Cor**: Também influencia a previsão, indicando potenciais disparidades raciais no mercado de trabalho.

#### Medidas de Importância das Features

- **Importância por Ganho (Gain)**: Mede o quanto cada feature contribuiu para a redução do erro em todas as árvores do modelo.
  
- **Importância por Cobertura (Cover)**: Mede o número relativo de observações relacionadas a esta feature.

- **Importância por Frequência (Frequency)**: Mede o número de vezes que a feature é usada em todas as árvores.

No modelo treinado, nível de ensino e região aparecem consistentemente entre as mais importantes, alinhando-se com os splits iniciais das árvores individuais.

### Explicação do Código: Notebook de Modelo GBM

O notebook implementa um pipeline completo para análise de disparidade salarial, organizado nas seguintes seções:

#### 1. Configuração do Ambiente

```python
# Instalação de bibliotecas
!pip install pandas numpy matplotlib seaborn scikit-learn xgboost shap

# Importação das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import xgboost as xgb
import shap
import warnings
warnings.filterwarnings('ignore')
```

#### 2. Carregamento e Preparação dos Dados

```python
# Carregar os dados
from google.colab import files
uploaded = files.upload()  # Upload do arquivo Main_database.xlsx

# Ler o arquivo Excel
df = pd.read_excel('Main_database.xlsx')

# Identificar colunas relevantes
genero_col = [col for col in df.columns if 'Genero' in col][0]
cor_raca_col = [col for col in df.columns if 'Cor/raca/etnia' in col][0]
uf_col = [col for col in df.columns if 'uf onde mora' in col][0]
nivel_ensino_col = [col for col in df.columns if 'Nivel de Ensino' in col][0]
faixa_salarial_col = [col for col in df.columns if 'Faixa salarial' in col][0]
```

#### 3. Pré-processamento dos Dados

```python
# Mapear UFs para regiões
regiao_mapping = {
    'AC': 'Norte', 'AM': 'Norte', 'AP': 'Norte', 'PA': 'Norte', 'RO': 'Norte', 'RR': 'Norte', 'TO': 'Norte',
    'AL': 'Nordeste', 'BA': 'Nordeste', 'CE': 'Nordeste', 'MA': 'Nordeste', 'PB': 'Nordeste', 
    'PE': 'Nordeste', 'PI': 'Nordeste', 'RN': 'Nordeste', 'SE': 'Nordeste',
    'DF': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'MS': 'Centro-Oeste', 'MT': 'Centro-Oeste',
    'ES': 'Sudeste', 'MG': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'RS': 'Sul', 'SC': 'Sul'
}

# Adicionar coluna de região
data['Regiao'] = data[uf_col].map(regiao_mapping)

# Categorizar faixa salarial
def categorizar_salario(faixa):
    if 'Até' in faixa or '1.000' in faixa or '2.000' in faixa:
        return 'Muito Baixa (Até R$ 2.000)'
    elif '3.000' in faixa or '4.000' in faixa:
        return 'Baixa (R$ 2.001 a R$ 4.000)'
    elif '6.000' in faixa or '8.000' in faixa:
        return 'Média (R$ 4.001 a R$ 8.000)'
    elif '12.000' in faixa or '16.000' in faixa:
        return 'Alta (R$ 8.001 a R$ 16.000)'
    else:
        return 'Muito Alta (Acima de R$ 16.000)'

data['Faixa_Salarial_Categorizada'] = data[faixa_salarial_col].apply(categorizar_salario)
```

#### 4. Treinamento do Modelo XGBoost

```python
# Criar o pipeline com o preprocessador e o modelo XGBoost
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', xgb.XGBClassifier(objective='multi:softprob', num_class=len(le_target.classes_), 
                                     random_state=42, use_label_encoder=False, eval_metric='mlogloss'))
])

# Definir os parâmetros para otimização
param_grid = {
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [3, 5, 7],
    'classifier__learning_rate': [0.01, 0.1],
    'classifier__subsample': [0.8, 1.0],
    'classifier__colsample_bytree': [0.8, 1.0]
}

# Treinar o modelo com GridSearchCV
grid_search.fit(X_train, y_train)
```

#### 5. Avaliação do Modelo

```python
# Fazer previsões no conjunto de teste
y_pred = best_model.predict(X_test)

# Avaliar o desempenho do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {accuracy:.4f}")

# Exibir o relatório de classificação
print(classification_report(y_test, y_pred, target_names=le_target.classes_))

# Criar a matriz de confusão
conf_matrix = confusion_matrix(y_test, y_pred)
```

#### 6. Interpretação do Modelo

```python
# Obter a importância das features
importances = xgb_model.feature_importances_

# Criar um DataFrame com as importâncias
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
})

# Ordenar por importância
importance_df = importance_df.sort_values('Importance', ascending=False)

# Análise SHAP para interpretabilidade do modelo
explainer = shap.Explainer(xgb_model)
shap_values = explainer(X_test_transformed)
```

### Resultados e Insights

O modelo GBM para previsão de faixa salarial revelou importantes insights sobre os fatores que influenciam os salários dos profissionais de dados no Brasil:

1. **Nível de Ensino**: Forte correlação positiva com faixa salarial, com profissionais com mestrado e doutorado tendo maior probabilidade de estar nas faixas salariais mais altas.

2. **Disparidades Regionais**: Profissionais no Sudeste, especialmente em São Paulo, tendem a estar em faixas salariais mais altas comparados a outras regiões.

3. **Disparidades de Gênero**: O modelo identificou diferenças nas distribuições salariais entre homens e mulheres, com homens tendo maior representação nas faixas salariais mais altas.

4. **Disparidades Raciais**: Pessoas brancas têm maior probabilidade de estar em faixas salariais mais altas comparadas a pessoas pardas e pretas.

5. **Interações Complexas**: O modelo capturou interações importantes, como o fato de que o impacto do nível de ensino na faixa salarial varia dependendo da região.

### Conclusão

O modelo GBM demonstrou ser uma escolha eficaz para prever faixas salariais com base em características demográficas e educacionais. Sua capacidade de capturar interações complexas entre variáveis e fornecer interpretações detalhadas através de feature importance e análise SHAP permite não apenas fazer previsões precisas, mas também entender os fatores que contribuem para as disparidades salariais no setor de dados no Brasil.

As descobertas do modelo podem informar políticas e iniciativas para reduzir disparidades salariais relacionadas a gênero, raça e região, além de destacar a importância da educação formal para progressão salarial na área de dados.
 

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




