# 20xx/xx/p1.py

import operator
import time

from p1 import parse_input

def get_path_to_humn(monke, monke_map, past_path):
	monke_o = monke_map[monke]

	if monke_o.get_type() == 'lit':
		return past_path, False

	operand_a = monke_o.get_operand_a()
	operand_b = monke_o.get_operand_b()

	current_path = past_path + [monke]

	if operand_a == 'humn' or operand_b == 'humn':
		return current_path, True

	path_through_a, found_a = get_path_to_humn(operand_a, monke_map, current_path)
	path_through_b, found_b = get_path_to_humn(operand_b, monke_map, current_path)

	if found_a:
		return path_through_a, found_a

	if found_b:
		return path_through_b, found_b

	return current_path, False

def identify_initial_path_to_humn(monke, monke_map):
	monke_o = monke_map[monke]

	operand_a = monke_o.get_operand_a()
	operand_b = monke_o.get_operand_b()

	path_to_humn_a, found_a = get_path_to_humn(operand_a, monke_map, [])
	path_to_humn_b, found_b = get_path_to_humn(operand_b, monke_map, [])

	if found_a:
		return path_to_humn_a, operand_b
	else:
		return path_to_humn_b, operand_a

def backtrace_humn(initial_val, parent, path_to_humn, monke_map):
	parent_o = monke_map[parent]

	if len(path_to_humn) > 0:
		monke_n = path_to_humn[0]
	else:
		monke_n = 'humn'

	humn_down_op_a = parent_o.get_operand_a() == monke_n

	if humn_down_op_a:
		non_humn_n = parent_o.get_operand_b()
	else:
		non_humn_n = parent_o.get_operand_a()

	non_humn_val = monke_map[non_humn_n].get_value(monke_map)

	monke_o = monke_map[monke_n]
	next_path = path_to_humn[1:]

	parent_op_string = parent_o.get_operator_string()

	if parent_op_string == ' + ':
		next_val = initial_val - non_humn_val
	elif parent_op_string == ' * ':
		next_val = initial_val / non_humn_val
	elif parent_op_string == ' - ':
		if humn_down_op_a:
			next_val = initial_val + non_humn_val
		else:
			next_val = non_humn_val - initial_val
	elif parent_op_string == ' / ':
		if humn_down_op_a:
			next_val = non_humn_val * initial_val
		else:
			next_val = non_humn_val / initial_val

	if len(path_to_humn) == 0:
		return next_val
	else:
		return backtrace_humn(next_val, monke_n, next_path, monke_map)

def execute(infn):
	monke_map = parse_input(infn)

	path_to_humn, other_monke = identify_initial_path_to_humn('root', monke_map)

	initial_val = monke_map[other_monke].get_value(monke_map)

	return backtrace_humn(initial_val, path_to_humn[0], path_to_humn[1:], monke_map)

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
