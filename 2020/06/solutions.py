from os import getcwd, path

groups = [[]]
i = 0
with open(path.join(getcwd(), '06', 'input.txt'), 'rt') as file:
    for line in file.readlines():
        line = line.rstrip('\n')
        if line == '':
            groups.append([])
            i += 1
        else:
            groups[i].append(line)

result_ex_1 = 0
result_ex_2 = 0
for group in groups:
    unique = list(set(''.join(group)))  # this is something that I've only learned recently.
    unique.sort()
    result_ex_1 += len(unique)
    for char in unique:
        if all([char in person for person in group]):
            result_ex_2 += 1


print(result_ex_1)
print(result_ex_2)
