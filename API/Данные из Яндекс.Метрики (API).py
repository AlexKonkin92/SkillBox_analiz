import requests
from yaml import load
from pprint import pprint
# импортируем токен для запросов к API
f = open('Токен Яндекс.Метрика.txt', 'r')
config = load(f)
token = config['token']
API_URL = 'https://api-metrika.yandex.ru/stat/v1/data'
# даты выгрузки отчета
startDate = '2018-02-12'
endDate = '2018-02-18'
# номер счетчика
counter = '21075004'
# название шаблона отчета
preset = 'traffic'
#фильтр по стране
filters = "ym:s:regionCountryName=='Россия'"
params = {
    'date1': startDate,
    'date2': endDate,
    'id': counter,
    'preset': preset,
    'oauth_token': token,
    'filters': filters
}
r = requests.get(API_URL, params = params)
data = r.json()
pprint(data['data'])