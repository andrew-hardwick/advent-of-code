# 20xx/xx/p1.py

import time


def parse_line(
        line):
    line = line.replace('   ', ' ')
    split = line.split(' ')
    return int(split[0]), int(split[1])


def parse_input(
        infn):
    with open(infn, 'r') as f:
        source = [parse_line(line) for line in f.readlines()]

    source = list(zip(*source))

    return source


def execute(
        infn):
    data = parse_input(infn)

    l1 = sorted(data[0])
    l2 = sorted(data[1])

    result = sum(abs(e1 - e2) for e1, e2 in zip(l1, l2))

    return result


def main(
        infn):
    pre = time.perf_counter()

    result = execute(infn)

    post = time.perf_counter()

    print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
    main('input.txt')
