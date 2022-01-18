# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 09:03:22 2022

@author: greta
"""

# Demander à l'utilisateur de saisir un nombre et
# vérifier qu'il s'agit bien d'un nombre. S'il ne 
# s'agit pas d'un nombre, afficher un message d'erreur.

nombre = input('Entrez un nombre entier --> ')
nombre_init = nombre


try:
    int(nombre)
    nombre = True
except ValueError:
    nombre = False
    print('Attention ce n est pas un nombre ')
    
print(f'{nombre_init} est bien un nombre valide')