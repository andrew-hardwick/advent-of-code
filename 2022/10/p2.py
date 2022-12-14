# 2022/10/p2.py

import json
import time

from p1 import parse_input


def convert_letter_pixels_to_key(letter_source):
	bin_char = 0
	for r_i, q in enumerate(letter_source):
		nibble = 0
		for p_i, p in enumerate(q):
			nibble += p << p_i

		bin_char += nibble << (r_i * 4)

	return str(bin_char)

def convert_screen_to_letter_pixels(screen):
	letter_count = int(len(screen[0]) / 5)

	letters = [[screen[r][l_i*5:(l_i*5)+4] for r in range(len(screen))] for l_i in range(letter_count)]

	return letters

def parse_letter(letter_source, chars):
	bin_char = convert_letter_pixels_to_key(letter_source)

	if bin_char in chars.keys():
		return chars[bin_char]
	else:
		return '?'

def execute(lkpfn, infn):
	machine = parse_input(infn)

	with open(lkpfn, 'r') as f:
		chars = json.loads(f.read())

	screen = []

	line = []

	while machine.unfinished():
		(count, pixel), registers = machine.tick()

		line.append(1 if pixel else 0)

		if count % 40 == 0:
			screen.append(line)
			line = []

	letters = [parse_letter(l, chars) for l in convert_screen_to_letter_pixels(screen)]

	return ''.join(letters)

def main(lkpfn, infn):
	pre = time.perf_counter()

	result = execute(lkpfn, infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('part_2_lookup', 'test2.txt')
	main('part_2_lookup', 'input.txt')
