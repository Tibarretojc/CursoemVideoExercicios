numero = (int(input('Digite aqui um número: ')),
int(input('Digite aqui um número: ')),
int(input('Digite aqui um número: ')),
int(input('Digite aqui um número: ')),
int(input('Digite aqui um número: ')))
print(f'Você digitou os números {numero}')
print(f'O número 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O número 3 apareceu na {numero.index(3)+1}º posição')
else:
    print('Valor 3 não encontrado nesta busca')
print('Os valores pares digitados foram ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')
    else:
        print('não foram 5encontrados')
        break
