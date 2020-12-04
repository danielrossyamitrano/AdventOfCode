numbers = [int(number.rstrip('\n')) for number in open('input.txt')]

cheked = []
result_ex1 = 0
result_ex2 = 0
for number in numbers:
    if number not in cheked:
        cheked.append(number)
    for other in numbers:
        if other not in cheked and result_ex1 == 0:
            if number + other == 2020:
                result_ex1 = number * other
                break
        if result_ex2 == 0:
            for another in numbers:
                if other not in cheked or another not in cheked:
                    if number + other + another == 2020:
                        result_ex2 = number*other*another
                        break
    if result_ex1 and result_ex2:
        break

print('result ex 1: ', result_ex1)
print('result ex 1: ', result_ex2)
