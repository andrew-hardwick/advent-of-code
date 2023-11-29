# 2022/10/p1.py

import time


class machine_t():
	def __init__(self, instructions):
		self._instructions = instructions
		self._pc = 0
		self._reg_x = 1
		self._reg_x_waiting = 1
		self._prior_active = 0
		self._waiting = False
		self._scan_pos = 0

	def tick(self):
		if self._prior_active > 0:
			self._prior_active -= 1

		else:
			if self._waiting:
				self._reg_x = self._reg_x_waiting

			instr = self._instructions[self._pc]
			self._pc += 1

			self._handle_instruction(instr)

		return self._draw_pixel(), [self._reg_x]

	def _handle_instruction(self, instr):
		if instr[0] == 'noop':
			return

		if instr[0] == 'addx':
			self._prior_active = 1
			self._waiting = True
			self._reg_x_waiting = self._reg_x +  int(instr[1])

	def _draw_pixel(self):
		min_sprite = self._reg_x - 1
		max_sprite = self._reg_x + 1

		self._scan_pos += 1

		return self._scan_pos, ((self._scan_pos - 1) % 40) in range(self._reg_x - 1, self._reg_x + 2)

	def unfinished(self):
		return self._pc < len(self._instructions) or self._prior_active > 0

def parse_input(infn):
	with open(infn, 'r') as f:
		instructions = [l.strip().split(' ') for l in f.readlines()]

	return machine_t(instructions)

def execute(infn):
	machine = parse_input(infn)

	count_interesting = [20 + (40 * i) for i in range(6)]

	result = 0

	while machine.unfinished():
		(count, pixel), registers = machine.tick()

		if count in count_interesting:

			result += count * registers[0]

	return count

def main(infn):
	pre = time.perf_counter()

	result = execute(infn)

	post = time.perf_counter()

	print(result, 'in', '{:.2f}'.format((post - pre) * 1000), 'ms')

if __name__ == '__main__':
	main('test1.txt')
	main('test2.txt')
	main('input.txt')
