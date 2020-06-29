'''Crie um programa que'leia a udade e o sexo de varias pessoas. Acada pessoa cadastrada, o programa deverá pergutar se o usuário
quer ou não continuar. No final, mostra:
A) QUantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.'''
tot18 = toth = totm20= 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('QUer continuar? [S/N} ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados.')
print(f'E temos {totm20} muçheres com menos de 20 anos')
