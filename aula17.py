#valores = []
#valores.append(1)
#valores.append(5)
#valores.append(9)
#valores.append(15)
#for cont in range(0, 5):
#    valores.append(int(input('Digite aqui seus valores: ')))

#for c,v in enumerate(valores):
#    print(f'Na posição {c} encontrei os valores {v}.....')
#print('Cheugei ao final da  lista')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'A lista A: {a}')
print(f'A Lista B: {b}')