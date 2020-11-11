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
        return Fraction(self.__numerator//fact,self.__denominator//fact)


    def __lt__(self, other):
        """
        Compare 2 fractions
        :param other: class, another Object
        :return: the expression
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.__numerator*other.__denominator < self.__denominator * other.__numerator

    def __gt__(self, other):
        """
        Compare 2 fractions
        :param other: class, another Object
        :return: the expression
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.__numerator*other.__denominator > self.__denominator*other.__numerator

    def __str__(self):
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign, abs(self.__numerator),
                                      abs(self.__denominator))

    def complement(self):
        """
        Return fraction's complement
        :return: class, a new Object
        """
        return Fraction(-1 * self.__numerator, self.__denominator)

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
        return Fraction(self.__numerator * other.__numerator,
                        self.__denominator * other.__denominator)

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
        return Fraction(self.__numerator * other.__denominator + self.__denominator * other.__numerator,
                        self.__denominator * other.__denominator)

    def deduct(self, other):
        """
        Deduct 2 fractions
        :param other: another object
        :return: class, a new Object containing deducted values from the original fractions
        """
        return Fraction(self.__numerator * other.__denominator - other.__numerator * self.__denominator,
                        self.__denominator * other.__denominator)


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

def user_interface():
    """
    Handling all commands input by the user
    :return: the interface of the program
    """
    object_dict = dict()
    while True:
        command = input("> ")
        if len(command.split(" ")) != 1 or len(command) == 0:
            print("Unknown command!")
        else:
            if command == "add":
                frac = str(input("Enter a fraction in the form integer/integer: "))
                name = str(input("Enter a name: "))
                nu = int(frac.split("/")[0])
                de = int(frac.split("/")[1])
                object_dict[name] = Fraction(nu, de)

            elif command == "print":
                name1 = str(input("Enter a name: "))
                if name1 in object_dict:
                    print(name1, "=", object_dict[name1])
                else:
                    print(f"Name {name1} was not found")

            elif command == "list":
                for k in sorted(object_dict):
                    print(k, "=", object_dict[k])

            elif command == "*":
                n1 = str(input("1st operand: "))
                if n1 not in object_dict:
                    print(f"Name {n1} was not found")
                else:
                    n2 = str(input("2nd operand: "))
                    if n2 not in object_dict:
                        print(f"Name {n2} was not found")
                    else:
                        frac1 = object_dict[n1]
                        frac2 = object_dict[n2]
                        mul = frac1.multiply(frac2)
                        print(frac1, "*", frac2, "=", mul)

                        mul = mul.simplify()
                        print("simplified", mul)

            elif command == "file":
                try:
                    file_name = str(input("Enter the name of the file: "))
                    file = open(file_name, mode="r")
                    lines = file.readlines()
                    for line in lines:
                        line=line.split("=")
                        nam=line[0]
                        if "/" in line[1]:
                            fraction=line[1].split("/")
                            object_dict[nam] = Fraction(int(fraction[0]), int(fraction[1]))
                        else:
                            print("Error: the file cannot be read.")
                            break

                except IOError:
                    print("Error: the file cannot be read.")

            elif command == "quit":
                print("Bye bye!")
                break


def main():
    user_interface()

if __name__ == "__main__":
    main()
