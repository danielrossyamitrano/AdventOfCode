from os import getcwd, path


prgm = []
with open(path.join(getcwd(), '08', 'input.txt'), 'rt') as file:
    for line in file.readlines():
        line = line.rstrip('\n').split(' ')
        instruction = line[0]
        value = int(line[1])
        prgm.append([instruction, value])


def run_instruction(prog, acc, pos):
    if pos >= len(prgm):
        return 'EOF'
    ins = prog[pos][0]
    val = prog[pos][1]
    if ins == 'nop':
        pos += 1
    elif ins == 'acc':
        acc += val
        pos += 1
    elif ins == 'jmp':
        pos += val
    return pos, acc


def debugger(progm, iteration, show_failure=True):
    accumulator = 0
    visited = []
    idx = 0
    while True:
        ran = run_instruction(progm, accumulator, idx)
        if ran == 'EOF':
            print('\niteration #{}'.format(iteration))
            print('program ran successfully')
            print('accumulator: ', accumulator)
            break
        else:
            idx, accumulator = ran

        if idx not in visited:
            visited.append(idx)
        else:
            if show_failure:
                print('\niteration #{}'.format(iteration))
                print('infinite loop on line #{}'.format(idx))
                print('accumulator: ', accumulator)
            break


# Part 1
debugger(prgm, 0)

# Part 2
_names = [i[0] for i in prgm]
_indices = [i for i in range(len(prgm)) if prgm[i][0] != 'acc']
_mods = [i[1] for i in prgm]


for i, indice in enumerate(_indices, start=1):
    names = _names.copy()
    if _names[indice] == 'nop':
        names[indice] = 'jmp'
    else:
        names[indice] = 'nop'
    debugged = list(zip(names, _mods))
    debugger(debugged, i, False)
