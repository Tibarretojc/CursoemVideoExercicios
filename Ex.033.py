a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro número: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O menor valor digitado foi {menor} e o maior foi {maior}')