# 2021/xx/p1.py

import time


def parse_line(line):
	split = line.strip().split(' ')

	command = split[0]
	val = int(split[1])

	if command == 'forward':
		return (0, val)
	elif command == 'down':
		return (val, 0)
	else:
		return (-val, 0)

def execute(input_file):
	with open(input_file, 'r') as f:
		entries = map(parse_line, f.readlines())

	hori = 0
	vert = 0
	aim = 0

	for d_aim, d_hori in entries:
		aim += d_aim
		hori += d_hori
		vert += aim * d_hori

	return hori * vert

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
