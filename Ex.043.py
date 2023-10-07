
peso = float(input('Digite seu peso (Kg) para o calculo do IMC: '))
altura = float(input('Digite sua altura (m) para o calculo do IMC: '))
imc = peso / (altura**2)
if imc < 18.5:
    print(f'Seu imc é de {imc:.2f} e você está abaixo do peso.')
elif imc < 25:
    print(f'Seu imc é de {imc:.2f} e você está no peso ideal.')
elif imc < 30:
    print(f'Seu imc é de {imc:.2f} e você está no sobrepeso.')
elif imc < 40:
    print(f'Seu imc é de {imc:.2f} e você está na faixa de obesidade.')
else:
    print(f'Seu imc é de {imc:.2f} e você estpá na faixa de obesidade mórbida.')

