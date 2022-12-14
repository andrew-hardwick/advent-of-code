# 2022/13/p2.py

import functools
import json
import time

from p1 import validate_pair, parse_input


def a_precedes_b(a, b):
	return 1 if validate_pair(a, b)[0] else 0

def execute(infn):
	packets = parse_input(infn)

	a = [[2]]
	b = [[6]]

	precede_a = sum((a_precedes_b(p, a) for p in packets))
	precede_b = sum((a_precedes_b(p, b) for p in packets))

	# adding 1 to both for indexing reasons
	# adding an additional 1 to 'b' to account for 'a'
	return (precede_a + 1) * (precede_b + 2)

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')