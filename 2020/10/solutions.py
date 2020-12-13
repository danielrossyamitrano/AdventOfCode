from os import getcwd, path

with open(path.join(getcwd(), '10', 'input.txt'), 'rt') as file:
    sample = [int(line.rstrip('\n')) for line in file.readlines()]

# sample = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
# sample = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32,
#           25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
# sample = [1, 2, 3, 4]

# Part 1
sample.sort()
differences = []
jolt = 0
for adapter in sample:
    differences.append(abs(adapter - jolt))
    jolt = adapter
else:
    sample.append(jolt + 3)
    differences.append(abs(sample[-1] - jolt))

print(differences.count(1) * differences.count(3))


# Part 2
d = {0: 1}


def calculate(x):
    if x <= 0:
        return 1
    elif x not in sample:
        return 0
    elif x == 1 and x not in d:
        d[x] = calculate(x - 1)
    elif x == 2 and x not in d:
        d[x] = calculate(x - 2) + calculate(x - 1)
    elif x not in d:
        d[x] = calculate(x - 3) + calculate(x - 2) + calculate(x - 1)
    return d[x]


# n4 = n(4-3) + n(4-2) + n(4-1)
# n4 = n(1) + n(2) + n(3)
# n4 = 1 + n(2-2) + n(2-1) + n(3-3) + n(3-2) + n(3-1)
# n4 = 1 + 1      + 1      + 1      + 1       + n(2)
# n4 = 5 + n(2-2) + n(2-1)
# n4 = 5 + n(0) + n(1)
# n4 = 5 + 1 + 1
# n4 = 7

# n5 = n(5-3) + n(5-2) + n(5-1)
# n5 = n(2) + n(3)                    + n(1) + n(2) + n(3)
# n5 = 2 + (n(3-3) + n(3-2) + n(3-1)) + 1 + 2 + (n(3-3) + n(3-2) + n(3-1))
# n5 = 2 + n(0) + n(1) + n(2) + 1 + 2 + n(0) + n(1) + n(2)
# n5 = 2 + 1    + 1    + 2    + 1 + 2 + 1     + 1   + n(2-2)+ n(2-1)
# n5 = 2 + 1    + 1    + 2    + 1 + 2 + 1     + 1   + 1   +  1
# n5 = 13

print(calculate(sample[-1]))
