# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 13:31:13 2022

@author: greta
"""



condition ='y'

while condition == 'y':
    nb = 1
    result = None
    table = int(input('choisir la table de multiplication  --> '))
    again = 'n'
    while nb != 11:
        result = table*nb
        print(f'{nb} x {table} = {result} ')
        nb  += 1
    condition = input('Voulez-vous une autre table ? (y/n) ')
    print(f'Merci à bientôt')