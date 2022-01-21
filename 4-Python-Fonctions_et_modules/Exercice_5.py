# -*- coding: windows-1252 -*-
#-----------------------------------------------------------------------------
# Exercice 5 - Calcul de l'exponentielle avec une s�rie enti�re
#
# On pourra utliser la fonction exp(x) du module math qui retourne e^x.
# (1) D�finir la fonction factorielle(n) qui retourne
# n! = n x (n - 1) x (n - 2) x ... x 1.
# (2) D�finir la fonction puissance(x, n) qui retourne x^n o� x est un r�el et
# n un entier.
# (3) D�finir une fonction serie_exp(x, n) qui retourne le fottant :
# sigma(i=0, n)(x^i/i!) = x^0/0! + x^1/1! + ... + x^n/n!
# (4) Ecrire un script qui demande un flottant x � l'utilisateur puis une
# pr�cision enti�re p et affiche la plus petite valeur n telle que :
# |sigma(i=0, n)(x^i/i!) - e^x| < 10^(-p)
#-----------------------------------------------------------------------------
from math import exp

def facto_iterative(n: int) -> int:
    """Retourne le factoriel de n (version it�rative)"""
    fact = 1
    for i in range(2, n +1):
        fact *= i
    return fact

def facto_recursive(n: int) -> int:
    """Retourne le factoriel de n (version r�cursive) """
    if n == 0:
        return 1
    else:
        return n * facto_recursive(n-1)
    
print(facto_recursive(2950))

print(facto_iterative(5))