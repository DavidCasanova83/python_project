# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:59:33 2022

@author: greta
"""

ma_liste = [1014, 4743, 4525, 3653, 4989, 1211, 2331, 4310, 3302, 2150, 2856, 1835,
     2624, 2850, 4491, 3, 3328, 3990, 2721, 6000]



i = 0

number_max = 0

max1_value = max2_value = ma_liste[0]


for n in ma_liste[1:]:
    if n > max1_value:
        max2_value = max1_value
        max1_value = n
    elif n > max2_value:
        max2_value = n
        
    i = i + 1




print(f'le nombre max est --->  {max1_value}')
print(f'le nombre max est --->  {max2_value}')