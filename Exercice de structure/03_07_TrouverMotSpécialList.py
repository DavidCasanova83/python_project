# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:01:14 2022

@author: greta
"""

words = ['Bonjour', 'catwoman', 'catcheur', 'caca', 'catmanduu', 'superman'
         , 'catwoman', 'catwoman', 'batman', 'robin', 'catwoman']

cat_list = [w.upper() for w in words if w.startswith('cat')]

print(cat_list)