# 2022/05/p1.py

import time


def parse_input(infn):
	with open(infn, 'r') as f:
		lines = [line.replace('\n', '').replace('\r', '') for line in f.readlines()]

	split_index = next(i for i, v in enumerate(lines) if v == '')

	board_source = lines[:split_index - 1]
	instructions = lines[split_index + 1:]

	# parse board
	board_count = len(lines[split_index - 1].replace(' ', ''))

	required_width = board_count * 4 + 1
	board_source = [br.ljust(required_width) for br in board_source]

	board_source = list(reversed(board_source))

	board = []

	for i in range(board_count):
		board.append([])

	for board_row in board_source:
		parsed_row = [board_row[(i * 4) + 1] for i in range(board_count)]

		for i in range(board_count):
			if not parsed_row[i] == ' ':
				board[i].append(parsed_row[i])

	# parse instructions
	instructions = [i.replace('move ', '').replace('from ', '').replace('to ', '') for i in instructions]
	instructions = [[int(e) for e in i.split(' ')] for i in instructions]

	return board, instructions

def execute_instruction(board, instruction):
	count, source, dest = instruction

	for i in range(count):
		board[dest - 1].append(board[source - 1].pop())

def get_top_of_each_column_on_board(board):
	return ''.join([br.pop() for br in board])

def execute(infn):
	board, instructions = parse_input(infn)

	for instruction in instructions:
		execute_instruction(board, instruction)

	return get_top_of_each_column_on_board(board)

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
