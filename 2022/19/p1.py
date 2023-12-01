# 20xx/xx/p1.py

import time

import numpy as np


def parse_blueprint(
		line):
	line = line.split(': ')[1]

	line = line.replace(' ore', ' ')
	line = line.replace(' clay', ' ')
	line = line.replace(' geode', ' ')
	line = line.replace(' obsidian', ' ')

	line = line.replace('Each  robot costs', '')
	line = line.replace(' and', '')
	line = line.replace('.', '')
	line = line.replace('  ', ' ')
	line = line.replace('  ', ' ')

	line = line.strip()
	
	costsource = line.split(' ')

	costs = [int(c) for c in costsource]

	ore_cost = np.zeros(4)
	ore_cost[0] = costs[0]

	clay_cost = np.zeros(4)
	clay_cost[0] = costs[1]

	obsidian_cost = np.zeros(4)
	obsidian_cost[0] = costs[2]
	obsidian_cost[1] = costs[3]

	geode_cost = np.zeros(4)
	geode_cost[0] = costs[4]
	geode_cost[2] = costs[5]

	blueprint = np.stack([ore_cost, clay_cost, obsidian_cost, geode_cost]).astype(int)

	return blueprint
	

def parse_input(
		infn):
	with open(infn, 'r') as f:
		blueprints = [parse_blueprint(line) for line in f.readlines()]

	return blueprints

def maximize_geodes(
		blueprint,
		time_limit):
	max_robots = blueprint.max(axis=0).astype(int)
	max_robots[3] = 10000

	print(blueprint)
	print(max_robots)
	print()

	state = {
		'time_left': time_limit,
		'robots': np.array([1, 0, 0, 0]).astype(int),
		'resources': np.zeros(4).astype(int)
	}

	max_geodes = 0

	possibilties = [state]

	while len(possibilties) > 0:
		state = possibilties.pop(0)

		if state['resources'][3] > max_geodes:
			print(state)

		max_geodes = max(max_geodes, state['resources'][3])

		# print(len(possibilties))

		# print(state)

		# some number of disqualifications
		if state['time_left'] == 0:
			continue

		# add states for actions
		for i in range(4):
			if state['robots'][i] < max_robots[i] and all(state['resources'] >= blueprint[i]):
				# print('buying a', i)
				next_state = state.copy()
				next_state['time_left'] -= 1
				next_state['resources'] = state['resources'] - blueprint[i] + state['robots']
				next_state['robots'][i] += 1

				possibilties.append(next_state)

		# add null state
		next_state = state.copy()
		next_state['time_left'] -= 1
		next_state['resources'] = state['resources'] + state['robots']

		possibilties.append(next_state)

	print(max_geodes)

	return max_geodes

def execute(
		infn):
	blueprints = parse_input(infn)

	geodes = [maximize_geodes(blueprint, 10) for blueprint in blueprints]

	quality = [i * g for i, g in enumerate(geodes)]

	result = sum(quality)

	return result


def main(
		infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('test1.txt')

