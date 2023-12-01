# 20xx/xx/p2.py

import time


digit_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

rev_digit_map = {
    'eno': 1,
    'owt': 2,
    'eerht': 3,
    'ruof': 4,
    'evif': 5,
    'xis': 6,
    'neves': 7,
    'thgie': 8,
    'enin': 9
}


def parse_input(
        infn):
    with open(infn, 'r') as f:
        data = (line.strip() for line in f.readlines())

    return data


def find_first(
        line):
    for i, v in enumerate(line):
        if v.isdigit():
            return int(v)
        for k in digit_map.keys():
            if line[i:i + len(k)] == k:
                return digit_map[k]


def find_last(
        line):
    rev_line = ''.join(reversed(line))

    for i, v in enumerate(rev_line):
        if v.isdigit():
            return int(v)
        for k in rev_digit_map.keys():
            if rev_line[i:i + len(k)] == k:
                return rev_digit_map[k]


def find_digits(
        line):
    first = find_first(line)
    last = find_last(line)

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

