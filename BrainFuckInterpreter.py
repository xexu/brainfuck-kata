import sys

class BrainFuckInterpreter:
	def __init__(self):
		self.tape = [0] * 30000
		self.data_pointer = 0
		self.program_pointer = 0

	def execute(self, program):
		output = ""
		while self.program_pointer < len(program):
			if program[self.program_pointer] == ">" and self.data_pointer < len(self.tape) - 1:
				self.data_pointer += 1

			elif program[self.program_pointer] == "<" and self.data_pointer > 0:
				self.data_pointer -= 1

			elif program[self.program_pointer] == "+":
				self.tape[self.data_pointer] += 1

			elif program[self.program_pointer] == "-":
				self.tape[self.data_pointer] -= 1

			elif program[self.program_pointer] == ".":
				# print chr(self.tape[self.data_pointer])
				output += chr(self.tape[self.data_pointer])

			elif program[self.program_pointer] == ",":
				self.tape[self.data_pointer] = ord(raw_input())

			elif program[self.program_pointer] == "[":
				if not self.tape[self.data_pointer]:
					self.program_pointer += program[self.program_pointer :].find("]")
					
			elif program[self.program_pointer] == "]":
				self.program_pointer = program[: self.program_pointer].rfind("[") - 1

			self.program_pointer += 1
		return output