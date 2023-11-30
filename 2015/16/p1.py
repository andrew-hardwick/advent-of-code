# 20xx/xx/p1.py

import time


def parse_attributes(
		source):
	split = source.split(',')

	attributes_source = ([attr.split(':') for attr in split])

	return dict([(name.strip(), int(value)) for name, value in attributes_source])


def parse_candidate_sue_info(
		line):
	line = line.strip()
	line = line.replace('Sue ', '')

	split = line.split(':')

	index = int(split[0])

	attribute_source = ':'.join(split[1:]).strip()

	return index, parse_attributes(attribute_source)


def parse_input(infn):
	with open(infn, 'r') as f:
		sues = [parse_candidate_sue_info(l) for l in f.readlines()]

	return dict(sues)


def parse_target_sue_info(
		infn):
	with open(infn, 'r') as f:
		source = ','.join([l.strip() for l in f.readlines()])

	return parse_attributes(source)

def identify_matching_sue(
		target,
		candidates):
	for sue, attributes in candidates.items():
		found = True
		for ak, av in attributes.items():
			found &= av == target[ak]

		if found:
			return sue


def execute(
		suefn,
		infn):
	target_sue_info = parse_target_sue_info(suefn)

	candidates = parse_input(infn)

	return identify_matching_sue(target_sue_info, candidates)


def main(
		suefn,
		infn):
	pre = time.perf_counter()

	result = execute(suefn, infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')


if __name__ == '__main__':
	main('sue_info.txt', 'input.txt')
