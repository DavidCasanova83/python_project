x = float(input('entrer un nombre  '))
y = 0

while x <= 100:
    x = x + 1
    y = x + y
    print(f'total = {y}')



x = float(input('entrer un nombre entier'))
y = 1

while y != 0:
    y = ((y-1) + x)
    print(f'total = {y}')
    x = float(input('entrer un nouvel entier'))