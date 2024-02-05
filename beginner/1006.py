A = float(input())
B = float(input())
C = float(input())

aWeight = 2
bWeight = 3
cWeight = 5
MEDIA = (A * aWeight + B * bWeight + C * cWeight)/(aWeight + bWeight + cWeight)

print("MEDIA = {:.1f}".format(MEDIA))