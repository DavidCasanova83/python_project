# -*- coding: windows-1252 -*-
#-----------------------------------------------------------------------------
# Exercice 10 - Nombres parfaits
#
# Un nombre parfait est un nombre qui est égal à la somme de tous ses diviseurs
# excepté lui-même. Par exemple 6 est un nombre parfait car 6 = 1+2+3.
# Ecrire un script qui affiche si un entier donné est un nombre parfait ou non.
#-----------------------------------------------------------------------------


repeat = 0
nb = 1
while repeat != 10000 :
    repeat = repeat +1
    result = 0
    for i in range (1,nb):
        if nb % i == 0:
            result = result + i
    if result == nb:
        print (f"{nb} est un nombre parfait")
    nb = nb +1