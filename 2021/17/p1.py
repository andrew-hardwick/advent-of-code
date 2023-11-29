# 2021/17/p1.py

import math
import time


def find_best_initial_velocities(target_x, target_y):
	min_x_velocity = int(math.sqrt(target_x[0] * 2))

	max_y_velocity = -1 - min(target_y)

	max_y_value = int((max_y_velocity + 1) * max_y_velocity / 2)

	return min_x_velocity, max_y_velocity, max_y_value

def load_target_area(infn):
	with open(infn, 'r') as f:
		source = f.readline()

	sanitized = source.replace('target area: x=', '').replace(', y=', ' ').replace('..', ' ')

	values = [int(i) for i in sanitized.split(' ')]

	return (values[0], values[1]), (values[2], values[3])

def execute(infn):
	target_x, target_y = load_target_area(infn)

	x_vel, y_vel, max_y_value = find_best_initial_velocities(target_x, target_y)

	return max_y_value

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
