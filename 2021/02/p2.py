# 2021/xx/p1.py

import time


def parse_line(line):
	split = line.strip().split(' ')

	return split[0], int(split[1])

def execute(input_file):
	with open(input_file, 'r') as f:
		entries = map(parse_line, f.readlines())

	horizontal = 0
	aim = 0
	depth = 0

	for command, val in entries:
		if command == 'forward':
			horizontal += val
			depth += val * aim
		elif command == 'down':
			aim += val
		else:
			aim -= val

	return horizontal * depth

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
