#comdição Se Simples
"""nome = str(input("Qual é o seu nome ? ")).strip()
if nome == "Gustavo":
    print("Que nome Lindo você tem")
else:
    print("Seu nome é tão normal!")
print("Bom dia, {} !".format(nome))"""""

#consição se Compostas
"""n1 = float(input("Digite a primeira nota: "))
n2 = float(input("DIgite a segunda nota: "))
m = (n1 + n2)/2
print("A sua média foi {:.1f}".format(m))
if m >= 6:
    print("Sua Média foi boa! parabéns!!")
else:
    print("Sua média fui ruim! ESTUDE MAIS!!!")"""

#Condição Se simplificada
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("DIgite a segunda nota: "))
m = (n1 + n2)/2
print("A sua média foi {:.1f}".format(m))
print("PARABÉNS!" if m>=6 else "ESTUDE MAIS!")
