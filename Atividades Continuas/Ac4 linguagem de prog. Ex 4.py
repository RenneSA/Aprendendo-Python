'''Faça um programa de resolução de tabuada. O programa deve inicialmente receber 2 números que indicam de quais números devem ser impressas a tabuada.
Por exemplo, se forem recebidos os valores 2 e 5, seu programa deve imprimir a tabuada de 2, 3, 4 e 5.
O programa só deve aceitar valores entre 1 e 9. Enquanto o usuário digitar valores que não sejam esses, emita uma mensagem de erro.

'''

n1 = int(input())
while n1 < 1 or n1 > 9:
    print('Insira um número inicial entre 1 e 9')
    n1 = int(input())
n2 = int(input())
while n2 < 1 or n2 > 9:
    print('Insira um número final entre 1 e 9')
    n2 = int(input())
if n1 <= n2:
    for x in range(n1, n2 + 1):
        for c in range(1, 10):
            print(f'{x} x {c} = {x * c}')
        print()
else:
    print('Nenhuma tabuada nesse intervalo')
