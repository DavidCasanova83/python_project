# -*- coding: windows-1252 -*-
#-----------------------------------------------------------------------------
# Exercice 12 - Critère de divisibilité par 3
#
# Dans cet exercice on suppose que l'utilisateur se limite aux nombres
# strictement positifs.
# Ecrire un script qui demande un entier à l'utilisateur et affiche si oui ou
# non il est divisible par 3 en utilisant uniquement l'opérateur arithmétique
# +.
#
# On rappelle que l'on peut savoir si un nombre est divisible par 3 sans
# utiliser les opérateurs de division / ou % en calculant la somme de ses
# chiffres décimaux. Si cette somme tient sur un seul chiffre et est divisible
# par 3 alors le nombre de départ est lui aussi divisible par 3. Sinon on
# calcule a somme des chiffres du nombre ainsi obtenu. Par exemple pour 31416
# on calcule 3+1+4+1+6 = 15 puis 1+5 = 6. Le nombre 6 est inférieur à 10 et
# divisible par 3 donc 31416 est divisible par 3.
#-----------------------------------------------------------------------------

n = int(input('Entrez un nombre entier positif'))

while n >= 10:
    sum_numbers = 0
    while n != 0:
        sum_numbers = sum_numbers + n % 10
        n = n // 10
    n = sum_numbers

if n == 3 or n == 6 or n==9:
    print('Divisible par 3')
else:
    print('Pas divisible par 3')