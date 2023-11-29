# 2022/15/p1.py

import itertools
import time


def mh_dist(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

def calc_overlap_at_y(d, a, dttr):
	x, y = a

	radius = d - dttr

	return x - radius, x + radius

def reduce_overlap(overlap):
	combine_test = itertools.combinations(overlap, 2)

	combined = True

	while combined:
		combined = False
		combine_result = []
		processed = []

		for a, b in combine_test:
			a_x1, a_x2 = a
			b_x1, b_x2 = b

			if a == b:
				pass
			elif (a_x1 < b_x2 and a_x2 >= b_x1) or (b_x1 < a_x2 and b_x2 >= a_x1):
				combined = True
				new_x1 = min((a_x1, b_x1))
				new_x2 = max((a_x2, b_x2))

				combine_result.append((new_x1, new_x2))

				processed.append(a)
				processed.append(b)
			else:
				if a not in processed:
					combine_result.append(a)
					processed.append(a)

				if b not in processed:
					combine_result.append(b)
					processed.append(b)

		combine_result = list(set(combine_result))
		combine_test = list(itertools.combinations(combine_result, 2))

		combined = combined and len(combine_test) > 0

	return combine_result

def parse_line(line):
	line = line.replace('Sensor at x=', '').replace(' y=', '')
	line = line.replace(': closest beacon is at x=', ', ').replace(' y=', '')

	s = [int(i) for i in line.split(',')]

	return (s[0], s[1]), (s[2], s[3])

def parse_input(infn):
	with open(infn, 'r') as f:
		data = [parse_line(l) for l in f.readlines()]

	return data

def execute(infn, test_row):
	data = parse_input(infn)

	x = [a[0] for a, b in data] + [b[0] for a, b in data]
	min_x = min(x)
	max_x = max(x)

	# calculate manhattan distance and distance to test_row
	data = [(mh_dist(a, b), a, b, abs(a[1] - test_row)) for a, b in data]

	# filter to just those rows that overlap the row of interest
	data = [(d, a, b, dttr) for d, a, b, dttr in data if dttr < d]

	# get boundaries of the overlap
	overlap = [calc_overlap_at_y(d, a, dttr) for (d, a, b, dttr) in data]

	overlap = reduce_overlap(overlap)

	coverage = [x2 - x1 for x1, x2 in overlap]

	return sum(coverage)

def main(infn, test_row):
	pre = time.perf_counter()

	result = execute(infn, test_row)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt', 10)
	main('input.txt', 2000000)
