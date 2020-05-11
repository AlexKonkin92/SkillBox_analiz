import xlwt 
from xlwt import Workbook 

# Workbook is created 
wb = Workbook() 

# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

#general syntax
#sheet1.write(row ,column, value) 

sheet1.write(0, 0, 'Key')  #добавляем наименования столбцов
sheet1.write(0, 1, 'comments') 
sheet1.write(0, 2, 'likes') 
sheet1.write(0, 3, 'reposts') 
sheet1.write(0, 4, 'views') 
sheet1.write(0, 5, 'date') 

row = 1
#iterate the each key-value pair of dictionary & insert into sheet
for k, v in empty_dict.items():
    sheet1.write(row, 0, k) 
    sheet1.write(row, 1, v[0]) #в словаре к одному ключу шел списк из значений, каждое значение записывается в отдельный столбец
    sheet1.write(row, 2, v[1]) 
    sheet1.write(row, 3, v[2]) 
    sheet1.write(row, 4, v[3]) 
    sheet1.write(row, 5, v[5]) 
    row = row + 1

wb.save('key_example3.xlsx') 