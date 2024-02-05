
NOME = str(input())
salary_monthly = float(input())
amount_sold = float(input())

TOTAL = (amount_sold * 0.15) + salary_monthly

print(f'TOTAL = R$ {TOTAL:.2f}')