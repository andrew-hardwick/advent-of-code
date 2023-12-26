# 20xx/xx/p2.py

from p1 import parse_input, steps_to_end

import functools
import math
import time


def execute(
		infn):
	directions, graph = parse_input(infn)

	nodes = [k for k in graph.keys() if k[2] == 'A']

	lengths = [steps_to_end(node, directions, graph) for node in nodes]

	return functools.reduce(math.lcm, lengths, 1)


def main(
		infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('input.txt')
