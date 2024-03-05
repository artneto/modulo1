#The following sequence of numbers 0 1 1 2 3 5 8 13 21... is known as the Fibonacci series. In this sequence, each number, after the first 2,
#  is equal to the sum of the previous 2. Write an algorithm that reads an integer N (N < 46) and outputs the first N numbers in that series.
N = int(input())
a = 0
b = 1

for i in range(N):
    print(a, end= " ")
    a, b = b, a + b
