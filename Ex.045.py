from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura
''')
jogador = int(input('Qual é a sua jogada? '))
print('Jo')
sleep(1)
print('ken')
sleep(1)
print('Po')
sleep(1)
print('-='*10)
print(f'Computador jogou {itens[computador]}')
print(f'Você jogou {itens[jogador]}')
print('-='*10)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Você Venceu')
    elif jogador == 2:
        print('Computador Venceu')
    else:
        print('Jogada Invalida')

elif computador == 1:
    if jogador == 0:
        print('Computador Venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Você Venceu')
    else:
        print('Jogada Invalida')
elif computador == 2:
    if jogador == 0:
        print('Você Venceu')
    elif jogador == 1:
        print('Computador Venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Invalida')



