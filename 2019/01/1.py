from math import floor


def calculate(value):
    return floor(value/3)-2


def recalculate(mass):
    totalmass = 0
    while mass > 0:
        mass = calculate(mass)
        if mass < 0:
            mass = 0

        totalmass += mass
    return totalmass


file = [int(i.rstrip('\n')) for i in open('input.txt').readlines()]
masses = [calculate(i) for i in file]
print('ex 1:', sum(masses))

extramass = [recalculate(i) for i in masses]
print('ex 2:', sum(masses)+sum(extramass))
