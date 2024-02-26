# Read 5 Integer values. Next, show how many values entered were even, how many values entered were
#  odd, how many values entered were positive and how many values entered were negative.
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

for i in range(num1, num2, num3, num4, num5):
    if i % 2 == 0:

print(f'{i} valor(es) par(es)')
print(f'{2} valor(es) impar(es)')
print(f'{1} valor(es) positivo(s)')
print(f'{3} valor(es) negativo(s)')

