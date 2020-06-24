"""import math
num = int(input('Digite um númro: '))
escolha = str(input("Digite 'b' (Binário) 'o' (Octal) ou 'h' (Hexadecimal): "))
bi = bin(num)
oc = oct(num)
he = hex(num)
if escolha == b:
    print('O numero Binário de {} é {}'.format(num, bi))
elif escolha == o:
    print('O número Octal de {} é {}. '.format(num, oc))
elif escolha == h:
    print('O número Hexadecimal de {} é {}'.format(num, he))
else:
    print('Reveja sua digitação!!!')"""

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para a converão
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua Opção é: '))
if opcao == 1:
    print("{} convertido para BINÁRIO é igual a {} ".format(num, bin(num)[2:])) #entre chaves inicia depois de 2 numeros do inicio.
elif opcao == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Você não digitou uma opçaõ de 1 a 3. Tente novomente com mais atenção')



