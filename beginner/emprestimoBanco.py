import time
cliente01 = int(input('Quando foi a abertura de sua conta em anos: '))
valor_deposito = float(input('Qual o valor do seu deposito: '))

sum01 = 2024 - cliente01

if sum01 >= 5 or valor_deposito >= 5000:
    print('processando')
    time.sleep(1)
    print('Aprovado')
else:
    print('Negado, voce ainda nao cumpriu os requirements')