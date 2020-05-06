orders_dict = {} 
with open('[sharewood.band] orders_by_source_and_medium.txt', 'r') as f:
    for line in f:
        line = line.strip().split('\t')       
        source = line[0]
        medium = line[1]
        orders_count = int( line[2] )      
        orders_dict.setdefault(source, {}) #если нет такого источника , то делаем вложенный словарь
        orders_dict[source].setdefault(medium, 0) #добавляем ключ - значение во вложенный словарь
        orders_dict[source][medium] = orders_count
def searchForLine(source , medium): #забираем значение из вложенного словаря
    if source in orders_dict:
        if medium in orders_dict[source]:
            return orders_dict[source][medium]
        else:
            return 0 
    else:
        return 0 
a = searchForLine('google', 'sem')
print(a)



