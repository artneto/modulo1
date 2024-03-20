#In this problem you must read 15 values and place them in 2 vectors depending on whether these values are even or odd. 
# But the size of each of the two vectors is 5 positions. Then, each time one of the two vectors fills, you must print
# the entire vector and use it again for the next numbers that are read. Once reading is complete, the content remaining
# in each of the two vectors must be printed, first printing the values of the odd vector. Each vector can be filled in as many times as necessary.
def imprimir_par(par):
    for i in range(len(par)):
        print(f'par[{i}] = {par[i]}')

def imprimir_impar(impar):
    for i in range(len(impar)):
        print(f'impar[{i}] = {impar[i]}')

par = []
impar = []

for i in range(15):
    num = int(input())
    if num % 2 == 0:
        par.append(num)
        if len(par) == 5:# Se o vetor par encheu, imprime e reinicia
            imprimir_par(par)
            par = []
    else:
        impar.append(num)
        if len(impar) == 5: # Se o vetor par encheu, imprime e reinicia
            imprimir_impar(impar)
            impar = []


imprimir_par(par)
imprimir_impar(impar)