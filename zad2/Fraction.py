# funckja do obliczenia nwd
def get_nwd(a, b):
    while a % b != 0:
        temp = a % b
        a = b
        b = temp
    return b


# funkcja do obliczenia nww
def get_nww(a, b):
    return a*b/get_nwd(a, b)


# funkcja do skracania ułamków
def reduce(numerator, denominator):
    nwd = get_nwd(abs(numerator), abs(denominator))
    return int(numerator/nwd), int(denominator/nwd)


# funkcja do przystosowania standardu ułamków
def use_standard(numerator, denominator):
    if numerator == 0 or denominator == 0:
        return 0, 0
    numerator, denominator = reduce(numerator, denominator)
    if numerator < 0 and denominator < 0:
        return int(abs(numerator)), int(abs(denominator))
    elif numerator > 0 > denominator:
        return int(-numerator), int(abs(denominator))
    else:
        return int(numerator), int(denominator)


class Fraction:
    # konstruktor
    def __init__(self, numerator, denominator):
        if numerator != 0 and denominator != 0:
            numerator, denominator = use_standard(numerator, denominator)
        self.numerator = numerator
        self.denominator = denominator

    # metoda do podnoszenia ułamka do podanej potęgi
    def to_power(self, power):
        self.numerator = pow(self.numerator, power)
        self.denominator = pow(self.denominator, power)

    # metoda do mnożenia ułamka przez podaną liczbę
    def multiply(self, number):
        self.numerator *= number
        self.numerator, self.denominator = use_standard(self.numerator, self.denominator)

    # metoda do dodawania ułamków
    def add_fraction(self, fraction):
        if self.numerator == 0 or self.denominator == 0:
            self.numerator += fraction.numerator
            self.denominator += fraction.denominator
        elif self.denominator == fraction.denominator:
            self.numerator += fraction.numerator
            self.numerator, self.denominator = use_standard(self.numerator, self.denominator)
        else:
            temp = self.denominator * fraction.denominator
            self.numerator = self.numerator * fraction.denominator
            temp_numerator = fraction.numerator * self.denominator
            self.numerator += temp_numerator
            self.denominator = temp
            self.numerator, self.denominator = use_standard(self.numerator, self.denominator)

    def equal(self, fraction):
        if self.numerator == fraction.numerator and self.denominator == fraction.denominator:
            return True
        else:
            return False

    def multiply_by_fraction(self, fraction):
        self.numerator *= fraction.numerator
        self.denominator *= fraction.denominator
        self.numerator, self.denominator = use_standard(self.numerator, self.denominator)