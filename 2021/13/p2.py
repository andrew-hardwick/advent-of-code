# 2021/xx/p1.py

import time

from p1 import parse_input, execute_fold


def print_dots(dots):
	max_x = max([x for x, y in dots]) + 1
	max_y = max([y for x, y in dots]) + 1

	print('\n')

	for y in range(max_y):
		line = ''
		for x in range(max_x):
			if (x, y) in dots:
				line += '#'
			else:
				line += '.'
		print(line)

	print('\n')

def execute(infn):
	dots, instructions = parse_input(infn)

	for instruction in instructions:
		dots = execute_fold(dots, instruction)

	print_dots(dots)

	return 0

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
