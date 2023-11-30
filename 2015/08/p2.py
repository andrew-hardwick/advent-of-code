# 2021/xx/p1.py

import time

from p1 import parse_input


def process_single_char(
        char):
    if char == '"' or char == '\\':
        return 1

    return 0


def process_single_line(
        line):
    return sum(process_single_char(c) for c in line) + 2


def execute(
        infn):
    data = parse_input(infn)

    total = sum(process_single_line(line) for line in data)

    return str(total)


def main(infn):
    pre = time.perf_counter()

    result = execute(infn)

    post = time.perf_counter()

    print(result, 'in', (post - pre) * 1000, 'ms')


if __name__ == '__main__':
    main('input.txt')

