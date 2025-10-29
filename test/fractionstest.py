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

    def test_not_equal_diff_numer(self) :
        numerA = random.randrange(1, 512)
        numerB = numerA + random.randrange(1, 511)
        denom = random.randrange(1, 1024)
        fractionA = src.fractions.Fraction(numerA, denom)
        fractionB = src.fractions.Fraction(numerB, denom)
        message = f"{fractionA} should not equal {fractionB}"
        self.assertNotEqual(fractionA, fractionB, message)
   
    def test_eq(self) :
        numer = random.randrange(1, 65536)
        denom = numer + random.randrange(1, 128)
        some_fraction = src.fractions.Fraction(numer, denom)
        same_fraction = src.fractions.Fraction(numer, denom)
        message = f"{some_fraction} should equal {same_fraction}"
        self.assertEqual(some_fraction, same_fraction, message)
        
    def test_not_equal_diff_denom(self) :
        index = random.randrange(0, self.NUMBER_OF_PRIMES - 1)
        numer = self.SOME_PRIMES[index]
        denomA = random.randrange(numer + 1, 2 * numer - 1)
        denomB = random.randrange(2 * numer + 1, 3 * numer - 1)
        fractionA = src.fractions.Fraction(numer, denomA)
        fractionB = src.fractions.Fraction(numer, denomB)
        message = f"{fractionA} should not equal {fractionB}"
        self.assertNotEqual(fractionA, fractionB, message)
    
    def test_equals_even_if_not_in_lowest_terms(self) :
        index = random.randrange(0, self.NUMBER_OF_PRIMES - 1)
        numer = self.SOME_PRIMES[index]
        denom = random.randrange(1, 256)
        mult = random.randrange(2, 32)
        some_fraction = src.fractions.Fraction(numer, denom)
        same_fraction = src.fractions.Fraction(numer * mult, denom * mult)
        message = f"{some_fraction} should equal {same_fraction}"
        self.assertEqual(some_fraction, same_fraction, message)
    
    def test_is_integer(self) :
        numer = random.randrange(-32768, 32767)
        instance = src.fractions.Fraction(numer, 1)
        message = f"Number {instance} should be an integer"
        assert instance.is_integer(), message

    def test_is_not_integer(self) :
        numer = random.randrange(1, 32767)
        denom = random.randrange(2, 32768)
        instance = src.fractions.Fraction(numer, denom)
        message = f"Number {instance} should not be an integer"
        assert not instance.is_integer(), message
    
if __name__ == '__main__' :
    unittest.main()
