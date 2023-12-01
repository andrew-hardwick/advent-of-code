# 2021/xx/p1.py

import time

import numpy


def parse_input(infn):
	direction_map = {
		'<': numpy.array([-1, 0]),
		'^': numpy.array([0, 1]),
		'>': numpy.array([1, 0]),
		'v': numpy.array([0, -1])
	}

	with open(infn, 'r') as f:
		steps = [direction_map[c] for c in f.read().strip()]

	return steps


def walk(steps):
	location = numpy.array([0, 0])

	visited = set()
	visited.add(tuple(location))

	for step in steps:
		location = location + step

		visited.add(tuple(location))

	return visited


def execute(infn):
	steps = parse_input(infn)

	visited = walk(steps)

	return len(visited)


def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')


if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')

