valores = []
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('-='*30)
print(f'Você digitou os seguintes valores {valores}')
print('-='*30)
print(f'O maior número digitado foi {max(valores)} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor número digitado foi {min(valores)} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()