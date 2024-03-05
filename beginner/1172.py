#Write a program that reads a vector X[10]. Next, replace all null and negative values of vector X by 1. Then show vector X.
#criar uma array com tamanho 10
X =[0] * 10

#Adicionar os numeros no array
for i in range(10):
    numbers = int(input())
    X[i] = numbers

#Ler o array
for i in range(10):
    if X[i] <= 0:
        print(f'X[{i}] = 1')
    else:
        print(f'X[{i}] = {X[i]}')