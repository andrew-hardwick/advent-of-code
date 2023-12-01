# 2021/xx/p1.py

import itertools
import time


def parse_line(line):
	return sorted([int(d) for d in line.split('x')], reverse=True)


def parse_input(infn):
	with open(infn, 'r') as f:
		entries = [parse_line(line) for line in f.readlines()]

	return entries


def calculate_paper(d):
	sides = [x * y for x, y in itertools.combinations(d, 2)]

	return sum([2 * s for s in sides]) + min(sides)


def execute(infn):
	dimensions = parse_input(infn)

	paper_per_package = [calculate_paper(d) for d in dimensions]

	return sum(paper_per_package)


def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')


if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')

