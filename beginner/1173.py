#Read a value and write a program that places the read value in the first position of a vector N[10].
#  In each subsequent position, place twice the value of the previous position. 
# For example, if the read value is 1, the vector values must be 1,2,4,8 and so on.
#  Show the vector next.
#For each vector position, write "N[i] = X", where i is the vector position and X is 
# the value stored at position i. The first number of vector N (N[0]) will receive the value of V.
v = int(input())
N =[0]*10
N[0] = v   

for i in range(1,10):
    N[i] = N[i - 1]* 2
    
for i in range(10):
    print(f'N[{i}] = {N[i]}')