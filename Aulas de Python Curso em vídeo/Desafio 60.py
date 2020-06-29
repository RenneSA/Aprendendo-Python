'''Faça um programa que leia e mostre o seu FATORIAL
Ex: 5"-5x4x3x2x1 = 120'''

"""""from math import factorial
n = int ( input('Digite um número para calcular o seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))"""


'''n = int(input("Digite um para calcular o seu Fatorial: "))
c = n
f = 1 # fator nulo de multiplicação é 1!!!
print('Calculando {}! '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print('X' if c > 1 else '=', end='')
    f *= c
    c -= 1
print("{}".format(f))'''

# tentetiva com o for . refazer
"""n = int(input("Digite um para calcular o seu Fatorial: "))
fat = 1
mult = 1
for c in range(n, 0, -1):
   fat = fat * i
print(fat)"""

