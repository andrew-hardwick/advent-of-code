# 2021/xx/p1.py

import hashlib
import time


def parse_input(infn):
	with open(infn, 'r') as f:
		data = f.read().strip()

	return data

def find_first_viable_hash(prepend, hash_leading_zeroes):
	salt = 0

	viable_compare = ''.join(['0'] * hash_leading_zeroes)

	while True:
		key = prepend + str(salt)

		hash_result = hashlib.md5(key.encode('utf-8')).hexdigest()

		if hash_result[0:hash_leading_zeroes] == viable_compare:
			return salt

		salt += 1

def execute(infn, hash_leading_zeroes):
	data = parse_input(infn)

	salt = find_first_viable_hash(data, hash_leading_zeroes)

	return salt

def main(infn, hash_leading_zeroes):
	pre = time.perf_counter()

	result = execute(infn, hash_leading_zeroes)

	post = time.perf_counter()

	print(result, 'in', (post - pre) * 1000, 'ms')

if __name__ == '__main__':
	main('test1.txt', 5)
	main('input.txt', 5)
