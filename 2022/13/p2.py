# 2022/13/p2.py

import functools
import json
import time

from p1 import validate_pair, parse_input


def compare_pair(a, b):
	return 1 if validate_pair(a, b)[0] else -1

def execute(infn):
	packets = parse_input(infn)

	a = [[2]]
	b = [[6]]

	packets.append(a)
	packets.append(b)

	key_func = functools.cmp_to_key(compare_pair)

	sorted_packets = sorted(packets, key=key_func, reverse=True)

	a_i = sorted_packets.index(a) + 1
	a_b = sorted_packets.index(b) + 1

	return a_i * a_b

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')