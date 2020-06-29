'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''
from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o  segundo valor: '))
opcao = 0
while opcao !=5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa]
    ''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        # soma = n1 + n2
        print('A soma de {} + {} é igual a {}'.format(n1, n2, n1+n2)) # format(n1, n2, soma)
    elif opcao == 2:
        # produto = n1 * n2
        print('A resuldato de {} X {} é {}'.format(n1, n2, n1*n2)) # formart(n1, n2, produto)
    elif opcao == 3:
        if n1 > n2:
             maior = n1
           # print('O Primeiro número {} é maior que o segundo número {}'.format(n1, n2))
        else:
             maior = n2
             print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior) )
            #print('O Segundo número {} é maior que o primeiro {} '.format(n2, n1))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o Primeiro valor: '))
        n2 = int(input('Digite o Segundo valor: '))
    elif opcao == 5:
        print('Finalizando!!!')
    else:
        print('Opação invalida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte Sempre!')