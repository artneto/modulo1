#Read a value to two decimal places, equivalent to a person's
#  salary from Lisarb. Then, calculate and show the amount this
#  person must pay in Income Tax, according to the table below.
# Remember that, if the salary is R$3002.00, the rate that applies 
# is 8% only on R$1000.00, as the salary range from R$0.00 to R$2000.00 
# is exempt from Income Tax. In the example provided (below), the rate is 8%
#  on R$1000.00 + 18% on R$2.00, which results in R$80.36 in total. The value 
# must be printed with two decimal places.

salario = float(input())
imposto = 0

if salario >= 0.00 and salario <= 2000.00:
    print('Isento')
elif salario <= 3000.00:
    imposto = (salario - 2000.00) * 0.08
    print(f'R$ {imposto:.2f}')
elif salario <= 4500.00:
    imposto = (1000.00 * 0.08) + ((salario - 3000.00) * 0.18)
    print(f'R$ {imposto:.2f}')
else:
    imposto = (1000.00 * 0.08) + (1500.00 * 0.18) + ((salario - 4500.00) * 0.28)
    print(f'R$ {imposto:.2f}')

