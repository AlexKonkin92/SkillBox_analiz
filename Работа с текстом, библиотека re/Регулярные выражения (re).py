import re
pattern = '.*/\d{8}-.*'
prog = re.compile(pattern)
with open('[sharewood.band] URLs.txt', 'r') as f:    
    for line in f:
        line = line.strip()        
        # если текст строки удовлетворяем регулярному выражению pattern, то выводим строку
        if prog.match( line ):
            print( line )


# In[7]:


li = ['9999999999', '999999-999', '99999x9999']
pattern = '[8-9]{1}[0-9]{9}' #начинается с 8 или 9, имеет 9 чисел
prog = re.compile(pattern)

for val in li:
    if prog.match(val):
        print ('yes')
    else:
        print ('no')




