# 2021/15/p1.py

import heapq
import time


def print_map(map_data, route):
	x_limit = len(map_data)
	y_limit = len(map_data[0])

	print('\n')

	for y in range(y_limit):
		line = ''

		for x in range(x_limit):
			if (x, y) in route or map_data[x][y] > 9:
				line += ' '
			else:
				line += str(map_data[x][y])

		print(line)

	print('\n')

def guess(start, end):
	return abs(start[0] - end[0]) + abs(start[1] - end[1])

def reconstruct_path(came_from, current):
	path = [current]

	while current in came_from:
		current = came_from[current]
		path.insert(0, current)

	return path

def a_star(map_data, start, goal, allowed_moves):
	start_guess = guess(start, goal)

	max_x, max_y = goal

	open_set = [(start_guess, start)]

	came_from = {}

	g_score = {}
	g_score[start] = 0

	f_score = {}
	f_score[start] = start_guess

	while len(open_set) > 0:
		_, current = heapq.heappop(open_set)

		if current == goal:
			return reconstruct_path(came_from, current), g_score[current]

		neighbors = [tuple(map(lambda a,b: a+b, current, p)) for p in allowed_moves]

		for neighbor in neighbors:
			n_x, n_y = neighbor

			if n_x >= 0 and n_y >= 0 and n_x <= max_x and n_y <= max_y:
				tent_g_score = g_score[current] + map_data[n_x][n_y]
				if neighbor not in g_score or tent_g_score < g_score[neighbor]:
					came_from[neighbor] = current
					g_score[neighbor] = tent_g_score

					neighbor_guess = guess(neighbor, goal)
					f_score[neighbor] = tent_g_score + neighbor_guess

					neighbor_entry = (f_score[neighbor], neighbor)

					if neighbor_entry not in open_set:
						heapq.heappush(open_set, neighbor_entry)

def tile_map(map_data, tile_count):
	x_extension = [[e + i for i in range(tile_count) for e in row] for row in map_data]

	y_extension = [[e + i for e in row] for i in range(tile_count) for row in x_extension]

	# hack for limits, won't work if tiled more than 8-9 times
	y_extension = [[e if e < 10 else e - 9 for e in row] for row in y_extension]

	return y_extension

def execute(infn, tile_count):
	with open(infn, 'r') as f:
		map_data = [[int(i) for i in str.strip(l)] for l in f.readlines()]

	map_data = tile_map(map_data, tile_count)

	start = (0, 0)
	end = (len(map_data[0]) - 1, len(map_data) - 1)

	allowed_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

	path, minimum_path_length = a_star(map_data, start, end, allowed_moves)

	return minimum_path_length

def main(infn, tile_count):
	pre = time.perf_counter()

	result = execute(infn, tile_count)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt', 1)
	main('input.txt', 1)
