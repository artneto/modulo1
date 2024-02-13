import time
from datetime import datetime

ano_atual = datetime.now().year

cliente01 = int(input('Qual ano foi a abertura de sua conta: '))
valor_deposito = float(input('Qual o valor do seu deposito: '))

sum01 = ano_atual - cliente01

if sum01 >= 5 or valor_deposito >= 5000:
    print('processando')
    time.sleep(0.5)
    print('Aprovado')
else:
    print('Negado, voce ainda nao cumpriu os requirements')