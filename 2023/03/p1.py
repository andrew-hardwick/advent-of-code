# 20xx/xx/p1.py

import time


def parse_input(
		infn):
	with open(infn, 'r') as f:
		source = (str.strip(line) for line in f.readlines())

	number_locs = []
	gear_locs = []
	symbol_locs = []

	for line_index, line in enumerate(source):
		parsing_number = False
		number_start_index = 0

		for char_index, char in enumerate(line):
			if char.isdigit():
				if not parsing_number:
					number_start_index = char_index

					parsing_number = True
			else:
				if parsing_number:
					number = int(line[number_start_index:char_index])

					number_locs.append((line_index, number_start_index, char_index - number_start_index - 1, number))

				parsing_number = False

				if char == '*':
					gear_locs.append((line_index, char_index))
					symbol_locs.append((line_index, char_index))
				elif char != '.':
					symbol_locs.append((line_index, char_index))

		if parsing_number:
			number = int(line[number_start_index:])
			number_locs.append((line_index, number_start_index, len(line) - number_start_index - 1, number))

	return number_locs, gear_locs, symbol_locs


def check_adjacent(
		number_loc,
		symbol_loc):
	number_line_index, number_start, number_length, number = number_loc
	symbol_line_index, symbol_char_index = symbol_loc

	number_end = number_start + number_length

	if abs(number_line_index - symbol_line_index) > 1:
		return False

	# overlapped
	if number_start <= symbol_char_index and symbol_char_index <= number_end:
		return True

	# edges
	if number_start - symbol_char_index == 1:
		return True

	if symbol_char_index - number_end == 1:
		return True

	return False


def execute(
		infn):
	number_locs, gear_locs, symbol_locs = parse_input(infn)

	result = 0

	for number_loc in number_locs:
		adjacent = False

		for symbol_loc in symbol_locs:
			adjacent |= check_adjacent(number_loc, symbol_loc)

		if adjacent:
			result += number_loc[3]

	return result


def main(
		infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('input.txt')
