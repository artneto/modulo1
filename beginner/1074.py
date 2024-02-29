#Read an integer value N. This value will be the number of values that will be read next.
# For each value read, show a message in English saying whether this read value is even (EVEN)
# odd (ODD), positive (POSITIVE) or negative (NEGATIVE).
# If the value is equal to zero (0), although the correct description is (EVEN NULL), 
# as by definition zero is even, your program should only print NULL.

N = int(input())

for c in range(N):
    valor = int(input(' '))
    if valor == 0:
        print('NULL')
    if valor > 0:
        print('POSITIVE')
        if valor % 2 != 0:
            print('ODD POSITIVE')
    if valor < 0:
        print('NEGATIVE')
        if valor % 2 != 0:
            print('ODD NEGATIVE')
    elif valor % 2 == 0:
        print('EVEN')
    else:
        print('ODD')
