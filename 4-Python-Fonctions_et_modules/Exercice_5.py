# -*- coding: windows-1252 -*-
#-----------------------------------------------------------------------------
# Exercice 5 - Calcul de l'exponentielle avec une série entière
#
# On pourra utliser la fonction exp(x) du module math qui retourne e^x.
# (1) Définir la fonction factorielle(n) qui retourne
# n! = n x (n - 1) x (n - 2) x ... x 1.
# (2) Définir la fonction puissance(x, n) qui retourne x^n où x est un réel et
# n un entier.
# (3) Définir une fonction serie_exp(x, n) qui retourne le fottant :
# sigma(i=0, n)(x^i/i!) = x^0/0! + x^1/1! + ... + x^n/n!
# (4) Ecrire un script qui demande un flottant x à l'utilisateur puis une
# précision entière p et affiche la plus petite valeur n telle que :
# |sigma(i=0, n)(x^i/i!) - e^x| < 10^(-p)
#-----------------------------------------------------------------------------
from math import exp

def facto_iterative(n: int) -> int:
    """Retourne le factoriel de n (version itérative)"""
    fact = 1
    for i in range(2, n +1):
        fact *= i
    return fact

def facto_recursive(n: int) -> int:
    """Retourne le factoriel de n (version récursive) """
    if n == 0:
        return 1
    else:
        return n * facto_recursive(n-1)
    
print(facto_recursive(2950))

print(facto_iterative(5))