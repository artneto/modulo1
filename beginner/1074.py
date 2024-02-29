#Read an integer value N. This value will be the number of values that will be read next.
# For each value read, show a message in English saying whether this read value is even (EVEN)
# odd (ODD), positive (POSITIVE) or negative (NEGATIVE).
# If the value is equal to zero (0), although the correct description is (EVEN NULL), 
# as by definition zero is even, your program should only print NULL.
N = int(input())

for _ in range(N):
    valor = int(input())
    if valor == 0:
        print('NULL')
    elif valor % 2 == 0:
        if valor > 0:
            print('EVEN POSITIVE')
        else:
            print('EVEN NEGATIVE')
    else:
        if valor > 0:
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')
