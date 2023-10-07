dis = float(input('Digite a distancia da Viagem: '))
if dis <= 200:
    valor = dis * 0.50
    print(f'O valor total da viagem será de R$ {valor:.2f}')
else:
    valor = dis * 0.45
    print(f'O valor total da viagem será de R$ {valor:.2f}')

