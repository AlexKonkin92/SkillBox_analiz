import requests
try:
    r = requests.get('https://ya.ru:81', timeout = 5)
except requests.ConnectionError:
    print('Похоже сервис недоступен, пробуем позже или пишем в техподдержку')





