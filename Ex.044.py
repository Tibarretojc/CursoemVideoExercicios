print(f'{"LOJAS BARRETO":=^40}')
produto = float(input('Digite o valor do produto: R$ '))
pagamento = float(input('''Digite a forma de pagamento:
[1]À Vista dinheiro/cheque
[2]À Vista no cartão
[3]Em 2 vezes no cartão
[4]Em 3 vezes ou mais com acréscimo
Qual a opção?
'''))

if pagamento == 1:
    total = produto - ( produto * 0.10)
    print(f'O valor à vista com desconto é de R$ {total:.2f}')
elif pagamento == 2:
    total = produto - (produto * 0.05)
    print(f'O valor à vista no cartão com desconto é de R$ {total:.2f}')
elif pagamento == 3:
    total = produto
    print(f'O valor parcelado em 2 vezes e sem desconto é de R$ {total:.2f} em 2 parcelas de {total / 2:.2f}')
elif pagamento == 4:
    total = produto + (produto * 0.20)
    parcel = int(input('Em quantas parcelas? '))
    totparcel = total / parcel
    print(f'O valor parcelado em {parcel} vezes com juros em parcelas de R$ {totparcel:.2f} no valor total de R$ {total:.2f}')
else:
    print('Opção Inválida, tente novamente')
