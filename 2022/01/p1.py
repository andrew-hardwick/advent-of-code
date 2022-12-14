# 2022/01/p1.py

import itertools
import time


def parse_input(infn):
	with open(infn, 'r') as f:
		source = (str.strip(l) for l in f.readlines())

	elves = (list(elf) for empty, elf in itertools.groupby(source, key=lambda x: x == '') if not empty)

	return ((int(i) for i in e) for e in elves)

def execute(infn):
	elves = parse_input(infn)

	totals = [sum(e) for e in elves]

	return max(totals)

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
