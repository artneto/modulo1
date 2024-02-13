print('ajude a encontrar o assasino')
print('*'*40)
corCabelo = str(input('Qual a cor do cabelo: ')).lower()
alergico  = str(input('Possui alergia (Y/N): ')).upper()
altura = str(input('Ele e Alto (Y/N): ')).upper()
corcunda = str(input('Possui alguma corcunda (Y/N): ')).upper()
job = str(input('Qual sua profissao: ')).lower()

if corCabelo == 'loiro' and alergico == 'Y' and altura == 'Y' and corcunda == 'Y' and job =='programador':
    print('Ele e o assasino')
else:
    print('Suspeito, porem nao e o assasino')

