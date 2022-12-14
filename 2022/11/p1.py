# 2022/11/p1.py

import itertools
import math
import operator
import time


class monke_t():
	def __init__(self, monke_id, starting_items, operation, test, targets):
		self.monke_id = monke_id
		self._items = starting_items
		self._operation = operation
		self._test = test
		self._targets = targets
		self._item_inspection_count = 0
		self._lcm = -1

	def insert(self, item):
		self._items.append(item)

	def set_lcm(self, lcm):
		self._lcm = lcm

	def get_test(self):
		return self._test

	def get_item_inspection_count(self):
		return self._item_inspection_count

	def process_turn(self, monke_map):
		while len(self._items) > 0:
			item = self._items.pop(0)

			item = self._operation(item)
			if self._lcm == -1:
				item = int(item / 3)
			else:
				item = item % self._lcm

			monke_map[self._targets[item % self._test == 0]].insert(item)

			self._item_inspection_count += 1


def parse_monke_op(line):
	expression = line.replace('Operation: new =', '').strip().split(' ')

	if expression[1] == '*':
		op_operator = operator.mul
	elif expression[1] == '+':
		op_operator = operator.add

	if expression[2] == 'old':
		# non-lit
		monke_op = lambda x: op_operator(x, x)
	else:
		monke_op = lambda x: op_operator(x, int(expression[2]))

	return monke_op

def parse_monke(monke_source):
	monke_id = int(monke_source[0].split(' ')[1].replace(':',''))

	starting_items = [int(i) for i in monke_source[1].replace('Starting items: ', '').split(',')]

	monke_op = parse_monke_op(monke_source[2])

	test = int(monke_source[3].replace('Test: divisible by', ''))

	targets = {
		True: int(monke_source[4].replace('If true: throw to monkey', '')),
		False: int(monke_source[5].replace('If false: throw to monkey', ''))
	}

	return monke_id, monke_t(monke_id, starting_items, monke_op, test, targets)

def parse_input(infn):
	with open(infn, 'r') as f:
		monke_source = [str.strip(l) for l in f.readlines()]

	# split monke_source by blank lines
	monke_source = [list(y) for x, y in itertools.groupby(monke_source, lambda z: z == '') if not x]

	monkes = [parse_monke(monke) for monke in monke_source]

	monke_map = dict(monkes)
	monkes = [m for i, m in monkes]

	return monkes, monke_map

def execute(infn, rounds, use_manual_lcm):
	monkes, monke_map = parse_input(infn)

	if use_manual_lcm:
		factors = (m.get_test() for m in monkes)

		# test values are mutually and actually prime
		lcm = math.prod(factors)

		for m in monkes:
			m.set_lcm(lcm)

	for i in range(rounds):
		for m in monkes:
			m.process_turn(monke_map)

	activity = list(sorted([m.get_item_inspection_count() for m in monkes], reverse=True))

	top_activity = activity[:2]

	return math.prod(top_activity)

def main(infn, rounds, use_manual_lcm):
	pre = time.perf_counter()

	result = execute(infn, rounds, use_manual_lcm)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt', 20, False)
	main('input.txt', 20, False)
