def euclidean_gcd(a, b) :
    while b != 0 :
        tempB = b
        b = a % b
        a = tempB
    return abs(a)

class Fraction :

    # TODO: Write tests for this
    def __init__(self, numer, denom) :
        self.numerator = numer
        self.denominator = denom
