# 20xx/xx/p2.py

import itertools
import time

from p1 import mh_dist, parse_input


def is_point_enclosed(p_t, sensors):
	for p_s, r_s in sensors:
		dist = mh_dist(p_t, p_s)

		if mh_dist(p_t, p_s) <= r_s:
			return True

	return False

def find_nearly_adjacent_pairs(sensors, spacing):
	candidate_pairs = itertools.combinations(sensors, 2)

	pairs = []

	for pair in candidate_pairs:
		(a, ra), (b, rb) = pair
		if mh_dist(a, b) == ra + rb + spacing:
			pairs.append(pair)

	return pairs

def get_line(pair):
	a, b = pair

	(xa, ya), ra = a
	(xb, yb), rb = b

	if (xa < xb and ya < yb) or (xa > xb and ya > yb):
		if xa < xb:
			point = (xa, ya + ra + 1)
		else:
			point = (xb, yb + rb + 1)
		return point, (1, -1)
	else:
		if xa < xb:
			point = (xa, ya - ra - 1)
		else:
			point = (xb, yb - rb - 1)
		return point, (1, 1)

def filter_per_slope(points, slope):
	result = set()

	for point in points:
		duplicate = False
		for analyzed in result:
			diff_x = (point[0] - analyzed[0]) * slope[0]
			diff_y = (point[1] - analyzed[1]) * slope[1]

			if diff_x == diff_y:
				duplicate = True

		if not duplicate:
			result.add(point)

	return [(p, slope) for p in result]

def remove_duplicate_lines(lines):
	pos_slope_points = [p for p, s in lines if s == (1, 1)]
	neg_slope_points = [p for p, s in lines if s == (1, -1)]

	return filter_per_slope(pos_slope_points, (1, 1)), filter_per_slope(neg_slope_points, (1, -1))

def find_intersection(line_pair):
	((xa, ya), (sxa, sya)), ((xb, yb), (sxb, syb)) = line_pair

	offset_y = ya - yb

	txa = xa + offset_y * syb
	tya = ya - offset_y

	if not (txa + xb) % 2 == 0:
		return None

	mid_offset = int((txa + xb) / 2 - txa)

	return (txa + mid_offset, tya + (mid_offset * sya))

def execute(infn):
	data = parse_input(infn)

	sensors = [(a, mh_dist(a, b)) for a, b in data]

	pairs = find_nearly_adjacent_pairs(sensors, 2)

	adjacency_lines = list(set([get_line(pair) for pair in pairs]))

	pos_lines, neg_lines = remove_duplicate_lines(adjacency_lines)

	intersections = set()

	for line_pair in itertools.product(pos_lines, neg_lines):
		intersections.add(find_intersection(line_pair))

	intersections = [i for i in intersections if not i == None]

	intersections = [i for i in intersections if not is_point_enclosed(i, sensors)]

	return intersections[0][0] * 4000000 + intersections[0][1]

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	#main('test2.txt')
	main('input.txt')
