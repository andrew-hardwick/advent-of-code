# 20xx/xx/p1.py

import math
import time


def parse_numbers_from_line(
		line):
	number_source = line.split(':')[1].strip()

	while '  ' in number_source:
		number_source = number_source.replace('  ', ' ')

	return [int(n) for n in number_source.split(' ')]

def parse_input(
		infn):
	with open(infn, 'r') as f:
		time_source, distance_source = [str.strip(line) for line in f.readlines()]

	times = parse_numbers_from_line(time_source)
	distances = parse_numbers_from_line(distance_source)    

	return zip(times, distances)


def find_record_breaking_count(
		time_limit,
		distance):
	discriminant = time_limit ** 2 - 4 * distance

	root_discriminant = discriminant ** 0.5

	lower_bound = math.floor((time_limit - root_discriminant) / 2)
	upper_bound = math.ceil((time_limit + root_discriminant) / 2)

	return upper_bound - lower_bound - 1


def execute(
		infn):
	data = parse_input(infn)

	result = 1

	for time_limit, distance in data:
		count = find_record_breaking_count(time_limit, distance)

		result *= count

	return result


def main(
		infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('input.txt')

