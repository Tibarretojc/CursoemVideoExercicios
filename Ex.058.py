from random import randint
from time import sleep
tentativas = 1
com = randint(0,10)
escolha = int(input('Digite aqui o seu chute de 0 a 10: '))
print('PROCESSANDO....')
sleep(2)
while escolha != com:
    if escolha == com:
        print('Você acertou, parabéns')
    elif escolha > 10:
        print('O número digitado deve ser entre 0 e 10, tente novamente!')
    else:
        tentativas +=1
        print('Você errou, tente novamente')
    escolha = int(input('Digite aqui o seu chute de 0 a 10: '))
    print('PROCESSANDO....')
    sleep(2)
print(f'o número certo era {com} e você precisou de {tentativas} tentativas para acertar! ')
