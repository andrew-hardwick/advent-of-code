# 2021/xx/p1.py

import time


def vowel_check(word):
	return sum([c in 'aeiou' for c in word]) >= 3


def double_letter_check(word):
	for i, c in enumerate(word[:-1]):
		if c == word[i + 1]:
			return True

	return False


def naughty_substring_check(word):
	check_strs = ['ab', 'cd', 'pq', 'xy']

	return not any(c_s in word for c_s in check_strs)


def determine_if_nice(word):
	return vowel_check(word) and double_letter_check(word) and naughty_substring_check(word)


def parse_input(infn):
	with open(infn, 'r') as f:
		entries = [str.strip(line) for line in f.readlines()]

	return entries


def execute(infn):
	data = parse_input(infn)

	nice_words = [w for w in data if determine_if_nice(w)]

	return len(nice_words)


def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')


if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')

