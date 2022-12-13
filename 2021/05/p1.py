# 2021//p1.py

import time


def parse_coords(line):
	return list(map(int, line.replace(' -> ', ',').split(',')))

def add_point(point_counts, point):
	if not point in point_counts:
		point_counts[point] = 0
	else:
		point_counts[point] = 1

def print_board(point_counts):
	board = [0] * 10

	for i in range(10):
		board[i] = ['.'] * 10

	for p in point_counts:
		board[p[0]][p[1]] = str(point_counts[p] + 1)

	for line in zip(*board):
		print(''.join(line))

def add_orthogonal(point_counts, constant, start, stop, direction):
	for dynamic in range(start, stop):
		point = (constant, dynamic) if direction else (dynamic, constant)

		add_point(point_counts, point)

def execute(input_file):
	with open(input_file, 'r') as f:
		entries = list(map(str.strip, f.readlines()))

	coords = list(map(parse_coords, entries))

	point_counts = {}

	for x1, y1, x2, y2 in coords:
		xs = [x1, x2]
		ys = [y1, y2]
		# horizontal
		if x1 == x2:
			add_orthogonal(point_counts, x1, min(ys), max(ys) + 1, True)
		# vertical
		elif y1 == y2:
			add_orthogonal(point_counts, y1, min(xs), max(xs) + 1, False)


	return sum(point_counts.values())

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
