# 2022/01/p2.py

import time

from p1 import parse_input


def execute(infn):
	elves = parse_input(infn)

	totals = sorted([sum(e) for e in elves], reverse=True)

	return sum(totals[:3])

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
