import requests
def exchange_rates(idi): #поиск наименования на русском по id
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']  #считываем со страницы данные о валютах
    for key in response:
        if response[key]['ID'] == idi:
            return response[key]['Name']

exchange_rates('R01565')
