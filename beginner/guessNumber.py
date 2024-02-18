# Create a game to guess the number, while the user doesnt get the right number
#programme keep asking
guessNumber = 3
count = 0
userGuess = int(input('Guess the number: '))

while userGuess != guessNumber:
    print(f'You guessed number {userGuess} try again')
    count += 1
    userGuess = int(input(f' you tried {count} times Please Guess the number again: '))

print('Well done! 3 is the right number')

