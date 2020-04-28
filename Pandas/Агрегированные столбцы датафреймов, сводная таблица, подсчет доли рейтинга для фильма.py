import pandas as pd
data = pd.read_csv('[sharewood.band] ratings.csv')
data_pivot = data.pivot_table(index = ['movieId', 'rating'], values = 'userId', aggfunc = 'count').reset_index()#посчитали кол-во оценок для каждого фильма по рейтингу
data_pivot['sum'] = data_pivot.groupby('movieId').userId.transform(lambda x: sum(x))#считаем сумму всех оценок для фильма
data_pivot['share'] = (data_pivot['userId'] / data_pivot['sum']) * 100
b = data_pivot[(data_pivot['movieId'] == 1)]#ставим фильтр на столбце   
b['share'].sum()#считаем сумму по столбцу




