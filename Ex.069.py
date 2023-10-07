contIdade = contHomens = contMulheres = 0
while True:
    idade = int(input('Qual sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo? ')).upper().split()[0]
        
    if idade >= 18:
        contIdade += 1
    if sexo == "M":
        contHomens += 1
    if sexo == "F" and idade < 20:
        contMulheres += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if resp == "N":
        break
print(f'{contIdade} pessoas tem mais de 18 anos')
print(f'{contHomens} Homens foram cadastrados')
print(f'{contMulheres} Mulheres tem menos de 20 anos')
