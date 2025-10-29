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
        self.denominator = denom // gcd

    def __str__(self) :
        return str(self.numerator) + "/" + str(self.denominator)
    
    # TODO: Write tests for this
    # Minus sign for negative fractions should be "&minus;"
    def HTML_str(self) :
        return "SORRY &mdash; NOT IMPLEMENTED YET"
    
    # TODO: Write tests for this
    # Tests should allow any valid TeX syntax that doesn't require importing 
    # packages
    def TeX_str(self) :
        return "SORRY --- NOT IMPLEMENTED YET"
