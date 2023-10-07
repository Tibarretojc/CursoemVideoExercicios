numero = int(input('Digite um número de 0 à 9999: '))
uni = numero // 1 % 10
dez = numero //10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
print(f'Unidade: {uni}')
print(f'Dezena: {dez}')
print(f'Centena: {cen}')
print(f'Milhar: {mil}')


