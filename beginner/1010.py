linhaUm = input()

codigo, peca, valor = linhaUm.split()
peca = int(peca)
valor = float(valor)
valor1 = peca * valor

linhaDois = input()

codigo2, peca2, valor2 = linhaDois.split()
peca2 = int(peca2)
valor2 = float(valor2)
valor2 = peca2 * valor2

valor_total = valor1 + valor2

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')