## 1. Estrutura da Classe MTEDataProcessor
A classe centraliza todas as operações de limpeza, seguindo o princípio de encapsulamento.
Atributos principais:

cbo_codes: Lista de códigos CBO (Classificação Brasileira de Ocupações) para filtrar profissionais de TI/dados.

column_mapping: Dicionário para renomear colunas do arquivo original para nomes mais intuitivos.

gender_mapping e race_mapping: Dicionários para traduzir códigos categóricos (ex: 1 → "Masculino").

## 2. Fluxo Principal do Processamento
O pipeline segue estas etapas para cada arquivo:

a. Leitura do Arquivo (read_file)
Lê o arquivo CSV com encoding latin1 e separador ;.

Seleciona apenas colunas relevantes (definidas em columns_to_read).

Converte campos numéricos com vírgula como separador decimal.

b. Filtragem por CBO (filter_by_cbo)
Renomeia colunas conforme column_mapping.

Filtra registros mantendo apenas os códigos CBO de tecnologia definidos.

Remove registros com CBOs não relevantes.

c. Limpeza de Salários (clean_salary_data)
Converte a coluna salario_medio_nominal para numérico.

Remove registros com salários inválidos (negativos ou não numéricos).

d. Mapeamento de Campos Categóricos (map_categorical_fields)
Traduz códigos numéricos para labels legíveis:

Gênero: 1 → "Masculino", 2 → "Feminino".

Raça/Cor: 4 → "Preta", 9 → "Parda".

Padroniza códigos de UF (ex: 12 → "AC").

e. Remoção de Colunas Redundantes (drop_redundant_columns)
Remove colunas originais após o mapeamento categórico (ex: genero_cod é substituído por genero).

## 3. Processamento em Lote (process_all_files)
Usa glob para encontrar todos os arquivos que correspondem ao padrão (ex: ./dados_mte/*.txt).

Processa cada arquivo individualmente e agrega os resultados em um único DataFrame.

Salva o resultado final em um arquivo CSV (dados_auxiliares_mte_limpos.csv).

## 4. Recursos Avançados
Tratamento de Erros:

Verifica a existência de colunas antes de operações críticas.

Ignora arquivos corrompidos (on_bad_lines='warn').

Logs detalhados em cada etapa para debug.

Customização:

CBOs e mapeamentos podem ser ajustados modificando os dicionários da classe.

Padrão de arquivos e caminhos de saída são parametrizáveis.

## 5. Saída Final
O dataset gerado contém:

Salários médios válidos e padronizados.

Dados demográficos traduzidos (gênero, raça, UF).

Apenas registros de profissionais de TI/dados (filtro por CBO).

Como Usar no GitHub
Estrutura de Pastas:

text
├── dados_mte/           # Pasta com arquivos originais do MTE (*.txt)
├── scripts/
│   └── mte_processor.py # Este script
└── README.md            # Documentação
Execução:

bash
python scripts/mte_processor.py
Resultado:
O arquivo dados_auxiliares_mte_limpos.csv será gerado no diretório raiz, pronto para integração com outras bases.
