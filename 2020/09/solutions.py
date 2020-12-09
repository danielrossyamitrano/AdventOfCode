from os import getcwd, path
with open(path.join(getcwd(), '09', 'input.txt'), 'rt') as file:
    sample = [int(i.rstrip('\n')) for i in file.readlines()]

# Part 1
preamble = 25
mi, ma = 0, preamble
next_number_idx = preamble - 1
proceed = True
result_ex1 = None
while next_number_idx + 1 < len(sample) and proceed:
    next_number_idx += 1
    number = sample[next_number_idx]
    section = sample[mi:ma]
    valid = False
    while not valid:
        if len(section):
            a = section.pop(0)
            for b in section:
                if number == (a + b):
                    valid = True
                    break
        else:
            result_ex1 = number
            proceed = False
            break
    ma += 1
    mi += 1

# Part 2
mi, ma = 0, 2
while True:
    section = sample[mi:ma]
    if not sum(section) == result_ex1:
        if ma + 1 < len(sample):
            ma += 1
        else:
            mi += 1
            ma = mi + 2
    else:
        section.sort()
        a = section[0]
        b = section[-1]
        result_ex2 = a + b
        break

print(result_ex1, 'is invalid')
print(result_ex2)
