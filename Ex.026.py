frase = str(input('Digite uma Frase: ')).upper().strip()
print(f'A Letra A aparece {frase.count("A")}')
print(f'A Primeira Letra A apareceu na posição {frase.find("A")+1}')
print(f' A última letra A apareceu na posição {frase.rfind("A")+1}')