# 20xx/xx/p1.py

import math
import re
import time

import numpy as np

def parse_line(line):
	numbers = [int(i) for i in re.findall(r'\d+', line)]

	ore_bot = (np.array([numbers[1], 0, 0, 0]), np.array([1, 0, 0, 0]))
	clay_bot = (np.array([numbers[2], 0, 0, 0]), np.array([0, 1, 0, 0]))
	obsidian_bot = (np.array([numbers[3], numbers[4], 0, 0]), np.array([0, 0, 1, 0]))
	geode_bot = (np.array([numbers[5], 0, numbers[6], 0]), np.array([0, 0, 0, 1]))

	return ore_bot, clay_bot, obsidian_bot, geode_bot

def parse_input(infn):
	with open(infn, 'r') as f:
		blueprints = [parse_line(l) for l in f.readlines()]

	return blueprints

def time_step(materials, producers, time, time_delta):
	return materials + (producers * time_delta), time + time_delta

	return [materials[i] + (producers[i] * time_delta) for i in range(4)], time + time_delta

def calculate_wait_time(blueprint, materials, producers, choice):
	possible_times = [math.ceil(i) for i in ((blueprint[choice][0] - materials) / producers) if i >= 1]

	if len(possible_times) > 0:
		return min(possible_times) + 1, possible_times

	return 0, possible_times

def choose_next(blueprint, time, time_limit, materials, producers, max_producers, choice, history):
	wait_time, possible_times = calculate_wait_time(blueprint, materials, producers, choice)

	test_history = [1, 1]

	if history == test_history:
		print('choice', choice)
		print(history)
		print('cost', blueprint[choice][0])
		print('materials', materials)
		print('producers', producers)
		print()

	if time + wait_time > time_limit:
		return materials[3] + producers[3] * (time_limit - time)

	materials, time = time_step(materials, producers, time, wait_time)

	if history == test_history:
		print('cost', blueprint[choice][0])
		print('time', time)
		print('possible_times', possible_times)
		print('wait_time', wait_time)
		print('materials', materials)
		print('producers', producers)
		print()

	materials = materials - blueprint[choice][0]

	materials, time = time_step(materials, producers, time, 1)

	producers = producers + blueprint[choice][1]

	if time >= time_limit:
		return materials[3] + producers[3] * (time_limit - time)

	if history == test_history:
		print('time', time)
		print('materials', materials)
		print('producers', producers)
		print()

	non_max_robots = set([i for i in range(4) if producers[i] < max_producers[i]])
	able_to_buy_robots = set([i for i in range(4) if all(not producers[j] == 0 or blueprint[i][0][j] == 0 for j in range(4))])

	robots_to_buy = non_max_robots & able_to_buy_robots

	next_history = history + [choice]

	child_geodes = [choose_next(blueprint, time, time_limit, materials.copy(), producers.copy(), max_producers, next_robot, next_history) for next_robot in robots_to_buy]

	return max(child_geodes)

def optimize(blueprint, time_limit):
	materials = np.array([0, 0, 0, 0])
	producers = np.array([1, 0, 0, 0])

	max_producers = np.array([max((blueprint[r][0][i] for r in range(4))) for i in range(4)])
	max_producers[3] = time_limit

	for i in range(2):
		next_bot = 1 - i

		geodes = choose_next(blueprint, 0, time_limit, materials, producers, max_producers, next_bot, [])

	return geodes

def execute(infn, time_limit):
	blueprints = parse_input(infn)

	test = optimize(blueprints[0], time_limit)

	return '??'

	geodes = [optimize(blueprint, time_limit) for blueprint in blueprints]

	quality_levels = [i * g for i, g in enumerate(geodes)]

	return sum(quality_levels)

def main(infn, time_limit):
	pre = time.perf_counter()

	result = execute(infn, time_limit)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt', 24)
#	main('input.txt')
