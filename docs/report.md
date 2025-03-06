# Disparidade Salarial dos Profissionais de Dados no Brasil


**Pedro Dias Soares, [pedro3soares@gmail.com] / [pdsoares@sga.pucminas.br]**

**Gabriel Bahia Leite, [bahiagabrie334@gmail.com] / [gabriel.bahia@sga.pucminas.br]**

**Gabriel Barroso Goulart Parreiras, email do aluno 3**

**Gabriel Chaves Nascimento, email do aluno 4**

**Gian Henrique Ticon e Silva Carvalho , email do aluno 5**

---

Professores:

**Hugo Bastos de Paula**


---

_Curso de Ciência de Dados, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---

_**Resumo**. Escrever aqui o resumo. O resumo deve contextualizar rapidamente o trabalho, descrever seu objetivo e, ao final, 
mostrar algum resultado relevante do trabalho (até 10 linhas)._

---


## Introdução

O Brasil experimentou um crescimento exponencial na indústria de dados devido à transformação digital do país e à crescente necessidade de trabalhadores qualificados. Embora as oportunidades sejam abundantes, os salários variam amplamente entre os trabalhadores, com fatores como falta de experiência, gênero, educação e tipo de empresa influenciando essa disparidade.

O objetivo deste estudo é identificar os principais fatores que influenciam a disparidade na remuneração dos profissionais de dados no Brasil com base em dados utilizando informações coletadas de uma ampla pesquisa setorial.

As disparidades salariais entre os profissionais de dados no Brasil são influenciadas por diversos fatores como idade, gênero dos profissionais de dados, do setor de emprego ou modelo de contratação e ainda o seu histórico educacional e experiência profissional. A necessidade aparentemente interminável de especialistas contrasta fortemente com as desigualdades estruturais que afetam a remuneração dos profissionais de dados.

Este estudo investiga os principais elementos que influenciam a variação de salários no campo de dados ao utilizar o conjunto de dados State of Data Brazil 2023 e outras bases para complementar a pesquisa. Empregando métodos da ciência de dados, busca-se identificar padrões salariais e oferecer insights relevantes para profissionais, empresas e formuladores de políticas públicas.

Espera-se que os resultados tragam um maior entendimento das disparidades salariais no campo, ajudando a desenvolver estratégias que incentivem a igualdade no mercado de tecnologia e ciência de dados.

###    Contextualização

A disparidade salarial é um tema recorrente no mercado de trabalho, afetando diferentes setores da economia. No Brasil, estudos do IBGE apontam que fatores como gênero, raça e escolaridade influenciam diretamente os rendimentos dos profissionais. No setor de tecnologia, essas desigualdades se manifestam de maneira particular, dado o crescimento acelerado da área e a necessidade de qualificação constante.

No campo da ciência de dados, a remuneração pode variar significativamente conforme experiência, formação acadêmica, setor de atuação e habilidades técnicas. O relatório State of Data Brazil 2023 destaca que profissionais com certificações específicas e atuação em empresas de grande porte tendem a ter salários mais altos, enquanto mulheres e grupos sub-representados ainda enfrentam desafios na equiparação salarial.

Diante desse cenário, este estudo busca analisar os fatores determinantes para a variação salarial dos profissionais de dados no Brasil, utilizando técnicas de ciência de dados para identificar padrões e oferecer insights para o mercado.


###    Problema

Nesse momento você deve apresentar o problema que seu agente pretende resolver. 
No entanto, não é a hora de comentar sobre a aplicação.
Descreva também o contexto em que essa aplicação será usada, se  houver: 
empresa, tecnologias, etc. Novamente, descreva apenas o que de  fato existir, 
pois ainda não é a hora de apresentar requisitos  detalhados ou projetos.

O **problema** pode ser algo vivido em uma empresa específica. Neste caso, o aluno deve 
sucintamente apresentar o cenário de problema da empresa. A empresa só deve ser citada 
explicitamente se o aluno tiver autorização para tal.




###    Objetivo geral

**Desenvolver um sistema inteligente para compreender os fatores que influenciam a variação salarial dos profissionais de dados no Brasil, utilizando técnicas de ciência de dados para identificar padrões e tendências.**

