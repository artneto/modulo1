#Read 1 integer value N (2 < N < 1000). Next, show the N multiplication table.

N = int(input())
for i in range(1,11):
    print(f'{i} x {N} = {i * N}')

