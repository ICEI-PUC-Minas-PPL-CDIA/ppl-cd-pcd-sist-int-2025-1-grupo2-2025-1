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

## 🎯 Público-Alvo da Aplicação

A aplicação tem como objetivo fornecer insights sobre disparidade salarial na área de dados no Brasil, ajudando diferentes perfis de usuários a tomar decisões estratégicas. 

## 🏢 Stakeholders e seus Papéis

| **Stakeholder**                 | **Nível de Interesse** | **Influência** | **Objetivos** |
|---------------------------------|----------------------|--------------|--------------|
| **Profissionais de Dados**          | Alto                 | Média        | Avaliar sua posição no mercado e planejar crescimento. |
| **Gestores e Recrutadores de RH**   | Alto                 | Alta         | Ajustar faixas salariais e estruturar políticas de retenção. |
| **Pesquisadores e Acadêmicos**      | Médio                | Média        | Explorar padrões e desigualdades no mercado. |
| **Órgãos Governamentais**           | Médio                | Alta         | Criar regulamentações e políticas de inclusão. |

## 👥 Perfis de Usuários (Personas)

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


Utilize a análise descritiva baseada em estatística de primeira ordem para descrever os dados.
Como descrever dados numéricos: média, desvio padrão, mínimo, máximo, quartis, histograma, etc.
Como descrever dados qualitativos (categóricos): moda (valor mais frequente), quantidade de valores distintos (categorias), distribuição das categorias (histograma), etc.


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
**Pergunta Orientada a Dados:** *Como fatores como formação acadêmica, habilidades técnicas e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?*


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

### Atributos relevantes da base de dados principal para 2ª pergunta orientada
**Pergunta Orientada a Dados:** *Qual é a relação entre o tempo de experiência na área de dados, o nível de senioridade e a faixa salarial dos profissionais no Brasil?*

| Atributo | Nome | Tipo | Subtipo | Descrição | Relevância |
|----------|------|------|---------|-----------|------------|
| P2i      | Tempo de Experiência | Quantitativo | Discreto | Anos de atuação na área de dados | Alta |
| P2g      | Nível de Senioridade | Qualitativo | Ordinal | Nível profissional alcançado (Júnior, Pleno, Sênior, etc.) | Alta |
| P2h      | Faixa Salarial | Qualitativo | Ordinal | Classificação salarial em faixas | Alta |

### Atributos relevantes da base de dados principal para 3ª pergunta orientada
**Pergunta Orientada a Dados:** *Como fatores como localização geográfica, formalidade no emprego e características demográficas (gênero e raça) interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?*

| Atributo                                           | Código de Referência | Tipo         | Subtipo                             | Descrição                                                                                     | Relevância  |
|----------------------------------------------------|-----------------------|--------------|-------------------------------------|-----------------------------------------------------------------------------------------------|------------|
| Faixa etária                                       | P1a1                  | Qualitativo  | Ordinal                             | Faixa etária do respondente                                                                   | Alta       |
| Gênero                                             | P1b                   | Qualitativo  | Nominal (Multivalorado)             | Identidade de gênero do respondente                                                           | Alta       |
| Não acredito que minha experiência profissional seja afetada     | P1e1                  | Qualitativo  | Nominal (Binário)                   | Resposta indicando que o respondente não acredita que sua experiência foi afetada             | Alta       |
| Experiência prejudicada devido à minha Cor/Raça/Etnia            | P1e2                  | Qualitativo  | Nominal (Binário)                   | Indicação de prejuízo na experiência profissional devido à cor, raça ou etnia                 | Alta       |
| Experiência prejudicada devido à minha identidade de gênero      | P1e3                  | Qualitativo  | Nominal (Binário)                   | Indicação de prejuízo na experiência profissional devido à identidade de gênero               | Alta       |
| P1l                                                | Nível de ensino alcançado            | Qualitativo | Ordinal               | Nível de ensino do respondente (graduação, mestrado, etc.)                                     | Alta       |
| P2h                                              | Faixa salarial mensal                     | Qualitativo  | Ordinal                             | Faixa salarial mensal do respondente                                                          | Alta       |
| P2i                                              | Tempo de experiência na área de dados     | Quantitativo | Discreto                            | Tempo de experiência do respondente na área de dados (em anos)                                | Alta       |


### Atualizar essa base de dados auxiliar
-https://sidra.ibge.gov.br/tabela/7446
-https://sidra.ibge.gov.br/tabela/7446
-
### **2- Atributos do banco de dados secundário "ESTUDO PANORAMA DAS CARREIRAS 2030;**
H2R PESQUISAS; TOTVS. Estudo Panorama das Carreiras 2030: o que esperar das profissões até o fim da década. Setembro/2023. Acesso em: 6 mar. 2025

**Cargos apresentados:** Há uma distribuição de cargos (estagiário, analista, especialista, coordenador, gerente, diretor, CEO/sócio), o que permite entender a hierarquia profissional.

**Área de atuação:** Os profissionais são classificados em Tech, Finance, RH e Marketing & Vendas, o que pode indicar diferenças salariais entre setores.

**Gênero:** O estudo menciona a participação de homens e mulheres, permitindo análise de disparidades entre os sexos.

**Escolaridade:** Dados sobre nível de formação (médio, superior, pós-graduação) podem ser correlacionados com salários.

**Experiência profissional:** O documento destaca que muitos profissionaistêm indicam que a experiência no setor pode influenciar a remuneração.

**Habilidades mais demandadas (Hard e Soft Skills):** Competências como análise de dados, inteligência artificial e gestão de projetos são mencionadas, o que pode justificar diferenças salariais.

**Tendências para 2030:** O estudo prevê que analistas de dados e especialistas em IA serão profissões valorizadas, o que pode indicar mudanças futuras nos salários.


---

## Microdados
### State of Data Brazil DATA HACKERS



----------------------------------------------------------------------------------------------------------------------------------------------

## 📊 Indução de modelos

### Modelo 1: Algoritmo

Substitua o título pelo nome do algoritmo que será utilizado. P. ex. árvore de decisão, rede neural, SVM, etc.
Justifique a escolha do modelo.
Apresente o processo utilizado para amostragem de dados (particionamento, cross-validation).
Descreva os parâmetros utilizados. 
Apresente trechos do código utilizado comentados. Se utilizou alguma ferramenta gráfica, apresente imagens
com o fluxo de processamento.

### Modelo 2: Algoritmo

Repita os passos anteriores para o segundo modelo.


## Resultados

### Resultados obtidos com o modelo 1.

Apresente aqui os resultados obtidos com a indução do modelo 1. 
Apresente uma matriz de confusão quando pertinente. Apresente as medidas de performance
apropriadas para o seu problema. 
Por exemplo, no caso de classificação: precisão, revocação, F-measure, acurácia.

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


# ✒️ REFERÊNCIAS 

DATA HACKERS. State of Data Brazil 2023. Disponível em: https://www.kaggle.com/datasets/datahackers/state-of-data-brazil-2023. Acesso em: 5 mar. 2025.

BAIN & COMPANY; DATA HACKERS. State of Data 2024. [S.l.]: Bain & Company, 2024. Disponível em: <https://www.stateofdata.com.br/>. Acesso em: 6 mar. 2025.

H2R PESQUISAS; TOTVS. Estudo Panorama das Carreiras 2030: o que esperar das profissões até o fim da década. Setembro/2023. Acesso em: 6 mar. 2025


# APÊNDICES

**Colocar link:**

Do código (armazenado no repositório);

Dos artefatos (armazenado do repositório);

Da apresentação final (armazenado no repositório);

Do vídeo de apresentação (armazenado no repositório).




