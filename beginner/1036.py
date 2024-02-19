# Read 3 floating point values and calculate the roots of the Bhaskara equation. If it is not possible to calculate the roots, display 
# the corresponding message “Unable to calculate”, if there is a division by 0 or a negative root.

A = float(input('first number: '))
B = float(input('Second number: '))
C = float(input('Third number: '))

calculo = (B ** 2) - 4 * A * C

if A == 0:
    print('Impossivel calcular')
elif calculo < 0:
    print('Impossivel calcular')
else: 
    R1 = (-B + calculo ** (1 / 2)) / (2 * A)
    R2 = (-B - calculo ** (1 / 2)) / (2 * A)
print(f'R1 = {R1:.5f} R2 = {R2:.5f}')
