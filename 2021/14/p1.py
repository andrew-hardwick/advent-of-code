# 2021/14/p1.py

import time


def parse_input(infn):
	with open(infn, 'r') as f:
		lines = [str.strip(l) for l in f.readlines()]

	template = lines[0]
	rules = dict([(tuple(a), b) for a, b in [l.split(' -> ') for l in lines[2:]]])

	counts = dict(((p, 1) for p in zip(template[:-1], template[1:])))

	return counts, rules, template[-1]

def execute_rules(current, rules):
	result = dict((p, 0) for p in rules.keys())

	for pair in current:
		count = current[pair]

		interstitial = rules[pair]

		new_p1 = (pair[0], interstitial)
		new_p2 = (interstitial, pair[1])

		result[new_p1] += count
		result[new_p2] += count

	return result

def execute(infn, count):
	current, rules, final_char = parse_input(infn)

	for i in range(count):
		current = execute_rules(current, rules)

	counts = dict((e, 0) for (e, _) in rules.keys())
	counts[final_char] = 1

	for pair in current:
		counts[pair[0]] += current[pair]

	counts = counts.values()

	return max(counts) - min(counts)

def main(infn, count):
	pre = time.perf_counter()

	result = execute(infn, count)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt', 10)
	main('input.txt', 10)
