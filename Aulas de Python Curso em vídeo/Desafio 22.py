nome = str(input("Digite seu nome completo: ")).strip()

print("Nome em letras Maiusculas", nome.upper())
print("Nome em letras Minusculas", nome.lower())
print("Seu nome tem ao todo {}:".format(len(nome) - nome.count(' ')))
print("Seu primeiro nome tem {} letras.".format(nome.find(' '))) #modo 1
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras.".format(separa[0], len(separa[0]))) #modo2

