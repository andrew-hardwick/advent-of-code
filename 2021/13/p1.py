# 2021/xx/p1.py

import time


def parse_input(infn):
	with open(infn, 'r') as f:
		lines = [str.strip(l) for l in f.readlines()]

	split_index = next(i for i, v in enumerate(lines) if v == '')

	dots = [tuple([int(i) for i in l.split(',')]) for l in lines[:split_index]]
	instructions = [tuple([int(i) for i in l.replace('fold along ', '').replace('x','0').replace('y','1').split('=')]) for l in lines[split_index + 1:]]

	return dots, instructions

def execute_fold(dots, instruction):
	fold_axis, fold_index = instruction

	if fold_axis == 0:
		dots = [(x, y) if x < fold_index else (2 * fold_index -x, y) for x, y in dots]
	else:
		dots = [(x, y) if y < fold_index else (x, 2 * fold_index - y) for x, y in dots]

	return set(dots)

def execute(infn):
	dots, instructions = parse_input(infn)

	dots = execute_fold(dots, instructions[0])

	return len(dots)

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
