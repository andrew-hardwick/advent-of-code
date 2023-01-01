# 2021/xx/p1.py

import time


def parse_input(infn):
	with open(infn, 'r') as f:
		data = [1 if c == '(' else -1 for c in f.read().strip()]

	return data

def execute(infn):
	data = parse_input(infn)

	result = sum(data)

	return result

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('input.txt')
