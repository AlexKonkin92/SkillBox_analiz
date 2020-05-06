orders_dict = {} #в словарь вносим ключ (наименование источника) и значение(кол-во посещений по источнику)
with open('[sharewood.band] orders_by_source.txt', 'r') as f:
    for line in f:
        line = line.strip().split('\t')  
        source = line[0]
        orders_count = int(line[1])
        orders_dict[source] = orders_count
def searchForLine( source): # в функции прогоняем источника из файла ниже и записываем кол-во посещений(значение по ключу)
    if source in orders_dict:
        return int(orders_dict[source])
    else:
        return 0   
with open('joined_by_source.txt', 'w') as f_joined: #создаем новый файл, в который будем записывать данные из файла ниже
    f_joined.write('{}\t{}\t{}\t{}\n'.format( 'source', 'visits', 'orders','konv') ) #названия столбцов для файла
    with open('[sharewood.band] visits_by_source.txt', 'r') as g:
        for line in g:
            line = line.strip().split('\t') 
            source = line[0]
            visits = int(line[1])
            orders = searchForLine(source)
            konv = round(orders / visits,3)
            f_joined.write('{}\t{}\t{}\t{}\n'.format( source, visits, orders,konv) ) #табуляция,табуляция,табуляция,enter
    
with open('joined_by_source.txt', 'r') as f:
    for line in f:
        line = line.strip().split('\t') 
        print (line)



