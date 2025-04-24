Dataset Survey carregado. Shape: (4746, 36)
Dataset Microdados carregado. Shape: (27, 12)

Nomes das colunas do Survey (APÓS LIMPEZA):
Index(['P1_l_Nivel_de_Ensino', 'P1_m_Área_de_Formação', 'P2_h_Faixa_salarial',
       'P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem',
       'P2_g_Nivel', 'P4_d_1_SQL', 'P4_d_2_R', 'P4_d_3_Python', 'P4_d_4_CCC',
       'P4_d_5_NET', 'P4_d_6_Java', 'P4_d_7_Julia', 'P4_d_8_SASStata',
       'P4_d_9_Visual_BasicVBA', 'P4_d_10_Scala', 'P4_d_11_Matlab',
       'P4_d_12_Rust', 'P4_d_13_PHP', 'P4_d_14_JavaScript',
       'P4_d_15_Não_utilizo_nenhuma_linguagem', 'P1_b_Genero',
       'P1_c_Corracaetnia', 'P2_b_Setor', 'P1_i_1_uf_onde_mora',
       'P2_f_Cargo_Atual',
       'P4_e_Entre_as_linguagens_listadas_abaixo_qual_é_a_que_você_mais_utiliza_no_trabalho',
       'P2_o_1_RemuneraçãoSalário', 'P2_o_2_Benefícios',
       'P2_o_3_Propósito_do_trabalho_e_da_empresa',
       'P2_o_4_Flexibilidade_de_trabalho_remoto',
       'P2_o_5_Ambiente_e_clima_de_trabalho',
       'P2_o_6_Oportunidade_de_aprendizado_e_trabalhar_com_referências_na_área',
       'P2_o_7_Plano_de_carreira_e_oportunidades_de_crescimento_profissional',
       'P2_o_8_Maturidade_da_empresa_em_termos_de_tecnologia_e_dados',
       'P2_o_9_Qualidade_dos_gestores_e_líderes',
       'P2_o_10_Reputação_que_a_empresa_tem_no_mercado'],
      dtype='object')

Verificando colunas selecionadas...
Coluna target encontrada: 'P2_h_Faixa_salarial'
Shape após seleção: (4746, 20)

NaNs no salário midpoint: 0
Shape após tratar salário: (4746, 20)
Processando ordinal: 'P1_l_Nivel_de_Ensino'
  Aviso: Categorias extras: ['Prefiro não informar']
Processando ordinal: 'P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem'
Processando ordinal: 'P2_g_Nivel'

Colunas Nominais: ['P1_m_Área_de_Formação', 'P4_e_Entre_as_linguagens_listadas_abaixo_qual_é_a_que_você_mais_utiliza_no_trabalho']
Colunas Numéricas: ['P4_d_1_SQL', 'P4_d_2_R', 'P4_d_3_Python', 'P4_d_4_CCC', 'P4_d_5_NET', 'P4_d_6_Java', 'P4_d_7_Julia', 'P4_d_8_SASStata', 'P4_d_9_Visual_BasicVBA', 'P4_d_10_Scala', 'P4_d_11_Matlab', 'P4_d_12_Rust', 'P4_d_13_PHP', 'P4_d_14_JavaScript', 'P1_l_Nivel_de_Ensino', 'P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem', 'P2_g_Nivel']

Imputação final OK.

Shapes: Treino X=(3559, 19), Teste X=(1187, 19)
Colunas Categóricas para LGBM: ['P1_m_Área_de_Formação', 'P4_e_Entre_as_linguagens_listadas_abaixo_qual_é_a_que_você_mais_utiliza_no_trabalho']

Instanciando e treinando o modelo LightGBM...

<ipython-input-1-551e857c82f3>:170: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.


  median_val = df_model[col].median(); df_model[col].fillna(median_val, inplace=True)
<ipython-input-1-551e857c82f3>:183: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.


  df_model[col].fillna('Desconhecido', inplace=True); df_model[col] = df_model[col].astype('category'); categorical_cols_nominal.append(col)
<ipython-input-1-551e857c82f3>:179: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.


  if pd.api.types.is_numeric_dtype(df_model[col]): df_model[col].fillna(0, inplace=True); numeric_cols.append(col)
<ipython-input-1-551e857c82f3>:183: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.


  df_model[col].fillna('Desconhecido', inplace=True); df_model[col] = df_model[col].astype('category'); categorical_cols_nominal.append(col)

