notas = [9.8, 7, 5.5, 8.9, 6.6, 4.9]
notasNovas = []

for i in notas:
    i = float(i)  #converter
    if i >= 7:  
        notasNovas.append(i)  #add to the list

print(f'Notas que serão mostradas: {notasNovas}')

any()
