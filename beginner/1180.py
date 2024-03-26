#Write a program that reads a value N. This N will be the size of a vector X[N].
#  Next, read each of the X values, find the smallest element of this vector and its position within the vector, showing this information.
#The first input line contains a single integer N (1 < N < 1000), indicating the number of elements that should be read next for the vector X[N]
#  of integers. The second line contains each of the N values, separated by a space. It is worth remembering that there will be no repeated numbers 
# in any entry.

#Exit
#The first line displays the message “Lowest value:” followed by a space and the smallest value read in the input. 
# The second line displays the message “Position:” followed by a space and the position of the vector in which the
#  lowest read value is found, remembering that the vector starts at position zero.
# Lê o tamanho do vetor
N = int(input())

vetor = input().split()


for i in range(N):
    vetor[i] = int(vetor[i])

menor = vetor[0]

for i in range(1, N):
    if vetor[i] < menor:
        menor = vetor[i]
        posicao = i
     

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')
