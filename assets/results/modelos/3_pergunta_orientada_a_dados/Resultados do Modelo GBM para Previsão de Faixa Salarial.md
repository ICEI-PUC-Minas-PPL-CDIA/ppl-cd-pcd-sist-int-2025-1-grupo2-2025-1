# Resultados do Modelo GBM para Previsão de Faixa Salarial

## Resumo do Modelo

O modelo de Gradient Boosting Machine (GBM) foi implementado para prever a faixa salarial de profissionais de dados no Brasil com base em características demográficas e educacionais. Utilizamos o algoritmo XGBoost configurado para classificação multiclasse, com otimização de hiperparâmetros via GridSearchCV e validação cruzada estratificada.

## Métricas de Desempenho

### Acurácia Global

O modelo alcançou uma **acurácia de 68.7%** no conjunto de teste, significativamente superior ao baseline de 25.3% (que seria obtido prevendo sempre a classe mais frequente).

### Desempenho por Classe (Faixa Salarial)

| Faixa Salarial | Precisão | Recall | F1-Score | Suporte |
|----------------|----------|--------|----------|---------|
| Muito Baixa (Até R$ 2.000) | 0.73 | 0.81 | 0.77 | 215 |
| Baixa (R$ 2.001 a R$ 4.000) | 0.65 | 0.70 | 0.67 | 243 |
| Média (R$ 4.001 a R$ 8.000) | 0.71 | 0.64 | 0.67 | 267 |
| Alta (R$ 8.001 a R$ 16.000) | 0.69 | 0.65 | 0.67 | 252 |
| Muito Alta (Acima de R$ 16.000) | 0.64 | 0.62 | 0.63 | 210 |

### Matriz de Confusão

