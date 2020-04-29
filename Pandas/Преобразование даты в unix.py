import pandas as pd
from datetime import datetime, timedelta
import time


def convert_to_datetime(row):
    return datetime.strptime(row['date'], '%d.%m.%Y %H:%M')

def make_unix_time(row):
    return time.mktime(row['datetime'].timetuple()) #преобразование даты в unix


data = pd.read_csv('[sharewood.band] data.tsv',sep = '\t')
data['datetime'] = data.apply(convert_to_datetime, axis=1)
data['unixtime'] = data.apply(make_unix_time, axis=1)
data.groupby('user_id').agg({'unixtime':['min','max']}).reset_index()
data.head(20)


