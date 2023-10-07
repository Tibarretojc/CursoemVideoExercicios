cont = soma = maior = menor = 0
resposta = ''
while resposta != "N":
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
total = soma / cont
print(f'Você digitou {cont} e média entre os números é de {total:.2f}')
print(f'O maior valor lido foi {maior} e o menor {menor}')
