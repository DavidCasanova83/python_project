# -*- coding: windows-1252 -*-
#-----------------------------------------------------------------------------
# Exercice 4.1 - Liste de mots
#
# Ecrire un script qui crée une liste de chaînes de caractères saisies pas
# l'utilisateur. La saisie s'arrête quand l'utilisateur rentre une chaîne vide.
#-----------------------------------------------------------------------------


s = None
ma_liste = []

i = 0

while s != '':
    s = input('Ajouter un mot ---> ')
    ma_liste.append(s)
    i = i +1


print(f'\nLa somme des nombres entiers entré est --> {ma_liste}')