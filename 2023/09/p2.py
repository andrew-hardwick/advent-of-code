# 20xx/xx/p2.py

from p1 import parse_input, get_subsequences

import time


def get_left_side(
		subsequence):
	result = 0

	for i, v in enumerate(subsequence):
		if i % 2 == 0:
			result += v[0]
		else:
			result -= v[0]

	return result

def execute(
		infn):
	report = parse_input(infn)

	result = 0

	for line in report:
		subsequences = get_subsequences(line)

		result += get_left_side(subsequences)

	return result


def main(
		infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('input.txt')
