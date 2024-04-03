notas = [9.8, 7, 5.5, 8.9, 6.6, 2.9]
notasNovas = []

for i in notas:
    i = float(i)  #converter
    if i >= 7:  
        notasNovas.append(i)  #add to the list

print(f'Notas que serão mostradas: {notasNovas}')

notaAcrescimo = 0.2
lista_somada = [elemento + notaAcrescimo for elemento in notas]
print(lista_somada)

for elemento in lista_somada:
    if elemento >= 7:
        print('O pai não vai mais castigá-la')
    else:
        print('O pai vai castigá-la')
