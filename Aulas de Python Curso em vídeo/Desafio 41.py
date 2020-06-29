from datetime import date
"""atleta = int(input("Digite a sua idade: "))

if atleta > 20:
    print("Categoria: MASTER")
elif atleta < 9:
    print("Categoria : MIRIM")
elif atleta < 14:
    print("Categoria: INFANTIL")
elif atleta <= 19:
    print("Categoria: JUNIOR")
elif atleta <= 20:
    print("Categoria: SENIOR")"""

ano = int(input('Coloque seu ano de Nascimento: '))
atual = date.today().year
idade = atual - ano
print('O Atleta tem {} anos'. format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')


