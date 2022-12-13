# 2021/09/p2.py

import functools
import itertools
import operator
import time


def is_low_point(source, max_x, max_y, cell):
	x, y = cell
	val = source[x][y]

	low_point = True

	if not x == 0:
		low_point &= source[x - 1][y] > val
	if not x == max_x:
		low_point &= source[x + 1][y] > val
	if not y == 0:
		low_point &= source[x][y - 1] > val
	if not y == max_y:
		low_point &= source[x][y + 1] > val

	return low_point

def calculate_basin_size(source, max_x, max_y, cell):
	basin_contents = [cell]
	checked_neighbors = [cell]
	unchecked_neighbors = generate_neighbors(checked_neighbors, cell)

	while len(unchecked_neighbors) > 0:
		neighbor_under_test = unchecked_neighbors.pop()
		x, y = neighbor_under_test

		if x >= 0 and y >= 0 and x <= max_x and y <= max_y:
			if not source[x][y] == 9:
				unchecked_neighbors.update(generate_neighbors(checked_neighbors, neighbor_under_test))
				basin_contents.append(neighbor_under_test)

		checked_neighbors.append(neighbor_under_test)

	return len(basin_contents)

def generate_neighbors(checked_neighbors, cell):
	x, y = cell

	deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

	result = set()

	for d_x, d_y in deltas:
		candidate = (x + d_x, y + d_y)

		if not candidate in checked_neighbors:
			result.add(candidate)

	return result

def pretty_print(source, len_x, len_y):
	print('')
	for i in range(len_x):
		for j in range(len_y):
			print(source[i * len_y + j], end='')
		print('')
	print('')

def execute(input_file):
	with open(input_file, 'r') as f:
		source = [[int(i) for i in str.strip(line)] for line in f.readlines()]

	len_x = len(source)
	len_y = len(source[0])

	cells = list(itertools.product(range(len_x), range(len_y)))

	max_x = len_x - 1
	max_y = len_y - 1

	f_is_low_point = functools.partial(is_low_point, source, max_x, max_y)
	f_calculate_basin_size = functools.partial(calculate_basin_size, source, max_x, max_y)

	basin_sizes = [f_calculate_basin_size(cell) for cell in cells if f_is_low_point(cell)]

	basin_sizes = list(sorted(basin_sizes, reverse=True))

	return functools.reduce(operator.mul, basin_sizes[:3], 1)

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
