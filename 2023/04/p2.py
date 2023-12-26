# 20xx/xx/p2.py

from p1 import parse_input, score_cards

import time


def execute(
		infn):
	cards = parse_input(infn)

	scores = score_cards(cards)

	card_counts = [1 for _ in scores]

	result = 0

	for index, score in enumerate(scores):
		total_card_score = card_counts[index]

		result += total_card_score

		for i in range(score):
			card_counts[index + i + 1] += total_card_score

	return result


def main(
		infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('input.txt')
