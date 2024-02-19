#create a program that reads any value and displays a message saying in which of the following ranges ([0,25], (25,50], (50,75], (75,100])
#  this value is found. Obviously if the value is not in any of these ranges, the message “Out of range” must be printed.
# The symbol ( represents "greater than". For example:
# [0.25] indicates values between 0 and 25,0000, inclusive.
# (25.50] indicates values greater than 25 Ex: 25.00001 up to the value 50.0000000
valor = float(input('Type any number: '))

if 0 <= valor <= 25:
    print('Intervalo [0,25]')
elif 25 < valor <= 50:
    print('Intervalo (25,50]')
elif 50 < valor <= 75:
    print('Intervalo (50,75]')
elif 75 < valor <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')