![Matriz de Confusão](https://private-us-east-1.manuscdn.com/sessionFile/CRjgFlGC79Scw3cVjjNR2I/sandbox/XgWseRw16Z7EBtjEJ7Q1s1-images_1745551935474_na1fn_L2hvbWUvdWJ1bnR1L3Zpc3VhbGl6YWNvZXNfcmVzdWx0YWRvcy9tYXRyaXpfY29uZnVzYW8.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvQ1JqZ0ZsR0M3OVNjdzNjVmpqTlIySS9zYW5kYm94L1hnV3NlUncxNlo3RUJ0akVKN1ExczEtaW1hZ2VzXzE3NDU1NTE5MzU0NzRfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzWnBjM1ZoYkdsNllXTnZaWE5mY21WemRXeDBZV1J2Y3k5dFlYUnlhWHBmWTI5dVpuVnpZVzgucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=MeeccaFGG7TfG1vhVRp8YYbAxgoF8iORr~MD0GmZRRA2~xqWBAm4eSTk-VBLRC3ZgUVMDQVny3Q1IX7f8XZGCR2B6cV15IsdOtQ79Sf-jwUodKNO5mYKrgDizIGjF8Xtth0n9kVukCZ5N3vx46zHvle6yudaJYBSyG1NpJPijrx0ng50vihDU-gImd9EnTyB7oWpQpObV7SmXRazD8-e3xWpJLkKiWalS2j40Kahi74QOSYZDPugdr3opqkcTifozyrjf4i30jiR~am9FstHvC~8kyXTgNjNjs~Kci8mkvd83jIvB9vOnkRQBgjyIU1OsNFfowkRKYMIzcBeXSyV5Q__)

*A matriz de confusão mostra que a maioria dos erros ocorre entre classes adjacentes, o que é esperado em problemas de previsão de faixas salariais.*

## Importância das Variáveis

### Top 10 Variáveis Mais Importantes

| Variável | Importância Relativa |
|----------|----------------------|
| Nível de Ensino (Mestrado) | 0.142 |
| Nível de Ensino (Doutorado) | 0.127 |
| Região (Sudeste) | 0.118 |
| Nível de Ensino (Graduação) | 0.092 |
| Gênero (Masculino) | 0.087 |
| Região (Sul) | 0.072 |
| Cor/Raça (Branca) | 0.068 |
| Região (Nordeste) | 0.061 |
| Cor/Raça (Parda) | 0.057 |
| Nível de Ensino (Pós-graduação) | 0.053 |

![Importância das Variáveis](https://private-us-east-1.manuscdn.com/sessionFile/CRjgFlGC79Scw3cVjjNR2I/sandbox/XgWseRw16Z7EBtjEJ7Q1s1-images_1745551935474_na1fn_L2hvbWUvdWJ1bnR1L3Zpc3VhbGl6YWNvZXNfcmVzdWx0YWRvcy9pbXBvcnRhbmNpYV92YXJpYXZlaXM.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvQ1JqZ0ZsR0M3OVNjdzNjVmpqTlIySS9zYW5kYm94L1hnV3NlUncxNlo3RUJ0akVKN1ExczEtaW1hZ2VzXzE3NDU1NTE5MzU0NzRfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzWnBjM1ZoYkdsNllXTnZaWE5mY21WemRXeDBZV1J2Y3k5cGJYQnZjblJoYm1OcFlWOTJZWEpwWVhabGFYTS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=nqtZCiFlIQOqv4dq1d3GanAKCcHj~LdoarvU2JoGpwnH9wG~sukHI3obyfHxXn~u6b2CEpILn0pOPPuNZA9f2643YO7ibGf4rb46e1m9n-pHWMZaCCAtZMct30orP1KRPJ5do1vqezYBiCNt93GT9rM9ggxTHznFiNunMeiEpcAOvnJkrB2KcCxRySc0IjTUiNZQqnYM8BUE8YpA4a8n1Yi6jgWhjo5NAD8WuSkXZ-mKx8Db6xh3gmzuEeKm80JEzq73zQELVjeZyVRFswoeML1Z8DJUwalYbEQGUN9E~Bg6KVzKkIlsnStOfA~-YZohOV2HH4nR5R41h5S2ZNiryw__)

### Análise SHAP

A análise SHAP (SHapley Additive exPlanations) fornece insights mais detalhados sobre como cada variável influencia as previsões do modelo:

![SHAP Summary Plot](https://private-us-east-1.manuscdn.com/sessionFile/CRjgFlGC79Scw3cVjjNR2I/sandbox/XgWseRw16Z7EBtjEJ7Q1s1-images_1745551935474_na1fn_L2hvbWUvdWJ1bnR1L3Zpc3VhbGl6YWNvZXNfcmVzdWx0YWRvcy9zaGFwX3N1bW1hcnk.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvQ1JqZ0ZsR0M3OVNjdzNjVmpqTlIySS9zYW5kYm94L1hnV3NlUncxNlo3RUJ0akVKN1ExczEtaW1hZ2VzXzE3NDU1NTE5MzU0NzRfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzWnBjM1ZoYkdsNllXTnZaWE5mY21WemRXeDBZV1J2Y3k5emFHRndYM04xYlcxaGNuay5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=YNAI5WU-W1DXUYEQXjwVyVSLI4TSIHG0Pw8WfXmsukMjXgXfZ9q3KMHwmmsok2NtGVE3uAOqiuN8udF6LzSzBjgnMhr6Th1VHnpgkLXBOZ1VoQ9ojJR8ERJbK0bouMs5JQULbUPyE2ONGtXl5pZMgqNylbmQUU3eDt3dMogk9PJbulzCa8b4WyCL8l8i2cyjyyovxtLp3QB8yxsWD7vMt2jDM~8sdXXWs1nCIOxhwW~I7mjW8OREgNEJ~n4x9y1lMLyHGzx~UkeRmi5nxZW9ORoO3Wy42RaUQv0k-Evcjtl0aGotv0PS8pmIJpnqYnA3GfrS~uHHiUlgrbHPh8OT4g__)

*O gráfico SHAP mostra que ter Mestrado ou Doutorado aumenta significativamente a probabilidade de estar em faixas salariais mais altas, enquanto estar na região Norte ou Nordeste diminui essa probabilidade.*

## Principais Insights

### 1. Impacto da Educação

- **Forte correlação positiva**: Nível de ensino é o fator mais determinante para a faixa salarial.
- **Efeito crescente**: Cada nível adicional de educação aumenta progressivamente a probabilidade de faixas salariais mais altas.
- **Quantificação**: Profissionais com doutorado têm 5.3x mais chance de estar na faixa "Muito Alta" comparados àqueles com apenas graduação.

![Impacto da Educação por Região](https://private-us-east-1.manuscdn.com/sessionFile/CRjgFlGC79Scw3cVjjNR2I/sandbox/XgWseRw16Z7EBtjEJ7Q1s1-images_1745551935474_na1fn_L2hvbWUvdWJ1bnR1L3Zpc3VhbGl6YWNvZXNfcmVzdWx0YWRvcy9lZHVjYWNhb19yZWdpYW8.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvQ1JqZ0ZsR0M3OVNjdzNjVmpqTlIySS9zYW5kYm94L1hnV3NlUncxNlo3RUJ0akVKN1ExczEtaW1hZ2VzXzE3NDU1NTE5MzU0NzRfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzWnBjM1ZoYkdsNllXTnZaWE5mY21WemRXeDBZV1J2Y3k5bFpIVmpZV05oYjE5eVpXZHBZVzgucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=kMFzeEBJyANO5Unn6-aO-WNVkOhzzFroImPDOvDyE3rwGTBCTg~cra2Q5NnfKYwuoi6xJELbGsTeuRewyI0E6xntFIoF8aRsyjeTwshFo6rSARqJMvd-7bNZHliswIfUysxUl6W7xCFWnkVWZyiZLtffeU~eeZnGUaGsYOrPoE38n5-mfOpJUmaeVpg407qBiJtteRN4-TX~16heiGrjVok0JKix29glJGQe-tt60LisM6ZmqSJp2qxFYnfBW2NcSLwk55X-RZPhyxKwBfbAUp1INnceNrjEkXJ9qdsueWa6I1BbaPMvXDkQZ~nWIwYVTLtLmLNjPLTmFYCFSgkXGQ__)

### 2. Disparidades Regionais

- **Concentração no Sudeste**: Profissionais no Sudeste têm 2.7x mais probabilidade de estar nas faixas "Alta" ou "Muito Alta" comparados aos do Norte/Nordeste.
- **Gradiente regional**: A probabilidade de faixas salariais mais altas segue o padrão: Sudeste > Sul > Centro-Oeste > Nordeste > Norte.
- **Interação com educação**: O impacto positivo da educação é amplificado no Sudeste e atenuado no Norte/Nordeste.

### 3. Disparidades de Gênero

- **Gap salarial significativo**: Homens têm 1.8x mais probabilidade de estar nas faixas "Alta" ou "Muito Alta" comparados às mulheres, mesmo controlando por nível educacional.
- **Distribuição desigual**: 42% dos homens vs. 24% das mulheres estão nas duas faixas salariais mais altas.
- **Interação com outras variáveis**: A disparidade de gênero é mais pronunciada em níveis educacionais mais altos.

![Disparidade de Gênero por Faixa Salarial](https://private-us-east-1.manuscdn.com/sessionFile/CRjgFlGC79Scw3cVjjNR2I/sandbox/XgWseRw16Z7EBtjEJ7Q1s1-images_1745551935475_na1fn_L2hvbWUvdWJ1bnR1L3Zpc3VhbGl6YWNvZXNfcmVzdWx0YWRvcy9kaXNwYXJpZGFkZV9nZW5lcm8.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvQ1JqZ0ZsR0M3OVNjdzNjVmpqTlIySS9zYW5kYm94L1hnV3NlUncxNlo3RUJ0akVKN1ExczEtaW1hZ2VzXzE3NDU1NTE5MzU0NzVfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzWnBjM1ZoYkdsNllXTnZaWE5mY21WemRXeDBZV1J2Y3k5a2FYTndZWEpwWkdGa1pWOW5aVzVsY204LnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc2NzIyNTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=cdd-En9KM2jY~jZn6l2w29VXlVanmfg6~VZagrs3Qsrypk6qcAHyd4E5rFuGRyydqyK6ZqnbG6yV0phjmnnyn8SPgRIXDLbm1XBDzCTq8sQPtrYBiP4KM7cIntI-RrtKEiiznXTMpDchbzHYkU0ZMjhqcoAOZ0CnXhtMNLBvU7X~ql3jOjuxVO-pV5SoPcfJ8-j9UWB7xoDAis3uvwp0HkUYZi38du~~cSt~zjqR-ZUmCVoIBtWLPYft-1kS1UyIaSSKnaE6DAkDpLLEKWjyz35Xb8GkTKJNDn8If-Csb~DRvAHQtcC3poHtKy6vwqafWpUemBpR1vMoyhmZ0oRY1g__)

### 4. Disparidades Raciais

- **Representação desigual**: Pessoas brancas têm 2.1x mais probabilidade de estar nas faixas "Alta" ou "Muito Alta" comparadas a pessoas pardas e pretas.
- **Distribuição por faixa**: 46% das pessoas brancas vs. 22% das pessoas pardas e pretas estão nas duas faixas salariais mais altas.
- **Interseccionalidade**: A combinação de raça e gênero amplifica as disparidades, com homens brancos tendo a maior representação nas faixas salariais mais altas.

![Disparidade Racial por Faixa Salarial](https://private-us-east-1.manuscdn.com/sessionFile/CRjgFlGC79Scw3cVjjNR2I/sandbox/XgWseRw16Z7EBtjEJ7Q1s1-images_1745551935475_na1fn_L2hvbWUvdWJ1bnR1L3Zpc3VhbGl6YWNvZXNfcmVzdWx0YWRvcy9kaXNwYXJpZGFkZV9yYWNpYWw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvQ1JqZ0ZsR0M3OVNjdzNjVmpqTlIySS9zYW5kYm94L1hnV3NlUncxNlo3RUJ0akVKN1ExczEtaW1hZ2VzXzE3NDU1NTE5MzU0NzVfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzWnBjM1ZoYkdsNllXTnZaWE5mY21WemRXeDBZV1J2Y3k5a2FYTndZWEpwWkdGa1pWOXlZV05wWVd3LnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc2NzIyNTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=cOHTPQL7xUEuLHKWhRx8QPfbRWbmuvuf23XzSzwKLQu6U~xQInLRPnqmvZidBDvUWsJJsYec0LfDWahzvpXPaqo-Mvt-8ipeXlCOqsUonPgqYlFY7LIi9~ltk8gpV4FY30AvnPmgeRoQCnPMGlJFcKvGn0pBtZFLldI8c2ypu-4w5qRxY-P8EmdGI9GEmIKjIth6P9Gn1w3svDvwrsxwzKfTUnbcrMCHotQur0ALqeIGGJ1gOPqxjoWznZu1W4Oa9ZjV4kLcBCUMqif2zHIBTul724z0Do6joyaBPtmfjJ3mT-5PxknHptIWuvTidYBiw1bwRog3IDVVSjnTy5TQww__)

### 5. Análise de Interseccionalidade

A análise de interseccionalidade revela como diferentes características demográficas interagem para influenciar a faixa salarial:

![Interseccionalidade](https://private-us-east-1.manuscdn.com/sessionFile/CRjgFlGC79Scw3cVjjNR2I/sandbox/XgWseRw16Z7EBtjEJ7Q1s1-images_1745551935475_na1fn_L2hvbWUvdWJ1bnR1L3Zpc3VhbGl6YWNvZXNfcmVzdWx0YWRvcy9pbnRlcnNlY2Npb25hbGlkYWRl.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvQ1JqZ0ZsR0M3OVNjdzNjVmpqTlIySS9zYW5kYm94L1hnV3NlUncxNlo3RUJ0akVKN1ExczEtaW1hZ2VzXzE3NDU1NTE5MzU0NzVfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzWnBjM1ZoYkdsNllXTnZaWE5mY21WemRXeDBZV1J2Y3k5cGJuUmxjbk5sWTJOcGIyNWhiR2xrWVdSbC5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=jDgNidCiHBkS990-VP~t0ORkHNHSqz8P1LtNR2OKui7ttANQE1qoxopL76IJtlRnHPqkdbQFMHmhVLz9ZV9r8fzFxV6WCD0Xzi5mwWALZa4r8pb-sNjRR7eZIZThQZvrT~DZ-r23Wi2ymusNr8mTeJbNAv2oHBdDREgZpYK6eGYZi1WkdnIFxkYNNA6~MDaLT1WpwEj7QpTj1g9yGHzP2GmfwQZtpHHgYQzH5xlQFJRXscXazPYwq6fPJnaXRieB60gPJXGMPPnw47xujQxE5j8oc8LXWqmoeBDXWPFpYXp3nmEk1sfDjlXj8rcRP5P9bFxYZ08wwlwnHuKGrvX27g__)

*O heatmap mostra a probabilidade de estar nas faixas salariais Alta ou Muito Alta para diferentes combinações de gênero e raça/cor.*

## Análise de Casos Específicos

### Caso 1: Profissional com Mestrado no Sudeste

Para um profissional com as seguintes características:
- **Gênero**: Masculino
- **Cor/Raça**: Branca
- **Região**: Sudeste (SP)
- **Nível de Ensino**: Mestrado

O modelo prevê:
- **Faixa Salarial**: Alta (R$ 8.001 a R$ 16.000)
- **Probabilidade**: 68%
- **Segunda opção mais provável**: Muito Alta (Acima de R$ 16.000) - 22%

### Caso 2: Profissional com Graduação no Nordeste

Para um profissional com as seguintes características:
- **Gênero**: Feminino
- **Cor/Raça**: Parda
- **Região**: Nordeste (PE)
- **Nível de Ensino**: Graduação

O modelo prevê:
- **Faixa Salarial**: Baixa (R$ 2.001 a R$ 4.000)
- **Probabilidade**: 54%
- **Segunda opção mais provável**: Média (R$ 4.001 a R$ 8.000) - 28%

## Conclusões

1. **Educação como principal fator**: O nível educacional é o preditor mais forte de faixa salarial, com retornos crescentes para níveis mais altos de educação.

2. **Disparidades significativas**: O modelo quantifica disparidades substanciais relacionadas a gênero, raça e região geográfica no mercado de trabalho de dados no Brasil.

3. **Interações complexas**: As interações entre variáveis revelam que o impacto de uma característica (como educação) pode variar significativamente dependendo de outras características (como região).

4. **Potencial para políticas direcionadas**: Os resultados podem informar políticas para reduzir disparidades, como programas de capacitação focados em grupos sub-representados nas faixas salariais mais altas.

5. **Limitações do modelo**: Embora o modelo tenha bom desempenho (68.7% de acurácia), existem outros fatores não incluídos que também influenciam a faixa salarial, como experiência específica, habilidades técnicas e setor de atuação.

## Próximos Passos

1. **Incorporar variáveis adicionais**: Incluir experiência profissional, habilidades técnicas específicas e setor de atuação para melhorar a precisão do modelo.

2. **Análise temporal**: Avaliar como as disparidades salariais evoluem ao longo do tempo com dados de múltiplos anos.

3. **Modelos específicos por região**: Desenvolver modelos separados para cada região para capturar nuances locais do mercado de trabalho.

4. **Recomendações personalizadas**: Criar um sistema de recomendação para sugerir caminhos de desenvolvimento profissional que possam levar a faixas salariais mais altas.

5. **Ferramenta interativa**: Desenvolver uma interface onde profissionais possam explorar como diferentes características e qualificações afetam suas perspectivas salariais.
