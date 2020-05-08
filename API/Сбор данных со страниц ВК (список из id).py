import requests
from pprint import pprint
users = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #список id
a,b = 0,0
url = 'https://api.vk.com/method/users.get?user_id=1&v=5.103&fields=sex,bdate&access_token=1757dd551757dd551757dd551117261cf9117571757dd5549e2f36928d68bfadaa3b16f'
for user in users:
    params = {
        'user_id': user, #ищем юзера, подставляя id из списка
        'v': 5.52,
        'fields': 'sex,bdate'
    }   
    r = requests.get(url, params = params)
    data = r.json()
    if data['response'][0]['sex'] == 1:
        a += 1
    elif data['response'][0]['sex'] == 2:
        b += 1
print(round(a/b,2)) #выводим отношение женщин к мужчинам





