somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print(f'------ {c}º Pessoa -----')
    nome = str(input('Digites seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [M/F] ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média das idades digitadas foi de {mediaidade}')
print(f'O nome do Homem mais velho é {nomevelho} e sua idade é de {maioridadehomem} anos.')
print(f'{totmulher20} Mulheres tem menos de 20 anos')


