# 2022/03/p1.py

import time


def parse_line(line):
	line = line.strip()

	half_len = int(len(line) / 2)

	fh = set(line[:half_len])
	sh = set(line[half_len:])

	intersection = ord(list(fh & sh)[0])

	if intersection >= 65 and intersection <= 91:
		# 'A' is 65 but we want it to be 27 so we subtract (65 - 27)->38
		priority = intersection - 38
	else:
		# 'a' is 97 but we want it to be 1 so we subtract (97 - 1)->96
		priority = intersection - 96

	return priority

def parse_input(infn):
	with open(infn, 'r') as f:
		source = (parse_line(l) for l in f.readlines())

	return source

def execute(infn):
	priorities = parse_input(infn)

	return sum(priorities)

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
