import requests
import xlwt 
from xlwt import Workbook 
from datetime import datetime, timedelta
from yaml import load
from pprint import pprint
with open('my_key.yaml', 'r') as f: #в файле находится мой токен, чтобы каждый раз не вводить
    config = load(f)
token = config['access_token']
url = 'https://api.vk.com/method/wall.get' #урл чтобы брать данные из группы
params = {
    'domain': 'ecoruss', #группа
    'filter': 'owner',
    'count': 100, #сколько записей
    'offset': 0,
    'access_token': token, #мой токен
    'v': 5.103
}
data = requests.get(url, params = params)
stats = {}
for record in data.json()['response']['items']:   
    if 'attachments' in record:
        title = record['text'] #заголовок
    elif 'copy_history' in record: #другой вид записи (не разобрался, не обычная запись)(есть пустые записи , только фотка, можно сделать, чтобы и по таким записям собиралась инфа)
        if 'link' in record['copy_history'][0]['attachments'][0]:
            title = record['copy_history'][0]['attachments'][0]['link']['title']
        elif 'poll' in record['copy_history'][0]['attachments'][0]: #опрос
            title = record['copy_history'][0]['attachments'][0]['poll']['question']
    stats[title] = [record['comments']['count'], record['likes']['count'], record['reposts']['count'], record['views']['count'],datetime.fromtimestamp(record['date']).strftime('%Y-%m-%d') ] #записываем данные по записи, переводим unix формат во временной

#нужны данные за вчерашний день

yesterday = (datetime.now() - timedelta(days = 1)).strftime('%Y-%m-%d')
empty_dict = {}
for title, line in sorted( stats.items(), key = lambda x: -(x[1][0]+x[1][1]+x[1][2]+x[1][3]) ): #сортировка по комментариям, не разобрался в ней, может не работать
    if line[4] == yesterday:
        empty_dict[title] = line

#запись в файл excel

# Workbook is created 
wb = Workbook() 

# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

#general syntax
#sheet1.write(row ,column, value) 

sheet1.write(0, 0, 'Key')  #добавляем наименования столбцов
sheet1.write(0, 1, 'comments') 
sheet1.write(0, 2, 'likes') 
sheet1.write(0, 3, 'reposts') 
sheet1.write(0, 4, 'views') 
sheet1.write(0, 5, 'date') 

row = 1
#iterate the each key-value pair of dictionary & insert into sheet
for k, v in empty_dict.items():
    sheet1.write(row, 0, k) 
    sheet1.write(row, 1, v[0]) #в словаре к одному ключу шел списк из значений, каждое значение записывается в отдельный столбец
    sheet1.write(row, 2, v[1]) 
    sheet1.write(row, 3, v[2]) 
    sheet1.write(row, 4, v[3]) 
    sheet1.write(row, 5, v[5]) 
    row = row + 1

wb.save('key_example3.xlsx')  #может быть пустой файл , внимательно смотреть фильтр