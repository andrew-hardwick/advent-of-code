# 2022/02/build_lookup_tables.py

import itertools


def score_part_1(oc, pc):
    oc_i = ord(oc) - 65
    pc_i = ord(pc) - 87

    return 3 * (((pc_i - oc_i) + 3) % 3) + pc_i

def score_part_2(oc, r):
    oc_i = ord(oc) - 65
    r_i = ord(r) - 88

    game_result = r_i * 3
    pc = (r_i + oc_i - 1) % 3 + 1

    return pc + game_result

def main():
    l1 = ['A', 'B', 'C']
    l2 = ['X', 'Y', 'Z']

    games = [(f'{e1} {e2}', score_part_1(e1, e2), score_part_2(e1, e2)) for e1, e2 in itertools.product(l1, l2)]

    part1_lookup = [f'{game},{p1}' for game, p1, p2 in games]
    part2_lookup = [f'{game},{p2}' for game, p1, p2 in games]

    with open('part_1_lookup', 'w') as f:
        f.write('\n'.join(part1_lookup))

    with open('part_2_lookup', 'w') as f:
        f.write('\n'.join(part2_lookup))

if __name__ == '__main__':
    main()
