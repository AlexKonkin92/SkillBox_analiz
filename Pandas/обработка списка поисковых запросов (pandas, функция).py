#обработка списка поисковых запросов и статистики рекламных кампаний

import pandas as pd
from urllib import parse
def campaign_name(row):#функция для вытаскивания campaign
    parsed = parse.urlsplit(row['link'])
    params_dict = parse.parse_qs(parsed.query)
    return params_dict['utm_campaign'][0]
#pd.set_option('display.max_columns', 500)#показать все столбцы
data = pd.read_excel(r'C:\Users\79851\PycharmProjects\Alex\venv\Файлы\ad_campaigns.xlsx')
data.rename(columns={'Название группы': 'group', 'Фраза (с минус-словами)': 'phrase','Продуктивность': 'effect', 'ID объявления': 'ad_id', 'Заголовок': 'title','Текст': 'text', 'Ссылка': 'link'}, inplace=True)
data['campaign'] = data.apply(campaign_name, axis=1)#применяем функцию для нового столбца
data['cnt'] = data['campaign'].apply(lambda x:len(x))#считаем кол-во символов для нового столбца
#print(data.groupby('campaign').agg(['min', 'max'])['effect'].reset_index().head())#min и max для столбца effect
data['phrase_length'] = data.apply(lambda row: len(row['phrase']), axis=1)#кол-во слов из столбца phrase
#print(data.groupby(['group', 'campaign']).count().sort_values('phrase', ascending=False).reset_index().head()) #сколько раз такая группа с таким camplaign встречается в файле
#print(data.groupby('campaign').agg({'effect': ['min', 'max'], 'phrase_length': 'mean'}).reset_index().head())#мин,макс и среднее для camplaign
print(data.groupby('campaign').agg(['sum'])['effect'].reset_index().sort_values('sum', ascending=True).head())#сумма по столбцу effect с сортировкой
#print(data.groupby('campaign').sum().reset_index().sort_values('effect', ascending=False).head())