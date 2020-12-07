from os import getcwd, path

rules = {}
with open(path.join(getcwd(), '07', 'input.txt'), 'rt') as file:
    for line in file.readlines():
        line = line.rstrip('\n').replace(', ', '.')[:-1]
        contains = line.split('bags contain')
        container_color, contained_bags = contains[0].strip(' '), contains[1].strip(' ').split('.')
        if contained_bags[0] == 'no other bags':
            contained = None
        else:
            contained = {}
            for bag in contained_bags:
                sentence = bag.split(' ')
                quantity = int(sentence[0])
                color = ' '.join(sentence[1:3])
                contained[color] = quantity

        rules[container_color] = contained

result_1 = []


def can_contain_color(key):
    for container in rules:
        can_contain_anything = rules[container] is not None
        if can_contain_anything and key in rules[container] and container not in result_1:
            can_contain_color(container)
            result_1.append(container)


def how_many(container):
    value = 0
    if rules[container] is not None:
        value += sum(rules[container].values())
        for bag_color in rules[container]:
            value += rules[container][bag_color] * how_many(bag_color)
    return value


my_bag_color = 'shiny gold'
can_contain_color(my_bag_color)
result_ex1 = len(result_1)
result_ex2 = how_many(my_bag_color)

print(result_ex1)
print(result_ex2)
