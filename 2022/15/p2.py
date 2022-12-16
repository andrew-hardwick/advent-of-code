# 2022/15/p2.py

import itertools
import math
import time

from p1 import parse_input, mh_dist

def is_tile_enclosed(tile, sensors):
	x, y, r_t = tile

	p_t = (x, y)

	for p_s, r_s in sensors:
		dist = mh_dist(p_t, p_s)

		if r_t == 0:
			#print(tile, p_s, r_s)
			pass
		if mh_dist(p_t, p_s) <= r_s - r_t:

			return True

	return False

def is_tile_offgrid(min_lim, max_lim, tile):
	x, y, r = tile

	min_x = x - r
	max_x = x + r
	min_y = y - r
	max_y = y + r

	if min_x > max_lim or max_x < min_lim or min_y > max_lim or max_y < min_lim:
		return True
	return False

def tesselate_tile(tile):
	x, y, r = tile

	if r == 0:
		return []
	if r == 1:
		r = 0
	else:
		if not r % 2 == 0:
			r += 1

		r = int(r / 2)

	offset_base = r

	if not offset_base % 2 == 0:
		offset_base -= 1
	if offset_base == 0:
		offset_base = 1

	offsets = [(0, 0), (offset_base, 0), (-offset_base, 0), (0, offset_base), (0, -offset_base)]

	new_points = [(x + a, y + b, r) for a, b in offsets]

	#print('adding ', new_points)

	return new_points

def tesselate_grid(min_lim, max_lim, linear_count):
	tile_width = int((max_lim - min_lim) / linear_count)

	if tile_width % 2 == 0:
		tile_width += 1

	r = int(tile_width / 2)

	oc_indices = range(min_lim, max_lim + 1, tile_width - 1)
	ic_indices = range(min_lim + r, max_lim + 1, tile_width - 1)

	oc_tiles = [(x, y, r) for x in oc_indices for y in oc_indices]
	ic_tiles = [(x, y, r) for x in ic_indices for y in ic_indices]

	return oc_tiles + ic_tiles

def parse_simple_line(line):
	nums = [int(i) for i in line.split(',')]

	return (nums[0], nums[1]), nums[2]

def parse_simple_input(infn):
	with open(infn, 'r') as f:
		result = [parse_simple_line(l) for l in f.readlines()]

	return result

def execute(infn, max_lim):
	data = parse_input(infn)

	min_lim = 0

	sensors = [(a, mh_dist(a, b)) for a, b in data]

	sensors = list(sorted(sensors, key=lambda x: x[1], reverse=True))

	tiles = tesselate_grid(min_lim, max_lim, 32)

	while len(tiles) > 0:
		tile = tiles.pop()
		x, y , r = tile

		if is_tile_offgrid(min_lim, max_lim, tile):
			# do nothing
			continue
		elif is_tile_enclosed(tile, sensors):
			# do nothing
			continue
		else:
			tiles.extend(tesselate_tile(tile))

			if r == 0:
				last_good_tile = tile

	x, y, r = last_good_tile

	return x * 4000000 + y

def main(infn, max_lim):
	pre = time.perf_counter()

	result = execute(infn, max_lim)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	#main('test1.txt', 20)
	#main('test2.txt', 20)
	main('input.txt', 4000000)
