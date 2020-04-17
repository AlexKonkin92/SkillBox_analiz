v = {}
i = 0
with open(r'C:\Users\79851\PycharmProjects\Alex\venv\Файлы\[sharewood.band] data_no_header.txt','r') as f:
    for line in f:
        line = line.strip().split('\t')
        a = line[2]#преобразовать столбец в нормальный вид
        c = float(line[8].replace(',', '.'))
        if a in v:
            v[a] = v[a]  + c
        else:
            v[a] = c

        # print(f'Текущий ID: {a}', v , sep = '\n')
        # print()
        i = i + 1
        if i > 7:
            break
print(v,i)