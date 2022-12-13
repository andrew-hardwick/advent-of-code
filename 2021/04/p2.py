# 2021/04/p1.py

import time



def evaluate_board(board):
	accumulators = [0] * 10

	for i in range(5):
		for j in range(5):
			accumulators[i] += board[i][j]
			accumulators[5 + i] += board[j][i]

	return min(accumulators) == 0

def check_boards_for_win(boards):
	found_win = False
	winning_boards = []

	for board in boards:
		if evaluate_board(board):
			winning_boards.append(board)
			found_win = True

	return found_win, winning_boards

def handle_draw(
	draw,
	boards):
	for board in boards:
		for line in board:
			if draw in line:
				index = line.index(draw)

				line[index] = 0

def print_board(board):
	for line in board:
		print('  '.join(map(str, line)))

def print_boards(boards):
	for board in boards:
		print('')
		print_board(board)
		print('')

def parse_input(lines):
	draw_order = list(map(int, lines[0].split(',')))

	board_source = lines[2:]

	boards = []
	working_board = []

	for line in board_source:
		if line == '':
			boards.append(working_board)
			working_board = []
		else:
			working_board.append(list(map(int, line.split(' '))))

	boards.append(working_board)

	return draw_order, boards

def parse_line(line):
	return line.strip().replace('  ', ' ')

def execute(input_file):
	with open(input_file, 'r') as f:
		entries = list(map(parse_line, f.readlines()))

	draw_order, boards = parse_input(entries)

	for draw in draw_order:
		handle_draw(draw, boards)

		win_exists, winning_boards = check_boards_for_win(boards)

		if win_exists:
			if len(boards) == 1:
				winning_board = winning_boards[0]
				break

			for board in winning_boards:
				boards.remove(board)

	return sum(map(sum, winning_board)) * draw

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')