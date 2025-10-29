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

if __name__ == '__main__' :
    unittest.main()
