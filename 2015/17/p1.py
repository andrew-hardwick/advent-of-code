# 20xx/xx/p1.py

import itertools
import time


def parse_input(infn):
	with open(infn, 'r') as f:
		data = [int(str.strip(l)) for l in f.readlines()]

	return list(sorted(data))


def count_valid_combinations(
		source,
		target,
		level,
		start_index,
		selected):
	total = sum(selected)

	if total > target:
		return [], True

	valid_children = []

	for i, v in enumerate(source[start_index:]):
		new_valid_children, limit = count_valid_combinations(source, target, level + 1, start_index + i + 1, selected + [ v ])

		if limit:
			break

		valid_children.extend(new_valid_children)

	if total == target:
		valid_children.append(level)

	return valid_children, False


def execute(
		infn,
		eggnog):
	source = parse_input(infn)

	valid_cases, _ = count_valid_combinations(source, eggnog, 0, 0, [])

	return len(valid_cases)


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
