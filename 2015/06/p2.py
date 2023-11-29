# 2021/xx/p1.py

import time

from p1 import parse_input, decorate


def execute(infn):
	instructions = parse_input(infn)

	ops = {
		'toggle': lambda x: x + 2,
		'off': lambda x: x - 1 if x > 0 else 0,
		'on': lambda x: x + 1
	}

	light_grid = decorate(instructions, ops)

	return int(sum(sum(light_grid)))

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('input.txt')
