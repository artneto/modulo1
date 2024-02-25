#Read a value to two decimal places, equivalent to a person's
#  salary from Lisarb. Then, calculate and show the amount this
#  person must pay in Income Tax, according to the table below.
# Remember that, if the salary is R$3002.00, the rate that applies 
# is 8% only on R$1000.00, as the salary range from R$0.00 to R$2000.00 
# is exempt from Income Tax. In the example provided (below), the rate is 8%
#  on R$1000.00 + 18% on R$2.00, which results in R$80.36 in total. The value 
# must be printed with two decimal places.

salary = float(input())
percent01 = 0.08
percent02 = 0.18
percent03 = 0.28

if salary >= 0 and salary <= 2000:
    print('Isento')
if salary >= 2001 and salary <= 3000:
    sum = salary - (salary * percent01)
    print(f'R${sum:.2f}')
if salary >= 3001 and salary <= 4499:
    impSal = salary - (percent02 * salary)
    print(f'R${impSal:.2f}')
if salary == 3002:
    imposto = (percent01 * 1000) +(percent02 * 2.00)
    print(f'R${imposto}')
if salary > 4500:
    acima = salary - (percent01 * 1000) +(percent03 * 2.00)
print(f'R${acima}')

