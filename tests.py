import unittest
from BrainFuckInterpreter import BrainFuckInterpreter

class TestBrainFuckInterpreter(unittest.TestCase):
	def setUp(self):
		self.bf = BrainFuckInterpreter()

	def test_hello_world(self):
		hello_world = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
		self.assertEqual(self.bf.execute(hello_world), "Hello World!\n")

if __name__ == '__main__':
    unittest.main()