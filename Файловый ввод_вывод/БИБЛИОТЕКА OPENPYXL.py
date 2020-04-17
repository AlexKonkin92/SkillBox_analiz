import openpyxl
d = 0
workbook = openpyxl.load_workbook(filename=r'C:\Users\79851\PycharmProjects\Alex\venv\Файлы\data.xlsx')
sheetName = workbook['data']
for line in sheetName['E2:I5']:
    #a = line[0].value
    b = line[1].value
    if b == 'yandex':#вывод суммы по яндексу
        c = line[4].value
        d = d + c
print(d)

# print(line[0].value)
# print(sheetName['E1'].value)#вывести значение одной ячейки
