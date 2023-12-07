# 20xx/xx/p1.py

import time


def splitIntoMaps(
		source):
	maps = []

	current = []

	for line in source:
		if 'map:' in line:
			current = []
		elif len(line) == 0:
			maps.append(current)
		else:
			current.append(line)

	maps.append(current)

	return maps


def parse_input(
		infn,
		seeds_contain_length):
	with open(infn, 'r') as f:
		source = [str.strip(line) for line in f.readlines()]

	seedSource = source[0].split(': ')[1].split(' ')

	seeds = []

	if seeds_contain_length:
		seeds = [(int(s), int(l)) for s, l in zip(seedSource[::2], seedSource[1::2])]		
	else:
		seeds = [(int(s), 1) for s in seedSource]

	mapRaw = source[2:]

	mapSource = splitIntoMaps(mapRaw)

	mapSource = ((e.split(' ') for e in m) for m in mapSource)

	maps = ([(int(e[0]), int(e[1]), int(e[2])) for e in m] for m in mapSource)

	return seeds, maps


def apply_map_entry(
		seed,
		map_entry):
	map_dest, map_start, map_len = map_entry
	map_end = map_start + map_len - 1

	seed_start, seed_len = seed
	seed_end = seed_start + seed_len - 1

	# seed encapsulated inside mapping
	if seed_start >= map_start and seed_end <= map_end:

		new_seed = (seed_start + map_dest - map_start, seed_len)

		return [], [new_seed]

	# mapping encapsulated inside seed
	if seed_start < map_start and seed_end > map_end:

		new_seed_one = (seed_start, map_start - seed_start)
		new_seed_two = (map_dest, map_len)
		new_seed_three = (map_end + 1, seed_end - map_end)

		return [new_seed_one, new_seed_three], [new_seed_two]

	if seed_start < map_start and seed_end <= map_end and seed_end >= map_start:

		new_seed_one = (seed_start, map_start - seed_start)
		new_seed_two = (map_dest, seed_end - map_start + 1)

		return [new_seed_one], [new_seed_two]

	if seed_start >= map_start and seed_end > map_end and seed_start <= map_end:

		new_seed_one = (seed_start + map_dest - map_start, map_end - seed_start + 1)
		new_seed_two = (map_end + 1, seed_end - map_end)

		return [new_seed_two], [new_seed_one]


	return [seed], []

def apply_map(
		seeds,
		mapping):
	result_seeds = []
	new_seeds = []

	for map_entry in mapping:
		for seed in seeds:
			raw, transformed = apply_map_entry(seed, map_entry)

			new_seeds.extend(raw)
			result_seeds.extend(transformed)

		seeds = new_seeds
		new_seeds = []

	result_seeds.extend(seeds)

	return result_seeds


def test_apply_map():

	seed = (10, 4)

	for i in range(6):
		map_entry = (50, 7 + i, 2)

		result = apply_map_entry(seed, map_entry)

		print(map_entry, seed, result)


def execute(
		infn,
		seeds_contain_length):
	seeds, maps = parse_input(infn, seeds_contain_length)

	for m in maps:
		seeds = apply_map(seeds, m)

	result = min(s for s, l in seeds)

	return result


def main(
		infn,
		seeds_contain_length):
	pre = time.perf_counter()

	result = execute(infn, seeds_contain_length)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('test1.txt', False)
	main('input.txt', False)
