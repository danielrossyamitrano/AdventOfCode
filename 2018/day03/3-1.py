from os import getcwd
demo = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

fabric = [[0 for i in range(1000)] for j in range(1000)]

puzzle_input = []
with open(getcwd() + '/input.txt', 'r') as file:
    for line in file:
        base = line.rstrip('\n')
        string = base.split(' @ ')[1]
        string = string.replace(': ', ',').replace('x', ',')
        x, y, w, h = [int(i) for i in string.split(',')]
        for X in range(x, x+w):
            for Y in range(y, y+h):
                fabric[X][Y] += 1

square_inches = 0
for row in fabric:
    for square in row:
        if square > 1:
            square_inches += 1

print(square_inches)
