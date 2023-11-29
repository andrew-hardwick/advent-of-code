# 2022/14/p1.py

import time


def parse_input(infn, insert_floor):
	with open(infn, 'r') as f:
		data = (str.strip(l) for l in f.readlines())

	rock_paths = [[tuple([int(i) for i in n.split(',')]) for n in l.split(' -> ')] for l in data]

	rocks = []

	for rock_path in rock_paths:
		lines = zip(rock_path[:-1], rock_path[1:])

		for (x1, y1), (x2, y2) in lines:
			if x1 == x2:
				y_s = [y1, y2]
				min_y = min(y_s)
				max_y = max(y_s)
				rocks.extend([(x1, y) for y in range(min_y, max_y + 1)])
			else:
				x_s = [x1, x2]
				min_x = min(x_s)
				max_x = max(x_s)
				rocks.extend([(x, y1) for x in range(min_x, max_x + 1)])

	rocks = list(set(rocks))

	y = list(set(y for x, y in rocks))

	max_y = max(y)
	min_x = -max_y - 10
	max_x = max_y + 11
	grid = [[1 if (x + 500, y) in rocks else 0 for x in range(min_x, max_x)] for y in range(0, max_y + 4)]

	if insert_floor:
		for x in range(min_x, max_x):
			grid[max_y + 2][x] = 1

	return grid, max_y + 2, min_x

def simulate_sand(grid, source, y_limit):
	current_x, current_y = source

	stopped = False

	while current_y <= y_limit:
		next_possibilities = [(current_x + x, current_y + 1) for x in [0, -1, 1]]

		moved_to_next_y = False

		for x, y in next_possibilities:
			if grid[y][x] == 0:
				current_x = x
				current_y = y
				moved_to_next_y = True
				break

		if not moved_to_next_y:
			grid[current_y][current_x] = 2
			return not (current_x, current_y) == source

	return False

def pretty_print(grid, fn):
	lines = []
	for row in grid:
		line = ''
		for e in row:
			if e == 1:
				line += '#'
			elif e == 2:
				line += 'O'
			else:
				line += ' '
		lines.append(line)

	with open(fn, 'w') as f:
		f.write('\n'.join(lines))

def execute(infn, insert_floor):
	grid, y_limit, min_x = parse_input(infn, insert_floor)

	source = (-min_x, 0)

	while simulate_sand(grid, source, y_limit):
		pass

	flat_grid = [e for row in grid for e in row]

	sand_filtered = [1 if fg == 2 else 0 for fg in flat_grid]

	return sum(sand_filtered)

def main(infn, insert_floor):
	pre = time.perf_counter()

	result = execute(infn, insert_floor)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt', False)
	main('input.txt', False)
