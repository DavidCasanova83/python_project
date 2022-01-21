# -*- coding: windows-1252 -*-
#-----------------------------------------------------------------------------
# Exercice 4.3 - Translate grec
#
# Les différents scripts doivent tous utiliser les fonctions ord() et chr().
#-----------------------------------------------------------------------------

ord_a = 97
ord_alpha = 945
delta_ord = ord_alpha - ord_a

s = input('Entrez une phrase en français -- > ')
new_s = ''

i = 0

while i < len(s):
    ch = chr(ord(i) + delta_ord)
    new_s += ch
    print(new_s)
    print(ord(new_s))
    i = i + 1