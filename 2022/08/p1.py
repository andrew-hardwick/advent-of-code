# 2022/08/p1.py

import time


def calculate_visible(forest_map):
	side = len(forest_map)

	# this function requires that the input be square
	assert(side == len(forest_map[0]))

	north_max = [-1] * side
	south_max = [-1] * side
	east_max = [-1] * side
	west_max = [-1] * side

	north_visible = [[1 for x in range(side)] for y in range(side)]
	south_visible = [[1 for x in range(side)] for y in range(side)]
	east_visible = [[1 for x in range(side)] for y in range(side)]
	west_visible = [[1 for x in range(side)] for y in range(side)]

	# north / south
	for y in range(side):
		for x in range(side):
			height = forest_map[y][x]

			if north_max[x] < height:
				north_max[x] = height
			else:
				north_visible[y][x] = 0

			south_y = side - y - 1

			height = forest_map[south_y][x]

			if south_max[x] < height:
				south_max[x] = height
			else:
				south_visible[south_y][x] = 0

	# east / west
	for x in range(side):
		for y in range(side):
			height = forest_map[y][x]

			if west_max[y] < height:
				west_max[y] = height
			else:
				west_visible[y][x] = 0

			east_x = side - x - 1

			height = forest_map[y][east_x]

			if east_max[y] < height:
				east_max[y] = height
			else:
				east_visible[y][east_x] = 0

	visible = [[0 for x in range(side)] for y in range(side)]

	for y in range(side):
		for x in range(side):
			visible[y][x] = north_visible[y][x] | south_visible[y][x] | east_visible[y][x] | west_visible[y][x]

	return visible

def print_map(forest_map):
	print('\n')

	for y in range(len(forest_map)):
		line = ''
		for x in range(len(forest_map[y])):
			line += str(forest_map[y][x])
		print(line)

	print('\n')

def parse_input(infn):
	with open(infn, 'r') as f:
		forest_map = [[int(e) for e in str.strip(l)] for l in f.readlines()]

	return forest_map

def execute(infn):
	forest_map = parse_input(infn)

	visible_map = calculate_visible(forest_map)

	return sum([sum(e) for e in visible_map])

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
