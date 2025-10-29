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
    
    def test_str_when_constructor_not_get_lowest_terms(self) :
        exp_numer = 2 * random.randrange(1, 2048) + 1
        exp_denom = 2 * exp_numer + 1
        power = 2 ** random.randrange(2, 16)
        multiplier = power * exp_numer * exp_denom
        numer = multiplier * exp_numer
        denom = multiplier * exp_denom
        instance = src.fractions.Fraction(numer, denom)
        expected = f"{exp_numer}/{exp_denom}"
        actual = str(instance)
        self.assertEqual(expected, actual)

    def test_constructor_sets_numerator_when_not_lowest_terms(self) :
        expected = 2 * random.randrange(1, 2048) + 1
        exp_denom = 2 * expected + 1
        power = 2 ** random.randrange(2, 16)
        multiplier = power * expected * exp_denom
        numer = multiplier * expected
        denom = multiplier * exp_denom
        instance = src.fractions.Fraction(numer, denom)
        actual = instance.numerator
        message = f"Getting numerator of {instance}"
        self.assertEqual(expected, actual, message)

    def test_constructor_sets_denominator_when_not_lowest_terms(self) :
        exp_numer = 2 * random.randrange(1, 2048) + 1
        expected = 2 * exp_numer + 1
        power = 2 ** random.randrange(2, 16)
        multiplier = power * exp_numer * expected
        numer = multiplier * exp_numer
        denom = multiplier * expected
        instance = src.fractions.Fraction(numer, denom)
        actual = instance.denominator
        message = f"Getting denominator of {instance}"
        self.assertEqual(expected, actual, message)

    def test_str_integer(self) :
        numer = random.randrange(-4096, 4095)
        instance = src.fractions.Fraction(numer, 1)
        expected = str(numer)
        actual = str(instance)
        self.assertEqual(expected, actual)

if __name__ == '__main__' :
    unittest.main()
