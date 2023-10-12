print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

listagem = ( 'Lápis' , 1.75,
'caneta', 2.50,
'livro', 50.00,
'lancheira', 15.75,
'giz', 2.15,
'mochila', 25.85,
'caderno', 2.45,
'canetas', 22.30)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)
