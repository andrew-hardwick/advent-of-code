# 2022/06/p1.py

import time


def find_first_unique_set(data, window_length):
	for w_s in range(len(data) - (window_length - 1)):
		if len(set(data[w_s:w_s + window_length])) == window_length:
			return w_s + window_length

	return -1

def parse_input(infn):
	with open(infn, 'r') as f:
		data = str.strip(f.readline())

	return data

def execute(infn, window_length):
	data = parse_input(infn)

	return find_first_unique_set(data, window_length)

def main(infn, window_length):
	pre = time.perf_counter()

	result = execute(infn, window_length)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt', 4)
	main('test2.txt', 4)
	main('input.txt', 4)
