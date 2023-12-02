# 20xx/xx/p2.py

import time

from p1 import parse_input


def execute(
        infn):
    data = parse_input(infn)

    result = 0

    for i, game in enumerate(data):
        minRed = 0
        minGreen = 0
        minBlue = 0

        for turn in game:
            for color, count in turn:
                if color == "red":
                    minRed = max(minRed, count)
                if color == "green":
                    minGreen = max(minGreen, count)
                if color == "blue":
                    minBlue = max(minBlue, count)

        result += minRed * minGreen * minBlue

    return result


def main(
        infn):
    pre = time.perf_counter()

    result = execute(infn)

    post = time.perf_counter()

    print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
    main('input.txt')

