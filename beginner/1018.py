# operador modulo %
#Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias
n = int(input())

# num dividido por inteiro por 100
notasDecem = n // 100
# o resto vai ser numero divido por 100
resto = n % 100

notasDeciquenta = resto // 50
resto = resto % 50

notasDevinte = resto // 20
resto = resto % 20

notasDedez = resto // 10
resto = resto % 10

notasDecinco = resto // 5
resto = resto % 5

notasDedois = resto // 2
resto = resto % 2

notasDeum = resto




print(n)
print(f'{notasDecem} nota(s) de R$ 100,00')
print(f'{notasDeciquenta} nota(s) de R$ 50,00')
print(f'{notasDevinte} nota(s) de R$ 20,00')
print(f'{notasDedez} nota(s) de R$ 10,00')
print(f'{notasDecinco} nota(s) de R$ 5,00')
print(f'{notasDedois} nota(s) de R$ 2,00')
print(f'{notasDeum} nota(s) de R$ 1,00')

