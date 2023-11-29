# 2022/02/execute.py

import time


def parse_table_entry(line):
	split = line.strip().split(',')

	return split[0], int(split[1])

def parse_input(infn):
	with open(infn, 'r') as f:
		source = (str.strip(l) for l in f.readlines())
	return source

def execute(lkpfn, infn):
	with open(lkpfn, 'r') as f:
		lookup = dict([parse_table_entry(l) for l in f.readlines()])

	games = parse_input(infn)

	return sum([lookup[g] for g in games])

def main(lkpfn, infn):
	pre = time.perf_counter()

	result = execute(lkpfn, infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('part_1_lookup', 'test1.txt')
	main('part_2_lookup', 'test1.txt')
	main('part_1_lookup', 'input.txt')
	main('part_2_lookup', 'input.txt')