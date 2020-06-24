"""sal = float(input("Digite o seu salário atual: "))
if sal > 1250:
    print("Seu aumento é R${:.2f} , seu novo salário é R${:.2f}".format(sal*0.10, sal*0.10+sal))
else:
    print("Seu aumento é R${:.2f} , seu novo salário é R${:.2f}".format(sal*0.15, sal*0.15+sal))"""

salario = float(input("Qual é o salário atual do funcionário? R$ "))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print("Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora".format(salario, novo))