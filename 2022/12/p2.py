# 2022/12/p2.py

import functools
import time

from p1 import parse_input, find_shortest_path


def is_complete_f(end, height_map, current):
	x, y = current

	return height_map[y][x] == 1

def execute(infn):
	_, end, edges, vertices, height_map = parse_input(infn, 2, False)

	is_complete = functools.partial(is_complete_f, _, height_map)

	shortest_path = find_shortest_path(end, edges, vertices, is_complete)

	return len(shortest_path) - 1

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
