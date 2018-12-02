from os import getcwd


puzzle_input = []
with open(getcwd()+'/input.txt','r') as file:
    for line in file:
        puzzle_input.append(int(line))
