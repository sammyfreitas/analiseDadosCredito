# ==============================================================
# 🧹 LIMPEZA E ENRIQUECIMENTO DOS DADOS - CREDIT CARD CUSTOMERS
# ==============================================================

import pandas as pd
import numpy as np

# 1. Ler o arquivo original (ajuste o caminho conforme sua pasta)
df = pd.read_csv('../data/BankChurners.csv')

# 2. Remover colunas que não serão utilizadas
colunas_remover = [
    'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1',
    'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'
]
df.drop(columns=colunas_remover, inplace=True)

# 3. Renomear colunas para português
df.rename(columns={
    'CLIENTNUM': 'id_cliente',
    'Attrition_Flag': 'status_cliente',
    'Customer_Age': 'idade',
    'Gender': 'genero',
    'Dependent_count': 'qtde_dependentes',
    'Education_Level': 'escolaridade',
    'Marital_Status': 'estado_civil',
    'Income_Category': 'faixa_renda',
    'Card_Category': 'categoria_cartao',
    'Months_on_book': 'meses_relacionamento',
    'Total_Relationship_Count': 'qtde_produtos',
    'Months_Inactive_12_mon': 'meses_inativo_12m',
    'Contacts_Count_12_mon': 'contatos_12m',
    'Credit_Limit': 'limite_credito',
    'Total_Revolving_Bal': 'saldo_revolvente',
    'Avg_Open_To_Buy': 'credito_disponivel_medio',
    'Total_Amt_Chng_Q4_Q1': 'var_qtd_transacoes_q4_q1',
    'Total_Trans_Amt': 'valor_total_transacoes',
    'Total_Trans_Ct': 'qtde_total_transacoes',
    'Total_Ct_Chng_Q4_Q1': 'var_ct_transacoes_q4_q1',
    'Avg_Utilization_Ratio': 'percentual_utilizacao'
}, inplace=True)

# 4. Corrigir textos e valores nulos
df.replace('Unknown', np.nan, inplace=True)
df['estado_civil'].fillna('Não informado', inplace=True)
df['escolaridade'].fillna('Não informado', inplace=True)
df['faixa_renda'].fillna('Não informado', inplace=True)

# 5. Criar variáveis derivadas
df['faixa_etaria'] = pd.cut(
    df['idade'],
    bins=[0, 30, 40, 50, 60, 70, 100],
    labels=['Até 30', '31-40', '41-50', '51-60', '61-70', '70+']
)

df['anos_relacionamento'] = (df['meses_relacionamento'] / 12).round(1)
df['percentual_limite_usado'] = (df['saldo_revolvente'] / df['limite_credito']).round(2)
df['valor_medio_transacao'] = (df['valor_total_transacoes'] / df['qtde_total_transacoes']).round(2)

# 6. Criar coluna binária de churn
df['alvo_churn'] = df['status_cliente'].apply(lambda x: 1 if x == 'Attrited Customer' else 0)

# 7. Salvar base limpa
df.to_csv('../data/clientes_cartao_limpo.csv', index=False, encoding='utf-8-sig')

# 8. Mostrar resumo da limpeza
print('✅ Base limpa salva em data/clientes_cartao_limpo.csv')
print(f'Total de registros: {len(df)}')
print(f'Colunas finais: {list(df.columns)}')
