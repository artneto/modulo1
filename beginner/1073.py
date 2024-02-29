#Read an integer value N. Present the square of each 
#of the even values, from 1 to N, including N, if applicable.
#The input contains an integer value N (5 < N < 2000).

N = int(input())

for i in range(1, N +1):
    if i % 2 == 0:
        square = i * i
        print(f'{i}^2 = {square}')
  