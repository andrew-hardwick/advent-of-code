# 20xx/xx/p1.py

from collections import deque
import math
import time


def parse_input(infn):
	with open(infn, 'r') as f:
		data = [-1 if c == '<' else 1 for c in f.readline().strip()]

	return deque(data)

def parse_rock(rock_source):
	rock = [int(r) for r in rock_source.strip().split(',')]

	return rock

def get_width(rock):
	max_width = 0

	for row in set(rock):
		width = 1

		while (1 << width) - 1 < row:
			width += 1

		if width > max_width:
			max_width = width

	return width

def get_rocks():
	with open('rock_lookup', 'r') as f:
		rocks = [parse_rock(r) for r in f.readlines()]

	rocks = [(rock, get_width(rock), len(rock)) for rock in rocks]

	return deque(rocks)

def get_initial_board():
	return [127]

def is_collided(board, rock, x, y):
	for i, row in enumerate(rock):
		if board[y + i] & row << x:
			return True

	return False

def cement_rock(board, rock, x, y):
	for i, row in enumerate(rock):
		board[y + i] = board[y + i] | row << x

def find_highest_rock(board):
	for i, row in enumerate(board):
		if row > 0:
			return i

	# unreachable with correct initialization
	return -1

def process_turn(board, rocks, jets, rock_index, jet_index, seen):
	rock, width, height = rocks[0]
	rocks.rotate(-1)
	rock_index += 1

	space_required = (height + 3) - find_highest_rock(board)

	if space_required > 0:
		for _ in range(space_required):
			board.insert(0, 0)

	x = 5 - width
	y = 0 if space_required > 0 else -space_required

	prev_x = x
	prev_y = y

	while True:
		# Horizontal Movement
		jet = jets[0]
		jets.rotate(-1)
		jet_index += 1

		if jet_index >= len(jets):
			jet_index = 0

		prev_x = x
		x -= jet

		if x < 0:
			x = 0
		if x + width > 7:
			x = 7 - width

		if is_collided(board, rock, x, y):
			x = prev_x

		# Vertical Movement
		prev_y = y
		y += 1

		if is_collided(board, rock, x, y):
			y = prev_y
			break

	cement_rock(board, rock, x, y)

	highest_rock = find_highest_rock(board)

	if len(board) > 15 + highest_rock:
		key = (rock_index, jet_index, sum([board[i + highest_rock] << (i * 7) for i in range(15)]))
	else:
		key = 0

	return key, len(board) - highest_rock - 1

def print_board(board, rock, height, rock_x, rock_y):
	floor = len(board) - 1

	for i, row in enumerate(board):
		if not rock_y == None and i >= rock_y and i < rock_y + height:
			row_str = ''.join(['#' if (1 << (6 - j) & row) else '@' if (1 << (6 - j) & (rock[i - rock_y] << rock_x)) else '.' for j in range(7)])
			print('|'+row_str+'|')
		elif i < floor:
			row_str = ''.join(['#' if (1 << (6 - j) & row) else '.' for j in range(7)])
			print('|'+row_str+'|')
		else:
			print('+_______+')

def execute(infn, width, target_rock_count):
	jets = parse_input(infn)
	rocks = get_rocks()
	board = get_initial_board()

	simulation_length = math.lcm(len(jets), len(rocks)) * 25

	partial = target_rock_count % simulation_length

	multiple = int(target_rock_count / simulation_length) - 1

	rock_index = -1
	jet_index = -1

	seen = {}
	heights = {}

	count = 0

	while True:
		key, height = process_turn(board, rocks, jets, rock_index, jet_index, seen)

		count += 1

		if key in seen.keys():
			break
		elif not key == 0:
			seen[key] = (height, count)
			heights[count] = height

	start_height, start_count = seen[key]

	period_height = height - start_height

	target_rock_count_without_start = target_rock_count - start_count

	period_length = count - start_count

	num_periods = int(target_rock_count_without_start / period_length)

	residual_count = target_rock_count_without_start % period_length

	residual_height = heights[residual_count + start_count] - heights[start_count]

	return start_height + period_height * num_periods + residual_height

def main(infn, width, target_rock_count):
	pre = time.perf_counter()

	result = execute(infn, width, target_rock_count)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt', 7, 2022)
	main('input.txt', 7, 2022)
