# 20xx/xx/p2.py

from p1 import parse_input

import time


def execute(
        infn):
    data = parse_input(infn)

    result = sum(e * data[1].count(e) for e in data[0])

    return result


def main(
        infn):
    pre = time.perf_counter()

    result = execute(infn)

    post = time.perf_counter()

    print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
    main('input.txt')
