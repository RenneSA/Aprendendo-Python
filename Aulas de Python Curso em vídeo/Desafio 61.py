'''REfaça o desadio 51, lendo o termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while'''

print('Gerador de PA')
print('-='*20)
primeiro = int( input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <=10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('Fim!')
