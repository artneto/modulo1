#Write a program that reads a value and displays the Fibonacci number corresponding 
# to this read value. Remember that the first 2 elements of the Fibonacci series are
#  0 and 1 and each next term is the sum of the 2 before it. All Fibonacci values calculated
#  in this problem must fit into an unsigned 64-bit integer.

n_test = int(input())

fibonacci_num = [0, 1]

for i in range(2, 60):
    fibonacci_num.append(fibonacci_num[i - 1] + fibonacci_num[i - 2])

for _ in range(n_test):
    n = int(input())
    print(f'Fib({n}) = {fibonacci_num[n]}')