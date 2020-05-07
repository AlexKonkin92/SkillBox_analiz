import requests
def exchange_rates(currency, format='full'): #на вход подается валют, по умолчанию вывод - всё
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']  #считываем со страницы данные о валютах
    if currency in response:
        data = response[currency]  #оставляем только выбранную валюту 
    else:
        return 'Unknown currency!'  
    if format == 'full': #какой формат на вывод
        return data   
    elif format == 'value':
        return data['Value']
    else:
        return 'Unknown format!'
exchange_rates('EUR','value')



