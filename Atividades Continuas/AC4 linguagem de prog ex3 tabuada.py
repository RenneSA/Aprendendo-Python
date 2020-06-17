'''Faça um programa que leia um número inteiro e imprima a tabuada de multiplicação deste número.
Suponha que o número lido da entrada é maior que zero.'''

n = int(input())
mult = 0
while mult <= 8 * n:
    mult = mult + n
    print("{} X {:.0f} = {}".format(n, mult / n, mult))