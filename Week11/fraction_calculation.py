class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        A function to simplify a fraction

        :return: class, A new Object containing simplified values of the fraction
        """
        fact = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator//fact
        self.__denominator = self.__denominator//fact

    def complement(self):
        """
        Return fraction's complement

        :return: class, a new Object
        """
        return Fraction(-1*self.__numerator, self.__denominator)

    def reciprocal(self):
        """
        Return fraction's reciprocal

        :return: class, a new Object
        """
        return Fraction(self.__denominator, self.__numerator)

    def multiply(self, other):
        """
        Multiply 2 fractions

        :param other: class, another object
        :return: class, a new object
        """
        return Fraction(self.__numerator*other.__numerator,
                        self.__denominator*other.__denominator)

    def divide(self, other):
        """
        Divide 2 fractions

        :param other: class, another object
        :return: class, a new object
        """
        return Fraction(self.__numerator * other.__denominator,
                        self.__denominator * other.__numerator)

    def add(self, other):
        """
        Addition of 2 fractions

        :param other: class, another Object
        :return: class, a new object
        """
        return Fraction(self.__numerator*other.__denominator + self.__denominator * other.__numerator,
                        self.__denominator*other.__denominator)

    def deduct(self, other):
        """
        Deduct 2 fractions

        :param other: another object
        :return: class, a new Object containing deducted values from the original fractions
        """
        return Fraction(self.__numerator*other.__denominator - other.__numerator * self.__denominator,
                        self.__denominator*other.__denominator)

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

