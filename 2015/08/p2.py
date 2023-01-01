# 2021/xx/p1.py

import time


def parse_input(infn):
	with open(infn, 'r') as f:
		entries = [str.strip(l) for l in f.readlines()]
	return entries

def execute(infn):
	data = parse_input(infn)

	# do the thing

	return '??'

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
