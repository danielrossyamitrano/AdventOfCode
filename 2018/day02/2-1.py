from os import getcwd

puzzle_input = []
with open(getcwd() + '/input.txt', 'r') as file:
    for line in file:
        puzzle_input.append(line.rstrip('\n'))
demo = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

twices = 0
thrices = 0
for code in puzzle_input:
    # get unique characters
    seen = set(code)

    # count them
    counted_2s = False
    counted_3s = False
    for character in seen:
        if code.count(character) == 2:
            counted_2s = True
        if code.count(character) == 3:
            counted_3s = True

    # discard doubles ('it only counts once')
    if counted_2s:
        twices += 1
    if counted_3s:
        thrices += 1

checksum = twices * thrices
print('twices:', twices, 'thrices:', thrices, 'checksum:', checksum)
