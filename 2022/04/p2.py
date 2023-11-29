# 2022/04/p2.py

import time

from p1 import parse_input


def execute(infn):
	sections = parse_input(infn)

	overlap = ((a[0] <= b[0] and a[1] >= b[0]) or (b[0] <= a[0] and b[1] >= a[0]) for a, b in sections)

	return sum(overlap)

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
