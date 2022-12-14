# 2022/04/p1.py

import time


def parse_line(line):
	split = (s.split('-') for s in line.split(','))

	sections = ((int(s[0]), int(s[1])) for s in split)

# sort so that the smaller section is always first in the sublists
	sections = sorted(sections, key=lambda x: x[1] - x[0])

	return sections

def parse_input(infn):
	with open(infn, 'r') as f:
		sections = (parse_line(l) for l in f.readlines())

	return sections

def execute(infn):
	sections = parse_input(infn)

	return sum([a[0] >= b[0] and a[1] <= b[1] for a, b in sections])

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
