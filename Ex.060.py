# from math import factorial
# num = int(input('Digite um valor e veja o seu fatorial: '))
# f = factorial(num)
# print(f'O fatorial de {num}! é {f}')

num = int(input('Digite um valor e veja seu fatorial: '))
c = num
f = 1
print(f'Calculando o fatorial {num}!')
while c > 0:
    print(f' {c} ', end='')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f)
