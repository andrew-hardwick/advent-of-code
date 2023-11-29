# 20xx/xx/p1.py

import time



def parse_input(infn):
	with open(infn, 'r') as f:
		data = [int(l) for l in f.readlines()]

	return data

def single_step(values, indices, index):
	length = len(values)

	offset = values[index] % (length - 1)

	start_loc = indices[index]

	end_loc = (start_loc + offset)  % (length - 1)

	if start_loc < end_loc:
		indices = [indices[i] - 1 if indices[i] > start_loc and indices[i] <= end_loc else indices[i] for i in range(length)]
	else:
		indices = [indices[i] + 1 if indices[i] < start_loc and indices[i] >= end_loc else indices[i] for i in range(length)]
	indices[index] = end_loc

	return indices

def mix(message):
	values = message.copy()
	indices = list(range(len(message)))

	length = len(message)

	for i in range(0, length):
		indices = single_step(values, indices, i)

	return [v for _, v in sorted(zip(indices, values))]

def calculate_coords(mixed, start_val, offsets):
	start_index = mixed.index(start_val)

	return [mixed[(start_index + offset) % len(mixed)] for offset in offsets]

def execute(infn, start_val, offsets):
	data = parse_input(infn)

	mixed = mix(data)

	coords = calculate_coords(mixed, start_val, offsets)

	return sum(coords)

def main(infn, start_val, offsets):
	pre = time.perf_counter()

	result = execute(infn, start_val, offsets)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	offsets = [(i + 1) * 1000 for i in range(3)]

	main('test1.txt', 0, offsets)
	main('input.txt', 0, offsets)
