# 2021/xx/p1.py

import time

from p1 import parse_input


def letter_pair_check(word):
	for i, c in enumerate(word[:-2]):
		pair = word[i:i + 2]

		if pair in word[i + 2:]:
			return True

	return False

def repeat_with_interstitial_check(word):
	for i, c in enumerate(word[:-2]):
		if c == word[i + 2]:
			return True

	return False

def determine_if_nice(word):
	return letter_pair_check(word) and repeat_with_interstitial_check(word)

def execute(infn):
	data = parse_input(infn)

	nice_words = [w for w in data if determine_if_nice(w)]

	return len(nice_words)

	return '??'

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test2.txt')
	main('input.txt')
