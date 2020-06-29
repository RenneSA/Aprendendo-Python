'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elemtentos
de uma Sequência de Fibonacci.
ex: 0 - 1 - 1 - 2 - 3 - 5 - 8'''

print('-='*50)
print('Sequencia de Fibonacci')
print('-='*50)
n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
print('~'*100)
print('{} -> {}'.format(t1, t2), end='')
cont = 3 # o contador começa a contar do 3 termo pq o 1 eo 2 o já são variáveis contadas
while cont <= n:
    t3 = t1 + t2
    print (' -> {}'.format(t3), end='')
    t1 = t2 # transição de termos que avança para o proxímo termo
    t2 = t3 # transição de termos que avança para o proxímo termo
    cont += 1 # aumenta um termo no laço
print('-> FIM')
print('~'*100)
