# 20xx/xx/p1.py

import time

import numpy as np


def parse_ingredient(
	line):
	line = line.strip()
	line = line.replace(':', '')
	line = line.replace(' capacity', '')
	line = line.replace(', durability', '')
	line = line.replace(', flavor', '')
	line = line.replace(', texture', '')
	line = line.replace(', calories', '')

	split = line.split(' ')

	ingredient = {}

	ingredient['name'] = split[0]
	ingredient['properties'] = np.array([int(p) for p in split[1:]])

	return ingredient

def parse_input(infn):
	with open(infn, 'r') as f:
		data = [parse_ingredient(l) for l in f.readlines()]

	return data

def get_max_properties(
		ingredients):
	max_properties = []

	for ingredient in ingredients:
		for index, prop in enumerate(ingredient['properties']):
			if index >= len(max_properties):
				max_properties.append(prop)
			else:
				max_properties[index] = max(max_properties[index], prop)

	return max_properties

def identify_upper_limit(
		ingredients,
		max_properties,
		absolute_limit):
	for ingredient in ingredients:
		ingredient['upper_limit'] = absolute_limit
		for index, prop in enumerate(ingredient['properties']):
			if prop < 0:
				offset_count_per = -prop / max_properties[index]

				total_count_per = offset_count_per + 1

				instance_count = int(100 / total_count_per)

				ingredient['upper_limit'] = min(ingredient['upper_limit'], instance_count)


def calculate_value(
		calorie_target,
		ingredient_counts,
		ingredients):
	total = np.zeros(len(ingredients[0]['properties']))

	for i, c in enumerate(ingredient_counts):
		total += ingredients[i]['properties'] * c

	scores = np.array([t if t > 0 else 0 for t in list(total)[:-1]])

	if calorie_target != -1 and total[-1] != 500:
		return 0

	return int(np.product(scores))


def find_optimal_value(
		budget,
		selected_ingredients,
		level,
		level_limit,
		ingredients,
		calorie_target):
	if level == len(ingredients):
		return calculate_value(calorie_target, selected_ingredients + [ budget ], ingredients)

	absolute_limit = budget - (level_limit - level)
	ingredient_limit = ingredients[level - 1]['upper_limit']

	limit = min(absolute_limit, ingredient_limit)

	return max(find_optimal_value(budget - count, selected_ingredients + [ count ], level + 1, level_limit, ingredients, calorie_target) for count in range(1, limit + 1))


def execute(
		infn,
		calorie_target,
		absolute_limit):
	ingredients = parse_input(infn)

	max_properties = get_max_properties(ingredients)

	identify_upper_limit(ingredients, max_properties, absolute_limit)

	result = find_optimal_value(absolute_limit, [], 1, len(ingredients), ingredients, calorie_target)

	return result

def main(
		infn,
		calorie_target,
		absolute_limit):
	pre = time.perf_counter()

	result = execute(infn, calorie_target, absolute_limit)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt', -1, 100)
	main('input.txt', -1, 100)
