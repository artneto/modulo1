#Write a program that reads an integer value N. This N is the number of lines of output that will be presented when executing the program.
N = int(input())

inicial = 1

for i in range(1, N * 4 + 1, 4):
    print(f'{i} {i + 1} {i + 2} PUM')

