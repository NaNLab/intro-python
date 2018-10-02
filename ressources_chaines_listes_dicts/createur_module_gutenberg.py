import codecs

def transformer_dictionnaire_gut():
    f = codecs.open('gutenberg.txt', 'r', 'utf-8-sig') #caractère \ufeff (BOM de utf-8) au début de la chaîne ... ( ? )
    S = 'liste_mots = ['
    for line in f:
        line = line[0:-1]
        S += '\'' + line + '\', '
    S = S[:-2] + ']'
    f.close()
    g = codecs.open('module_gutenberg.py', 'w', 'utf-8')
    g.write(S)
    g.close()

transformer_dictionnaire_gut()
