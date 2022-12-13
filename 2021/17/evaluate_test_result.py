# evaluate_test_result.py


def main(infn):
	with open(infn, 'r') as f:
		lines = [str.strip(l) for l in f.readlines()]

	lines = [l.split(' ') for l in lines]
	lines = [e.split(',') for l in lines  for e in l if not e == '']
	x_s = [int(x) for x, y in lines]
	y_s = [int(y) for x, y in lines]

	x_s = list(sorted(set(x_s)))
	y_s = list(sorted(set(y_s)))


	print(x_s)
	print()
	print(y_s)


if __name__ == '__main__':
	main('test2.txt')
