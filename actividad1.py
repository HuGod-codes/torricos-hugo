import pandas as pd
import random
import sklearn

def thingToNum(value):
    num = 0
    digitos = set(['1','2','3','4','5','6','7','8','9','0'])
    for i in value:
        if i == '.':
            return num
        elif i in digitos:
            num = num * 10 + int(i)
    return num

# ------ Lectura y analisis exploratorio de datos -------

# df = pd.read_csv("datos/ejemplo_data.csv")
# print(df.dtypes)

# df = df.astype({'ID':'int', 'Activo':'bool'})
# print(df.dtypes)

# print(df)

# df['Unidades'] = df['Unidades'].apply(thingToNum)
# df['2016'] = df['2016'].apply(thingToNum)
# df = df.astype({'Unidades':'int', '2016':'float'})

# print(df)
# print(df.dtypes)

# ---- Lectura y analisis exploratorio de datos 2  -----

# df2 = pd.read_csv("datos/ecommerce_data.csv", parse_dates = [4], date_format = "%d/%m/%y %H:%M", encoding = 'unicode_escape')
# print(df2.dtypes)

# print(df2[:10])

# df2['InvoiceNo'] = df2['InvoiceNo'].apply(thingToNum)
# df2 = df2.astype({'InvoiceNo':'int', 'Description':'str'})
# print(df2.dtypes)

# df2 = df2.astype({'Quantity':'int', 'UnitPrice':'float'})

# df2[['Date', 'Time']] = df2['InvoiceDate'].str.split(' ', expand=True)
# del df2['InvoiceDate']

# df2['Price'] = df2['Quantity'] * df2['UnitPrice']
# print(df2[140:155])

# df2.to_csv('new_ecommerce_data.csv', index=False)

# - Exploracion de funciones de pandas -

# ---------  Estadisticas Descriptivas  ----------

# people = {'ID': [], 'Age': [], 'Height': [], 'Grade': []}

# for i in range(50):

#     n = [random.randint(65,90) for _ in range(4)]

#     id = chr(n[0])
#     for l in random.choices(range(10), k = 6):
#         id += str(l)

#     people['ID'].append(id)
#     people['Age'].append(n[1]-47)
#     people['Height'].append(1+n[2]/100)
#     people['Grade'].append(99*(n[3]-65)/25+1)

# people['Approved'] = ['YES' if grade >= 51 else 'NO' for grade in people['Grade']]

# dfPeople = pd.DataFrame(people)

# print(dfPeople.describe())
# print(dfPeople.var(numeric_only=True))
# print(dfPeople.cov(numeric_only=True))

# ------  Transformacion e Imputacion de datos  -------

dfR = pd.read_csv("datos/ratings_data.csv")
dfB = pd.read_csv("datos/books_data.csv", sep=';', encoding = 'unicode_escape')

dfB.info()
print(dfB.isna().sum())