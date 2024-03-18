#Write a program that reads a value T and fills a vector N[1000] 
# with the sequence of values from 0 to T-1 repeatedly, as per the example below. Print vector N.
# The input contains an integer value T (2 ≤ T ≤ 50).
# For each position of the vector, write "N[i] = x", where i is the position of the vector and x is the value stored at that position.

T = int(input())

N = []

for i in range(1000):
    N.append(i % T)

for i in range(1000):
    print(f"N[{i}] = {N[i]}")