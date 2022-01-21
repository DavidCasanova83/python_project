# -*- coding: windows-1252 -*-
#-----------------------------------------------------------------------------
# Exercice 1 : les nombres parfaits
#
# Les diviseurs propres d'un nombre sont tous les diviseurs du nombre excepté
# lui-même. Par exemple les diviseurs propres de 8 sont 1, 2, 4.
# Un nombre est parfait s'il est égal à la somme de ses diviseurs propres, par
# exemple 6 = 1 + 2 + 3.
# (1) Ecrire une fonction som_div_propres(n) qui retourne la somme des
# diviseurs propres de l'entier n.
# (2) Ecrire une fonction est_parfait(n) qui retourne le booléen True si le
# nombre n est parfait.
# (3) Ecrire une procédure affiche_parfait(k) qui affiche tous les nombres
# parfaits plus petits que 2^k.
#-----------------------------------------------------------------------------
from tqdm import tqdm

def som_div_propres(n: int) -> int:
    """Retourne la somme des diviseurs propres de n."""
    s = 0
    for div in range(1,n):
        if n % div == 0:
            s += div
    return s

def est_parfait(n: int) -> bool:
    """Reourne True si n est parfait et Fale sinon."""
    return n == som_div_propres(n)

def affiche_parfait(k: int):
    """ Affiche tous """
    for i in tqdm(range(2**k)):
        if est_parfait(i):
            print(f"\n {i} est parfait.")
            
affiche_parfait(10)





#-----------------------------------------------------------------------------
# Exercice 2 : les nombres presque parfaits
#
# Un nombre n est presque-parfait si la somme de ses diviseurs propres est
# égale à n - 1.
# (1) Ecrire une fonction est_presque_parfait(n) qui retourne le booléeen True
# si le nombre n est presque-parfait.
# (2) Ecrire une procédure affiche_presque_parfait(k) qui affiche tous les
# nombres presque-parfaits plus petits que 2^k.            
#-----------------------------------------------------------------------------


def est_presque_parfait(n: int) -> bool:
    """ retourne True si le nombre n est presque parfait """
    return (n - 1) == som_div_propres(n)

def affiche_presque_parfait(k: int):
    """ Affiche tous """
    for i in tqdm(range(2**k)):
        if est_presque_parfait(i):
            print(f"\n {i} est presque parfait.")
            
affiche_presque_parfait(10)

#-----------------------------------------------------------------------------
# Exercice 3 : les nombres amicaux
#
# Deux nombres n et m sont dits amicaux s'ils sont égaux à la somme des
# diviseurs propres de l'autre.
# Par exemple, les nombres 220 et 284 sont amicaux, la somme des diviseurs
# propres de 220 est 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284 et
# la somme des diviseurs propres de 284 est 1 + 2 + 4 + 71 + 142 = 220.
# (1) Ecrire une fonction amicaux(n, m) qui retourne le booléen True si les
# nombres n et m sont amicaux.
# (2) Ecrire une procédure affiche_amicaux(k) qui affiche tous les nombres
# amicaux plus petits que 2^k. Notons que pour un n donné, son ami potentiel
# est som_div_propres(n). Pour lister les nombres amicaux, il faut vérifier que
# n et som_div_propres(n) sont amicaux pour chaque n compris entre 1 et 2^k.
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# Tests.
#-----------------------------------------------------------------------------