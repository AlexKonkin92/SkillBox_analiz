import pandas as pd
def ea(row):#пишем функцию для заполнения столбца годами
    years = [str(i) for i in range (1950 ,2011)]#переводим в str, тк поиск будет вестись по строке
    for i in years:
        if i in row['title']:
            return i
    return 1900
        
    
movies = pd.read_csv('[sharewood.band] movies.csv')
data = pd.read_csv('[sharewood.band] ratings.csv')
movies['year'] = movies.apply(ea,axis = 1)
joined = movies.merge(data, on='movieId', how='left')#объединяем таблицы
a = joined.groupby('year').agg({'rating' : 'mean'}).reset_index().sort_values('rating', ascending = False)#среднее по годам
a.head(10)




