from data import puzzle_input
demo = ['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']



twices = 0
thrices = 0
for code in puzzle_input:
    #get unique characters
    seen = []
    counted_2s = False
    counted_3s = False
    for character in code:
        if character not in seen:
            seen.append(character)
    
    # count them
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

checksum = twices*thrices
print('twices:',twices, 'thrices:',thrices, 'checksum:',checksum)
