# p1.py

import time


def parse_line(line):
	return list(map(int, line.strip()))

def execute(input_file):
	with open(input_file, 'r') as f:
		entries = list(map(parse_line, f))

	sums = list(map(sum, zip(*entries)))

	threshold = len(entries) / 2

	a = [1 if cell > threshold else 0 for cell in sums]

	#binary conversion
	a = sum([c << i for i, c in enumerate(reversed(a))])

	b = (2 ** len(entries[0])) - a - 1

	return a * b

def main(input_file):
	start = time.perf_counter()

	result = execute(input_file)

	end = time.perf_counter()

	print(result, f'in {(end - start) * 1000} ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')