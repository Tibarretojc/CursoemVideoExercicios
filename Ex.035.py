r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da tereceira reta: '))
if r1 < r2 + r3 and r2 <r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triangulo com essas retas.')
else:
    print('Não é possível formar um triangulo com essas retas.')