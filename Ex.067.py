print('='*30)
print('Programa de Tabuada')
print('='*30)
while True:
    num = int(input('Digite aqui o número que você quer ver na tabuada: '))
    print('='*30)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('='*30)
print('Fim do Programa de Tabuada! Volte Sempre')
