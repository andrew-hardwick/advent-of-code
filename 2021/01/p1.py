# 2021/01/p1.py

import time


def parse_line(line):
	return int(line.strip())

def execute(input_file):
	with open(input_file, 'r') as f:
		entries = list(map(parse_line, f.readlines()))

	return sum([a > b for a, b in zip(entries[1:], entries[:-1])])

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
	