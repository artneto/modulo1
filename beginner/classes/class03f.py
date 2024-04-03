valores_01 = [2, 8, 10, 11, 42]

dobro = 2
triplo = 3
quadrado = 4
metade = 2

novoDobro = [elemento * dobro for elemento in valores_01]
print(novoDobro)

novoTriplo = [elemento * triplo for elemento in valores_01]
print(novoTriplo)

novoQuadrado = [elemento * quadrado for elemento in valores_01]
print(novoQuadrado)

novoMetade = [ i // metade for i in valores_01]
print(novoMetade)
