# 2022/19/p1.py

import itertools
import re
import time


def parse_line(line):
	numbers = [int(i) for i in re.findall(r'\d+', line)]

	ore_cost = [numbers[1], 0, 0, 0]
	cla_cost = [numbers[2], 0, 0, 0]
	obs_cost = [numbers[3], numbers[4], 0, 0]
	geo_cost = [numbers[5], 0, numbers[6], 0]

	return ore_cost, cla_cost, obs_cost, geo_cost

def parse_input(infn):
	with open(infn, 'r') as f:
		blueprints = [parse_line(l) for l in f.readlines()]

	return blueprints

def able_to_purchase(blueprint, materials, choice):
	return all(materials[i] >= blueprint[choice][i] for i in range(4))

def time_step(materials, producers, time, time_delta):
	return [materials[i] + (producers[i] * time_delta) for i in range(4)], time + time_delta

def buy(materials, blueprint, choice):
	return [materials[i] - blueprint[choice][i] for i in range(4)]

def unable_to_produce(blueprint, producers, choice):
	return any(producers[i] == 0 and blueprint[choice][i] > 0 for i in range(4))

def choose_next(blueprint, time, time_limit, materials, producers, max_producers, choice, history):
	max_geodes = 0
	best_child_history = []

	if history == [1]:
		print(history, choice, time)
		print(materials, blueprint[choice])
		print(able_to_purchase(blueprint, materials, choice))
		print()

	if time > time_limit:
		return materials[3], history

	# TODO make this do the necessary time steps without looping (and do an additional instead of below)
	while not able_to_purchase(blueprint, materials, choice):
		if time > time_limit:
			return materials[3], history
		materials, time = time_step(materials, producers, time, 1)

	if time > time_limit:
		return materials[3], history

	materials = buy(materials, blueprint, choice)
	this_history = history.copy() + [choice]
	materials, time = time_step(materials, producers, time, 1)

	if time > time_limit:
		return materials[3], history

	producers[choice] += 1

	# decide on buying additional producers here
	for next_choice in range(3, -1, -1):
		if producers[next_choice] < max_producers[next_choice] and not unable_to_produce(blueprint, producers, next_choice):
			geodes, child_history = choose_next(blueprint, time + 1, time_limit, materials.copy(), producers.copy(), max_producers, next_choice, this_history.copy())

			if geodes > max_geodes:
				max_geodes = geodes
				best_child_history = child_history

	return max_geodes, best_child_history

def optimize(blueprint, time_limit):
	materials = [0, 0, 0, 0]
	producers = [1, 0, 0, 0]

	max_producers = [max(blueprint[p][m] for p in range(4)) for m in range(4)]
	max_producers[3] = time_limit

	# we can only buy choices 0 or 1 so we should only call for those
	results = [choose_next(blueprint, 0, time_limit + 1, materials, producers, max_producers, choice, []) for choice in range(2)]

	print(results, max_producers)

	geodes, history = sorted(results, reverse=True)[0]

	print(geodes, history)

	return geodes

def execute(infn, time_limit):
	blueprints = parse_input(infn)

	optimal_results = [optimize(blueprint, time_limit) for blueprint in blueprints]

	print(optimal_results)

	return '??'

def main(infn, time_limit):
	pre = time.perf_counter()

	result = execute(infn, time_limit)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt', 24)
	#main('input.txt', 24)
