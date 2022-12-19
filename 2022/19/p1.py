# 2022/19/p1.py

import re
import time


def parse_line(line):
	numbers = [int(i) for i in re.findall(r'\d+', line)]

	ore_cost = [numbers[1], 0, 0, 0]
	clay_cost = [numbers[2], 0, 0, 0]
	obsidian_cost = [numbers[3], numbers[4], 0, 0]
	geode_cost = [0, numbers[5], numbers[6], 0]

	return ore_cost, clay_cost, obsidian_cost, geode_cost

def parse_input(infn):
	with open(infn, 'r') as f:
		costs = [parse_line(l) for l in f.readlines()]

	return costs

def calculate_unit_benefit(costs):

	# calculate how much each producer contributes to making 1 geode



	return [2 ** i for i in range(4)]

def calculate_mat_fractions(mats, costs):
	return [[mats[j] / costs[i][j] if not costs[i][j] == 0 else 1 for j in range(4)] for i in range(4)]

def simulate(costs, time_limit):
	ore_cost, clay_cost, obsidian_cost, geode_cost = costs

	producers = [1, 0, 0, 0]
	mats = [0, 0, 0, 0]

	unit_benefits = calculate_unit_benefit(costs)

	for _ in range(time_limit):
		new_mats = [i for i in producers]

		unable_to_purchase = False

		while not unable_to_purchase:
			mat_fractions = calculate_mat_fractions(mats, costs)

			buy_rating = [(unit_benefits[i], i) for i in range(4) if all([mat_fractions[i][j] >= 1 for j in range(4)])]

			buy_rating = sorted(buy_rating, reverse=True)

			if len(buy_rating) == 0:
				unable_to_purchase = True
				continue

			fraction_of_target, target_index = buy_rating[0]

			mats = [mats[i] - costs[target_index][i] for i in range(4)]
			producers[target_index] += 1

		mats = [mats[i] + new_mats[i] for i in range(4)]

		print(_, mats, producers, unit_benefits)

def execute(infn, time_limit):
	costs = parse_input(infn)

	optimal_results = [simulate(cost, time_limit) for cost in costs]

	return '??'

def main(infn, time_limit):
	pre = time.perf_counter()

	result = execute(infn, time_limit)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt', 24)
	#main('input.txt')
