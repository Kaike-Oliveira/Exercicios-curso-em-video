from time import sleep

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
s = n1 + n2

print('Calculando...')
sleep(1)

print('O resultado da soma entre {} e {} é \033[34m{:.2f}\033[34m!'.format(n1, n2, s))