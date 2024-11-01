import pandas as pd


# ------ Lectura y analisis exploratorio de datos -------

def thingToNum(value):
    num = 0
    digitos = set(['1','2','3','4','5','6','7','8','9','0'])
    for i in value:
        if i == '.':
            return num
        elif i in digitos:
            num = num * 10 + int(i) 
    return num

df = pd.read_csv("datos/ejemplo_data.csv")
print(df.dtypes)

df = df.astype({'ID':'int', 'Activo':'bool'})
print(df.dtypes)

print(df)

df['Unidades'] = df['Unidades'].apply(thingToNum)
df['2016'] = df['2016'].apply(thingToNum)
df = df.astype({'Unidades':'int', '2016':'float'})

print(df)
print(df.dtypes)

# ---- Lectura y analisis exploratorio de datos 2  -----

df2 = pd.read_csv("datos/ecommerce_data.csv", parse_dates = [4], date_format = "%d/%m/%y %H:%M", encoding = 'unicode_escape')
print(df2.dtypes)

print(df2[:10])

df2['InvoiceNo'] = df2['InvoiceNo'].apply(thingToNum)
df2 = df2.astype({'InvoiceNo':'int', 'Description':'str'})
print(df2.dtypes)

df2 = df2.astype({'Quantity':'int', 'UnitPrice':'float'})

df2[['Date', 'Time']] = df2['InvoiceDate'].str.split(' ', expand=True)
del df2['InvoiceDate']

df2['Price'] = df2['Quantity'] * df2['UnitPrice']

print(df2[140:155])

df2.to_csv('new_ecommerce_data.csv', index=False)

# ---------  Estadisticas Descriptivas  ----------


