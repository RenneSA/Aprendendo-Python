from datetime import date
"""""ano = float(input('Digite o seu ano de nascimento: '))
ali = date.today().year - ano
if ali == 18:
    print('Você precisa se alistar esse ano!!!')
if ali > 18:
    print('Já passou o ano do seu alistamento ele foi em {:.0f}'.format(ano + 18))
else:
    print('Você ainda é muito novo para se alistar! Seu ano de alistamento é {:.0f}'.format(ano + 18))"""
atual = date.today().year
nasc = int(input('Ano do seu nascimento com quatro digitos: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se Alistar IMEDIATEMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos para o Alistamento".format(saldo))
    #ano = saldo + atual
    print("Seu alistamento será em".format(atual + saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu Alistamento foi em {}'.format(ano))

