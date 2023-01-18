from time import sleep

valor = input('Digite algo: ')

print('Processando...')
sleep(1)

print('Esse valor é um(a) {}'.format(type(valor)))
print('É composto só de espaços? {}'.format(valor.isspace()))
print('É número? {}'.format(valor.isnumeric()))
print('É composto apenas de letras? {}'.format(valor.isalpha()))
print('É alfanumérico? {}'.format(valor.isalnum()))
print('Está em maiúsculas? {}'.format(valor.isupper()))
print('Está em minúsculas? {}'.format(valor.islower()))
print('Está capitalizada? {}'.format(valor.istitle()))