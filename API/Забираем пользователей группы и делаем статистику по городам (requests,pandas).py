import time
import requests
import pandas as pd
%matplotlib inline
#забираем пользователей из группы и делаем список

url = 'https://api.vk.com/method/groups.getMembers'
count = 10 #кол-во пользователей за раз
offset = 0 #смещение будет производиться на кол-во выгрузки
user_ids = []
while offset < 100:   #поменять, смотря какое кол-во пользователей нужно будет выгрузить 
    params = {
        'group_id': 'dohod_ru',
        'v': 5.73,
        'count': count,
        'offset': offset,
        'access_token': '1757dd551757dd551757dd551117261cf9117571757dd5549e2f36928d68bfadaa3b16f'
    }  
    r = requests.get(url, params = params)
    data = r.json()   
    user_ids += data['response']['items']  
    offset += count
    time.sleep(0.5)
    
#находим город у пользователя и делаем график

url = 'https://api.vk.com/method/users.get?user_id=1&v=5.103&fields=sex,bdate,city&access_token'
a = {}
for user in user_ids:
    params = {
    'user_ids': user,
    'v': 5.73,
    'fields': 'sex,bdate,city',
    'access_token': '1757dd551757dd551757dd551117261cf9117571757dd5549e2f36928d68bfadaa3b16f'
    }
    r = requests.get(url, params = params)
    data = r.json()
    if 'city' in data['response'][0]:
        if data['response'][0]['city']['title']  in a:
            a[data['response'][0]['city']['title']] += 1
        else:
            a[(data['response'][0]['city']['title'])] = 1
df = pd.DataFrame.from_dict(a,orient = 'index').reset_index() #создаем df из словаря для удобства работы
df.rename(columns = {'index': 'city', 0: 'users'}, inplace = True) #переименовываем столбцы
df = df.sort_values('users', ascending = False) 
df['category'] = df.apply(lambda x: x['city'] if x['users'] > 2 else 'другие', axis = 1) #добавляем новый столбец
df.head().plot(kind = 'bar',x='city',y='users') #строим диаграмму
#df.head().plot(kind = 'pie', y = 'users', figsize= (7, 7))
#print(df)