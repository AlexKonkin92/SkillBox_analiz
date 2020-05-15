import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import re
emails = pd.read_csv('emai_base.CSV', sep = '\t', names = ['email'])
pattern = '([\w\.-]+)@([\w]+(\.ru|\.com))'

# то что стоит в первых скобках
#re.search(pattern, 'username@yandex.ru').group(1)
#Результат: 'username'
# то что стоит во вторых скобках
#re.search(pattern, 'username@yandex.ru').group(2)
#Результат: 'yandex.ru'
# то что стоит во внутренних скобках
#re.search(pattern, 'username@yandex.ru').group(3)
#Результат: '.ru'

def get_email_domain(row):
    if re.match(pattern, row['email']): #просматриваем mail из столбца email на принадлежность паттерну
        return re.search(pattern, row['email']).group(2)   #если маска совпадает, то отдаем домен
    else:
        return 'wrong email'
emails = pd.read_csv('emai_base.CSV', sep = '\t', names = ['email'])
emails['domain'] = emails.apply(get_email_domain, axis = 1) #в новый столбец записываем домен
emails['domain'].hist() #график




