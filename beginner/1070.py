#Read an integer value X. Then present the 6 consecutive odd values starting from X,
#  one value per line, including X if applicable.

X = int(input())

for i in range(X, X + 12):
    if i % 2 != 0:
        print(i)
