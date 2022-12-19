# 2022/19/p1.py

import itertools
import re
import time


def parse_line(line):
	numbers = [int(i) for i in re.findall(r'\d+', line)]

	ore_cost = [numbers[1], 0, 0]
	cla_cost = [numbers[2], 0, 0]
	obs_cost = [numbers[3], numbers[4], 0]
	geo_cost = [numbers[5], 0, numbers[6]]

	return ore_cost, cla_cost, obs_cost, geo_cost

def parse_input(infn):
	with open(infn, 'r') as f:
		costs = [parse_line(l) for l in f.readlines()]

	return costs

def calculate_unit_benefit(costs):

	# calculate how much each producer contributes to making 1 geode



	return [2 ** i for i in range(4)]

def calculate_mat_fractions(mats, costs):
	return [[mats[j] / costs[i][j] if not costs[i][j] == 0 else 1 for j in range(4)] for i in range(4)]

def simulate(costs, time_limit, purchase_order, max_geodes, r_geo_count):
	producers = [1, 0, 0, 0]
	materials = [0, 0, 0, 0]

	purchase_index = 0

	new_producer = -1

	for minute in range(time_limit):
		if purchase_index < len(purchase_order):
			purchase = purchase_order[purchase_index]

			if (time_limit - minute) *

			#print('temp', materials, costs, purchase_index, purchase_order, purchase)

			if all(materials[i] >= costs[purchase][i] for i in range(3)):
				new_producer = purchase
				materials = [materials[i] - costs[purchase][i] for i in range(3)] + [materials[3]]
				purchase_index += 1

		materials = [materials[i] + producers[i] for i in range(4)]

		if (24 - minute) * r_geo_count + materials[3] < max_geodes:
			#print('early exit')
			return 0

		#print(minute + 1, producers, new_producer, materials, costs[new_producer])

		if new_producer > -1:
			producers[new_producer] += 1
			new_producer = -1


	return materials[3]

def ordering_valid(order):
	index_1 = order.index(1)
	index_2 = order.index(2)
	index_3 = order.index(3)

	return index_3 > index_2 and index_2 > index_1 and order[-1] == 3

def optimize(costs, time_limit):
	r_ore_cost, r_cla_cost, r_obs_cost, r_geo_cost = costs

	max_geodes = 0
	max_geode_producers = 2

	best_working_geode_purchase = 0

	for r_ore_count in range(0, 2):
		for r_cla_count in range(1, 5):
			for r_obs_count in range(1, 4):
				for r_geo_count in range(max_geode_producers, 5):
					purchases = [1] * r_cla_count + [2] * r_obs_count + [3] * r_geo_count

					if len(purchases) > 12:
						continue

					orderings = list(itertools.permutations(purchases, len(purchases)))

					max_geodes_per_run = 0
					max_order = []

					for order in orderings:
						if ordering_valid(order):
							#print('starting simulation', order, purchases)
							geodes = simulate(costs, time_limit, [0] * r_ore_count + list(order), max_geodes, r_geo_count)

						if geodes > max_geodes_per_run:
							max_order = order
							max_geodes_per_run = geodes

					if max_geodes_per_run > max_geodes:
						max_geodes = max_geodes_per_run
						max_geode_producers = r_geo_count

	return max_geodes

def execute(infn, time_limit):
	costs = parse_input(infn)

	optimal_results = [optimize(cost, time_limit) for cost in costs]

	print(optimal_results)

	return '??'

def main(infn, time_limit):
	pre = time.perf_counter()

	result = execute(infn, time_limit)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt', 24)
	#main('input.txt', 24)
