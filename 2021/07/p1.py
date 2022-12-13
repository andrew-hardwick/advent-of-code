# 2021/07/p1.py

import time


def get_fuel_cost(crabs, target_position):
	cost = 0
	for crab in crabs:
		cost += abs(crab - target_position)

	return cost

def walk_to_lowest_cost(crabs, starting_point, cost, inc):
	position = starting_point + inc
	next_cost = get_fuel_cost(crabs, position)

	while(cost > next_cost):
		position += inc

		cost = next_cost
		next_cost = get_fuel_cost(crabs, position)

	return min([cost, next_cost])


def execute(input_file):
	with open(input_file, 'r') as f:
		crabs = [int(i) for i in str.strip(f.read()).split(',')]

	# do the thing
	starting_point = int(sum(crabs) / len(crabs))
	fuel_cost = get_fuel_cost(crabs, starting_point)
	one_less_cost = get_fuel_cost(crabs, starting_point - 1)
	one_more_cost = get_fuel_cost(crabs, starting_point + 1)

	if one_less_cost < fuel_cost:
		starting_point = starting_point - 1
		fuel_cost = walk_to_lowest_cost(crabs, starting_point, one_less_cost, -1)
	elif one_more_cost < fuel_cost:
		starting_point = starting_point + 1
		fuel_cost = walk_to_lowest_cost(crabs, starting_point, one_more_cost, 1)

	return fuel_cost

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
