'''n = int(input("Digite um numero inteiro: "))
mult = 1
result = 0
while mult <= 10:
    result = mult * n
    mult = mult + 1
    print("{} x {} = {}".format(n, mult-1, result))'''

n = int(input("Digite um numero inteiro: "))
mult = 0
while mult <= 9 * n:
    mult = mult + n
    print("{} x {:.0f} = {}".format(n, mult / n, mult))
