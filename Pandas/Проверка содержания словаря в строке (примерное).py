import pandas as pd
geo_data = {

    'Центр': ['москва', 'тула', 'ярославль'],

    'Северо-Запад': ['петербург', 'псков', 'мурманск'],

    'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']

}
def geo_classification(row):#проверяем значения в столбце keyword
    for region, city_list in geo_data.items():
        for city in city_list:
            if city in row['keyword']:#петербург в петербурге
                return region
    return 'undefined'
data = pd.read_csv(r'C:\Users\79851\PycharmProjects\Alex\venv\Файлы\[sharewood.band] keywords.csv')
data['city_group'] = data.apply(geo_classification, axis=1)
a = data[(data['city_group'] == 'Северо-Запад')]#пример
print(a.head(20))
#print(data.groupby('city_group').count().head())#считаем по каждому региону строки