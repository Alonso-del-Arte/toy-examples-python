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
        if (self.denominator == 1) :
            return str(self.numerator)
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

    # TODO: Write tests for this
    def is_integer(self) :
        return True
    
    # TODO: Write tests for this
    def __add__(self, addend) :
        return self

    # TODO: Write tests for this
    def __neg__(self) :
        return self

    # TODO: Write tests for this
    def __sub__(self, subtrahend) :
        return self

    # TODO: Write tests for this
    def __mul__(self, multiplicand) :
        return self

    # TODO: Write tests for this
    def reciprocal(self) :
        return self

    # TODO: Write tests for this
    def __truediv__(self, divisor) :
        return self
