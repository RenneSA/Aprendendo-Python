'''Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o úsuario digitar o valor 999.
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag). '''
soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')
