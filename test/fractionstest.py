import random
import unittest

import src.fractions

class FractionTest(unittest.TestCase) :
    
    SOME_PRIMES = [277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 
                   353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 
                   431, 433, 439, 443, 449]
    
    NUMBER_OF_PRIMES = len(SOME_PRIMES)
    
    def test_euclidean_gcd_same_number(self) :
        expected = random.randrange(1, 32767)
        actual = src.fractions.euclidean_gcd(expected, expected)
        msg = f"Reckoning gcd({expected}, {expected})"
        self.assertEqual(expected, actual, msg)

    def test_euclidean_gcd_same_negative_number(self) :
        a = random.randrange(-32767, -1)
        expected = -a
        actual = src.fractions.euclidean_gcd(a, a)
        num_str = str(a)
        msg = f"Reckoning gcd({a}, {a})"
        self.assertEqual(expected, actual, msg)

    def test_euclidean_gcd(self) :
        expected = 2 * random.randrange(3, 65535) + 1
        a = 2 * expected
        b = expected * (expected + 2)
        actual = src.fractions.euclidean_gcd(a, b)
        msg = f"Reckoning gcd({a}, {b})"
        self.assertEqual(expected, actual, msg)

    def test_constructor_sets_numerator(self) :
        expected = random.randrange(1, 1024)
        denom = 2 * expected + 1
        instance = src.fractions.Fraction(expected, denom)
        actual = instance.numerator
        self.assertEqual(expected, actual)
    
    def test_constructor_sets_denominator(self) :
        numer = random.randrange(1, 1024)
        expected = 2 * numer + 1
        instance = src.fractions.Fraction(numer, expected)
        actual = instance.denominator
        self.assertEqual(expected, actual)
    
    def test_str(self) :
        numer = random.randrange(1, 32767)
        denom = numer + 1
        instance = src.fractions.Fraction(numer, denom)
        expected = f"{numer}/{denom}"
        actual = str(instance)
        self.assertEqual(expected, actual)
    
if __name__ == '__main__' :
    unittest.main()
