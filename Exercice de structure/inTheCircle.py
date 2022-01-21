# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:33:10 2022

@author: greta
"""

#Les ensembles !
#collection non ordonnées

import matplotlib.pyplot as plt
from random import randrange

N = 10
x_circle = 50
y_circle = 30
radius = 20

points = [(randrange(0,101), randrange(0,101)) for i in range(N)]
x = [p[0] for p in points]
y = [p[1] for p in points]

plt.title('Exercice final sur les structures de données')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.scatter(x, y, marker="+", color='r')
ax.add_patch(circle)

print(points)

x_in_circle =[]
y_in_circle=[]
for x, y in points:
    dX = x_circle - x
    dY = y_circle - y
    dist = (dX**2 +dY**2) ** 0.5
    if dist <= radius:

