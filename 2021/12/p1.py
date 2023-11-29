# 2021/12/p1.py

import time


class node_t():
	def __init__(self, name, small_cave_passage_count):
		self._name = name
		self.neighbors = []
		self._small_cave_double_passage_allowed_count = small_cave_passage_count
		self._small_cave = name == name.lower()

	def __str__(self):
		joiner = "','"
		if len(self.neighbors) > 0:
			return f"{self._name} -- {self._allowable_visits} -- ['{joiner.join([n._name for n in self.neighbors])}']"
		else:
			return f'{self._name} -- {self._allowable_visits} -- []'

	def add_adjacent(self, adjacent_node):
		self.neighbors.append(adjacent_node)

	def valid_target(self, past, nodes):
		proposed = past + [self._name]
		small_caves = [p for p in proposed if nodes[p]._small_cave]

		if self._name == 'start':
			return False

		return  not self._small_cave or len(small_caves) - len(set(small_caves)) <= self._small_cave_double_passage_allowed_count


def parse_and_create_nodes(edges, small_cave_passage_count):
	edges = [tuple(e.split('-')) for e in edges]

	node_names = set([n for e in list(zip(*edges)) for n in e])

	edges = edges + [(b, a) for a, b in edges]

	nodes = {}

	for name in node_names:
		nodes[name] = node_t(name, small_cave_passage_count)

	for a, b in edges:
		nodes[a].add_adjacent(nodes[b])

	return nodes

def find_valid_paths(past, start, end, nodes):
	if start == end:
		return [[end._name]]

	current = past + [start._name]

	future = []

	for n in start.neighbors:
		if n.valid_target(current, nodes):
			future.extend([[start._name] + p for p in find_valid_paths(current, n, end, nodes)])

	return future

def execute(input_file):
	with open(input_file, 'r') as f:
		edges = [str.strip(l) for l in f.readlines()]

	nodes = parse_and_create_nodes(edges, 0)

	start = nodes['start']
	end = nodes['end']

	paths = find_valid_paths([], start, end, nodes)

	return len(paths)

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt') # 10
	main('test2.txt') # 19
	main('test3.txt') # 226
	main('test4.txt') # 2
	main('input.txt')
