# 20xx/xx/p1.py

import itertools
import time


def parse_line(
        line):
    line = line.strip().replace('gain ', '').replace('lose ', '-')
    line = line.replace(' would', '')
    line = line.replace(' happiness units by sitting next to', '')
    line = line.replace('.', '')

    split_line = line.split(' ')

    return split_line[0], split_line[2], int(split_line[1])


def calculate_total_happiness(
        seating_chart,
        happiness_dict):
    pairs = list(zip(seating_chart[:-1], seating_chart[1:]))
    pairs.append((seating_chart[-1], seating_chart[0]))

    return sum(happiness_dict[pair] for pair in pairs)


def parse_input(
        infn):
    with open(infn, 'r') as f:
        data = [parse_line(line) for line in f.readlines()]

    people = list(set(p1 for p1, _0, _1 in data))

    happiness_dict = {}

    for p_1, p_2, gain in data:
        if (p_1, p_2) not in happiness_dict.keys():
            happiness_dict[(p_1, p_2)] = 0
        if (p_2, p_1) not in happiness_dict.keys():
            happiness_dict[(p_2, p_1)] = 0

        happiness_dict[(p_1, p_2)] += gain
        happiness_dict[(p_2, p_1)] += gain

    return people, happiness_dict


def execute(
        infn,
        add_nullo):
    people, happiness_dict = parse_input(infn)

    if add_nullo:
        for person in people:
            happiness_dict[(person, 'nullo')] = 0
            happiness_dict[('nullo', person)] = 0

        people.append('nullo')

    perms = itertools.permutations(people)

    total_happiness_all_perms = (calculate_total_happiness(perm, happiness_dict) for perm in perms)

    result = max(total_happiness_all_perms)

    return result


def main(
        infn,
        add_nullo):
    pre = time.perf_counter()

    result = execute(infn, add_nullo)

    post = time.perf_counter()

    print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
    main('input.txt', False)

