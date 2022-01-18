# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 10:11:13 2022

@author: greta
"""
#Entrer le nombre 1

a = float(input('Entrer le nombre entier a -- > '))

#Choisir l'opérateur

op = input('Entrer l opérateur à utiliser ')
#Choisir le nombre 2

b = float(input('Entrer le nombre entier b --> '))



if op == "+":
    print('opérateur valide\n')
    result = a + b
    print(f'Votre résultat est {result}')
elif op == "-":
    print('opérateur valide\n')
    result = a - b
    print(f'Votre résultat est {result}')
elif op == "x":
    print('opérateur valide \n')
    result = a * b
    print(f'Votre résultat est {result}')
elif op =="/":
    print('opérateur valide\n')
    result = a / b
    print(f'Votre résultat est {result}')
else:
    print('opérateur invalide\n')

print(f'Votre résultat est {result}')