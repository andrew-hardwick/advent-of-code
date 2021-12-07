# 2021/xx/p2.py

import time


def parse_line(line):
	return line.strip()

def execute(input_file):

	with open(input_file, 'r') as f:
		entries = list(map(parse_line, f.readlines()))

	# do the thing
	result = 0

	return result

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
