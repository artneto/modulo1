cartas01 = list(map(int, input().split()))
num_carta = int(input())
new_list = 0

cartas01.append(num_carta)
cartas01.remove(min(cartas01))
print(sorted(cartas01))
new_list = sum(cartas01)

print(new_list)
        