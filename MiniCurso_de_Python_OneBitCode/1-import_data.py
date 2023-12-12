import pandas as pd

# importando dados de um arquivo excel
data = pd.read_excel('VendaCarros.xlsx')

print(data)

# Lista os primeiros registros
print(data.head())

# Contagem de valores po fabricante
print(data['Fabricante'].value_counts())