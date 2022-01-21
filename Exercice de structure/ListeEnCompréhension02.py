# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 13:13:17 2022

@author: greta
"""

Sentence = ['110', '525', '333']

Int_sentence = [int(n) for n in Sentence if len(n) >= 3]

print(Int_sentence)