#Read 2 integer values (A and B). Afterwards,
#  the program should display a message "Are Multiples" or "Not Multiple", indicating whether the values read are multiples of each other.

A, B = map(int, input().split())

if A % B == 0 or B % A == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')