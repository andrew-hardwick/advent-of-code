# 2022/18/p2.py

from collections import deque
import time

import numpy as np

from p1 import parse_input


def get_max(cubes):
	x, y, z = zip(*cubes)

	return max(max(x), max(y), max(z))

def calculate_surface_area(cubes):
	limit = get_max(cubes)
	length = limit + 3
	lengths = (length, length, length)

	internal = np.zeros(lengths)
	external = np.zeros(lengths)

	for x, y, z in cubes.keys():
		internal[x + 1, y + 1, z + 1] = 1

	unprocessed = set([(0, 0, 0)])
	external[(0, 0, 0)] = 1

	dirs = [(x - 1, y - 1, z - 1) for x in range(3) for y in range(3) for z in range(3)]
	dirs = [d for d in dirs if sum(abs(e) for e in d) == 1]

	surface_area = 0

	while len(unprocessed) > 0:
		examining = unprocessed.pop()

		next_voxels = [tuple([sum(x) for x in zip(examining, dir)]) for dir in dirs]

		for voxel in next_voxels:
			if any([a < 0 or a >= length for a in voxel]):
				continue

			if external[voxel]:
				continue

			if internal[voxel]:
				surface_area += 1
				continue

			external[voxel] = 1
			unprocessed.add(voxel)

	print_body(external, length)

	return surface_area

def print_body(volume, length):
	print()
	for i in range(length):
		print_slice(volume[i], length)
		print()

def print_slice(slice, length):
	for i in range(length):
		line = '   '
		for j in range(length):
			line += '#' if slice[i, j] == 1 else ' '
		print(line)

def execute(infn):
	cubes = parse_input(infn)

	return calculate_surface_area(cubes)

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	#main('test2.txt')
	#main('test3.txt')
	#main('test4.txt')
	main('input.txt')
