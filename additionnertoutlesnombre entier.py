n = float(input('entrez une note sur 20  --> '))

if n > 10:
    print(f'Examen réussi ')
    if n <=12:
        print(f'avec mention assez bien ')
    if n <=14:
        print(f'avec mention bien ')
    if n <=16:
        print(f'avec mention Trés bien ')
    if n >=18:
        print(f'avec mention Excellente ')
else:
    print(f'Examen Raté - Pauvre merde!')