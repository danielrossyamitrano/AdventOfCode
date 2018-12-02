from os import getcwd

puzzle_input = []
with open(getcwd()+'/input.txt', 'r') as file:
    for line in file:
        puzzle_input.append(int(line))


value = 0
for mod in puzzle_input:
    value += mod

print(value)
