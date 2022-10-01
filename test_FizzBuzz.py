import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

	def test_3_should_return_fizz(self):
		self.assertEqual(FizzBuzz(3), "Fizz")
		self.assertEqual(FizzBuzz(6), "Fizz")

	def test_5_should_return_buzz(self):
		self.assertEqual(FizzBuzz(5), "Buzz")
		self.assertEqual(FizzBuzz(10), "Buzz")

	def test_9_should_return_fizzfizz(self):
		self.assertEqual(FizzBuzz(9), "FizzFizz")
		self.assertEqual(FizzBuzz(18), "FizzFizz")

	def test_25_should_return_buzzbuzz(self):
		self.assertEqual(FizzBuzz(25), "BuzzBuzz")
		self.assertEqual(FizzBuzz(50), "BuzzBuzz")    
	
	def test3_and_5_should_return_fizzbuzz(self):
		self.assertEqual(FizzBuzz(15), "FizzBuzz")
		self.assertEqual(FizzBuzz(30), "FizzBuzz")

	def test9_and_25_should_return_fizzfizzbuzzbuzz(self):
		self.assertEqual(FizzBuzz(225), "FizzFizzBuzzBuzz")
		self.assertEqual(FizzBuzz(450), "FizzFizzBuzzBuzz")

	def testwhat_should_return_nofizzbuzz(self):
		self.assertEqual(FizzBuzz(7), "NoFizzBuzz")
		self.assertEqual(FizzBuzz(11), "NoFizzBuzz")
		self.assertEqual(FizzBuzz(10001), "NoFizzBuzz")	

if __name__ == '__main__':
	unittest.main()