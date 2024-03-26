contador = 1

linha = []

matriz = []
for i in range(2):
    linha = []
    for i in range(2):
        linha.append(contador)
        contador+=1
        matriz.append(linha)
print(linha)


