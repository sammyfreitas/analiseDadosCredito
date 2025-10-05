import pandas as pd

# 1. Ler a base
df = pd.read_csv('clientes_cartao_limpo.csv')

# 2. Limpeza simples (exemplo)
df['estado_civil'] = df['estado_civil'].fillna('Não informado')

# 3. Agrupar e calcular médias
resumo = (
    df.groupby('estado_civil', dropna=False)
      .agg(idade_media=('idade', 'mean'),
           limite_medio=('limite_credito', 'mean'),
           qtde_clientes=('id_cliente', 'count'))
      .round(2)
      .reset_index()
)

# 4. Ordenar
resumo = resumo.sort_values('limite_medio', ascending=False)

print(resumo)