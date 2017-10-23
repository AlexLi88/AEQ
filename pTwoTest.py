import unittest
from POne import POne
"""
Test cases for part one
"""
class TestTransformer(unittest.TestCase):
	def setUp(self):
		pass

	def testCase1(self):
		pone = POne()
		self.assertEqual(pone.findPeakAndValley([6]), 1, "Wrong result")

	def testCase2(self):
		pone = POne()
		self.assertEqual(pone.findPeakAndValley([8,6]), 1, "Wrong result")

	
	def testCase3(self):
		pone = POne()
		self.assertEqual(pone.findPeakAndValley([8,6]), 1, "Wrong result")

	
	def testCase4(self):
		pone = POne()
		self.assertEqual(pone.findPeakAndValley([6]), 1, "Wrong result")

	
	def testCase5(self):
		pone = POne()
		self.assertEqual(pone.findPeakAndValley([2,6,6,6,3]), 2, "Wrong result")

	
	def testCase6(self):
		pone = POne()
		self.assertEqual(pone.findPeakAndValley([6,6,6,8,9,7]), 2, "Wrong result")

	
	def testCase7(self):
		pone = POne()
		self.assertEqual(pone.findPeakAndValley([7,1,1,3,2]), 3, "Wrong result")

	
	def testCase8(self):
		pone = POne()
		self.assertEqual(pone.findPeakAndValley([7,1,1,1,3,3,3,4,4,5,6]), 2, "Wrong result")



if __name__ == '__main__':
	unittest.main()