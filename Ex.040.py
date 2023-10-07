nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota_final = (nota1 + nota2)/2
if nota_final < 5.0:
    print(f'Você foi reprovado, sua média final foi de {nota_final}')
elif nota_final < 7.0:
    print(f'Sua média final foi {nota_final} e você está de recuperação')
else:
    print(f'Sua média final foi de {nota_final} e você está aprovado')