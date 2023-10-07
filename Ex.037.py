from time import sleep

num = int(input('Digite aqui o número para conversão: '))
base = int(input('''Digite:
[1] para BINÁRIO 
[2] para OCTAL 
[3] para HEXADECIMAL.
 '''))
print('Prcessando conversão, aguarde....')
sleep(2)

print(f'O número escolhido foi: {base}')

if base == 1:
    print(f'O valor digitado {num} convertido para número Binário é de {bin(num)[2:]}.')
elif base == 2:
    print(f'O valor digitado {num} convertido para número Octal é de {oct(num)[2:]}.')
elif base == 3:
    print(f'O valor digitado {num} convertido para número Hexadecimal é de {hex(num)[2:]}.')
else:
    print('Você informou um número inválido, tente novamente.')