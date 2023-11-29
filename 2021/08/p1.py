# 2021/08/p1.py

import time

def check_qualify(entry):
	valid_lengths = [2, 3, 4, 7]

	return len(entry) in valid_lengths

def execute(input_file):
	with open(input_file, 'r') as f:
		lines = [str.strip(line).split(' | ') for line in f.readlines()]

	outputs = (' '.join([l[1] for l in lines])).split(' ')

	validity = [check_qualify(entry) for entry in outputs]

	return sum(validity)

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
