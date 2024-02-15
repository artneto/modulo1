import random
#Pedra perde para papel
#papel perde para tesoura
#tesoura perde para a pedra
userChoice = input('Choose between\n'
' Paper, rock, scissor: ')

usedObject = ['rock', 'Paper', 'scissor']
computadorChoice = random.choice(usedObject)

print(f'{usedObject} choice and {computadorChoice} choice')

if userChoice == computadorChoice:
    print(f'Player choice {userChoice} and computer choise is {computadorChoice}, this is a tie')
elif userChoice == 'Paper':
    if computadorChoice == 'rock':
        print(f'Paper wins!')
elif userChoice == 'rock':
    if computadorChoice == 'scissor':
        print(f'rock wins!')
elif userChoice == 'scissor':
    if computadorChoice == 'paper':
        print(f'scissor wins!')
else:
    print('option not found, try again')