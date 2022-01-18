# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 09:31:14 2022

@author: greta
"""

# Demander à l'utilisateur de saisir l'horaire
time = input('Entrer un horaire sous la forme hh:mm --> ')

# Extraction des heures et des minutes

h = int(time[0:2])
m = int(time[3:5])

# Vérification des heures et des minutes.

h_valid = (h >= 0) and (h <= 23)
m_valid = (m >= 0) and (m <= 59)

if h_valid and m_valid:
    duration = h * 60 + m
    time_dwam = 8 * 60 + 30  # dwam commence à 08:30
    
    if duration < time_dwam:
        print('En avance !')
    elif duration == time_dwam:
        print('A l heure !')
    else:
        print('En retard')
else:
    print('Saisie Incorrecte')