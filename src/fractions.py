def euclidean_gcd(a, b) :
    while b != 0 :
        tempB = b
        b = a % b
        a = tempB
    return abs(a)

class Fraction :

    def __init__(self, numer, denom) :
        gcd = euclidean_gcd(numer, denom)
        self.numerator = numer // gcd
        self._temp_denom = denom // gcd
        self.denominator = denom // gcd

    def __str__(self) :
        return str(self.numerator) + "/" + str(self._temp_denom)
