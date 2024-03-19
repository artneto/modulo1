#In this problem you must read 15 values and place them in 2 vectors depending on whether these values are even or odd. 
# But the size of each of the two vectors is 5 positions. Then, each time one of the two vectors fills, you must print
# the entire vector and use it again for the next numbers that are read. Once reading is complete, the content remaining
# in each of the two vectors must be printed, first printing the values of the odd vector. Each vector can be filled in as many times as necessary.

par = []
impar = []

for _ in range(15):
    element = int(input())
    if element % 2 == 0:
        if len(par) < 5:
            par.append(element)
        else:
            for i in range(5):
                print(f'par[{i}] = {par[i]}')
            par.clear()
            par.append(element)
    else:
        if len(impar) < 5:
            impar.append(element)
        else:
            for i in range(5):
                print(f'impar[{i}] = {impar[i]}')
            impar.clear()
            impar.append(element)

for i in range(len(par)):
    print(f'par[{i}] = {par[i]}')

for i in range(len(impar)):
    print(f'impar[{i}] = {impar[i]}')


#com funcao .clear uso sempre que preciso reiniciar os vetores par e impar sempre que um deles atingir o tamanho máximo. 