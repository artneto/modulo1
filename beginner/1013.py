# Ler os três valores como entrada
linhaOne = input()

A, B, C = linhaOne.split()
A = float(A)
B = float(B)
C = float(C)

# Encontrar o maior entre a e b
maior_ab = (A + B + abs(A - B)) // 2

# Encontrar o maior entre o maior de a e b e c
maior = (maior_ab + C + abs(maior_ab - C)) // 2

# Imprimir o resultado
print(maior, "eh o maior")
