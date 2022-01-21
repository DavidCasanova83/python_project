# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:28:09 2022

@author: greta
"""

# Créer un script permettant de trier la liste suivante.
#Attention ne pas utiliser la fonction sort ! 

int_list = [50,20,100,80,10,40,70,30,60,90]

def bubble_sort(li: list) -> list:
    """Permet de trier par ordre croissant """
    size = len(li)
    for i in range(0, size-1):
        for j in range(0,size-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                
bubble_sort(int_list)
print(int_list)