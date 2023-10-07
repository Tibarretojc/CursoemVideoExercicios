from datetime import date
atual = date.today().year
cont = 0
cont_menor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano {c}º pessoa nasceu? '))
    idade = atual - ano
    if idade >= 21:
        cont += 1
    else:
        cont_menor += 1
print(f'{cont} pessoas são maiores de idade')
print(f'{cont_menor} pessoas ainda não atingiram a maioridade.')



