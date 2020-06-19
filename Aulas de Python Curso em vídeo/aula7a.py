n1 = int(input('Um Valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma eh {}, A muntiplicacao eh {} e a divisao e {:.3f}'.format(s , m, d), end='') #\n que a linha e end='' manter na mesma linha

print('Divisao Inteira {} e Potencia{}'.format(di, e))
