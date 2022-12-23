# 20xx/xx/p1.py

from collections import deque
import time


def parse_cell(cell_source):
	if cell_source == ' ':
		return 0
	elif cell_source == '.':
		return 1
	elif cell_source == '#':
		return 2

def parse_instructions(inst_source):
	inst_source = inst_source.replace('R', ' R ').replace('L', ' L ').split(' ')

	inst_length = len(inst_source)

	num_moves = int(inst_length / 2) + (1 if not inst_length % 2 == 0 else 0)
	num_turns = int(inst_length / 2)

	moves = [int(inst_source[i * 2]) for i in range(num_moves)]
	turns = [-1 if inst_source[(i * 2) + 1] == 'L' else 1 for i in range(num_turns)]

	return moves, turns

def parse_board(board_source):
	initial_board =  [[parse_cell(c) for c in row] for row in board_source]

	max_length = max(len(row) for row in initial_board)

	final_board = [row + ([0] * (max_length - len(row))) for row in initial_board]

	return final_board

def parse_input(infn):
	with open(infn, 'r') as f:
		source = [l.replace('\n', '') for l in f.readlines()]

	board = parse_board(source[:-2])

	instructions = parse_instructions(source[-1])

	return board, instructions

def move_within_limit(start, delta, upper_limit):
	result = start + delta

	if result < 0:
		result = upper_limit
	if result > upper_limit:
		result = 0

	return result

def perform_move(board, position, direction, move, limits):
	x, y = position
	d_x, d_y = direction
	x_limit, y_limit = limits

	for _ in range(move):
		c_x = move_within_limit(x, d_x, x_limit)
		c_y = move_within_limit(y, d_y, y_limit)

		if board[c_y][c_x] == 2:
			# print('running into rock')
			return x, y

		while board[c_y][c_x] == 0:
			# print('phantom zone')
			c_x = move_within_limit(c_x, d_x, x_limit)
			c_y = move_within_limit(c_y, d_y, y_limit)

			if board[c_y][c_x] == 2:
				# print('running into rock')
				return x, y

		x = c_x
		y = c_y

	return x, y

def get_initial_player_position(board, directions):

	return x, y, facing

def walk(board, instructions):
	moves, turns = instructions

	directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

	y_limit = len(board) - 1
	x_limit = len(board[0]) - 1

	limits = (x_limit, y_limit)

	x = board[0].index(1)
	y = 0
	facing = 0

	# print('initial')
	# print(x, y, facing, directions[facing])
	# print()

	while True:
		if len(moves) == 0:
			break

		move = moves.pop(0)

		x, y = perform_move(board, (x, y), directions[facing], move, limits)

		# print('moved:', move)
		# print(x, y, facing, directions[facing])
		# print()

		if len(turns) == 0:
			break

		turn = turns.pop(0)

		facing = move_within_limit(facing, turn, 3)

		# print('turned', turn)
		# print(x, y, facing, directions[facing])
		# print()

	return x + 1, y + 1, facing

def print_board(board):
	for row in board:
		line = ''

		for cell in row:
			if cell == 0:
				line += 'O'
			elif cell == 1:
				line += '.'
			elif cell == 2:
				line += '#'

		print(line)

def execute(infn):
	board, instructions = parse_input(infn)

	#print_board(board)

	column, row, facing = walk(board, instructions)

	# do the thing
	result = row * 1000 + column * 4 + facing

	return result

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
