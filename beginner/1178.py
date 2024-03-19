#Read a value X. Place this value in the first position of a vector N[100]. 
# In each subsequent position of N (1 to 99), place half of the value stored 
# in the previous position, as shown in the example below. Print vector N.
#The input contains a double precision value with 4 decimal places.
#For each position of the vector N, write "N[i] = Y", where i is the position of the vector and Y 
# is the value stored at that position. Each vector value must be presented with 4 decimal places.

X = float(input())
N =[0]*100
N[0] = X

for i in range(1, 100):
    N[i] = N[i - 1] / 2

for i in range(100):
    print(f'N[{i}] = {N[i]:.4f}')