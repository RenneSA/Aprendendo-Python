"""pri = int(input('Digite o valor do primeiro Elemento: '))
ra = int(input('Digite o valor da Razão: '))
for c in range(pri, 10+1, ra):
    print('Seu elemento é {}, sua razão é {} sua PA é {} '.format(pri, ra, c))"""

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='-> ')
print('Acabou')
