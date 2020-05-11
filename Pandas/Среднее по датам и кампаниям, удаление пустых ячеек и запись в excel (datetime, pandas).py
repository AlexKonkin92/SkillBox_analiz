import pandas as pd
from datetime import datetime

def datetime_to_date(date_string):
    """Перевод даты покупки в формат %Y-%m-%d"""   
    try:
        # пробуем расшифровать дату в формате '%d.%m.%Y %H:%M'
        date_datetime = datetime.strptime(date_string['date'], '%d.%m.%Y %H:%M')   
    except ValueError:   #если ошибка ValueError(можно поставить другую или убрать тип ошибки)     
        # пробуем расшифровать дату в формате '%d.%m.%YT %H:%M:%S'
        try:
            date_datetime = datetime.strptime(date_string['date'], '%d.%m.%YT %H:%M:%S')    
        except:
            # ни один из известных форматов не подошел, возвращаем 'undefined'
            return 'undefined'    
    return date_datetime.strftime('%Y-%m-%d')

def row_cpa(row):
    """Делим на млн значения столбца"""   
    if row['medium'] == 'cpa-partners':
        new_cost = round(row['amount_paid'] / 1000000,2)
    else:
        new_cost = row['amount_paid']
    return new_cost
    
#при чтении файла заменяем все точки на запятые (decimal) (смотреть внимательно , может в наименовании поменяться)
data = pd.read_csv('[sharewood.band] real_data_no_header.txt', decimal=',', sep = '\t', names = ['id', 'date', 'user_id', 'duration', 'medium', 'source', 'cost', 'order_id', 'amount_paid'])
data['dateTime'] = data.apply(datetime_to_date, axis = 1) #новый столбец для новой даты
data.dropna(axis = 0, inplace = True) #удаляем строки, в которых есть пустые (NaN) значения
data['NewCost'] = data.apply(row_cpa, axis = 1) #новая стоимость
#data.groupby('dateTime','medium').agg({'NewCost': ['mean']})
a = data.groupby(['dateTime','medium']).agg({'NewCost': ['sum']})
a.sort_values('dateTime',ascending = False)

#записываем данные в excel - файл
a.to_excel('result7.xlsx', index=False)



