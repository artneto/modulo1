#Create a program that receives the ten names that were drawn in the
#lady bingo. Knowing that bingo had ten prizes, inform
#Ms. Sueli, what was the first time she was drawn and how many times was her name
#he appeared. Considering that the ladies named Eneide and Nair were not there to
#receive the prize, the program also informs how many more draws should be
#made to complete the ten prizes.
nomes = input() .split(' ')

primeiro_sorteada = nomes.index('sueli') + 1
contar_sueli = nomes.count('sueli')


if 'eneide' in nomes:
    nomes.remove('eneide')
if 'nair' in nomes:
    nomes.remove('nair')
sorteios_restant = 10 - len(nomes)


print(nomes)
print(primeiro_sorteada)
print(contar_sueli)
print(sorteios_restant)