times = ('Botafogo', 'Bragantino', 'Gremio', 'Palmeiras', 'Flamengo', 'Fluminense', 'Atlético-MG',
         'Atletico-Pr', 'Fortaleza', 'São Paulo', 'Cuiaba', 'Cruzeiro', 'Corinthians', 'Internacional', 
         'Santos', 'Goias', 'Vasco da Gama', 'Bahia', 'América- MG', 'Coritiba')
#print(f'Segue a Colocação dos times no brasdileirão {times}')
cont = 1
for t in times:
    print(f'{cont} - {t}')
    cont += 1
print('-='*20)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('-='*20)
print(f'Os 4 últimos times são: {times[-4:]}')
print('-='*20)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('-='*20) 
print(f'O São Paulo está em {times.index("São Paulo")+1}º lugar')


