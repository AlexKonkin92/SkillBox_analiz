a = True
with open(r'C:\Users\79851\PycharmProjects\Alex\venv\GitHub\stepic_study\[sharewood.band] user_ids_headers.txt','r') as f:
    for line in f:
        line = line.strip()
        if a:
            a = False
        else:
            print(line)
