#Calculate the average consumption of a car
# by providing the total distance traveled (in km) and the total fuel used (in liters).

# X represent KM
# Y represent total fuel spent, with a digit after the decimal point.

X = int(input())
Y = float(input())

cosumo_total = X / Y

print(f'{cosumo_total:.3f} km/l)