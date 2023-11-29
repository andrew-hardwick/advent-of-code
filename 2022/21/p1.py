# 20xx/xx/p1.py

import operator
import time


class lit_monke_t():
	def __init__(self, value):
		self._value = value

	def __str__(self):
		return 'lit: ' + str(self._value)

	def get_value(self, monke_map):
		return self._value

	def set_parent(self, parent):
		self._parent = parent

	def set_value(self, value):
		self._value = value

	def get_type(self):
		return 'lit'

class op_monke_t():
	def __init__(self, operand_a, operand_b, monke_op, operator_string):
		self._operand_a = operand_a
		self._operand_b = operand_b

		self._monke_op = monke_op
		self._operator_string = operator_string

	def __str__(self):
		return 'op: ' + self._operand_a + self._operator_string + self._operand_b

	def get_value(self, monke_map):
		operand_a = monke_map[self._operand_a].get_value(monke_map)
		operand_b = monke_map[self._operand_b].get_value(monke_map)

		self._cached_value = self._monke_op(operand_a, operand_b)

		return self._cached_value

	def set_parent(self, parent):
		self._parent = parent

	def get_operand_a(self):
		return self._operand_a

	def get_operand_b(self):
		return self._operand_b

	def get_operator_string(self):
		return self._operator_string

	def get_type(self):
		return 'op'

def parse_monke_op(expression):
	expression_split = expression.split(' ')

	operand_a = expression_split[0]
	operand_b = expression_split[2]

	if expression_split[1] == '*':
		monke_op = operator.mul
	elif expression_split[1] == '+':
		monke_op = operator.add
	elif expression_split[1] == '-':
		monke_op = operator.sub
	elif expression_split[1] == '/':
		monke_op = operator.floordiv

	operator_string = ' ' + expression_split[1] + ' '

	return operand_a, operand_b, monke_op, operator_string

def parse_monke(monke_source):
	initial_split = monke_source.strip().split(': ')

	name = initial_split[0]

	ops = ['+', '-', '*', '/']

	if any(op in initial_split[1] for op in ops):
		operand_a, operand_b, monke_op, operator_string = parse_monke_op(initial_split[1])

		monke = op_monke_t(operand_a, operand_b, monke_op, operator_string)
		parents = [(operand_a, name), (operand_b, name)]
	else:
		monke = lit_monke_t(int(initial_split[1]))
		parents = []

	return name, monke, parents

def parse_input(infn):
	with open(infn, 'r') as f:
		parsed_monkes = [parse_monke(l) for l in f.readlines()]

	monkes = dict((n, m) for n, m, _ in parsed_monkes)

	parents = dict(r for _, _, rs in parsed_monkes for r in rs)

	for name in monkes.keys():
		if name in parents.keys():
			monkes[name].set_parent(parents[name])

	return monkes

def execute(infn):
	monke_map = parse_input(infn)

	# do the thing
	result = monke_map['root'].get_value(monke_map)

	return result

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
