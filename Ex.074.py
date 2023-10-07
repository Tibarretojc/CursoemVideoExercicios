from random import randint
lista = (randint(1, 10), randint(1, 10), randint(1, 10),
randint(1, 10), randint(1, 10),)
print('-='*20)
print(f'Os números sorteados foram {lista}')
print('-='*20)
print(f'O maior número sorteado foi {max(lista)}')
print('-='*20)
print(f'O menor número sorteado foi {min(lista)}')
