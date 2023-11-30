# 2021/xx/p1.py

import time


def parse_input(infn):
	with open(infn, 'r') as f:
		entries = [str.strip(l) for l in f.readlines()]
	return entries

def count_actual_chars(line):
	working_line = line[1:-1]

	working_line = working_line.replace('\\"', ' ')

	working_line = working_line.replace('\\\\', ' ')

	len_before_special_chars = len(working_line)

	working_line = working_line.replace('\\x', '')

	len_after_special_chars = len(working_line)

	special_chars_removed = int((len_before_special_chars - len_after_special_chars) / 2)

	len_after_special_chars -= special_chars_removed

	return len(line), len_after_special_chars

def execute(infn):
	data = parse_input(infn)

	counts = [count_actual_chars(line) for line in data]

	return sum(b - a for b, a in counts)

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('input.txt')

