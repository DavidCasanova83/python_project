# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 09:46:31 2022

@author: greta
"""

def estPremier(n):
    i = 2
    result = None
    while i < n and n % i != 0:
        i = i + 1
    if i == n:
        result = True
    else:
        result = False
    return result

def affichePremier (n_max:int):
    for i in range(n_max+1):
        if estPremier(i):
            print (i)
            
affichePremier(10)