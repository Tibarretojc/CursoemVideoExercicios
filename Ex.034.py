salario = float(input('Digite aqui seu salário: R$ '))
if salario > 1250.00:
    aumento = salario * 0.10
    print(f'Seu aumento será de {aumento:.2f} e o novo salário será de R$ {salario + aumento:.2f}')
else:
    aumento = salario * 0.15
    print(f'Seu aumento será de {aumento:.2f} e o novo salário será de: R$ {salario + aumento:.2f}')