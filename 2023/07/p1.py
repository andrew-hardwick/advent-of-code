# 2023/07/p2.py

import time


def type_hand(
		hand,
		jokers_wild):
	if jokers_wild:
		hand_without_j = [c for c in hand if c != 'J']
		sorted_hand = sorted(hand_without_j)
		wildcard_count = len(hand) - len(hand_without_j)
	else:
		sorted_hand = sorted(hand)
		wildcard_count = 0

	maxCardCount = 0
	differentCards = 0

	previous_card = ' '
	cardCount = 1

	for card in sorted_hand:
		if card != previous_card:
			maxCardCount = max(cardCount, maxCardCount)
			cardCount = 1
			differentCards += 1
		else:
			cardCount += 1
		previous_card = card

	maxCardCount = max(cardCount, maxCardCount) + wildcard_count

	if wildcard_count == 5:
		maxCardCount = 5
		differentCards = 1

	type = 0

	if maxCardCount == 1:     # High Card
		return 1
	if maxCardCount == 2: 
		if differentCards == 4: # One Pair
			return 2
		else:                   # One Pair
			return 3
	if maxCardCount == 3:
		if differentCards == 3: # Three of a Kind
			return 4
		else:                   # Full House
			return 5
	if maxCardCount == 4:
		return 6
	if maxCardCount == 5:
		return 7


def replace_char(
		c,
		jokers_wild):
	if c == 'T':
		return 10
	if c == 'J':
		if jokers_wild:
			return 0
		else:
			return 11
	if c == 'Q':
		return 12
	if c == 'K':
		return 13
	if c == 'A':
		return 14

	return c

def parse_line(
		line,
		jokers_wild):
	line = line.strip()

	hand = line[:5]
	hand_values = [int(replace_char(c, jokers_wild)) for c in hand]
	bid = int(line[5:])
	hand_type = type_hand(hand, jokers_wild)

	return hand, hand_values, bid, hand_type


def parse_input(
		infn,
		jokers_wild):
	with open(infn, 'r') as f:
		data = (parse_line(line, jokers_wild) for line in f.readlines())

	return data


class HandComparator(tuple):
	def __lt__(a, b):
		_0, handA, _1, typeA = a
		_0, handB, _1, typeB = b

		if typeA == None:
			print(handA)

		if typeA != typeB:
			return typeA < typeB

		for cA, cB in zip(handA, handB):
			if cA != cB:
				return cA < cB

		return 0


def execute(
		infn, jokers_wild):
	cards = parse_input(infn, jokers_wild)

	sorted_cards = sorted(cards, key=HandComparator)

	result = 0

	for i, hand_tuple in enumerate(sorted_cards):
		hand, hand_values, bid, type = hand_tuple

		result += (i + 1) * bid

	return result


def main(
		infn, jokers_wild):
	pre = time.perf_counter()

	result = execute(infn, jokers_wild)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('test.txt', False)
	main('input.txt', False)

