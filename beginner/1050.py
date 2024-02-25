#Read an integer that represents a long-distance area code.
# Then, inform which city the area code belongs to, considering the table below:
ddd_city = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'
}

numero = int(input())

if numero in ddd_city:
   print(ddd_city[numero])
else:
    print('DDD nao cadastrado')

