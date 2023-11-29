# 2022/03/p2.py

import functools
import time


uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate_group_indices(base_index, group_size):
	start = base_index * group_size

	return tuple(range(start, group_size + start))

def evaluate_group(source, group_indices):
	groups = [set(source[i]) for i in group_indices]

	intersection = ord(list(functools.reduce(lambda a,b: a & b, groups))[0])

	if intersection >= 65 and intersection <= 91:
		# 'A' is 65 but we want it to be 27 so we subtract (65 - 27)->38
		priority = intersection - 38
	else:
		# 'a' is 97 but we want it to be 1 so we subtract (97 - 1)->96
		priority = intersection - 96

	return priority

def parse_input(infn):
	with open(infn, 'r') as f:
		source = [str.strip(l) for l in f.readlines()]

	return source

def execute(infn, group_size):
	source = parse_input(infn)

	if not len(source) % group_size == 0:
		raise ValueError("Source length is not a multiple of group_size")

	group_count = int(len(source) / group_size)

	indices = (generate_group_indices(i, group_size) for i in range(group_count))

	func = functools.partial(evaluate_group, source)

	priorities = [func(group_indices) for group_indices in indices]

	return sum(priorities)

def main(infn, group_size):
	pre = time.perf_counter()

	result = execute(infn, group_size)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt', 3)
	main('input.txt', 3)
