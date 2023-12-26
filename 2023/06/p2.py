# 20xx/xx/p2.py

from p1 import parse_input, find_record_breaking_count

import time


def condense_number(
		source):
	return int(''.join([str(i) for i in source]))


def execute(
		infn):
	data = parse_input(infn)

	times, distances = zip(*data)

	time_limit = condense_number(times)
	distance = condense_number(distances)

	return find_record_breaking_count(time_limit, distance)


def main(
		infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('input.txt')

