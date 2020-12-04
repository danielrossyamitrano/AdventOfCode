# Preprocessing: read file and group individual passwords in one list.
chunks = [[]]
i = 0
with open('input.txt', 'rt') as file:
    for line in file.readlines():
        if not line.isspace():
            chunks[i].append(line.rstrip('\n'))
        else:
            chunks.append([])
            i += 1
# Preprocessing convert the lists into a master dictionary
master = []
for i, item in enumerate([' '.join(chunk).split(' ') for chunk in chunks]):
    master.append({})
    for pair in item:
        master[i].update({tuple(pair.split(':'))})

keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
valid_ex1 = 0
valid_ex2 = 0
for item in master:
    # Part 1
    initially_valid = False
    if len(item) == len(keys):
        valid_ex1 += 1
        initially_valid = True
    elif len(item) == len(keys)-1:
        if keys[-1] not in item:
            valid_ex1 += 1
            initially_valid = True

    # Part 2
    if initially_valid:
        maybe_valid = []
        if 1920 <= int(item['byr']) <= 2002:
            maybe_valid.append(True)
        if 2010 <= int(item['iyr']) <= 2020:
            maybe_valid.append(True)
        if 2020 <= int(item['eyr']) <= 2030:
            maybe_valid.append(True)
        if item['hgt'].endswith('in') or item['hgt'].endswith('cm'):
            h = int(item['hgt'][:-2])
            if item['hgt'].endswith('in'):
                maybe_valid.append(59 <= h <= 76)
            elif item['hgt'].endswith('cm'):
                maybe_valid.append(150 <= h <= 193)
        if item['ecl'] in 'amb blu brn gry grn hzl oth'.split(' '):
            maybe_valid.append(True)
        if len(item['pid']) == 9:
            maybe_valid.append(True)
        if item['hcl'].startswith('#') and len(item['hcl']) == 7:
            maybe_valid.append(True)

        if all(maybe_valid) and len(maybe_valid) == len(keys)-1:
            valid_ex2 += 1


print(valid_ex1)
print(valid_ex2)
