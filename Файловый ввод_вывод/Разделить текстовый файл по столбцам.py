total_sum = 0
with open(r'C:\Users\79851\PycharmProjects\Alex\venv\GitHub\stepic_study\[sharewood.band] data_3_columns.txt','r') as f:
    for line in f:
        line = line.strip().split('\t')
        a = line[0]#преобразовать столбец в нормальный вид
        b = line[1]
        c = float(line[2].replace(',','.'))#меняем , на .  и делаем числовой формат
        if b == 'google':#выводим сумму накопительным итогом для гугл
            total_sum = total_sum + c
            print(f'Текущая сумма расходов: {total_sum}')
        #print(a,b,c)