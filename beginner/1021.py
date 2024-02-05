valor = float(input())

notasCem = valor // 100
resto = valor % 100
notasCin = resto // 50
resto = resto % 50
notasVin = resto // 20
resto = resto % 20
notasDez = resto // 10
resto = resto % 10
notasCinco = resto // 5
resto = resto % 5
notasDois = resto // 2
resto = resto % 2
#moedas
moedasOne = resto // 1.00
resto = resto % 1.00
moedasCinque = resto // 0.50
resto = resto % 0.50
moedasVint = resto // 0.25
resto = resto % 0.25
moedasDez = resto // 0.10
resto = resto % 0.10
moedasCincoC = resto // 0.05
resto = resto % 0.05
moedasOneCen = resto/ 0.01


print('NOTAS:')
print(f'{notasCem:.0f} nota(s) de R$ 100.00')
print(f'{notasCin:.0f} nota(s) de R$ 50.00')
print(f'{notasVin:.0f} nota(s) de R$ 20.00')
print(f'{notasDez:.0f} nota(s) de R$ 10.00')
print(f'{notasCinco:.0f} nota(s) de R$ 5.00')
print(f'{notasDois:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moedasOne:.0f} moeda(s) de R$ 1.00')
print(f'{moedasCinque:.0f} moeda(s) de R$ 0.50')
print(f'{moedasVint:.0f} moeda(s) de R$ 0.25')
print(f'{moedasDez:.0f} moeda(s) de R$ 0.10')
print(f'{moedasCincoC:.0f} moeda(s) de R$ 0.05')
print(f'{moedasOneCen:.0f} moeda(s) de R$ 0.01')