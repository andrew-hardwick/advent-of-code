# 2021/18/p1.py

import json
import time


def max_depth(num):
	if type(num) == int:
		return 0
	else:
		return max((max_depth(c) + 1 for c in num))

def max_value(num):
	if type(num) == int:
		return num
	else:
		return max((max_value(c) for c in num))

def split(num):
	if max_value(num) > 9:
		return False

	num.clear()

	return True

def explode(num):
	result = []

	if max_depth(num) < 5:
		return False

	#blah blah
	num.clear()

	return True


def sfn_add(a, b):
	return [a, b]

def sfn_reduce(num):
	result = num

	while explode(result) or split(result):
		print('exploding or splitting', result)
		return result
		pass

	return result

def execute(infn):
	with open(infn, 'r') as f:
		entries = (json.loads(str.strip(l)) for l in f.readlines())

	result = next(entries)

	for e in entries:
		result = sfn_reduce(sfn_add(result, e))

		print(result, max_depth(result))

	print(result)

	# do the thing

	return 0

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	#main('test2.txt')
	#main('input.txt')
