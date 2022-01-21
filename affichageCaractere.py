# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 08:33:32 2022

@author: greta
"""

s= input('Rentrez-votre adresse mail---> ')

r = 0
i = 0


while i != len(s):
    if s[i] == 'a':
        r = r + 1
    elif s[i] == 'à':
        r = r + 1
    elif s[i] == 'A':
        r = r + 1
    elif s[i] == 'â':
        r = r + 1
    i = i + 1
print(r)