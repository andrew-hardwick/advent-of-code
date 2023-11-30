# 20xx/xx/p1.py

import time


def parse_line(
		line):
	line = line.strip()

	return [1 if c == '#' else 0 for c in line]

def parse_input(
		infn):
	with open(infn, 'r') as f:
		data = [parse_line(l) for l in f.readlines()]

	return data


def print_board(
		board):
	print()
	for line in board:
		for c in line:
			print('#' if c == 1 else '.', end='')
		print()
	print()


def cell_step(
		board,
		board_dim,
		i,
		j,
		fixed_corners):
	if fixed_corners:
		if i == 0 and j == 0:
			return 1
		if i == 0 and j == board_dim - 1:
			return 1
		if i == board_dim - 1 and j == 0:
			return 1
		if i == board_dim - 1 and j == board_dim - 1:
			return 1

	x_lower_limit = -1
	x_upper_limit = 2

	y_lower_limit = -1
	y_upper_limit = 2

	if i == 0:
		x_lower_limit = 0
	if i == board_dim - 1:
		x_upper_limit = 1
	if j == 0:
		y_lower_limit = 0
	if j == board_dim - 1:
		y_upper_limit = 1

	neighbor_sum = 0

	for x in range(x_lower_limit, x_upper_limit):
		for y in range(y_lower_limit, y_upper_limit):
			if x == 0 and y == 0:
				continue
			neighbor_sum += board[x + i][y + j]

	current = board[i][j]

	if current == 1 and (neighbor_sum == 2 or neighbor_sum == 3):
		return 1
	if current == 0 and neighbor_sum == 3:
		return 1
	return 0


def step(
		board,
		board_dim,
		fixed_corners):
	result = []

	for i in range(board_dim):
		result.append([])

		for j in range(board_dim):
			result[i].append(cell_step(board, board_dim, i, j, fixed_corners))

	return result

def turn_on_corners(
		board,
		board_dim):
	board[0][0] = 1
	board[0][board_dim - 1] = 1
	board[board_dim - 1][0] = 1
	board[board_dim - 1][board_dim - 1] = 1

	return board

def get_lights_on_count(
		board):
	total = 0

	for line in board:
		total += sum(line)

	return total


def execute(
		infn,
		step_count,
		fixed_corners):
	board = parse_input(infn)

	board_dim = len(board)

	if fixed_corners:
		board = turn_on_corners(board, board_dim)

	for _ in range(step_count):
		board = step(board, board_dim, fixed_corners)

	return get_lights_on_count(board)


def main(
		infn,
		step_count,
		fixed_corners):
	pre = time.perf_counter()

	result = execute(infn, step_count, fixed_corners)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('test1.txt', 4, False)
	main('input.txt', 100, False)
