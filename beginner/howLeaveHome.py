print('Pheno precisar ir no office.\n'
'Porem ele precisar ver o tempo')
print('='*40)
tempo = input('Selecione o clima:\n'
' Chovendo\n'
' Ventando\n'
' Muito Sol\n'
'selecione a opcao: ').strip().lower()


if tempo  == 'Chovendo':
    tipoDeChuva = input('Qual tipo de chuva: Normal/ Granizio: ')
    print(tipoDeChuva)
    if tipoDeChuva == 'Normal':
        print('leve uma jaqueta')
    if tipoDeChuva == 'Granizio':
        print('leve uma jaqueta de couro')
elif tempo == 'Ventando':
       tipoDeVento = input('Qual tipo de chuva: Forte/ Brisa: ')
       print(tipoDeVento)
       if tipoDeVento == 'Forte':
        print('leve uma jaqueta de Couro')
       if tipoDeVento == 'Brisa':
        print('leve uma jaqueta fina')
elif tempo == 'Muito Sol':
        tipoDeSol = input('Qual tipo de sol: Forte/ Frio: ')
        print(tipoDeSol)
        if tipoDeSol == 'Forte':
            print('Passe protetor solar')
        if tipoDeSol == 'Frio':
            print('leve uma jaqueta fina')
else:
    print('Opcao nao encontrada')
