file = open('input.txt').readlines()

valid_ex1 = 0
valid_ex2 = 0
for item in file:
    # Part 1
    key, value = item.rstrip('\n').split(':')
    password = value.lstrip(' ')
    ex = key.replace('-', ' ').split(' ')
    mi, ma, char = [int(i) for i in ex[:-1]]+[ex[2]]
    if mi <= password.count(char) <= ma:
        valid_ex1 += 1

    # Part 2
    idx_a, idx_b = mi-1, ma-1
    exa = password[idx_a] == char
    exb = password[idx_b] == char
    if exa and not exb or exb and not exa:
        valid_ex2 += 1


print(valid_ex1)
print(valid_ex2)
