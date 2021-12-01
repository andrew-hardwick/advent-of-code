# 2021/01/p1.py

def parse_line(line):
	return int(line.strip())

def main(input_file):
	with open(input_file, 'r') as f:
		entries = map(parse_line, f.readlines())

	last = 0
	count = -1

	for entry in entries:
		if entry > last:
			count += 1
		last = entry

	print(count)

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
	