# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 13:57:51 2022

@author: greta
"""

# Résoudre le probleme des tours de hanoi 
def hanoi(n , A, B, C):
    if n==1:
        print("Disk 1 from",A,"to",B)
        return 
    hanoi(n-1, A, C, B)
    print("Disk",n,"from",A,"to",B)
    hanoi(n-1, C, B, A)
    
hanoi(15,'A','B','C')