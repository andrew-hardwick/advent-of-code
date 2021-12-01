# 2021/01/p2.py

def parse_line(line):
	return int(line.strip())

def main(input_file):
	with open(input_file, 'r') as f:
		entries = list(map(parse_line, f.readlines()))

	last = 0
	count = -1

	for i, entry in enumerate(entries):
		if i > 1:
			window = sum(entries[i - 2 : i + 1])
			if window > last:
				count += 1
			last = window

	print(count)

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
