from os import getcwd
from os.path import join

ruta = join(getcwd(), 'input.txt')
file = open(ruta)

numbers = [int(number.rstrip('\n')) for number in file]

cheked = []
for number in numbers:
    if number not in cheked:
        cheked.append(number)
    for other in numbers:
        for another in numbers:
            if other not in cheked or another not in cheked:
                if number + other + another == 2020:
                    print(number*other*another)
