# 2021/07/p2.py

import time


fuel_cost_cache = {}

def get_specific_cost(crab, target_position):
	distance = abs(crab - target_position)

	if not distance in fuel_cost_cache:
		fuel_cost_cache[distance] = (distance + 1) * distance / 2

	return fuel_cost_cache[distance]

def get_fuel_cost(crabs, target_position):
	cost = [get_specific_cost(crab, target_position) for crab in crabs]

	return sum(cost)

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
