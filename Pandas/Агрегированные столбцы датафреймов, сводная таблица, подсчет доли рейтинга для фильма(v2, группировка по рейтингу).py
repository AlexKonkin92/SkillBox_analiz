def new_rat(row):
    a = row['rating']
    if a <= 2:
        return 'Низкий'
    if a <= 4:
        return 'Средний'
    return 'Высокий'
import pandas as pd
data = pd.read_csv('[sharewood.band] ratings.csv')
data['new_rat'] = data.apply(new_rat,axis = 1)
data_pivot = data.pivot_table(index = ['movieId', 'new_rat'], values = 'userId', aggfunc = 'count').reset_index()
data_pivot['sum'] = data_pivot.groupby('movieId').userId.transform(lambda x: sum(x))
data_pivot['share'] = round((data_pivot['userId'] / data_pivot['sum']) * 100,2)
b = data_pivot[(data_pivot['movieId'] == 356)]
b
