def run(data):
    for start in range(0, len(data)-1, 4):
        end = start + 4
        opcode, idx_a, idx_b, output_idx = data[start:end]
        if opcode == 99:
            break
        elif opcode == 1:
            value_a, value_b = data[idx_a], data[idx_b]
            data[output_idx] = value_a+value_b
        elif opcode == 2:
            value_a, value_b = data[idx_a], data[idx_b]
            data[output_idx] = value_a*value_b
    return data[0]


# program = [1,1,1,4,99,5,6,0,99]
file = open('input.txt')
_program = [int(i) for i in file.readline().split(',')]
file.close()

# settings for solution 1
# program[1] = 12  # noun
# program[2] = 2  # verb

# settings for solution 2
noun, verb = 0, 0
for verb in range(100):
    for noun in range(100):
        program = _program.copy()
        program[2] = verb
        program[1] = noun
        try:
            if run(program) == 19690720:
                print(100 * noun+verb)
                break
        except IndexError:
            pass
