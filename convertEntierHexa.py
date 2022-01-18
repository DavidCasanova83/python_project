n_init = n = int(input('Entrez un nombre entier --> '))

string_convert = '0123456789ABCDEF' # petite table ascii maison
base = int(input('Entrez une base (comprise entre 2 et 16) --> ')) # choix de la base de convertion

n_target = '' # sauvegarde du caractere ascii dans une string 

while n != 0:
    digit = n % base
    n_target = string_convert[digit] + n_target
    n = n//base
print(f'{n_target}') # afficher la valeur de la string