# 2021/xx/p1.py

import time


def parse_int(source):
	last_index = len(source) - 1

	return sum([source[i] << (last_index - i) for i in range(len(source))])

def parse_packet(packet_source):
	packet = {}

	packet['version'] = parse_int(packet_source[0:3])
	packet['type'] = parse_int(packet_source[3:6])

	finish_index = 0

	if packet['type'] == 4:
		# literal
		continue_index = 6
		literal_source = []

		while True:
			literal_source.extend(packet_source[continue_index + 1:continue_index + 5])

			if not packet_source[continue_index]:
				break

			continue_index += 5

		packet['contents'] = parse_int(literal_source)
		finish_index = continue_index + 5
	else:
		# operator (to be expanded I'm sure)
		if packet_source[6]:
			# count of subpackets
			subpacket_start = 18

			subpacket_count = parse_int(packet_source[7:subpacket_start])

			packet['contents'] = []

			internal_start = 0

			while len(packet['contents']) < subpacket_count:
				subpacket, internal_start = parse_packet(packet_source[subpacket_start:])

				subpacket_start = subpacket_start + internal_start

				packet['contents'].append(subpacket)

			finish_index = subpacket_start
		else:
			# length of subpackets in bits
			subpacket_start = 22

			subpacket_length = parse_int(packet_source[7:subpacket_start])

			expected_end = subpacket_start + subpacket_length

			packet['contents'] = []

			internal_start = 0

			while subpacket_start < expected_end:
				subpacket, internal_start = parse_packet(packet_source[subpacket_start:expected_end])

				subpacket_start = subpacket_start + internal_start

				packet['contents'].append(subpacket)

			finish_index = subpacket_start

	return packet, finish_index

def get_all_version_numbers(packet):
	result = [packet['version']]

	if packet['type'] == 4:
		return result
	else:
		result.extend([vn for p in packet['contents'] for vn in get_all_version_numbers(p)])

		return result

def print_packet_tree(packet, level):
	indent = ''.join(['  '] * level)
	operator_map = {0: 'sum', 1: 'prod', 2: 'min', 3: 'max', 5: 'gt', 6: 'lt', 7: 'eq'}

	if packet['type'] == 4:
		print(f'{indent}literal', f'ver: {packet["version"]}', f'val: {packet["contents"]}')
	else:
		print(f'{indent}operator', f'ver: {packet["version"]}', operator_map[packet['type']])
		for subpacket in packet['contents']:
			print_packet_tree(subpacket, level + 1)

def convert_to_nibble(c):
	c_int = int(c, 16)

	return [(c_int & (1 << i)) >> i for i in range(3, -1, -1)]

def load_packets(infn):
	with open(infn, 'r') as f:
		packet_strings = (str.strip(l) for l in f.readlines())

	packet_source = [[bit for c in l for bit in convert_to_nibble(c)] for l in packet_strings]

	packets = [parse_packet(ps) for ps in packet_source]
	packets = [p for p, li in packets]

	return packets

def execute(infn):
	packets = load_packets(infn)

	version_numbers = [get_all_version_numbers(packet) for packet in packets]

	if len(packets) == 1:
		return sum(version_numbers[0])
	else:
		return [sum(vn) for vn in version_numbers]

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
