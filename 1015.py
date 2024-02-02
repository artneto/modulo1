import math

linhaOne = input()
x1, y1 = linhaOne.split()
x1 = float(x1)
y1 = float(y1)

linhaTwo = input()
x2, y2 =linhaTwo.split()
x2 = float(x2)
y2 = float(y2)

Distancia = ((x2 - x1)**2) + ((y2 - y1)**2)
resultado = math.sqrt(Distancia)

print(f'{resultado:.4f}')