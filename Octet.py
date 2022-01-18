# -*- coding: windows-1252 -*-
#-----------------------------------------------------------------------------
# Exercice 13 - Critère de divisibilité par 11
#
# Ecrire un script qui demande un entier à l'utilisateur et affiche si oui ou
# non il est divisible par 11 en utilisant uniquement les opérateurs
# arithmétiques + et -.
#
# Pour savoir si un nombre est divisible par 11, on vérifie si la somme
# alternée de ses chiffres tient sur un chiffre et vaut 0. Sinon on calcule la
# somme des chiffres du nombre ainsi obtenu. Par exemple pour 7260319 on
# calcule 7-2+6-0+3-1+9 = 22 puis 2-2 = 0 et donc 7260319 est divisible par 11.
#-----------------------------------------------------------------------------

n = float(input('Entrez un nombre entier --> '))
result = 0

while n != 0:
    result = n%2
    print(float(f'{result}'))
    n = n/2