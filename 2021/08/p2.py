# 2021/08/p1.py

import time

def matches(item, pattern):
	for p in pattern:
		if not p in item:
			return False
	return True

def identify_easy(source):
	f_id = {}

	#identify 1
	f_id[1] = ''.join(sorted(next(e for e in source if len(e) == 2)))

	#identify 4
	f_id[4] = ''.join(sorted(next(e for e in source if len(e) == 4)))

	#identify 7
	f_id[7] = ''.join(sorted(next(e for e in source if len(e) == 3)))

	#identify 8
	f_id[8] = ''.join(sorted(next(e for e in source if len(e) == 7)))

	return f_id

def identify_hard(f_id, source):
	#identify 3
	f_id[3] = ''.join(sorted(next(e for e in source if len(e) == 5 and matches(e, f_id[1]))))

	#identify 5
	test_pattern_for_five = [c for c in f_id[4] if c not in f_id[1]]
	f_id[5] = ''.join(sorted(next(e for e in source if len(e) == 5 and matches(e, test_pattern_for_five))))

	#identify 2
	f_id[2] = ''.join(sorted(next(e for e in source if len(e) == 5 and not matches(e, f_id[3]) and not matches(e, f_id[5]))))

	#identify 0
	f_id[0] = ''.join(sorted(next(e for e in source if len(e) == 6 and matches(e, f_id[7]) and not matches(e, f_id[4]))))

	#identify 9
	f_id[9] = ''.join(sorted(next(e for e in source if len(e) == 6 and matches(e, f_id[4]))))

	#identify 6
	f_id[6] = ''.join(sorted(next(e for e in source if len(e) == 6 and not matches(e, f_id[0]) and not matches(e, f_id[9]))))



def execute(input_file):
	with open(input_file, 'r') as f:
		lines = [str.strip(line).split(' | ') for line in f.readlines()]

	pattern_source = [' '.join(l).split(' ') for l in lines]
	outputs = [reversed([''.join(sorted(e)) for e in l[1].split(' ')]) for l in lines]

	total = 0

	for pattern, output in zip(pattern_source, outputs):
		f_id = identify_easy(pattern)
		identify_hard(f_id, pattern)

		lookup = dict((v, k) for k, v in f_id.items())

		total += sum([10 ** i * lookup[v] for i, v in enumerate(output)])

	return total

def main(input_file):
	pre = time.perf_counter()

	result = execute(input_file)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
