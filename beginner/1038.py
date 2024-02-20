#Based on the table below, write a program 
# that reads the code of an item and the quantity of this item. Next, calculate and show the amount of the bill payable.
# Definição da tabela de itens
menu = {
    1: {'especificacao': 'cachorro quente', 'preco': 4.00},
    2: {'especificacao': 'X-salada', 'preco': 4.50},
    3: {'especificacao': 'X-bacon', 'preco': 5.00},
    4: {'especificacao': 'torrada simples', 'preco': 2.00},
    5: {'especificacao': 'refrigerante', 'preco': 1.00}
}

# Entrada dos valores do código do item e quantidade
codigo, quantidade = map(int, input().split())

# Verificação se o código está presente na tabela de itens
if codigo in menu:
    # Cálculo do total a pagar
    total_pagar = menu[codigo]['preco'] * quantidade
    print(f'Total: R$ {total_pagar:.2f}')
else:
    print('Código de item inválido')
