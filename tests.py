import unittest
import Test_Unitaire as test

class Exercice_2_Test_case(unittest.TestCase):

    def test_inf(self):
        self.assertEqual(test.exercice_2(-5, -2, 5), -255)
        self.assertEqual(test.exercice_2(-10, 0, 5), -255)
        self.assertEqual(test.exercice_2(-1, 0, 5), -255)

    def test_sup(self):
        self.assertEqual(test.exercice_2(8, -2, 5), 255)
        self.assertEqual(test.exercice_2(10, -6, 0), 255)
        self.assertEqual(test.exercice_2(-1, -10, -5), 255)

    def test_inter(self):
        self.assertEqual(test.exercice_2(2, -2, 5), 2)
        self.assertEqual(test.exercice_2(-3, -6, 0), -3)
        self.assertEqual(test.exercice_2(0, 0,  0), 0)
        self.assertEqual(test.exercice_2(1, 1, 5), 1)

    #def test_born(self):
     #   self.assertRaises(ValueError, test.exercice_2(5, 3, 2))
      #  self.assertRaises(ValueError, test.exercice_2(-5, 0, -2))


class Exerice_3_Test_case(unittest.TestCase):

    def test1(self):
        self.assertEqual(test.Exercice_3.aire())