#Based on the table below, write a program 
# that reads the code of an item and the quantity of this item. Next, calculate and show the amount of the bill payable.
menu = [
    {'codigo': 1, 'especificacao': 'cachorro quente', 'preco': 4.00},
    {'codigo': 2, 'especificacao': 'X-salada', 'preco': 4.50},
    {'codigo': 3, 'especificacao': 'X-bacon', 'preco': 5.00},
    {'codigo': 4, 'especificacao': 'torrada simples', 'preco': 2.00},
    {'codigo': 5, 'especificacao': 'refrigerante', 'preco': 1.00}
]

pedido_01 = int(input('Type the code number:  '))
pedidoQty = int(input('Type the quantity: '))

