nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))
nota4 = float(input('Digite a quarta nota do aluno: '))
nota = (nota1 + nota2 + nota3 + nota4)/4
print(f'Somando sua média..... média total {nota:.2f}')
if nota >= 6.0:
    print('Parabens, você passou de ano!!!')
elif nota >= 4.0:
    print('Voce terá que fazer uma subistituta!!!')
else:
    print(f'Sua média ficou em {nota} e assim você foi reprovado!!!')

