# 20xx/xx/p1.py

import time


def parse_input(
		infn):
	with open(infn, 'r') as f:
		data = [str.strip(line) for line in f.readlines()]

	directions = data[0]

	graph_source = data[2:]

	graph = {}

	for line in graph_source:
		line_split = line.split(' = ')

		node = line_split[0]
		children = tuple(line_split[1].replace('(', '').replace(')', '').split(', '))

		graph[node] = children

	return directions, graph


def steps_to_end(
		start,
		directions,
		graph):
	result = 0
	node = start

	while True:
		for c in directions:
			left_child, right_child = graph[node]

			if c == 'L':
				node = left_child
			else:
				node = right_child

			result += 1

			if node[2] == 'Z':
				return result


def execute(
		infn):
	directions, graph = parse_input(infn)

	node = 'AAA'

	return steps_to_end(node, directions, graph)


def main(
		infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('input.txt')
