# 20xx/xx/p1.py

import json
import time


def parse_input(
        infn):
    with open(infn, 'r') as f:
        data = json.loads(f.read())

    return data


def sum_numbers_in_list(
        source,
        ignore_red):
    return sum(sum_numbers_in_item(item, ignore_red) for item in source)


def sum_numbers_in_dict(
        source,
        ignore_red):
    if ignore_red and 'red' in source.values():
        return 0

    return sum(sum_numbers_in_item(source[key], ignore_red) for key in source.keys())


def sum_numbers_in_item(
        item,
        ignore_red):
    if isinstance(item, list):
        return sum_numbers_in_list(item, ignore_red)
    if isinstance(item, dict):
        return sum_numbers_in_dict(item, ignore_red)
    if isinstance(item, int):
        return item
    if isinstance(item, str):
        return 0


def execute(
        infn,
        ignore_red):
    data = parse_input(infn)

    result = sum_numbers_in_item(data, ignore_red)

    return result


def main(
        infn,
        ignore_red):
    pre = time.perf_counter()

    result = execute(infn, ignore_red)

    post = time.perf_counter()

    print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
    main('input.txt', False)

