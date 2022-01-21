# -*- coding: windows-1252 -*-
#-----------------------------------------------------------------------------
# Exercice 2 - Création de listes
#
# (1) Ecrire un script qui génère une liste d'entiers donnés en entrée par
#     l'utilisateur, la saisie s'arrête pour la valeur 0.
#
# (2) Modifier le script pour qu'il affiche le nombre d'entiers et leur somme
#     en parcourant la liste.
#-----------------------------------------------------------------------------


s = None
ma_liste = []

i = 0
j = 0
somme = 0

while s != '0':
    s = input('Ajouter un nombre entier ---> ')
    ma_liste.append(s)
    i = i +1

while j != len(ma_liste):
    somme = somme + (int(ma_liste[j]))
    j = j + 1


print(f'\nLa somme des nombres entiers entré est --> {somme}')
print(f'Et il y un total de {j} nombres entiers')