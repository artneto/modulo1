linhaOne = input()

A, B, C = linhaOne.split()
A = float(A)
B = float(B)
C = float(C)
pi = 3.14159

#a) a área do triângulo retângulo que tem A por base e C por altura.
TRIANGULO = (A * C)/2
#b) a área do círculo de raio C. (pi = 3.14159)
CIRCULO = pi*(C**2)
#c) a área do trapézio que tem A e B por bases e C por altura.
TRAPEZIO = (B + A)*C/2
#d) a área do quadrado que tem lado B.
QUADRADO = (B ** 2)
#e) a área do retângulo que tem lados A e B.
RETANGULO = (A * B)

print(f'TRIANGULO: {TRIANGULO:.3f}')
print(f'CIRCULO: {CIRCULO:.3f}')
print(f'TRAPEZIO: {TRAPEZIO:.3f}')
print(f'QUADRADO: {QUADRADO:.3f}')
print(f'RETANGULO: {RETANGULO:.3f}')