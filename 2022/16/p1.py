# 2022/16/p1.py

import functools
import heapq
import time


def parse_line(line):
	line = line.strip()
	line = line.replace('Valve ', '')
	line = line.replace(' has flow rate=', ',')
	line = line.replace('tunnels', 'tunnel')
	line = line.replace('valves', 'valve')
	line = line.replace('leads', 'lead')
	line = line.replace('; tunnel lead to valve ', ',')
	line = line.replace(', ', ',')

	split = line.split(',')

	return split[0], split[1], split[2:]

def parse_input(infn):
	with open(infn, 'r') as f:
		data = [parse_line(l) for l in f.readlines()]

	cave_map = {}

	for name, flow, linked in data:
		cave_map[name] = {}
		cave_map[name]['flow'] = int(flow)
		cave_map[name]['linked'] = linked

	return cave_map

def reconstruct_path(prev, end):
	current = end

	path = [current]

	while current in prev.keys():
		current = prev[current]
		path.append(current)

	return path

def find_shortest_path(start, edges, vertices, is_complete):
	dist = {}
	dist[start] = 0

	prev = {}

	max_length = (len(vertices) + 1) ** 2

	unprocessed = []

	for v in vertices:
		if not v == start:
			dist[v] = max_length

		heapq.heappush(unprocessed, (dist[v], v))

	while len(unprocessed) > 0:
		_, u = heapq.heappop(unprocessed)

		if is_complete(u):
			return reconstruct_path(prev, u)

		for v in edges[u]:
			alt = dist[u] + 1

			if alt < dist[v]:
				dist[v] = alt
				prev[v] = u

				# adjust distance in heap (and reheap the heap)
				unprocessed = [(d, unp) if not unp == v else (alt, v) for d, unp in unprocessed]
				heapq.heapify(unprocessed)

	return vertices

def complete_when_reached_room(target, current):
	return target == current

def find_paths_to_targets_from_room(current, valid_targets, cave_edges, cave_vertices):
	linked = []

	for target in valid_targets:
		if target == current:
			continue

		is_complete = functools.partial(complete_when_reached_room, target)
		path_to_other_room = find_shortest_path(current, cave_edges, cave_vertices, is_complete)

		linked.append((target, len(path_to_other_room) - 1))

	return sorted(linked)

def process_map(cave_map):
	rooms_with_flow = [k for k in cave_map.keys() if not cave_map[k]['flow'] == 0]

	cave_edges = dict([(k, cave_map[k]['linked']) for k in cave_map.keys()])
	cave_vertices = list(cave_map.keys())

	new_map = {}

	for room in rooms_with_flow:
		new_map[room] = {}
		new_map[room]['flow'] = cave_map[room]['flow']
		new_map[room]['linked'] = dict(find_paths_to_targets_from_room(room, rooms_with_flow, cave_edges, cave_vertices))
		new_map[room]['available'] = list(new_map[room]['linked'].keys())

	return new_map, rooms_with_flow, cave_edges, cave_vertices

def find_best_path(past, past_flow, length_limit, current, minute, time_limit, cave_map):
	if past == ['BB']:
		linked = cave_map[current]['linked']
		available = cave_map[current]['available']

		print('available: ', available)

	if minute > time_limit:
		return past, past_flow

	if len(past) > length_limit:
		return past, past_flow

	linked = cave_map[current]['linked']

	next_past = past + [current]
	next_minute = minute

	flow = past_flow

	if current not in past:
		flow_time = time_limit - next_minute - 1

		if flow_time < 0:
			flow_time = 0

		flow += cave_map[current]['flow'] * flow_time
		next_minute += 1

	next_steps = [find_best_path(next_past, flow, length_limit, link, next_minute + linked[link], time_limit, cave_map) for link in cave_map[current]['available'] if link not in past and link in linked]

	if len(next_steps) == 0:
		return next_past, flow

	return max(next_steps, key=lambda s: s[1])

def execute(infn):
	cave_map = parse_input(infn)

	cave_map, rooms_with_flow, cave_edges, cave_vertices = process_map(cave_map)

	paths_from_AA = dict(find_paths_to_targets_from_room('AA', rooms_with_flow, cave_edges, cave_vertices))

	paths = [find_best_path(['AA'], 0, len(rooms_with_flow), next_edge, paths_from_AA[next_edge], 30, cave_map) for next_edge in paths_from_AA.keys()]

	return max([flow for path, flow in paths])

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
