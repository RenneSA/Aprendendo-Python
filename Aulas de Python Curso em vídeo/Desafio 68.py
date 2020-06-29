'''Faça um programa que jogue par ou impar com o computador. O jogo sé será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele consquistou no final do jogo.'''
v = 0
from random import randint
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
        print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')


