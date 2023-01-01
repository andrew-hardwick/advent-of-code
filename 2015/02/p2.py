# 2021/xx/p1.py

import math
import time

from p1 import parse_input


def calculate_ribbon(d):
	wrap = 2 * sum(d[1:])

	bow = math.prod(d)

	return wrap + bow

def execute(infn):
	dimensions = parse_input(infn)

	ribbon_per_package = [calculate_ribbon(d) for d in dimensions]

	return sum(ribbon_per_package)

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
