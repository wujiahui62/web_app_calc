import unittest
import calc

class Test_000_Calculator(unittest.TestCase):

    def test_single_digit(self):
        i = 0
        for c in '0123456789':
            self.assertEqual(calc.evaluate(c),i)
            i = i + 1
    
    def test_multiple_digits(self):
        self.assertEqual(calc.evaluate('99999'),99999)
        self.assertEqual(calc.evaluate('12345'),12345)
        self.assertEqual(calc.evaluate('99999'),99999)
        self.assertEqual(calc.evaluate('99'),99)
        self.assertEqual(calc.evaluate('00'),00)

    def test_negative_numbers(self):
        self.assertEqual(calc.evaluate('-123'),-123)
        self.assertEqual(calc.evaluate('-1'),-1)
        self.assertEqual(calc.evaluate('0'),0)
        self.assertEqual(calc.evaluate('---123'),-123)

    def test_floating_numbers(self):
        self.assertEqual(calc.evaluate('123.456'),123.456)
        self.assertEqual(calc.evaluate('-123.456'),-123.456)


    def test_hexadecimal_numbers(self):
        self.assertEqual(calc.evaluate('0x00'),0)
        self.assertEqual(calc.evaluate('0x10'),16)
        self.assertEqual(calc.evaluate('0xff'),255)
        self.assertEqual(calc.evaluate('0xFF'),255)

    def test_scientific_notation(self):
        self.assertEqual(calc.evaluate("11E5"), 1100000.0)
        self.assertEqual(calc.evaluate("11E05"), 1100000.0)
        self.assertEqual(calc.evaluate("1.2345E05"), 123450.0)
        self.assertEqual(calc.evaluate("1.1234E0"), 1.1234)
        self.assertEqual(calc.evaluate("-1.2345E05"), -123450.0)


if __name__ == "__main__":
    unittest.main()
