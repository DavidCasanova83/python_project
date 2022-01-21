# -*- coding: windows-1252 -*-
#-----------------------------------------------------------------------------
# Exercice 3 - Maximum d'une liste
#
# (1) Ecrire un script qui affiche la valeur du plus grand entier d'une liste
#     d'entiers prédéfinie.
# (2) Modifier le script précédent pour qu'il affiche en plus la valeur du
#     deuxième plus grand entier de la liste.
# (3) Modifier le script précédent pour qu'il affiche également les indices de
#     ces deux nombres.
#-----------------------------------------------------------------------------


ma_liste = [1014, 4743, 4525, 3653, 4989, 1211, 2331, 4310, 3302, 2150, 2856, 1835,
     2624, 2850, 4491, 3, 3328, 3990, 2721, 6000]



i = 0

number_max = 0 


while i != len(ma_liste):
    if ma_liste[i] > number_max:
        number_max = ma_liste[i]
    i = i + 1
    
print(f'le nombre max est --->  {number_max}')
ma_liste[number_max] = ma_liste[number_max] + int(0)
print(f'le nombre max est --->  {number_max}')

