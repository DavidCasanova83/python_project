# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 08:50:49 2022

@author: greta
"""


def table_mult(t:int) -> str:
    
    """ Retourne la table de t sous la forme d'une chaine de caracteres."""
    result = ""
    n = 1
    for i in range (1, 11):
        result += f"{t} * {i} = {t*i}\n"
    return result
        
t2 = table_mult(2)
t9 = table_mult(9)


print(t2)