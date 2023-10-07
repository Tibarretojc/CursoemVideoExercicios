print('Gerador de PA')
print('-=' * 10)
pt = int(input('Digite aqui o PRIMEIRO TERMO: '))
razao = int(input('Digite aqui a RAZÃO: '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f' {termo} ->', end=' ')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f' "Progressão finalizada com {total} termos mostrados" ')
