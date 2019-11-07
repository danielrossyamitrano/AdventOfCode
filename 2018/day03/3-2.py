from pygame import Rect

rects = []
with open('input.txt', 'r') as file:
    for line in file:
        base = line.rstrip('\n')
        string = base.split(' @ ')[1]
        string = string.replace(': ', ',').replace('x', ',')
        x, y, w, h = [int(i) for i in string.split(',')]
        r = Rect(x, y, w, h)
        rects.append(r)

for j, rect in enumerate(rects, start=1):
    collide_list = [i for i in rects if i is not rect]
    if not rect.collidelist(collide_list):
        print(j)
