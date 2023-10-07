total = maisMil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Digite o nome do Produto: '))
    valor = float(input('Digite o valor do Produto: R$ '))
    cont += 1
    total += valor
    if valor >= 1000:
        maisMil += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    resp = ' '
    while resp not in "SN":
        resp = str(input('Você quer comprar mais produtos? [S/N]')).upper().split()[0]
    if resp == 'N':
        break
print(f'O valor total gasto foi de {total:.2f}')
print(f'{maisMil} produto/s acima de R$ 1.000,00')
print(f'O produto mais barato foi {barato} e custa R$ {menor:.3f}')