# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 09:56:02 2022

@author: greta
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 08:33:32 2022

@author: greta
"""

s = input('Rentrez-votre adresse mail---> ')
new_s = ''

i = 0

while i != len(s):
    if s[i] == 'a':
        new_s = new_s +  '1'
    elif s[i] == 'b':
        new_s = new_s + '2'
    elif s[i] == 'c':
        new_s = new_s + '3'
    else:
        new_s += s[i]
    i = i + 1
    
print(new_s)


