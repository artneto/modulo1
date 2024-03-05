#Read an integer N and calculate all its divisors.

N = int(input())
divisorSoma= 0

for i in range(1, N + 1):
    if N % i == 0:
        print(i)