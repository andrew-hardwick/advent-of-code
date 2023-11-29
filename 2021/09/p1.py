# 2021/09/p1.py

import itertools
import time


def get_risk_level_if_low_point(source, cell, max_x, max_y):
	x, y = cell

	val = source[x][y]

	adjacent_count = 0

	if not x == 0:
		adjacent_count += 1
		if val >= source[x - 1][y]:
			val = -1
	if not x == max_x:
		adjacent_count += 1
		if val >= source[x + 1][y]:
			val = -1
	if not y == 0:
		adjacent_count += 1
		if val >= source[x][y - 1]:
			val = -1
	if not y == max_y:
		adjacent_count += 1
		if val >= source[x][y + 1]:
			val = -1

	return (val + 1, adjacent_count)

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

	computed = [get_risk_level_if_low_point(source, cell, max_x, max_y) for cell in cells]

	risk_levels = [r for r, a in computed]

	adjacent_counts = [a for r, a in computed]

	return sum(risk_levels)

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
