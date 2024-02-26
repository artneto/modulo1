# Read 5 Integer values. Next, show how many values entered were even, how many values entered were
#  odd, how many values entered were positive and how many values entered were negative.
numeros=[]

pares = 0
impar = 0
positivo = 0
negativo = 0

for i in range(5):
    user_collection = int(input())
    numeros.append(user_collection)
    if user_collection % 2 == 0:
        pares += 1

    if user_collection % 2 !=0:
        impar += 1
    
    if user_collection > 0:
        positivo += 1

    elif user_collection < 0:
        negativo += 1

print(f'{pares} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
    
                

