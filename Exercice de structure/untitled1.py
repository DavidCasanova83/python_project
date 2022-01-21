# -*- coding: windows-1252 -*-
#-----------------------------------------------------------------------------
# Exercice 2 - Création de listes
#
# (1) Générer N entiers aléatoires compris entre 0 et 100
#     Et les stockers dans une liste
#
#
#
#-----------------------------------------------------------------------------

from random import randrange
from tqdm import tqdm

N = 10 #nombre entier generer



ma_liste = []
somme = 0

for i in tqdm(range(N)):
    n = randrange(1,100)
    somme = somme + n
    ma_liste.append(n)
    
mean = somme / len(ma_liste)

print(f'Moyenne : {mean}')
print(ma_liste)
