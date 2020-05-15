from pymystem3 import Mystem
m = Mystem()
i = 0
with open( 'keywords.txt', 'r', encoding = 'utf-8' ) as f:
    for line in f:
        line = line.strip().split('\t')
        word = line[0]
        wordCount = line[1]
        lemmas = m.lemmatize( word )
        print( word, ''.join(lemmas) )
        if i > 10:
            break
        i += 1



from pymystem3 import Mystem
m = Mystem()
i = 0
a = 'и хрюкотали зелюки как мюмзики в мове'
lemmas = m.lemmatize( a )
print( a, ''.join(lemmas) ,sep = '\n')


import pymorphy2
morph = pymorphy2.MorphAnalyzer()
i = 0
with open( 'keywords.txt', 'r', encoding = 'utf-8' ) as f:
    for line in f:
        line = line.strip().split('\t')       
        word = line[0]
        wordCount = line[1]        
        morph_analyze = morph.parse( word )
        print( word, morph_analyze[0].normal_form )        
        if i > 5:
            break        
        i += 1


