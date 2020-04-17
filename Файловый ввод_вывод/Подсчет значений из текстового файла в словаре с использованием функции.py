def source_type(line):#создаем ф-цию, в которой вводим строку, преобразовываем нужные столбцы и возвращаем две переменные
    a = line[4]
    b = line[5]
    c = float(line[-1].replace(',', '.'))
    if c >= 20:
        orderType = 'expensive'
    else:
        orderType = 'cheap'
    if b == 'google' or b == 'yandex':
        if a == 'seo' or a == 'sem':
            sourceType = 'search engines seo'
        elif a == 'brand':
            sourceType = 'search engines brand'
        else:
            sourceType = 'search engines undefined'
    else:
        sourceType = 'other'
    return sourceType, orderType

source = {}
with open(r'C:\Users\79851\PycharmProjects\Alex\venv\Файлы\[sharewood.band] data_no_header.txt','r') as f:
    for line in f:
        line = line.strip().split('\t')
        sourceType, orderType = source_type(line)#берем переменные из ф-ции
        z = sourceType + ' ' + orderType
        if z in source:#создаем словарь
            source[z] = source[z] + 1#считаем кол-во по каждому критерию
        else:
            source[z] = 1
print(source)
