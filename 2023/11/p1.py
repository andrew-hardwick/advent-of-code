# 20xx/xx/p1.py

import itertools
import time


def parse_input(
		infn):
	with open(infn, 'r') as f:
		data = [str.strip(line) for line in f.readlines()]

	result = []

	width = len(data[0]) # data is assumed to be non-empty and rectangular

	blankColumnCounts = []
	blankColumnCount = 0

	for x in range(width):
		blankColumn = True

		for line in data:
			blankColumn = blankColumn and line[x] != '#'

		if blankColumn:
			blankColumnCount = blankColumnCount + 1

		blankColumnCounts.append(blankColumnCount)


	blankRowCount = 0
	for y, line in enumerate(data):
		blankRow = True

		for x, c in enumerate(line):
			blankRow = blankRow and c != '#'

			if c == '#':
				result.append((x, y, blankColumnCounts[x], blankRowCount))

		if blankRow:
			blankRowCount = blankRowCount + 1

	return result


def execute(
		infn,
		expansion_factor):
	data = parse_input(infn)

	pairs = itertools.combinations(data, 2)

	expansion_factor = expansion_factor - 1
	total_distance = 0

	for a, b in pairs:
		a_x, a_y, a_extra_x, a_extra_y = a
		b_x, b_y, b_extra_x, b_extra_y = b

		a_x_total = a_x + (a_extra_x * expansion_factor)
		a_y_total = a_y + (a_extra_y * expansion_factor)

		b_x_total = b_x + (b_extra_x * expansion_factor)
		b_y_total = b_y + (b_extra_y * expansion_factor)

		delta_x = max(a_x_total, b_x_total) - min(a_x_total, b_x_total)
		delta_y = max(a_y_total, b_y_total) - min(a_y_total, b_y_total)

		total_distance += (delta_x + delta_y)

	return total_distance


def main(
		infn,
		expansion_factor):
	pre = time.perf_counter()

	result = execute(infn, expansion_factor)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('input.txt', 2)
