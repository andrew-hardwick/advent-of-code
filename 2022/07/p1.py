# 2022/07/p1.py

import random
import string
import time


current_salt = 256

def add_salt(filename):
	global current_salt
	current_salt = current_salt + 1

	salt = hex(current_salt)

	return filename + f'+{salt}'

def parse_input(infn):
	with open(infn, 'r') as f:
		history = [str.strip(l).split(' ') for l in f.readlines()]

	file_sizes = {}
	dir_contents = {}

	current_directory = '/'
	dir_contents[current_directory] = set()
	parents = {}

	for line in history:
		if line == ['$', 'cd', '/']:
			continue
		if line[0] == '$' and line[1] == 'cd':
			if line[2] == '..':
				current_directory = parents[current_directory]
			else:
				# find next directory in dir_contents dictionary
				next_directory = next((d for d in dir_contents[current_directory] if d.split('+')[0] == line[2]))
				parents[next_directory] = current_directory
				current_directory = next_directory
				dir_contents[current_directory] = set()
		elif line[0] == '$' and line[1] == 'ls':
			# do nothing
			pass
		elif line[0] == 'dir':
			# directory
			dir_contents[current_directory].add(add_salt(line[1]))
		else:
			# sized file
			filename = add_salt(line[1])
			dir_contents[current_directory].add(filename)
			file_sizes[filename] = int(line[0])

	return dir_contents, file_sizes, '/'

def determine_dir_total_size(dir_contents, file_sizes, current):
	if current in file_sizes.keys():
		return file_sizes[current], {current: file_sizes[current]}

	if current not in dir_contents.keys() or len(dir_contents[current]) == 0:
		return 0, {current: 0}

	current_contents = [(c, determine_dir_total_size(dir_contents, file_sizes, c)) for c in dir_contents[current]]

	child_sizes = [b for a, (b, c) in current_contents]
	total_size = sum(child_sizes)

	child_dir_sizes = [c for a, (b, c) in current_contents]

	content_directory_sizes = {current: total_size}

	for d in child_dir_sizes:
		for k in d.keys():
			content_directory_sizes[k] = d[k]

	return total_size, content_directory_sizes

def filter_directories(dir_and_file_sizes, file_sizes):
	return dict([(k, dir_and_file_sizes[k]) for k in dir_and_file_sizes.keys() if k not in file_sizes.keys()])

def print_structure(dir_contents, file_sizes, current, level):
	result = ['  '] * level
	dir_with_contents = True

	display = current.split('+')[0]

	if current in file_sizes.keys():
		result += [f'- {display} (file, size={file_sizes[current]})']
		dir_with_contents = False

	elif current not in dir_contents.keys() or len(dir_contents[current]) == 0:
		result += [f'- {display} (empty dir)']
		dir_with_contents = False

	else:
		result += [f'- {display} (dir)']

	print(''.join(result))

	if dir_with_contents:
		_ = [print_structure(dir_contents, file_sizes, c, level + 1) for c in sorted(dir_contents[current])]

def execute(infn, limit):
	dir_contents, file_sizes, root = parse_input(infn)

	total_size, dir_and_file_sizes = determine_dir_total_size(dir_contents, file_sizes, root)

	dir_sizes = filter_directories(dir_and_file_sizes, file_sizes)

	size_only = list(sorted(dir_sizes.values()))

	within_limit = [v for v in size_only if v <= limit]

	return sum(within_limit)

def main(infn, limit):
	pre = time.perf_counter()

	result = execute(infn, limit)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt', 100000)
	main('input.txt', 100000)
