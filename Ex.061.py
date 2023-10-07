print ('Gerador de PA')
print ('-=' * 10)
pt = int(input('Digite aqui o PRIMEIRO TERMO: '))
razao = int(input('Digite aqui a RAZÃO: '))
decimo = pt + (11 - 1) * razao
for c in range(pt, decimo, razao):
    print(f'{c}', end=' -> ')
print('ACABOU')
