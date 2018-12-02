from os import getcwd

puzzle_input = []
with open(getcwd() + '/input.txt', 'r') as file:
    for line in file:
        puzzle_input.append(int(line))

frequencies = []
value = 0
running = 1
with open(getcwd() + '/ex2_result.txt', "tw") as file:
    instance = -1
    while running:
        for mod in puzzle_input:
            value += mod
            if value in frequencies:
                instance += 1
                file.write('repeated frequency #' + str(instance) + ': ' + str(value) + '\n')
                running = 0
            else:
                frequencies.append(value)
