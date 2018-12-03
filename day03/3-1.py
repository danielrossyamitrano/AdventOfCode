from os import getcwd
from pygame.mask import Mask

demo = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']


class Rect:
    x = 0
    y = 0
    w = 0
    h = 0

    def __init__(self, i, x, y, w, h):
        self.idx = i
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.size = w, h
        self.mask = Mask(self.size)
        self.mask.fill()

    def __repr__(self):
        return '#{} @ {},{}: {}:{}'.format(self.idx, self.x, self.y, self.w, self.h)

    def overlap_area(self, other):
        return self.mask.overlap_area(other.mask, self.get_rel_pos(other))

    def get_rel_pos(self, other):
        x = other.x - self.x
        y = other.y - self.y
        return x, y


fabric = Rect(0, 0, 0, 1000, 1000)

puzzle_input = []
with open(getcwd() + '/input.txt', 'r') as file:
    for line in file:
        base = line.rstrip('\n')
        idx, string = base.split(' @ ')
        idx = int(idx[1:])
        string = string.replace(': ', ',').replace('x', ',')
        args = [int(i) for i in string.split(',')]
        rect = Rect(idx, *args)
        puzzle_input.append(rect)

square_inches = 0
while len(puzzle_input) > 1:
    a = puzzle_input.pop(0)
    for b in puzzle_input:
        square_inches += a.overlap_area(b)

# the answer is wrong, is too high
print(square_inches)
