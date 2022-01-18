# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 08:40:10 2022

@author: greta
"""

time_user = input('entrer une heure au format hh:mm --> ')
heure = float(time_user[0:2])
minute = float(time_user[3:])

print(heure)
print(minute)


if heure <= 24 and heure >= 0:              #Controle de la validité de l'heure
    print('Heure valide')
    if minute <= 60 and minute >=0:        #Controle de la validité des minutes
        print('Minute valide')
        if heure > 9:                          #Controle du retard apres 09h
            print('Vous êtes en retard')
        else:
            print('Vous êtes à l heure ')      # à l'heure avant 09h
    else:
        print('Minute invalide')               # Minute invalide
else:
    print('Heure invalide')                    # Heure invalide