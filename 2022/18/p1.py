# 20xx/xx/p1.py

from collections import deque
import time


def prune_for_adjacency(cubes):
	cube_keys = list(cubes.keys())

	for i, a in enumerate(cube_keys):
		for b in cube_keys[i + 1:]:
			xa, ya, za = a
			xb, yb, zb = b

			d_x = xa - xb
			d_y = ya - yb
			d_z = za - zb

			if d_y == 0 and d_z == 0:
				if d_x == -1:
					cubes[a] = cubes[a] & 0b101111
					cubes[b] = cubes[b] & 0b011111
				elif d_x == 1:
					cubes[a] = cubes[a] & 0b011111
					cubes[b] = cubes[b] & 0b101111

			if d_x == 0 and d_z == 0:
				if d_y == -1:
					cubes[a] = cubes[a] & 0b111011
					cubes[b] = cubes[b] & 0b110111
				elif d_y == 1:
					cubes[a] = cubes[a] & 0b110111
					cubes[b] = cubes[b] & 0b111011

			if d_x == 0 and d_y == 0:
				if d_z == -1:
					cubes[a] = cubes[a] & 0b111110
					cubes[b] = cubes[b] & 0b111101
				elif d_z == 1:
					cubes[a] = cubes[a] & 0b111101
					cubes[b] = cubes[b] & 0b111110

def parse_input(infn):
	with open(infn, 'r') as f:
		data = dict([(tuple([int(i) for i in l.split(',')]), 63) for l in f.readlines()])

	return data

def execute(infn):
	cubes = parse_input(infn)

	prune_for_adjacency(cubes)

	return sum((v.bit_count() for v in cubes.values()))

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
