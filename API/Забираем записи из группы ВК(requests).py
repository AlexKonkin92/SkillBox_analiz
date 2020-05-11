import requests
from yaml import load
from datetime import datetime, timedelta
from pprint import pprint
with open('my_key.yaml', 'r') as f: #в файле находится мой токен, чтобы каждый раз не вводить
    config = load(f)
token = config['access_token']
url = 'https://api.vk.com/method/wall.get' #урл чтобы брать данные из группы
params = {
    'domain': 'ecoruss', #группы
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
pprint(stats)