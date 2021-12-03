# p2.py

import time

def convert_list_to_binary(source):
	return sum([c << i for i, c in enumerate(reversed(source))])

def find_most_used_bit(
	source,
	index):
	total = sum([e[index] for e in source])
	target = (len(source) / 2)

	return total == target, 1 if total > target else 0

def parse_line(line):
	return list(map(int, line.strip()))

def execute(input_file):
	with open(input_file, 'r') as f:
		entries = list(map(parse_line, f))

	sums = [0] * len(entries[0])

	ox_source = entries.copy()
	scr_source = entries.copy()

	print('')

	for index, c in enumerate(entries[0]):
		if len(ox_source) > 1:
			# filter down based on this index
			equal, most_used_bit = find_most_used_bit(ox_source, index)
			if not equal:
				print(index, len(ox_source), most_used_bit)
				ox_source = [s for s in ox_source if s[index] == most_used_bit]
			else:
				print(index, len(ox_source), 1)
				ox_source = [s for s in ox_source if s[index] == 1]
		if len(scr_source) > 1:
			# filter down based on this index
			equal, most_used_bit = find_most_used_bit(ox_source, index)
			if not equal:
				least_used_bit = 1 - most_used_bit
				scr_source = [s for s in scr_source if s[index] == least_used_bit]
			else:
				ox_source = [s for s in ox_source if s[index] == 0]

	a = convert_list_to_binary(ox_source[0])
	b = convert_list_to_binary(scr_source[0])

	print('')
	print(len(ox_source))
	print(len(scr_source))

	print(ox_source[0])
	print(scr_source[0])

	print(a, b)

	return a * b


def main(input_file):
	start = time.perf_counter()

	result = execute(input_file)

	end = time.perf_counter()

	print(result, f'in {(end - start) * 1000} ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')