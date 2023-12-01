# 2021/xx/p1.py

import time

import numpy as np


def parse_line(line):
	line = line.strip()
	line = line.replace('turn ', '')
	line = line.replace(' through ', ',')
	line = line.replace(' ', ',')

	split = line.split(',')

	return split[0], [int(s) for s in split[1:]]


def parse_input(infn):
	with open(infn, 'r') as f:
		instructions = [parse_line(line) for line in f.readlines()]

	return instructions


def decorate(instructions, ops):
	edge_length = 1000

	light_grid = np.zeros((edge_length, edge_length))

	for instruction, (x1, y1, x2, y2) in instructions:
		op = ops[instruction]

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				light_grid[x][y] = op(light_grid[x][y])

	return light_grid


def execute(infn):
	instructions = parse_input(infn)

	ops = {
		'toggle': lambda x: 1 - x,
		'off': lambda x: 0,
		'on': lambda x: 1
	}

	light_grid = decorate(instructions, ops)

	return int(sum(sum(light_grid)))


def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')


if __name__ == '__main__':
	main('input.txt')

