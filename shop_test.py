#shop_test.py

import unittest
from shop import SumatranBeans

class SumatranBeans_Test(unittest.TestCase):

	def test_SumatranBeans_correct_inventory(self):
		inv1 = SumatranBeans(0)
		inv2 = SumatranBeans(10)
		self.assertEqual(inv1.displaystock(), 0)
		self.assertEqual(inv2.displaystock(), 10)


	def test_SaleMade(self):
		inv = SumatranBeans(15)
		self.assertEqual(inv.SaleMade(-1), None)

	def test_SaleMade_for_zero_number_of_items(self):
		inv = SumatranBeans(15)
		self.assertEqual(inv.SaleMade(0), None)


	def test_SaleMade_for_invalid_positive_number_of_items(self):
		inv = SumatranBeans(8)
		self.assertEqual(inv.SaleMade(11), None)


if __name__ == '__main__':
    unittest.main()