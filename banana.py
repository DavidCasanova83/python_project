# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 10:33:03 2022

@author: greta
"""

word = "anna"
size = len(word)

i = 0

condition = None

while i != size:
    if word[i] != word[-i -1]:
        condition = 'Non Pal'
    else:
        condition = 'Pal'
    i = i +1
print(condition)