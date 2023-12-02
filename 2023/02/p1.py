# 20xx/xx/p1.py

import time


def parse_set(
        cubeSet):
    setSplit = (cube.split(' ') for cube in cubeSet.split(', '))

    return ((color, int(count)) for count, color in setSplit)


def parse_line(line):
    sets = line.strip().split(': ')[1].split('; ')

    return (parse_set(s) for s in sets)


def parse_input(
        infn):
    with open(infn, 'r') as f:
        data = (parse_line(line) for line in f.readlines())

    return data


def execute(
        infn):
    data = parse_input(infn)

    limits = {}

    limits["red"] = 12
    limits["green"] = 13
    limits["blue"] = 14

    result = 0

    for i, game in enumerate(data):
        validGame = True

        for turn in game:
            for color, count in turn:
                validGame &= count <= limits[color]

        if validGame:
            result += i + 1

    return result


def main(
        infn):
    pre = time.perf_counter()

    result = execute(infn)

    post = time.perf_counter()

    print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
    main('input.txt')

