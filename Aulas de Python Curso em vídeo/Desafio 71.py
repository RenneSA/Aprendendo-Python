''' Crie um programa que simule o funcionamento de um caixa eletrônico. Ninício, pergunte ao usuáriom qual será o valor sacado
(número Inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('='* 30)
print('{:.^30}'.format(' BANCO RSA '))
print('='* 30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='* 30)
print('Volte sempre ao BANCO RSA! Tenha um bom dia!')

