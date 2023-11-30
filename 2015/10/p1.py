# 20xx/xx/p1.py

import time


def parse_input(
        infn):
    with open(infn, 'r') as f:
        data = [int(c) for c in f.read()]

    return data


def iterate(
        source):
    result = []

    current = source[0]
    count = 1

    for e in source[1:]:
        if e == current:
            count += 1
        else:
            result.append(count)
            result.append(current)

            current = e
            count = 1

    result.append(count)
    result.append(current)

    return result


def execute(
        infn,
        iteration_count):
    data = parse_input(infn)

    for _ in range(iteration_count):
        data = iterate(data)

    result = len(data)

    return result


def main(
        infn,
        iteration_count):
    pre = time.perf_counter()

    result = execute(infn, iteration_count)

    post = time.perf_counter()

    print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
    main('input.txt', 40)

