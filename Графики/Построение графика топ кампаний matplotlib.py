import pandas as pd
data = pd.read_csv('[sharewood.band] ad_campaigns_stats.csv')
data['campaign'].value_counts().index #считаем популярные кампании
most_popular_campaigns = data.campaign.value_counts().index[:5].tolist() #вносим топ5 в список
data = data[data['campaign'].isin(most_popular_campaigns)] #сортируем df по списку
data['campaign'].unique() #проверка, что кампании только топ5
get_ipython().run_line_magic('matplotlib', 'inline #чтобы строить график онлайн')
data['campaign'].hist() #построить график
