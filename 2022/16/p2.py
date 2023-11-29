# 2022/16/p2.py

import itertools
import time

from p1 import parse_input, process_map, find_paths_to_targets_from_room, find_best_path

def execute(infn):
	cave_map = parse_input(infn)

	cave_map, rooms_with_flow, cave_edges, cave_vertices = process_map(cave_map)

	paths_from_AA = dict(find_paths_to_targets_from_room('AA', rooms_with_flow, cave_edges, cave_vertices))

	combinations_for_me = []

	width = 0

	for i in range(int(len(rooms_with_flow) / 2) - width, int(len(rooms_with_flow) / 2) + 1):
		combinations_for_me.extend([list(x) for x in itertools.combinations(rooms_with_flow, i)])

	print(len(combinations_for_me))

	max_flow = 0

	for i, combination_for_me in enumerate(combinations_for_me):
		if i % 100 == 0:
			print('processed', i, 'items')

		combination_for_elephant = [r for r in rooms_with_flow if r not in combination_for_me]

		for my_room in combination_for_me:
			cave_map[my_room]['available'] = combination_for_me

		for elephant_room in combination_for_elephant:
			cave_map[elephant_room]['available'] = combination_for_elephant

		my_paths = [find_best_path(['AA'], 0, len(combination_for_me), next_edge, paths_from_AA[next_edge], 26, cave_map) for next_edge in combination_for_me]
		elephant_paths = [find_best_path(['AA'], 0, len(combination_for_elephant), next_edge, paths_from_AA[next_edge], 26, cave_map) for next_edge in combination_for_elephant]

		flow = max([flow for path, flow in my_paths]) + max([flow for path, flow in elephant_paths])

		if flow > max_flow:
			max_flow = flow

	# do the thing
	result = 0

	return max_flow

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
