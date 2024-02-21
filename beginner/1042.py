#Read 3 integer values and sort them
# in ascending order. At the end, show the values in ascending order, a blank line and then the values in the sequence as they were read.

A, B, C = map(int, input().split())

valoresOriginal = [A, B, C]

if A > C:
    A, C = C, A
if A > B:
    A, B = B, A 
if B > C: 
    B, C = C, B
print(A)
print(B)
print(C)
print()
print(valoresOriginal[0])
print(valoresOriginal[1])
print(valoresOriginal[2])