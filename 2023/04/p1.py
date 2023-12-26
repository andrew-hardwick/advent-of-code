# 20xx/xx/p1.py

import time


def split_into_length_3_substrings(
		line):
	return set([line[i:i + 3] for i in range(0, len(line), 3)])


def parse_card(
		line):
	number_source = line.strip().split(':')[1]

	winning_numbers, owned_numbers = number_source.split(' |')

	winning_numbers = split_into_length_3_substrings(winning_numbers)
	owned_numbers = split_into_length_3_substrings(owned_numbers)

	return winning_numbers, owned_numbers


def parse_input(
		infn):
	with open(infn, 'r') as f:
		cards = [parse_card(line) for line in f.readlines()]

	return cards


def score_cards(
		cards):
	return [len(winning & owned) for winning, owned in cards]


def execute(
		infn):
	cards = parse_input(infn)

	scores = score_cards(cards)

	result = sum([(1 << score - 1) for score in scores if score > 0])

	return result


def main(
		infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('input.txt')
