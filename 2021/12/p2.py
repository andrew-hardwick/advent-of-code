# 2021/12/p1.py

import time

from p1 import parse_and_create_nodes, find_valid_paths


def execute(input_file):
	with open(input_file, 'r') as f:
		edges = [str.strip(l) for l in f.readlines()]

	nodes = parse_and_create_nodes(edges, 1)

	start = nodes['start']
	end = nodes['end']

	paths = find_valid_paths([], start, end, nodes)

	return len(paths)

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt') # 36
	main('test2.txt') # 103
	main('test3.txt') # 3509
	main('test4.txt') # 2
	main('input.txt')
