file = open('input.txt').readlines()

rows = []
for line in file:
    line = line.rstrip('\n')
    rows.append([i for i in line])

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
ex1 = 0
trees_ex2 = []
for i, slope in enumerate(slopes):
    x, y = -slope[0], -slope[1]
    trees_ex2.append(0)
    while True:
        x += slope[0]
        # less hardcoded as suggested by Reddit user u/Chrinkus
        if x >= len(rows[y]):
            x = x - len(rows[y])
        y += slope[1]
        if y >= len(rows):
            break

        if rows[y][x] == '#':  # suggested by Reddit user u/MiataCory
            if i == 1:
                ex1 += 1
            trees_ex2[i] += 1


print(ex1)

ex2 = trees_ex2[0]
for i in trees_ex2[1:]:
    ex2 *= i

print(ex2)
