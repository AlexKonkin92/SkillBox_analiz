import pandas as pd
data = pd.read_csv (r'C:\Users\79851\PycharmProjects\Alex\venv\Файлы\power.csv')
a = data[ (data['country']=='Lithuania') | (data['country']=='Latvia') | (data['country']=='Estonia') ] #оставляем строки с такими странами
b = a[(a['year'] >= 2005) & (a['year'] <= 2010)]#выставляем год
df = b.drop(b.loc[(b['quantity'] <= 0)].index)#удаляем строки со значениями 0 и меньше нуля
df = df[(df['category'] == 4) | (df['category'] == 12) | (df['category'] == 21)]#оставляем нужные категории
print(df['quantity'].sum())#суммируем по столбцу