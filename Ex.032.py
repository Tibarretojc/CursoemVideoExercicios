from datetime import date
ano = int(input('digite o ano para saber se ele é bissexto: '))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano foi bissexto')
else:
    print('Esse ano não foi bissexto')
