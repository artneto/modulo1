#You must make a program that presents the sequence as shown in the example below.

for i in range(1, 10, 2):
    for j in range(7, 4, -1):
        print(f"I={i} J={j}")
    if i < 9:
        for j in range(9, 6, -1):
            print(f"I={i} J={j}")
    else:
        print(f"I={i} J=13")
