# 20xx/xx/p2.py

import time


digit_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def parse_line(
        line):
    line = line.strip()

    index_map = {}

    for k in digit_map.keys():
        index_map[k] = len(line) + 1
        location = line.find(k)

        if location != -1:
            index_map[k] = location

    first_key, index = min(list(index_map.items()), key=lambda x: x[1])

    line_from_left = line
    if index < len(line):
        line_from_left = line[:index] + digit_map[first_key] + line[len(first_key) + index:]

    index_map = {}

    for k in digit_map.keys():
        index_map[k] = -1
        location = line.rfind(k)

        if location != -1:
            index_map[k] = location

    first_key, index = max(list(index_map.items()), key=lambda x: x[1])

    line_from_right = line
    if index > 0:
        line_from_right = line[:index] + digit_map[first_key] + line[len(first_key) + index:]

    return line_from_left, line_from_right


def parse_input(
        infn):
    with open(infn, 'r') as f:
        data = (parse_line(line) for line in f.readlines())

    return data


def find_digits(
        line):
    line_from_left, line_from_right = line

    first = -1
    last = -1

    for c in line_from_left:
        if c.isdigit():
            if first == -1:
                first = c
                break

    for c in reversed(line_from_right):
        if c.isdigit() and last == -1:
            last = c
            break

    return first, last


def execute(
        infn):
    data = parse_input(infn)

    found_digits = (find_digits(lines) for lines in data)

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
    main('test2.txt')
    main('input.txt')

