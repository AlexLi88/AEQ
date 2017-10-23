"""
A unittest for Transformer class
"""
import unittest
from Transformer import Transformer

class TestTransformer(unittest.TestCase):
	def setUp(self):
		pass

	def testSpecialRuleOne(self):
		t1 = Transformer('Bluestreak, A, 7,4,4,4,4,4,4,4')
		t2 = Transformer('Predaking, D, 10, 5, 0, 8, 7, 9, 9, 8')
		t1.battle(t2)
		self.assertEqual(t1.eliminated, True, "Wrong battle result")
		self.assertEqual(t2.eliminated, False, "Wrong battle result")

	def testSpecialRuleTwo(self):
		t1 = Transformer('Optimus Prime, A, 10, 10, 8, 10, 10, 10, 8, 10')
		t2 = Transformer('Cutthroat, D, 4,4,4,4,4,4,4,4')
		t1.battle(t2)
		self.assertEqual(t1.eliminated, False, "Wrong battle result")
		self.assertEqual(t2.eliminated, True, "Wrong battle result")

	def testSpecialRuleThree(self):
		t1 = Transformer('Optimus Prime, A, 10, 10, 8, 10, 10, 10, 8, 10')
		t2 = Transformer('Predaking, D, 10, 5, 0, 8, 7, 9, 9, 8')
		t1.battle(t2)
		self.assertEqual(t1.eliminated, True, "Wrong battle result")
		self.assertEqual(t2.eliminated, True, "Wrong battle result")

	def testBattleStrength(self):
		t1 = Transformer('Bluestreak, A, 7,4,4,4,4,4,4,4')
		t2 = Transformer('Cutthroat, D, 4,4,4,4,4,4,4,4')
		t1.battle(t2)
		self.assertEqual(t1.eliminated, False, "Wrong battle result")
		self.assertEqual(t2.eliminated, True, "Wrong battle result")

	def testBattleCourage(self):
		t1 = Transformer('Bluestreak, A, 4,4,4,4,4,8,4,4')
		t2 = Transformer('Cutthroat, D, 4,4,4,4,4,4,4,4')
		t1.battle(t2)
		self.assertEqual(t1.eliminated, False, "Wrong battle result")
		self.assertEqual(t2.eliminated, True, "Wrong battle result")

	def testBattleSkill(self):
		t1 = Transformer('Bluestreak, A, 4,4,4,4,4,4,4,10')
		t2 = Transformer('Cutthroat, D, 4,4,4,4,4,4,4,4')
		t1.battle(t2)
		self.assertEqual(t1.eliminated, False, "Wrong battle result")
		self.assertEqual(t2.eliminated, True, "Wrong battle result")

	def testBattleOverallRating(self):
		t1 = Transformer('Bluestreak, A, 6,4,4,4,5,5,8,1')
		t2 = Transformer('Cutthroat, D, 6,4,4,4,5,5,4,1')
		t1.battle(t2)
		self.assertEqual(t1.eliminated, False, 'Wrong battle result')
		self.assertEqual(t2.eliminated, True, "Wrong battle result")

if __name__ == '__main__':
	unittest.main()