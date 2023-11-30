# 20xx/xx/p1.py

import time


def parse_input(
        infn):
    with open(infn, 'r') as f:
        data = [ord(c) - 97 for c in f.read()]

    data = list(reversed(data))

    return data


def increment(
        password):
    password[0] += 1

    index = 0

    while password[index] > 25:
        password[index] = 0
        password[index + 1] += 1

        index += 1


def does_not_contain_increasing_sequence(
        password,
        sequence_length):
    for a, b, c in zip(password[:-2], password[1:-1], password[2:]):
        if a - b == 1 and b - c == 1:
            return False

    return True


def does_not_contain_two_pairs(
        password):
    pairs = set()

    for a, b in zip(password[:-1], password[1:]):
        if a == b:
            pairs.add(a)

        if len(pairs) > 1:
            return False

    return True


def is_ok_password(
        password):
    if 8 in password or 11 in password or 14 in password:
        return False
    if does_not_contain_increasing_sequence(password, 3):
        return False
    if does_not_contain_two_pairs(password):
        return False

    return True


def unintify_password(
        password):
    return ''.join(chr(ord('a') + i) for i in reversed(password))


def find_next_password(
        password):
    increment(password)

    while not is_ok_password(password):
        increment(password)

    return password


def execute(
        infn,
        count):
    password = parse_input(infn)

    for _ in range(count):
        password = find_next_password(password)

    return unintify_password(password)


def main(
        infn,
        count):
    pre = time.perf_counter()

    result = execute(infn, count)

    post = time.perf_counter()

    print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
    main('input.txt', 1)

