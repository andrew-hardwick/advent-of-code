# 20xx/xx/p1.py

import time


def parse_input(
        infn):
    with open(infn, 'r') as f:
        data = (str.strip(line) for line in f.readlines())

    return data


def find_digits(
        line):
    first = -1
    last = 0

    for c in line:
        if c.isdigit():
            if first == -1:
                first = c
            last = c

    return first, last


def execute(
        infn):
    data = parse_input(infn)

    found_digits = (find_digits(line) for line in data)

    combined = (int(f'{a}{b}') for a, b in found_digits)

    result = sum(combined)

    return result


def main(
        infn):
    pre = time.perf_counter()

    result = execute(infn)

    post = time.perf_counter()

    print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
    main('test1.txt')
    main('input.txt')

