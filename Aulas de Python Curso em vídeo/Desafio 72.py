'''Crie um programa que tenha uma tupla totalmente preenchida com uma contegem por extenso, de ZERO até vinte.
Seu programa deve ler pelo teclado (entre 0 e 20) e mostra-lo por extenso.'''


cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
        'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
        'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
        'Quinze', 'Dezesseis', 'Dezessete','Dezoito',
        'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um númeor entre 0 e 20: '))
    if 0<= n <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você Digitou o número {cont[n]}')

