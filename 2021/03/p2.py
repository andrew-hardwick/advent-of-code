# p2.py

import time


def find_most_used_bit(
	source,
	index):
	total = sum([e[index] for e in source])
	target = (len(source) / 2)

	return total == target, 1 if total > target else 0

def find_least_used_bit(
	source,
	index):
	equal, most_used_bit = find_most_used_bit(source, index)

	return equal, 1 - most_used_bit

def filter(
	source,
	index,
	selector,
	val_if_equal):
	if len(source) > 1:
		equal, result = selector(source, index)
		if not equal:
			return [s for s in source if s[index] == result]
		else:
			return [s for s in source if s[index] == val_if_equal]
	return source

def parse_line(line):
	return list(map(int, line.strip()))

def execute(input_file):
	with open(input_file, 'r') as f:
		entries = list(map(parse_line, f))

	ox_source = entries.copy()
	scr_source = entries.copy()

	for index, c in enumerate(entries[0]):
		ox_source = filter(ox_source, index, find_most_used_bit, 1)
		scr_source = filter(scr_source, index, find_least_used_bit, 0)

	# binary conversion
	a = int(''.join(map(str, ox_source[0])), 2)
	b = int(''.join(map(str, scr_source[0])), 2)

	return a * b

def main(input_file):
	start = time.perf_counter()

	result = execute(input_file)

	end = time.perf_counter()

	print(result, f'in {(end - start) * 1000} ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')