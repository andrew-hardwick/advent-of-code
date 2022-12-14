# 2022/05/p2.py

import time

from p1 import parse_input, get_top_of_each_column_on_board


def execute_instruction(board, instruction):
	count, source, dest = instruction

	crane = []

	for i in range(count):
		crane.append(board[source - 1].pop())

	for i in range(count):
		board[dest - 1].append(crane.pop())

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
