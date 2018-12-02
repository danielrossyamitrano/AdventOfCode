from data import puzzle_input, getcwd

frequencies = []
value = 0
running = 1
with open(getcwd()+'/ex2_result.txt',"tw") as file:
    instance = -1
    while running:
        for mod in puzzle_input:
            value += mod
            if value in frequencies:
                instance += 1
                file.write('repeated frequency #'+str(instance)+': '+str(value)+'\n')
                running = 0
            else:
                frequencies.append(value)