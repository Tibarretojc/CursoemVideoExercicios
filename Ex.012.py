preco = float(input('Digite aqui o valor do produto:R$ '))
desconto = preco*0.05
novo_preco = preco-desconto
print(f'O valor do produto é R$ {preco:.2f} e com desconto de 5% será de R$ {novo_preco:.2f}')
