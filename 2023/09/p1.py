# 20xx/xx/p1.py

import time


def parse_input(
		infn):
	with open(infn, 'r') as f:
		data = ([int(e) for e in line.strip().split(' ')] for line in f.readlines())

	return data


def get_subsequences(
		line):
	at_bottom = False

	result = [line]

	current_sequence = line

	while not at_bottom:
		next_sequence = []

		all_zero = True

		for e1, e2 in zip(current_sequence[:-1], current_sequence[1:]):
			delta = e2 - e1

			all_zero &= delta == 0

			next_sequence.append(delta)

		result.append(next_sequence)
		current_sequence = next_sequence

		at_bottom = all_zero

	return result


def execute(
		infn):
	report = parse_input(infn)

	result = 0

	for line in report:
		subsequences = get_subsequences(line)

		result += sum(e[-1] for e in subsequences)

	return result


def main(
		infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('input.txt')
