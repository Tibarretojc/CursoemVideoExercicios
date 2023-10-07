casa = float(input('Digite aqui o Valor do Imóvel: R$ '))
sal = float(input('Digite aqui o seu salário: R$ '))
anos = int(input('Digite aqui em quantos anos pretende pagar o financiamento?: '))
prestacao = casa / (anos * 12)
minimo = sal * 0.30
print(f'Para pagar a casa no valor de R$ {casa:.2f} em {anos} anos, o valor da prestação será de R$ {prestacao:.2f}')
if prestacao <= minimo:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo Negado!')