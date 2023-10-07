from random import randint


vitoria = 0
while True:
    jogador = int(input('Digite seu número: '))
    comp = randint(0, 10)
    vencedor = jogador + comp
    tipo = ' '
    while tipo not in 'IP':
        tipo = str(input('Digite se você quer Par [P] ou [I]? ')).upper().split() [0]
    print(f'Você Jogou {jogador} e o computador {comp}. Total de {vencedor}')
    print('Deu Par' if vencedor % 2 == 0 else 'Deu Ímpar')
    if tipo == 'P':
        if vencedor % 2 == 0:
            print('Você Ganhou')
            vitoria += 1
        else:
            print('Você Perdeu')
            break
    elif tipo == 'I':
        if vencedor % 2 == 1:
            print('Você Ganhou')
        else:
            print('Você Perdeu')
            break
    print('Vamos jogar novamente?')
print(f'Game Over! Você venceu {vitoria} vezes')
