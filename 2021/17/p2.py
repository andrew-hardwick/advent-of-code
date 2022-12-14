# 2021/17/p2.py

import math
import time

from p1 import load_target_area


def valid(x_vel, y_vel, min_x, max_x, min_y, max_y):
	x = 0
	y = 0

	while x < max_x and y > min_y:
		x += x_vel
		if x_vel > 0:
			x_vel -= 1

		y += y_vel
		y_vel -= 1

		if x >= min_x and x <= max_x and y >= min_y and y <= max_y:
			return True

	return False

def find_valid_initial_velocities(target_x, target_y):
	min_x = min(target_x)
	max_x = max(target_x)

	min_y = min(target_y)
	max_y = max(target_y)

	min_x_velocity = int(math.sqrt(min_x * 2))
	max_x_velocity = max_x

	min_y_velocity = min_y
	max_y_velocity = -1 - min_y

	valid_velocities = []

	for x_vel in range(min_x_velocity, max_x_velocity + 1):
		for y_vel in range(min_y_velocity, max_y_velocity + 1):
			if valid(x_vel, y_vel, min_x, max_x, min_y, max_y):
				valid_velocities.append((x_vel, y_vel))

	return valid_velocities

def execute(infn):
	target_x, target_y = load_target_area(infn)

	valid_velocities = find_valid_initial_velocities(target_x, target_y)

	return len(valid_velocities)

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
