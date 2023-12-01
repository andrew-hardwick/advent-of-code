# 20xx/xx/p2.py

import time

from p1 import parse_input


def convert_reindeer_to_dict(
        reindeer_data):
    name, speed, active_time, rest_time = reindeer_data

    reindeer = {}
    reindeer['name'] = name
    reindeer['speed'] = speed
    reindeer['active_time'] = active_time
    reindeer['rest_time'] = rest_time
    reindeer['state'] = True
    reindeer['time_in_state'] = 0
    reindeer['distance'] = 0
    reindeer['points'] = 0

    return reindeer


def individual_sim_step(
        reindeer):
    reindeer['time_in_state'] += 1

    if reindeer['state']:
        reindeer['distance'] += reindeer['speed']

        if reindeer['time_in_state'] == reindeer['active_time']:
            reindeer['time_in_state'] = 0
            reindeer['state'] = False
    else:
        if reindeer['time_in_state'] == reindeer['rest_time']:
            reindeer['time_in_state'] = 0
            reindeer['state'] = True


def sim_step(
        reindeer):
    for individual in reindeer:
        individual_sim_step(individual)

    max_distance = max(ind['distance'] for ind in reindeer)

    for individual in reindeer:
        if individual['distance'] == max_distance:
            individual['points'] += 1


def execute(
        infn,
        time_to_fly):
    source = parse_input(infn)

    reindeer = [convert_reindeer_to_dict(r) for r in source]

    for index in range(time_to_fly):
        sim_step(reindeer)

    best_reindeer = max(reindeer, key=lambda x: x['points'])

    result = best_reindeer['points']

    return result


def main(
        infn,
        time_to_fly):
    pre = time.perf_counter()

    result = execute(infn, time_to_fly)

    post = time.perf_counter()

    print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
    main('test1.txt', 1000)
    main('input.txt', 2503)

