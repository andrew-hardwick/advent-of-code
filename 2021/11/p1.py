# 2021/11/p1.py

import functools
import itertools
import time


def print_board(max_x, board):
	print('\n')
	for x in range(max_x + 1):
		print(''.join([str(e) for e in board[x]]))
	print('\n')

def evaluate_step(all_octopi, surrounding, max_x, max_y, board):
	evaluated_flashes = set()
	non_evaluated_flashes = set()

	for octopus in all_octopi:
		x, y = octopus

		board[x][y] += 1

		if board[x][y] > 9:
			non_evaluated_flashes.add(octopus)


	while len(non_evaluated_flashes) > 0:
		current_flash = non_evaluated_flashes.pop()

		x, y = current_flash

		for d_x, d_y in surrounding:
			c_x, c_y = (x + d_x, y + d_y)

			if c_x >= 0 and c_x <= max_x and c_y >= 0 and c_y <= max_y:
				board[c_x][c_y] += 1

				if board[c_x][c_y] > 9 and (c_x, c_y) not in evaluated_flashes:
					non_evaluated_flashes.add((c_x, c_y))

		evaluated_flashes.add(current_flash)

	for x, y in all_octopi:
		if board[x][y] > 9:
			board[x][y] = 0

	return len(evaluated_flashes)

def execute(input_file):
	with open(input_file, 'r') as f:
		lines = [str.strip(l) for l in f.readlines()]

	board = [[int(e) for e in l] for l in lines]

	max_x = len(board) - 1
	max_y = len(board[0]) - 1

	step_count = 100

	flash_total = 0

	all_octopi = list(itertools.product(range(max_x + 1), range(max_y + 1)))
	surrounding = list(itertools.product(range(-1, 2), range(-1, 2)))
	surrounding = [s for s in surrounding if not s == (0, 0)]

	func_evaluate_step = functools.partial(evaluate_step, all_octopi, surrounding, max_x, max_y)

	for i in range(step_count):
		flash_total += func_evaluate_step(board)

	return flash_total

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('test2.txt')
	main('input.txt')
