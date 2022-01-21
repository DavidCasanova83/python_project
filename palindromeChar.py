# -*- coding: windows-1252 -*-
#-----------------------------------------------------------------------------
# Exercice 3.1 - Palindrome
#
# Ecrire un script qui affihe côte-à-côte les caractères opposés d'un mot saisi
# en entrée, c'est-à-dire le premier à coté du dernier, le second à cot& de
# l'avant dernier etc...
# Exemple d'exécution :
# Entrez une chaîne de caractères : Bonjour
# Br
# ou
# no
# jj
#-----------------------------------------------------------------------------


s = input('Ecrire un mot --> ')
size = len(s)/2
i = 0
t = len(s)


while i < size:
    print(s[i] + s[t-1])
    i = i +1
    t = t -1