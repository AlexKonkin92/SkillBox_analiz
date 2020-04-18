roi_stats = {}
cpa_commission = {'burgerclub': 0.3, 'food-delivery': 0.25}  # комиссия по партнерам cpa
cpc_commission = {'city-magazine': 7, 'foody': 9}  # комиссия по партнерам cpc
fixed_commission = 4  # комиссия по остальным партнерам


def source_type(line):  # создаем ф-цию, в которой вводим строку, преобразовываем нужные столбцы
    b = line[5]  # source
    c = float(line[-1].replace(',', '.'))  # paid
    d = float(line[6].replace(',', '.'))  # cost
    if b in cpa_commission:
        return b, d + c * cpa_commission[b], c #считаем полные расходы (cost + комиссия) для каждого типа (source)
    if b in cpc_commission:
        return b, d + cpc_commission[b], c
    return b, d + fixed_commission, c


# v = source_type(['40443', '05.10.2016 23:18', '1010', '0,000925926', 'seo', 'burgerclub', '1', '6243', '20,20'])
# print(v)

with open(r'C:\Users\79851\PycharmProjects\Alex\venv\Файлы\[sharewood.band] data_no_header.txt', 'r') as f:
    for line in f:
        line = line.strip().split('\t')
        source, cost, paid = source_type(line)
        if source in roi_stats:
            roi_stats[source]['cost'] += cost
            roi_stats[source]['paid'] += paid
        else:
            roi_stats[source] = {}#создаем вложенный словарь
            roi_stats[source]['cost'] = cost #добавляем во вложенный словарь cost и paid
            roi_stats[source]['paid'] = paid
for source in roi_stats.keys(): # добавляем во вложенные словари показатель ROI
    roi_stats[source]['roi'] = (roi_stats[source]['paid'] - roi_stats[source]['cost'])/roi_stats[source]['cost']
for source, value in roi_stats.items():
    print(source,value['roi'])
    #print('{}\t{:.2f}'.format(source, value['roi'])) #вывод с двумя знаками



