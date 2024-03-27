#Make a program that reads five notes, returns the contestant's final score
#and which notes were discarded. Test your output and check if it is the same as
#example below, with the same number of decimal places.

Notas = input() .split(' ')

for i in range(5):
    Notas[i] = float(Notas[i])

maior = max(Notas)
menor = min(Notas)

somaFinal = (sum(Notas) - maior - menor)/3

print(somaFinal)
print(maior)
print(menor)