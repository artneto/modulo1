# Create a programme that print from 1 to 1000 counting 2:
for i in range(1,1001,2):
    print(i)

##Cereate a programme that print from 0 to 100 and print barril for every multiple of 3

for i in range(101):
    if i % 3 ==0:
        print('barril', end=" ")
    else:
        print(i, end= " ")

# Check if the number is even or odd: 

player01 = int(input('Type a number: '))

if player01 % 2 == 0:
    print(f'{player01} number is even')
else:
    print(f'{player01} number is odd')