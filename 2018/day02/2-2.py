from os import getcwd

demo = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

puzzle_input = []
with open(getcwd() + '/input.txt', 'r') as file:
    for line in file:
        puzzle_input.append(line.rstrip('\n'))

pares = {}
max_coincidences = 0
a, b = None, None

while len(puzzle_input) > 1:
    code_a = puzzle_input.pop(0)
    for code_b in puzzle_input:
        coincidences = 0
        for i in range(len(code_a)):
            if code_a[i] == code_b[i]:
                coincidences += 1

        if coincidences > max_coincidences:
            max_coincidences = coincidences
            a = code_a
            b = code_b

common_letters = ''
for i, char in enumerate(a):
    if char == b[i]:
        common_letters += char

with open(getcwd() + '/ex2_result.txt', "tw") as file:
    file.write(common_letters)
