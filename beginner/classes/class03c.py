#Create a guessing game in Python, where the user must guess a random number between 1 and 100.
#  With each mistake, the player must receive a new clue, until they guess the correct value.
#  At the end, report how many attempts it took the player to get it right.
import random
numeroSecreto = random.randint(1,3)

player_01 = int(input())

if player_01 == numeroSecreto:
    print('win')
else:
    if numeroSecreto % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar')
    if numeroSecreto % 3 == 0:
        print('número é divisível por 3')
    else:
        print('número não é divisível por 3')
    if  numeroSecreto >= 50:
        print('O número é maior que 50')
    else:
        print('O número é menor que 50')

print(numeroSecreto)