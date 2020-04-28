import pandas as pd
data = pd.read_csv('[sharewood.band] ratings.csv')
#data.groupby('movieId').agg({'rating':['max','mean']})
#data.groupby('userId').agg({'rating':'count'}).sort_values(by = ['rating'] , ascending = [False]).reset_index()#посмотрели кол-во оценок по убыванию
a = data.groupby('userId').agg({'rating':'count'}).reset_index()
b = a[(a['rating'] >= 100)]#отфильтровали тех, кто сделал больше 100 оценок
film_fans_user_ids = b['userId'].tolist()#внесли данные id  в список
fans_data = data[data['userId'].isin(film_fans_user_ids) ]#отфильтровали id в dataframe по списку
g = fans_data.groupby('userId').agg({'timestamp' : ['min','max']}).reset_index()
g['def_c'] = g['timestamp']['max'] - g['timestamp']['min']#посчитали в новом столбце разность между мин и макс
round(g['def_c'].mean() / 86400,2)#среднее по столбцу

