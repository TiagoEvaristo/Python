import pandas as pd

# importando dados de um arquivo excel
data = pd.read_excel('VendaCarros.xlsx')
print(type(data))

# selecionando colunas
df = data[['Fabricante', 'Ano', 'ValorVenda']]
print(df.head())

# pivot table
pivot_table = df.pivot_table(
    index='Ano',
    columns='Fabricante',
    values='ValorVenda',
    aggfunc='sum'
)

print(pivot_table)

# exportando para excel
pivot_table.to_excel('data/datapivot_table.xlsx', sheet_name='Relatorio')