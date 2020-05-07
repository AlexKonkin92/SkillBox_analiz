#!/usr/bin/env python
# coding: utf-8

# In[14]:


def fillLevels( lineRemainder ): #создаем словарь с большим кол-вом вложенных ключей
    dict2fill = {}
    if len( lineRemainder ) > 1:
        dict2fill[ lineRemainder[0] ] = fillLevels( lineRemainder[1:] )
    else:
        return lineRemainder[0]
    return dict2fill

def checkLevels( levelDict, level, line ): #пустой словарь, 0 , строки поочередно
    if line[ level ] in levelDict: #проверка каждого уровня в словаре
        checkLevels( levelDict[ line[ level ] ], level + 1, line ) #если есть , то идет проверка след.уровня
        return levelDict
    else:
        levelDict[ line[ level ] ] =  fillLevels( line[ level + 1: ] ) #если ключа нет, то словарь дополняется с помощью функции
        return levelDict

data = [
    ['2016-10-01', 'google', 'sem', 5],
    ['2016-10-01', 'google', 'seo', 1],
    ['2016-10-01', 'newsletter', 'email', 1]
]
data_dict = {}
for line in data:
    data_dict = checkLevels(data_dict, 0, line)
    
    
def findLineValue( finalDict, line ): #функция поиска кол-ва покупок по параметрам
    if len( line ) > 1:
        if line[ 0 ] in finalDict: #проверка каждого ключа в словаре
            return findLineValue( finalDict[ line[ 0 ] ], line[1:] ) #если ключ есть , то опускаемся на уровень ниже
        else:
            return 0
    else:
        if line[0] in finalDict:
            return finalDict[ line[0] ]
        else:
            return 0

    
findLineValue( data_dict, ['2016-10-01', 'google', 'sem'] )





# In[ ]:




