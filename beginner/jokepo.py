import random

#Pedra perde para papel
#papel perde para tesoura
#tesoura perde para a pedra

while True:
    userChoice = str(input('Choose between\n'
    'Paper, rock, scissor: ')).lower()

    usedObject = ['rock', 'Paper', 'scissor']
    computadorChoice = random.choice(usedObject)

    print(f'Player choice: {userChoice} and computer choice: {computadorChoice}')

    if userChoice == computadorChoice:
            print(f'Player choice {userChoice} and computer choise is {computadorChoice}, this is a tie')
    elif userChoice == 'Paper':
        if computadorChoice == 'rock':
            print(f'Paper wins!')
        else:
            print('Scissor wins')
    elif userChoice == 'rock':
        if computadorChoice == 'scissor':
            print(f'rock wins!')
        else:
            print('Paper wins')
    elif userChoice == 'scissor':
        if computadorChoice == 'paper':
            print(f'scissor wins!')
        else:
            print('rock wins!')
    else:
        print('option not found, try again')

    play_again = str(input('Dou you want play again (Y/N): ')).lower()
    if play_again != 'Y':
        break