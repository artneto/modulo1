#Read an integer that represents a long-distance area code.
# Then, inform which city the area code belongs to, considering the table below:
DDD = (61 , 71, 11, 21, 32, 19, 27, 31)
Destination = ('Brasilia', 'Salvador', 'SP', 'RJ', 'Juiz de fora', 'Campinas', 'Vitoria', 'BH')


numero = int(input())

if numero in DDD:
    index = DDD.index(numero)
    cidade = Destination[index]
    print(cidade)
else:
    print('DDD nao cadastrado')

