from random import randint
from time import sleep
escolha = int(input('Digite aqui o seu chute de 0 a 5: '))
com = randint(0,5)
print('PROCESSANDO....')
sleep(2)
if escolha == com:
    print('Você acertou, parabéns')
else:
    print('Você errou, tente novamente')
print(f'o número certo era {com} ')
