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

    def is_integer(self) :
        return self.denominator == 1
    
    # TODO: Write tests for this
    def __eq__(self, other) :
        if self.numerator != other.numerator :
            return False
        return self.denominator == other.denominator
    
    def __add__(self, addend) :
        cross_numerA = self.numerator * addend.denominator
        cross_numerB = addend.numerator * self.denominator
        cross_denom = self.denominator * addend.denominator
        return Fraction(cross_numerA + cross_numerB, cross_denom)

    def __neg__(self) :
        return Fraction(-self.numerator, self.denominator)

    def __sub__(self, subtrahend) :
        return self.__add__(subtrahend.__neg__())

    # TODO: Write tests for this
    def __mul__(self, multiplicand) :
        return self

    # TODO: Write tests for this
    def reciprocal(self) :
        return self

    # TODO: Write tests for this
    def __truediv__(self, divisor) :
        return self
