r1 = float(input('Digite aqui o tamanho da primeira reta: '))
r2 = float(input('Digite aqui o tamanho da segunda reta: '))
r3 = float(input('Digite aqui o tamanho da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'É possivel formar um triangulo')
    if r1 == r2 == r3:
        print(f'Esta sequencia de retas formaram um Trinagulo Equilátero')
    elif r1 != r2 != r3 != r1:
        print(f'Este Triangulo tem lados diferentes e formará um Escaleno')
    else:
        print(f'Este Triangulo tem todos os lados diferentes e formará um Isóceles')
else:
    print('Estas retas não podem formar um triangulo')