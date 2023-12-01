# 2021/xx/p1.py

import time

from p1 import op_node_t, get_ops, parse_input


def execute(infn, target):
	node_map = parse_input(infn)

	ops = get_ops()

	node_map['b'] = op_node_t([node_map[target].get_value(node_map)], ops['MONAD'], 'MONAD')

	for n in node_map.keys():
		node_map[n].reset()

	return node_map[target].get_value(node_map)


def main(infn, target):
	pre = time.perf_counter()

	result = execute(infn, target)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')


if __name__ == '__main__':
	main('test1.txt', 'd')
	main('input.txt', 'a')

