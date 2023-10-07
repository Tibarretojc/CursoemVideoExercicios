from random import shuffle
nome1 = input('Digite o primeiro aluno: ')
nome2 = input('Digite o segundo aluno: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print(f'A Ordem de apresentação será: {lista}')
