num = int(input('Digite um número e veja se ele é primo: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}',end=' ')
print(f'\n\033[m0 número {num} foi divisível {cont} vezes')
if cont == 2:
    print(f'E por isso ele é primo')
else:
    print(f'Ee por isso ele não é primo')