####    Objetivos específicos

1. **Exploração e Análise dos Dados:**
    - Examinar a base de dados *State of Data Brazil 2023* e bases auxiliares para identificar variáveis relevantes que impactam os salários.
    - 
2. **Identificação de Fatores Relevantes:**
    - Analisar variáveis como nível de experiência, localização geográfica, setor de atuação, nível educacional, habilidades técnicas, entre outras.
    - 
3. **Aplicação de Modelos Preditivos:**
    - Testar algoritmos de aprendizado de máquina para prever a variação salarial com base nos fatores identificados.
    - 
4. **Interpretação dos Resultados:**
    - Avaliar quais fatores apresentam maior impacto e como eles se relacionam com as diferenças salariais.
    - 
5. **Geração de Insights para o Mercado:**
    - Fornecer recomendações baseadas nos achados, podendo auxiliar profissionais de dados e empresas na tomada de decisões estratégicas.





###    Justificativas

Mostre também as **justificativas** para o  desenvolvimento do seu trabalho e, caso deseje, 
destaque alguma contribuição do trabalho.

A justific ativa deve descrever a importância ou a motivação para o desenvolvimento do 
sistema inteligente escolhido. Indique as razões pelas quais você escolheu seus objetivos 
específicos ou as razões para aprofundar em certos aspectos do software.




##    Público alvo

Este estudo será de interesse para diversos grupos, incluindo:

- **Profissionais de dados** (cientistas, engenheiros, analistas e gestores) que desejam entender como sua posição no mercado afeta seus rendimentos.
- **Empresas de tecnologia e RH** interessadas em estruturar políticas salariais mais justas e competitivas.
- **Pesquisadores e acadêmicos** que estudam desigualdade no mercado de trabalho e tendências salariais na tecnologia.
- **Órgãos governamentais e associações da indústria** que buscam criar políticas de inclusão e equidade no setor de tecnologia e ciência de dados.





## Análise exploratórida dos dados

###    Dicionário de dados

Apresente uma descrição das bases de dados a serem utilizadas. 
Dicionários de dados devem conter as bases de dados, os nomes dos atributos 
com seu significado, seu tipo (inteiro, real, textual, categórico, etc).

Este projeto deve utilizar pelo menos duas fontes de dados. Uma fonte principal e 
uma fonte para enriquecimentos dos dados principais.


###    Descrição de dados

Utilize a análise descritiva baseada em estatística de primeira ordem para descrever os dados.
Como descrever dados numéricos: média, desvio padrão, mínimo, máximo, quartis, histograma, etc.
Como descrever dados qualitativos (categóricos): moda (valor mais frequente), quantidade de valores distintos (categorias), distribuição das categorias (histograma), etc.


## Preparação dos dados

A preparação dos dados consiste dos seguintes passos:

> - Seleção dos atributos
> - Tratamentos dos valores faltantes ou omissos: remoção, substituição, indução, etc.
> - Tratamento dos valores inconsistentes: conversão, remoção de dados duplicados, remoção ou tratamento de ouliers.
> - Conversão de dados: p. ex. numérico para categórico, categórico para binário, etc.


## Indução de modelos

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


# REFERÊNCIAS

DATA HACKERS. State of Data Brazil 2023. Disponível em: https://www.kaggle.com/datasets/datahackers/state-of-data-brazil-2023. Acesso em: 5 mar. 2025.

BAIN & COMPANY; DATA HACKERS. State of Data 2024. [S.l.]: Bain & Company, 2024. Disponível em: <https://www.stateofdata.com.br/>. Acesso em: 6 mar. 2025.

H2R PESQUISAS; TOTVS. Estudo Panorama das Carreiras 2030: o que esperar das profissões até o fim da década. Setembro/2023. Acesso em: 6 mar. 2025


# APÊNDICES

**Colocar link:**

Do código (armazenado no repositório);

Dos artefatos (armazenado do repositório);

Da apresentação final (armazenado no repositório);

Do vídeo de apresentação (armazenado no repositório).




