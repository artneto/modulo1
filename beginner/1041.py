#Read 2 values with one decimal place (x and y), which must represent the coordinates of a 
# point on a plane. Next, determine which quadrant the point belongs to, or whether it is on one of the Cartesian axes or at the origin (x = y = 0).

x, y = map(float, input().split())

if x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')
elif x == 0 and y != 0:
    print('Eixo Y')
elif x != 0 and y == 0:
    print('Eixo X')
else:
    print('Origem')