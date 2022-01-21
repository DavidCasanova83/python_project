
cont = True
list_of_words=''

while cont is True:
    s = input('Saisie une chaine de caractere -- > ')
    list_of_words += s + " "
    cont = (s != "")
print(list_of_words)

