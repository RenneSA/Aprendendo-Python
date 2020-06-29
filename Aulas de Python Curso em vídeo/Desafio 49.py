'''n = int(input('Digite o multiplicador: '))
for c in range(0,10+1,1):
    print('{} x {} = {} '.format(n,c,c*n))'''

num = int(input('Digite um número para saber a sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
