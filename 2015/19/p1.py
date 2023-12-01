# 20xx/xx/p1.py

import time


def parse_input(
        infn):
    with open(infn, 'r') as f:
        source = (str.strip(line) for line in f.readlines())

    replacements = []

    mode = 'subs'
    for line in source:
        if mode == 'subs':
            if len(line) == 0:
                mode = 'molecule'
                continue
            replacements.append(line.split(' => '))
        else:
            molecule = line
    return molecule, replacements


def get_unique_molecules(
        molecule,
        replacements):
    unique_molecules = set()

    for key, repl in replacements:
        split_by_key = molecule.split(key)

        for i in range(1, len(split_by_key)):
            left_hand = key.join(split_by_key[:i])
            right_hand = key.join(split_by_key[i:])

            candidate = left_hand + repl + right_hand

            unique_molecules.add(candidate)

    return unique_molecules


def execute(
        infn):
    molecule, replacements = parse_input(infn)

    # do the thing
    unique_molecules = get_unique_molecules(molecule, replacements)

    return len(unique_molecules)


def main(
        infn):
    pre = time.perf_counter()

    result = execute(infn)

    post = time.perf_counter()

    print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
    main('input.txt')

