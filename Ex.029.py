vel = float(input('Digite a velocidade do veículo: '))
if vel > 80:
    print('Você ultrapassou o limite de velocidade e será multado.')
    valor_multa = (vel - 80) *7
    print(f'Sua multa será de R$ {valor_multa:.2f}')
else:
    print('Você andou dentro da velocidade permitida. Parabéns')