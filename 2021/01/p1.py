# 2021/01/p1.py

import time


def parse_line(line):
	return int(line.strip())

def main(input_file):
	pre = time.perf_counter()

	with open(input_file, 'r') as f:
		entries = map(parse_line, f.readlines())

	last = 0
	count = -1

	for entry in entries:
		if entry > last:
			count += 1
		last = entry

	post = time.perf_counter()
	print(count, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
	