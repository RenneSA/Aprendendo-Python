"""m1 = float(input('Digite a média 1: '))
m2 = float(input('Digite a média 2: '))
m3 = float(input('Digite a média 3: '))
media = (m1 + m2 + m3)/3
if media < 5:
    print("Reprovado!!! sua note {:.1f} é abaixo da média necessária".format(media))
if media > 7:
    print('Aprovado por {:.1f} acima da média'.format(media - 7))
if media <= 6.9 and media >= 5:
    print('Em Recuperação por {:.1f} na média'.format(media - 5))"""

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2 ,media))
if 7> media >= 5:
    print('O aluno está em RECUPERAÇÃO')
elif media < 5:
    print('Aluno está REPROVADO')
elif media >= 7:
    print('Aluno está APROVADO')