[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.073341 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 67
[LightGBM] [Info] Number of data points in the train set: 3559, number of used features: 17
[LightGBM] [Info] Start training from score 10000.500000
Training until validation scores don't improve for 50 rounds
Did not meet early stopping. Best iteration is:
[96]	valid_0's l1: 3539.56
Treinamento concluído.

Predizendo e avaliando no conjunto de teste...
MAE: R$ 3,539.56 | RMSE: R$ 5,637.24 | R²: 0.4971

--- Interpretação do Modelo ---

7.1 Importância Geral das Features (Gain):

<Figure size 1000x600 with 0 Axes>


7.2 Visualização de Árvore Individual (Exemplo: Árvore 0):
   -> Usando lgb.plot_tree:

<Figure size 3000x2000 with 0 Axes>


   -> Usando graphviz:

leaf 0: 9350.500 P1_l_Nivel_de_Ensino ≤ 1.500 yes P1_l_Nivel_de_Ensino ≤ 2.500 no leaf 8: 9600.500 yes leaf 18: 10000.500 no P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem ≤ 2.500 yes leaf 7: 10000.500 no P4_e_Entre_as_linguagens_listadas_abaixo_qual_é_a_que_você_mais_utiliza_no_trabalho = 2 yes P2_g_Nivel ≤ 0.000 no leaf 3: 9350.500 yes P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem ≤ 2.500 no leaf 6: 9500.500 P4_d_3_Python ≤ 0.000 yes P1_l_Nivel_de_Ensino ≤ 3.500 no leaf 19: 9700.500 yes leaf 29: 9700.500 no yes P1_l_Nivel_de_Ensino ≤ 1.500 no leaf 9: 9500.500 yes P4_d_3_Python ≤ 0.000 no leaf 20: 9700.500 yes P4_d_9_Visual_BasicVBA ≤ 0.000 no leaf 22: 9700.500 yes leaf 23: 9700.500 no P2_g_Nivel ≤ 1.500 yes P4_d_9_Visual_BasicVBA ≤ 0.000 no leaf 2: 9700.500 P4_d_1_SQL ≤ 0.000 yes P1_l_Nivel_de_Ensino ≤ 2.500 no leaf 17: 10000.500 yes leaf 30: 10000.500 no P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem ≤ 2.500 yes P4_e_Entre_as_linguagens_listadas_abaixo_qual_é_a_que_você_mais_utiliza_no_trabalho = 12 no leaf 15: 10000.500 yes P1_l_Nivel_de_Ensino ≤ 2.500 no leaf 21: 10000.500 yes leaf 28: 10400.500 no yes leaf 10: 9700.500 no P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem ≤ 3.500 yes P4_e_Entre_as_linguagens_listadas_abaixo_qual_é_a_que_você_mais_utiliza_no_trabalho = 7||10||12||14 no leaf 1: 9500.500 P1_l_Nivel_de_Ensino ≤ 2.500 yes leaf 24: 10000.500 no P2_g_Nivel ≤ 1.500 yes P4_d_3_Python ≤ 0.000 no leaf 5: 10000.500 P1_l_Nivel_de_Ensino ≤ 2.500 yes leaf 25: 10000.500 no yes P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem ≤ 6.500 no leaf 14: 10000.500 yes leaf 16: 10400.500 no yes P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem ≤ 5.500 no leaf 4: 10400.500 P4_d_3_Python ≤ 0.000 yes leaf 13: 10000.500 no P2_g_Nivel ≤ 1.500 yes leaf 12: 10400.500 no yes P4_d_3_Python ≤ 0.000 no leaf 11: 10800.500 yes P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem ≤ 6.500 no leaf 26: 10400.500 yes leaf 27: 10400.500
no


--- 7.3 Interpretação SHAP (Recomendada para GBM) ---
Calculando SHAP values...
Cálculo SHAP concluído.

Plotando Resumo SHAP (dot)...

/usr/local/lib/python3.11/dist-packages/shap/plots/_beeswarm.py:1153: UserWarning: Tight layout not applied. The left and right margins cannot be made large enough to accommodate all Axes decorations.
  pl.tight_layout()
<ipython-input-1-551e857c82f3>:311: UserWarning: Tight layout not applied. The left and right margins cannot be made large enough to accommodate all Axes decorations.
  plt.title("SHAP Summary Plot (Dot)"); plt.tight_layout(); plt.show()


Plotando Resumo SHAP (bar)...

/usr/local/lib/python3.11/dist-packages/shap/plots/_beeswarm.py:1153: UserWarning: Tight layout not applied. The left and right margins cannot be made large enough to accommodate all Axes decorations.
  pl.tight_layout()
<ipython-input-1-551e857c82f3>:315: UserWarning: Tight layout not applied. The left and right margins cannot be made large enough to accommodate all Axes decorations.
  plt.title("SHAP Summary Plot (Bar)"); plt.tight_layout(); plt.show()


Plotando SHAP Dependence Plots...

Plotando Dependência SHAP: 'P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem' vs Salário (colorido por 'P1_l_Nivel_de_Ensino')
  Erro plot dependência 'P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem': 'final_order'

Plotando Dependência SHAP: 'P4_d_3_Python' vs Salário (colorido por 'P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem')


Plotando Dependência SHAP: 'P1_l_Nivel_de_Ensino' vs Salário (colorido por 'P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem')
  Erro plot dependência 'P1_l_Nivel_de_Ensino': 'final_order'

Plotando Dependência SHAP: 'P2_g_Nivel' vs Salário (colorido por 'P2_i_Quanto_tempo_de_experiência_na_área_de_dados_você_tem')
  Erro plot dependência 'P2_g_Nivel': 'final_order'

--- Fim da Análise ---


