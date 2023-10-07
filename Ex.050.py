soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite aqui um valor para soma-lo: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números pares e a soma total desses pares é de {soma}')