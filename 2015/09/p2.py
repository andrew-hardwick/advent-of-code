# 20xx/xx/p2.py

import time

from p1 import parse_input, calculate_distances


def execute(infn):
    legs_distances = parse_input(infn)

    distances = calculate_distances(legs_distances)

    result = max(distances)

    return result


def main(infn):
    pre = time.perf_counter()

    result = execute(infn)

    post = time.perf_counter()

    print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
    main('input.txt')

