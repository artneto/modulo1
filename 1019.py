N = int(input())

#Divida o número total de segundos pelo 
#número de segundos em uma hora (3600) para obter o número de horas.

horas = N // 3600
resto = N % 3600
minutos = resto //60
resto = minutos % 60
segundos = resto // 60
rest_segundos = segundos % 60
second = rest_segundos


print(f'{horas}:{minutos}:{resto}')