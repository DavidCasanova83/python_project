# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 10:24:21 2022

@author: greta
"""

#Lancés de dé
from random import randrange
import matplotlib.pyplot as plt


N = 10


launches = [0]*6
figure = plt.figure()

legends = ['A', 'B', 'C', 'D', 'E', 'F']

values = [10,20,15,5,35,25]

plt.bar(legends, values, 0.5, color ="b")

plt.show(1)