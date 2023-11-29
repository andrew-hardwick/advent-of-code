# 2021/10/p1.py

import functools
import time

from p1 import evaluate

def execute(input_file):
	with open(input_file, 'r') as f:
		entries = (str.strip(l) for l in f.readlines())

	completion_map = {'(': ')', '[': ']', '{': '}', '<': '>'}
	corrupted_score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
	incomplete_score_map = {')': 1, ']': 2, '}': 3, '>': 4}

	func_evaluate = functools.partial(evaluate, completion_map, corrupted_score_map, incomplete_score_map)

	evaluation = (func_evaluate(e) for e in entries)

	scores = list(sorted([i_score for check, c_score, i_score in evaluation if i_score > 0]))

	middle_index = int(len(scores) / 2)

	return scores[middle_index]

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
