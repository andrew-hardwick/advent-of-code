# pull_input.py

import os
import time

from aocd import get_data


def main():
	for y in range(2015, 2023):
		if not os.path.exists(str(y)):
			os.mkdir(str(y))

		for d in range(25):
			day = d + 1
			day_str = str(day).zfill(2)

			print('pulling', y, day_str)

			day_folder = os.path.join(str(y), day_str)

			if not os.path.exists(day_folder):
				os.mkdir(day_folder)

			data = get_data(day=day, year=y)

			with open(os.path.join(day_folder, 'input.txt'), 'w') as f:
				f.write(data)

			print(y, day_str, 'pulled successfully')

			time.sleep(.5)

if __name__ == '__main__':
	main()