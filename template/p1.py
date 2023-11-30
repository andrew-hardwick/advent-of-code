# 20xx/xx/p1.py

import time


def parse_input(
        infn):
    with open(infn, 'r') as f:
        data = (str.strip(line) for line in f.readlines())

    return data


def execute(
        infn):
    data = parse_input(infn)

    # do the thing
    result = 0

    return result


def main(
        infn):
    pre = time.perf_counter()

    result = execute(infn)

    post = time.perf_counter()

    print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
    main('input.txt')

