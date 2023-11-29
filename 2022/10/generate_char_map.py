# 2022/10/generate_char_map.py

import json

from p2 import convert_letter_pixels_to_key, convert_screen_to_letter_pixels


def main(infn):
	with open(infn, 'r') as f:
		lines = [str.strip(l) for l in f.readlines()]

	actuals = lines[0]

	chars = lines[2:]

	chars = [[int(i) for i in r] for r in chars]

	letters = convert_screen_to_letter_pixels(chars)

	keys = [convert_letter_pixels_to_key(letter) for letter in letters]

	result = dict(zip(keys, actuals))

	with open('part_2_lookup', 'w') as f:
		f.write(json.dumps(result))

if __name__ == '__main__':
	 # char_source.txt is a file containing letters and their 4x6 pixel representations.
	 # the file is not checked into this repository due to copyright declarations by advent of code.
	main('char_source.txt')
