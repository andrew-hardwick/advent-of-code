# 2021/xx/p2.py

import time


def execute(infn):
	with open(infn, 'r') as f:
		entries = [str.strip(l) for l in f.readlines()]

	# do the thing

	return 0

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
