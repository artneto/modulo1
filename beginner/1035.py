#Read 4 integer values A, B, C and D. Next, if B is greater than C and if D is greater than A, and
# the sum of C and D is greater than the sum of A and B and if C and D, 
# both, are positive and if variable A is par write the message "Values accepted", otherwise write "Values not accepted".

A, B, C, D = map(int, input().split())

if B > C and D > A and (C + D) > (B + A) and C > 0 and D > 0 and A % 2 == 0:
    print('Valores aceitos')
        
else:
    print('Valores nao aceitos')