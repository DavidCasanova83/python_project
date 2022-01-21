# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:19:06 2022

@author: greta
"""

# Dictionnaires
#collection d'objet hétérogènes modifiables

#Syntaxe: {cle_1:element_1, cle_2:element_2,}

d = {
     'marty': {'first_name':'Marty', 'last_name':'Mc Fly', 'age':18},
     'doc': {'first_name':'Emmett', 'last_name':'Brown', 'age':50},
     'biff': {'first_name':'Biff', 'last_name':'Tannen', 'age':18},
     }

d['georges'] = {'first_name':'Georges'}

d.get ('marty').values()

d2 = d.copy() #Copy dico


#fusion

d.update(d2)