# 2021/16/p2.py

import math
import time

from p1 import load_packets, print_packet_tree

def evaluate(packet):
	p_type = packet['type']
	cont = packet['contents']

	if p_type == 4:
		return cont
	elif p_type == 0: # sum
		return sum((evaluate(sub_p) for sub_p in cont))
	elif p_type == 1: # prod
		return math.prod((evaluate(sub_p) for sub_p in cont))
	elif p_type == 2: # min
		return min((evaluate(sub_p) for sub_p in cont))
	elif p_type == 3: # max
		return max((evaluate(sub_p) for sub_p in cont))
	elif p_type == 5: # greater than
		return 1 if evaluate(cont[0]) > evaluate(cont[1]) else 0
	elif p_type == 6: # less than
		return 1 if evaluate(cont[0]) < evaluate(cont[1]) else 0
	elif p_type == 7: # equal to
		return 1 if evaluate(cont[0]) == evaluate(cont[1]) else 0

	return 0

def execute(infn):
	packets = load_packets(infn)

	results = (evaluate(p) for p in packets)

	if len(results) == 1:
		return results[0]
	else:
		return results

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test2.txt')
	main('input.txt')
