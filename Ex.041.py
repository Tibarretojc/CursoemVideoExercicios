from datetime import date
atual = date.today().year
nascimento = int(input('Digite seu nascimento: '))
idade = atual -nascimento
if idade <= 9:
    print(f'Sua idade é de {idade} anos e você pertence a categoria MIRIM')
elif idade <= 14:
    print(f'Sua idade é de {idade} anos e você pertence a categoria INFANTIL')
elif idade <= 19:
    print(f'Sua idade é de {idade} anos e você pertence a categoria JUNIOR')
elif idade <= 25:
    print(f'Sua idade é de {idade} anos e você pertence a categoria SÊNIOR')
else:
    print(f'Sua idade é de {idade} anos e você pertence a categoria MASTER')


