#from math import hypot
#co = float(input('Digite aqui o comprimento do Cateto Oposto: '))
#ca = float(input('Digite aqui o comprimento do Cateto Adjscente: '))
#print(f'O Comprimento da Hipotenusa é: {hypot(co, ca):.2f}')

#O programa acima utiliza-se de módulo, o abaixo de uma formula matematica

co = float(input('Digite o Comprimento do Cateto Oposto: '))
ca = float(input('Digite o Comprimento do Cateto Adjascente: '))
hi = (co**2 + ca**2)**(1/2)
print(f'A hipotenusa vai medir {hi:.2f}')
