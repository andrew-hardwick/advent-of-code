# 20xx/xx/p1.py

import time


digit_map = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}


def parse_line(
        line,
        replace_text_with_digits):
    line = line.strip()

    if replace_text_with_digits:
        for k, v in digit_map.items():
            line = line.replace(k, v)

    return line


def parse_input(
        infn,
        replace_text_with_digits):
    with open(infn, 'r') as f:
        data = (parse_line(line, replace_text_with_digits) for line in f.readlines())

    return data


def execute(
        infn,
        replace_text_with_digits):
    data = parse_input(infn, replace_text_with_digits)

    found_digits = ([int(c) for c in line if c.isdigit()] for line in data)

    combined = (digits[0] * 10 + digits[-1] for digits in found_digits)

    result = sum(combined)

    return result


def main(
        infn,
        replace_text_with_digits):
    pre = time.perf_counter()

    result = execute(infn, replace_text_with_digits)

    post = time.perf_counter()

    print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
    main('test1.txt', False)
    main('input.txt', False)

