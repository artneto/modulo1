idade_dias = int(input())

ano = idade_dias // 365
resto = idade_dias %  365
meses = resto // 30
resto = resto % 30
dia = resto

print(f'{ano} ano(s)')
print(f'{meses} mes(es)')
print(f'{dia} dia(s)')