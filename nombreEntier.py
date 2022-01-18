nombre = None
pairNumber = 0
impairNumber = 0
resultPair = None


while nombre != 0:
    
    nombre = float(input('Saisir un nombre: '))
    
    if nombre%2 == 0:
        pairNumber = nombre + pairNumber
        
    else:
        impairNumber = nombre + impairNumber
print(f' La somme des nombres pairs est = {pairNumber}')
print(f' La somme des nombres impairs est = {impairNumber}')