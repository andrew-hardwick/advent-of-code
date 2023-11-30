# 20xx/xx/p1.py

import itertools
import time


def parse_line(
        line):
    line = line.strip()
    line = line.replace(' to ', ' ')
    line = line.replace(' = ', ' ')

    return line.split(' ')


def parse_input(
        infn):
    with open(infn, 'r') as f:
        data = [parse_line(line) for line in f.readlines()]

    result = {}

    for loc_a, loc_b, distance in data:
        int_distance = int(distance)
        result[(loc_a, loc_b)] = int_distance
        result[(loc_b, loc_a)] = int_distance

    return result


def calculate_distance(
        stops,
        leg_distances):
    legs = list(zip(stops[:-1], stops[1:]))

    return sum(leg_distances[leg] for leg in legs)


def calculate_distances(
        leg_distances):
    destinations = list(set([a for a, _ in leg_distances.keys()]))

    perms = itertools.permutations(destinations)

    return [calculate_distance(perm, leg_distances) for perm in perms]


def execute(
        infn):
    leg_distances = parse_input(infn)

    distances = calculate_distances(leg_distances)

    return str(min(distances))


def main(
        infn):
    pre = time.perf_counter()

    result = execute(infn)

    post = time.perf_counter()

    print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
    main('input.txt')

