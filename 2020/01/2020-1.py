numbers = [int(number.rstrip('\n')) for number in open('input.txt')]

result_ex1 = 0
result_ex2 = 0
for i, number in enumerate(numbers):
    for other in numbers[:i+1]:  # looping by index as suggested by GitHub user einacio
        if result_ex1 == 0:  # inverted "in clause" as suggested by GitHub user einacio
            if number + other == 2020:
                result_ex1 = number * other
                break
        if result_ex2 == 0:
            for another in numbers[:i+2]:
                if number + other + another == 2020:
                    result_ex2 = number*other*another
                    break
    if result_ex1 and result_ex2:
        break

print('result ex 1: ', result_ex1)
print('result ex 1: ', result_ex2)
