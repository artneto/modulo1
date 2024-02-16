#create a programme that ask if Zilda finished her task
# if is not finished she will get a scolding msg 

zildaAnswer = input('Zilda, have you finished  your homework (y/n): ').lower()

while zildaAnswer !='y':
    print('Zilda, hurry up or you cant meet your friends')
    zildaAnswer = input('Zilda, have you finished  your homework (y/n): ').lower()
print('Well done Zilda!')