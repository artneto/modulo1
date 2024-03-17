#Write a program that reads a vector A[100]. At the end, show all positions in the vector that store a value less than or equal to 10 and the value stored in each of the positions.
#The input contains 100 values, which can be integers, reals, positive or negative.
#For each vector value less than or equal to 10, write "A[i] = x", where i is the position of the vector and x is the value stored at the position, with one place after the decimal point.
A = [0]*100

for i in range(100):
    V = float(input())
    A[i] = V

for i in range(len(A)):
    if A[i] <= 10:
        print(f'A[{i}] = {A[i]:.1f}')