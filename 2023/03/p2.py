# 20xx/xx/p2.py

from p1 import parse_input, check_adjacent

import time


def execute(
		infn):
	number_locs, gear_locs, symbol_locs = parse_input(infn)

	result = 0

	for gear_loc in gear_locs:
		numbers = []

		for number_loc in number_locs:
			if check_adjacent(number_loc, gear_loc):
				numbers.append(number_loc[3])

		if len(numbers) == 2:
			result += numbers[0] * numbers[1]

	return result


def main(
		infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('input.txt')
