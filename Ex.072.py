cont = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        print(f'Você digitou o número {cont[num]}')
        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Você quer digitar mais algum número? [S/N]')).upper().split()[0]
        if resposta == 'N':
            break
    else:
        print('tente novamente')
print('Fim do programa')
        
    

        

    

    
    

    
     
