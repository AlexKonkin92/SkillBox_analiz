def date_range(start_date, end_date):
    """
    Возвращает список дат между start_date и end_date с шагом в день.
    Если start_date > end_date, то возвращает пустой список. 
    Пример
    date_range('2018-01-01', '2018-01-07')
    [
        '2018-01-01',
        '2018-01-02',
        '2018-01-03',
        '2018-01-04',
        '2018-01-05',
        '2018-01-06',
        '2018-01-07'
    ]
    """ 
    date_range_list = []
    current_date = start_date  
    current_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')   
    while current_date_dt <= end_date_dt:
        date_range_list.append(current_date)        
        current_date_dt += timedelta(days=1)
        current_date = current_date_dt.strftime('%Y-%m-%d')    
    return date_range_list
