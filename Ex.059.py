n1 = int(input('Digite aqui o Primeiro número: '))
n2 = int(input('Digite aqui o Segundo Valor: '))
escolha = int(input('''Qual a operação a ser realizada? 
[1] Somar
[2] Multiplicar
[3] Maior Número
[4] Digitar Novos Números
[5] Sair do Programa
'''))
while escolha != 5:
    if escolha == 1:
        print(n1 + n2)
        break
    elif escolha == 2:
        print(n1 * n2)
        break
    elif escolha == 3:
        if n1 > n2:
            print(f'O Número maior é {n1}')
            break
        else:
            print(f'O número maior é {n2}')
            break
    elif escolha == 4:
        n1 = int(input('Digite aqui o Primeiro número: '))
        n2 = int(input('Digite aqui o Segundo Valor: '))
        escolha = int(input('''Qual a operação a ser realizada? 
        [1] Somar
        [2] Multiplicar
        [3] Maior Número
        [4] Digitar Novos Números
        [5] Sair do Programa
        '''))
print('Fim do Programa')

