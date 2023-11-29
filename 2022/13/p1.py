# 2022/13/p1.py

import itertools
import json
import time


def validate_pair(a, b):
	if type(a) == int and type(b) == int:
		return a < b, a == b

	elif type(a) == list and type(b) == list:
		result = False, True

		index = 0
		while(result[0] == False and result[1] == True):
			if index >= len(b) and index >= len(a):
				return False, True
			elif index >= len(b):
				return False, False
			elif index >= len(a):
				return True, False

			result = validate_pair(a[index], b[index])
			index += 1

		return result
	elif type(a) == list and type(b) == int:
		return validate_pair(a, [b])

	elif type(a) == int and type(b) == list:
		return validate_pair([a], b)

	# unreachable
	return False, False

def parse_input(infn):
	with open(infn, 'r') as f:
		packet_source = (str.strip(l) for l in f.readlines())

	return [json.loads(p) for p in packet_source if not p == '']

def execute(infn):
	packets = parse_input(infn)

	packet_pairs = (tuple(packets[i*2:(i*2)+2] for i in range(int(len(packets) / 2))))

	valid = ((i + 1, validate_pair(a, b)[0]) for i, (a, b) in enumerate(packet_pairs))

	valid_indices = (i for i, v in valid if v)

	return sum(valid_indices)

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
