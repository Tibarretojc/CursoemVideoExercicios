num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print(f'O primeiro valor [{num1}] é maior que o segundo [{num2}]')
elif num2 > num1:
    print(f'O Segundo valor [{num2}] é maior que o primeiro [{num1}]')
else:
    print(f'Não existe valor menor, os números [{num1}] e [{num2}] são iguais.')

