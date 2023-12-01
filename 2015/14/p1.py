# 20xx/xx/p1.py

import time


def parse_line(
        line):
    line = line.strip()
    line = line.replace(' can fly', '')
    line = line.replace(' km/s for', '')
    line = line.replace(' seconds, but then must rest for', '')
    line = line.replace(' seconds.', '')

    split = line.split()

    return split[0], int(split[1]), int(split[2]), int(split[3])


def parse_input(
        infn):
    with open(infn, 'r') as f:
        data = [parse_line(line) for line in f.readlines()]

    return data


def fly_single_reindeer(
        reindeer_data,
        time_to_fly):
    name, speed, active_time, rest_time = reindeer_data

    period = active_time + rest_time

    full_cycles = int(time_to_fly / period)

    remaining_time = time_to_fly % period

    full_cycle_distance = speed * active_time * full_cycles

    additional_distance = min(remaining_time, active_time) * speed

    return name, full_cycle_distance + additional_distance


def execute(
        infn,
        time_to_fly):
    data = parse_input(infn)

    individual_results = [fly_single_reindeer(reindeer, time_to_fly) for reindeer in data]

    best_reindeer = max(individual_results, key=lambda x: x[1])

    result = best_reindeer[1]

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

