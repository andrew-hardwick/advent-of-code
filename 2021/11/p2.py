# 2021/11/p1.py

import functools
import itertools
import time

from p1 import evaluate_step


def execute(input_file):
	with open(input_file, 'r') as f:
		lines = [str.strip(l) for l in f.readlines()]

	board = [[int(e) for e in l] for l in lines]

	max_x = len(board) - 1
	max_y = len(board[0]) - 1

	all_octopi = list(itertools.product(range(max_x + 1), range(max_y + 1)))
	surrounding = list(itertools.product(range(-1, 2), range(-1, 2)))
	surrounding = [s for s in surrounding if not s == (0, 0)]

	func_evaluate_step = functools.partial(evaluate_step, all_octopi, surrounding, max_x, max_y)

	synchronous_count = (max_x + 1) * (max_y + 1)

	step_count = 1

	while(func_evaluate_step(board) < synchronous_count):
		step_count += 1

	return step_count

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
