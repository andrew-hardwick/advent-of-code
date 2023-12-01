# 2021/xx/p1.py

import time

from p1 import parse_input, walk


def execute(infn):
	steps = parse_input(infn)

	santa_steps = steps[0::2]
	robot_steps = steps[1::2]

	all_visited = walk(santa_steps) | walk(robot_steps)

	return len(all_visited)


def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')


if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')

