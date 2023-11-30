# 20xx/xx/p2.py

import time

from p1 import parse_target_sue_info, parse_input


def identify_matching_sue(
		target,
		candidates):
	for sue, attributes in candidates.items():
		found = True
		for ak, av in attributes.items():
			if ak == 'cats' or ak == 'trees':
				found &= av > target[ak]
			if ak == 'pomeranians' or ak == 'goldfish':
				found &= av < target[ak]
			else:
				found &= av == target[ak]

		if found:
			return sue


def execute(
		suefn,
		infn):
	target_sue_info = parse_target_sue_info(suefn)

	candidates = parse_input(infn)

	return identify_matching_sue(target_sue_info, candidates)


def main(
		suefn,
		infn):
	pre = time.perf_counter()

	result = execute(suefn, infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('sue_info.txt', 'input.txt')
