from math import floor, ceil
from os import getcwd, path

high = []
result_ex1 = 0
seats = []

with open(path.join(getcwd(), '05', 'input.txt'), 'rt') as file:
    for line in file.readlines():
        sample = line.rstrip('\n')

        mi, ma = 0, 127
        row = 0
        for char in sample[0:7]:
            if char == 'F':
                ma = floor((ma-mi)/2+mi)
            elif char == 'B':
                mi = ceil(ma/2)+ceil(mi/2)

            row = mi if char == 'F' else ma if char == 'B' else 0

        mi, ma = 0, 7
        column = 0
        for char in sample[-3:]:
            if char == 'L':
                ma = floor((ma - mi) / 2 + mi)
            elif char == 'R':
                mi = ceil(ma / 2) + ceil(mi / 2)

            column = mi if char == 'L' else ma if char == 'R' else 0

        seat_id = row*8+column
        seats.append(seat_id)
        high.append(seat_id)
        result_ex1 = max(high)


print('result ex1:', result_ex1)

result_ex2 = 0
seats.sort()
asientos = []
for row in range(128):
    for column in range(8):
        asientos.append(row*8+column)

asientos.sort()

for silla in asientos:
    x = silla % 8
    y = silla // 128
    if silla not in seats and y not in (0, 7):
        result_ex2 = silla
        break

print('result ex2:', result_ex2)
