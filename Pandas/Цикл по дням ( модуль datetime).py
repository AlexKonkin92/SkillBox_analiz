import pandas as pd
from datetime import datetime, timedelta
startDate = '2017-01-01'
endDate = '2017-01-07'
startDate_datetime = datetime.strptime( startDate, '%Y-%m-%d' )#переводим в тип даты
endDate_datetime = datetime.strptime( endDate, '%Y-%m-%d' )
current_day = startDate_datetime #создаем переменную, начальная дата
while current_day <= endDate_datetime: #нужно вывести список дат с ... по
    print( current_day.strftime( '%Y-%m-%d' ) )  #вывод в формате строки  
    current_day += timedelta( days = 1 )
