# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 10:11:13 2022

@author: greta
"""
#Entrer le nombre 1



condition ='y'


while condition == 'y':
    a = float(input('Entrer le nombre entier a -- > '))

    op = input('Entrer l opérateur à utiliser ')

    b = float(input('Entrer le nombre entier b --> '))
    if op == "+":
        print('opérateur valide\n')
        result = a + b
    elif op == "-":
        print('opérateur valide\n')
        result = a - b
    elif op == "x":
        print('opérateur valide \n')
        result = a * b
    elif op =="/":
        print('opérateur valide\n')
        result = a / b
    else:
        print('opérateur invalide\n')
    
    print(f'Votre résultat est {result}')
    
    condition = input("Voulez-vous continuer (y/n) ? ")