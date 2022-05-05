import sys
sys.path.append('../')

from unittest import TestCase, main
from unittests.calculator import calculator

class CalculatorTest(TestCase):
    
    def test_plus(self):
        self.assertEqual(calculator('3+5'), 8)

    
    def test_minus(self):
        self.assertEqual(calculator('8-2'), 6)

    
    def test_division(self):
        self.assertEqual(calculator('9/3'), 3)
    

    def test_multiplication(self):
        self.assertEqual(calculator('7*4'), 28)


    def test_no_symbol(self):
        with self.assertRaises(ValueError) as e:
            calculator('randomtextwithoutsymbols')
        self.assertEqual('Выражение должно содержать знак из списка (+-/*)', e.exception.args[0])


    def test_two_symbols(self):
        with self.assertRaises(ValueError) as e:
            calculator('3+4+5')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])


    def test_many_symbols(self):
        with self.assertRaises(ValueError) as e:
            calculator('3+4*5')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])


    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('3.7+6.9')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])


    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('first_string+second_string')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])


if __name__ ==  '__main__':
    main()