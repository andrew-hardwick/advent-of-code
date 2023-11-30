# 20xx/xx/p2.py

import time

from p1 import parse_input, count_valid_combinations


def execute(
		infn,
		eggnog):
	source = parse_input(infn)

	valid_cases, _ = count_valid_combinations(source, eggnog, 0, 0, [])

	minimum = min(valid_cases)

	return len([c for c in valid_cases if c == minimum])


def main(
		infn,
		eggnog):
	pre = time.perf_counter()

	result = execute(infn, eggnog)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('test1.txt', 25)
	main('input.txt', 150)
