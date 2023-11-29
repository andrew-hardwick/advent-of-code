# 2021/06/p1.py

import time


def load_fish(fish_source):
	fish = [0] * 9

	for new_fish in fish_source:
		fish[new_fish] += 1

	return fish

def grow_fish(fish):
	new_fish = fish[0]

	for i in range(8):
		fish[i] = fish[i + 1]

	fish[6] = fish[6] + new_fish
	fish[8] = new_fish

def execute(input_file):
	with open(input_file, 'r') as f:
		fish_source = [int(i) for i in str.strip(f.read()).split(',')]

	fish = load_fish(fish_source)

	for i in range(80):
		grow_fish(fish)

	return sum(fish)

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
