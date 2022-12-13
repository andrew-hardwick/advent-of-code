# 2021/10/p1.py

import functools
import time


def evaluate(completion_map, corrupted_score_map, incomplete_score_map, entry):
	closure_stack = []

	for c in entry:
		if c in completion_map:
			closure_stack.append(completion_map[c])
		else:
			check = closure_stack.pop()
			if not check == c:
				return True, corrupted_score_map[c], 0

	incomplete_score = 0

	for c in reversed(closure_stack):
		incomplete_score *= 5
		incomplete_score += incomplete_score_map[c]

	return False, 0, incomplete_score

def execute(input_file):
	with open(input_file, 'r') as f:
		entries = (str.strip(l) for l in f.readlines())

	completion_map = {'(': ')', '[': ']', '{': '}', '<': '>'}
	corrupted_score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
	incomplete_score_map = {')': 1, ']': 2, '}': 3, '>': 4}

	func_evaluate = functools.partial(evaluate, completion_map, corrupted_score_map, incomplete_score_map)

	evaluation = (func_evaluate(e) for e in entries)

	return sum((c_score for check, c_score, i_score in evaluation))

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
